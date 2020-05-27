import cv2
from PIL import Image
import pytesseract
from yt_to_frame import video_to_frames_url_auto
from dm import chinese_str
from preprocess import preprocess, transcribe
from translate import Translator
text = 'Hello'

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
'''for i in range(1,5):
    temp = Image.open('C:/Users/Ciaran/Desktop/video_1/newcroppbw2.v{}.jpg'.format(i))
    text = (pytesseract.image_to_string(temp, lang='chi_sim'))
    text = chinese_str(text)
    print(((text)))'''
#url = 'https://www.youtube.com/watch?v=yzs5YShQdrY'
#video_to_frames_url_auto(url)
#39743
#29059
folder = 'C:/Users/Ciaran/Desktop/video_1/'

images = [folder+'39743.jpg', folder+'29059.jpg']
for i in range(2400, 3001, 50):
    image = folder+'{}.jpg'.format(i)
    image  = cv2.imread(image)
    processed_img  = preprocess(image)
    raw_output = transcribe(processed_img)
    print(raw_output)
    subtitle  = chinese_str(raw_output)
    '''cv2.imshow("frame", image)
    cv2.waitKey(4000)
    cv2.imshow("frame", processed_img)
    cv2.waitKey(4000)'''
