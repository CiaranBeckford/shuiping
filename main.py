import cv2
from PIL import Image
import pytesseract
import jieba
from yt_to_frame import video_to_frames_url_auto
from dm import chinese_str
from preprocess import preprocess, transcribe
from translate import Translator
from columbia_year_3 import init_dict, check_dict



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
chinese_dict = init_dict()
proficiency = set()
query_set = set()
img_count = 0
in_dict_count = 0
query_count = 0
for i in range(2400, 65000, 50):
    image = folder+'{}.jpg'.format(i)
    image  = cv2.imread(image)

    processed_img  = preprocess(image)
    raw_output = transcribe(processed_img)
    subtitle  = chinese_str(raw_output)
    paddle_list = list(jieba.cut(subtitle))
    known_words = list()
    unknown_words = list()
    for query in paddle_list:
        result = check_dict(query, chinese_dict)
        if result[0] is True:
            proficiency.add((query),)
            known_words.append(query)
            in_dict_count+=1
        else:
            unknown_words.append(query)
        query_set.add((query),)
    " ".join(known_words)
    " ".join(unknown_words)
    print("Original subtitle: "+str(subtitle)+" | "+"Known Words: "+str(known_words)+" | "+"Unknown Words: "+str(unknown_words))
    cv2.imshow("", image)
    cv2.waitKey(1000)
    img_count+=1
    print(img_count)


print("query_count_unique: "+str(len(query_set)))
print("in_dict_count: "+str(in_dict_count))
print(proficiency)
print(len(proficiency))
