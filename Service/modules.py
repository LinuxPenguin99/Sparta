import os
import json
from deepface import DeepFace
import cv2

def face_analysis(img_path):
    analysis_result = DeepFace.analyze(img_path)[0]
    file = './face_data.json'
    with open(file, 'w') as f:
        json.dump(analysis_result, f)
        

def face_param(analysis_result):
    emotion = analysis_result['dominant_emotion']
    gender = analysis_result['dominant_gender']
    age = analysis_result['age']
    return emotion, gender, age
    
def box_draw(img_path):
    result = DeepFace.analyze(img_path)[0]
    regions = list(result['region'].values())[:4]
    emotion = result['dominant_emotion']
    gender = result['dominant_gender']
    age = result['age']
    print(regions)
    x, y, w, h = regions[0], regions[1], regions[2], regions[3]
    img = cv2.imread(img_path, cv2.IMREAD_COLOR)
    cv2.rectangle(img, rec = (x, y, w, h), thickness = 5, color = (0, 0, 255))
    cv2.putText(img, f'Gender: {gender}', org = (10, 200), fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale = 5, color = (0, 0, 255), thickness = 4, lineType = cv2.LINE_AA)
    cv2.putText(img, f'Age: {age}', org = (10, 400), fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale = 5, color = (0, 0, 255), thickness = 4, lineType = cv2.LINE_AA)
    cv2.putText(img, f'Emotion: {emotion}', org = (10, 600), fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale = 5, color = (0, 0, 255), thickness = 4, lineType = cv2.LINE_AA) 
    #cv2.imshow('',img)
    #cv2.waitKey(0)
    cv2.imwrite('./result.jpg', img)
    
