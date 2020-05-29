import cv2
import numpy as np
import pytesseract
from pytesseract import Output


# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def binarize(image):
    height,width = image.shape
    for i in range(height):
        for j in range(width):
            if image[i][j] < 218:
                image[i][j] = 0
    return image
# noise removal
def remove_noise(image):
    return cv2.medianBlur(image,5)

#thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

#dilation
def dilate(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.dilate(image, kernel, iterations = 1)

#erosion
def erode(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.erode(image, kernel, iterations = 1)

#opening - erosion followed by dilation
def opening(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

#canny edge detection
def canny(image):
    return cv2.Canny(image, 100, 200)

#skew correction
def deskew(image):
    coords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated

#template matching
def match_template(image, template):
    return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)

def preprocess(img):
    scale_percent = 50 # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    h_sixth = int(height/6)
    w_sixth = int(width/4)
    new_height = height-h_sixth
    new_width = width-w_sixth
    img = img[new_height:(height-15), w_sixth:new_width]

    img = get_grayscale(img)

    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    (thresh, blackAndWhiteImage) = cv2.threshold(img, 168, 255, cv2.THRESH_TOZERO)

    blackAndWhiteImage = ~blackAndWhiteImage
    img  = blackAndWhiteImage
    return img
def transcribe(img):
    custom_config = r'-l chi_sim --psm 6'
    res = pytesseract.image_to_string(img, config=custom_config)

    return str(res)

#resized_img = cv2.resize(img, (1600,900) )

#img = cv2.bilateralFilter(img,9,75,75)
    # Convert to gray    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    # Apply dilation and erosion to remove some noise

#img = cv2.GaussianBlur(img, (5, 5), 0)
