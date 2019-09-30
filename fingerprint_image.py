from __future__ import division
import cv2
import numpy as np
import time
import math


# caffe 모델과 가중치값 저장
protoFile = "Model/pose_deploy.prototxt"
weightsFile = "Model/pose_iter_102000.caffemodel"

# 22개의 손가락 마디 포인트를 지정해줌
nPoints = 22

POSE_PAIRS = [ [0,1],[1,2],[2,3],[3,4],[0,5],[5,6],[6,7],[7,8],[0,9],[9,10],[10,11],[11,12],[0,13],[13,14],[14,15],[15,16],[0,17],[17,18],[18,19],[19,20] ]
net = cv2.dnn.readNetFromCaffe(protoFile, weightsFile)
#이미지 가져오는 부분

path = "Image/00.jpg" #이미지 경로 지정
frame = cv2.imread(path)

line_frame = np.copy(frame)
fingerprint_circle_frame = np.copy(frame)
dark_frame = np.copy(frame)
frameCopy = np.copy(frame)

frameWidth = frame.shape[1]
frameHeight = frame.shape[0]
aspect_ratio = frameWidth/frameHeight

#임계값 설정
threshold = 0.1

t = time.time()

inHeight = 368
inWidth = int(((aspect_ratio*inHeight)*8)//8)
inpBlob = cv2.dnn.blobFromImage(frame, 1.0 / 255, (inWidth, inHeight), (0, 0, 0), swapRB=False, crop=False)

net.setInput(inpBlob)

output = net.forward()

print("time taken by network : {:.3f}".format(time.time() - t))

points = []

for i in range(nPoints):
    # confidence map of corresponding body's part.
    probMap = output[0, i, :, :]
    probMap = cv2.resize(probMap, (frameWidth, frameHeight))
    # Find global maxima of the probMap.
    minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)

#적용된 모델을 이미지의 포인트 숫자와 원으로 표현
    if prob > threshold :
        cv2.circle(frameCopy, (int(point[0]), int(point[1])), 2, (0, 255, 255), thickness=-1, lineType=cv2.FILLED)
        cv2.putText(frameCopy, "{}".format(i), (int(point[0]), int(point[1])), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, lineType=cv2.LINE_AA)
        points.append((int(point[0]), int(point[1])))
    else :
        # 포인트에 값이 없을시 None대입
        points.append(None)


f1 = [points[20],points[16],points[12],points[8],points[4]]
f2 = [points[19],points[15],points[11],points[7],points[3]]


print(f1)
print(f2)

finger= []
finger_second = []


#점찍고 라인그려주는 부분
def draw_line():
    for pair in POSE_PAIRS:
        partA = pair[0]
        partB = pair[1]

    #손가락의 라인을 그려주고 점을 찍어줌
        if points[partA] and points[partB]:
            cv2.line(line_frame, points[partA], points[partB], (0, 255, 255), 2)
            cv2.circle(line_frame, points[partA], 2, (0, 0, 255), thickness=-1, lineType=cv2.FILLED)
            cv2.circle(line_frame, points[partB], 2, (0, 0, 255), thickness=-1, lineType=cv2.FILLED)
    return cv2.imshow('line_frame',line_frame)


def draw_circle():
    for i,v in enumerate(f1):
        if f1[i] != None and f2[i] != None :
            finger.append(f1[i])
            finger_second.append(f2[i])

    for i in range(len(finger)):
    #손가락 마디의 중심좌표 X,Y
        fingerprint_X = int((finger[i][0] + finger_second[i][0]) / 2)
        fingerprint_Y = int((finger[i][1] + finger_second[i][1]) / 2)
        first_X = finger[i][0]
        first_Y = finger[i][1]
        second_X = finger_second[i][0]
        second_Y = finger_second[i][1]
        X = first_X - second_X
        Y = first_Y - second_Y
    # circle_size = finger[i][0] - fingerprint_X +  fingerprint_Y - finger[i][1]

# 타원의 손 모양에 맞게 틀어줘야 함으로 각을 구해 타원을 틀어줌
        Z = math.sqrt(math.pow(X, 2) + math.pow(Y, 2))
        radius = int(Z/2)
        half_radius = int(radius / 2)
        acos =  math.acos(X/Z) * 57.3

    #타원그리는 함수
        #Y축을 기준으로 각도를 지정해줌 손가락이 위를 향할 경우 각의 마이너스, 손가락이 아래를 향할 경우 각의 플러스
        if first_Y >= second_Y :
            acos = acos
        else:
            acos = -acos
        print(acos)
        cv2.ellipse(fingerprint_circle_frame,(fingerprint_X, fingerprint_Y),(radius,half_radius),acos,0,360,(255,255,125),2)
        cv2.ellipse(dark_frame,(fingerprint_X, fingerprint_Y),(radius,half_radius),acos,0,360,(0,0,0),-1)
    return fingerprint_circle_frame,dark_frame

def bit_xor():
    #원본이미지와 지문부분만 검정색으로 칠한 이미지를 Xor연산(같은 색일 경우 검정색으로 다른색은 흰색)
    go_xor = cv2.bitwise_xor(draw_circle()[1],frame)
    #medianblur사용해서 지문 부위만 흐림효과 추가
    go_xor = cv2.medianBlur(go_xor,3)
    return go_xor



    #원본 이미지와 xor이미지를 합성함
def bit_or():
    changed_image = cv2.bitwise_or(bit_xor(),frame)
    return changed_image


# half_radius = 30
#
# y1 = finger[3][1] - half_radius
# y2 = finger_second[3][1] + half_radius
# x1 = finger[3][0] - half_radius
# x2 = finger_second[3][0] + half_radius
#
# frame1 = frame[y1:y2, x1:x2]
# frame1 = cv2.resize(frame1,(360,580))
# img1 = changed_image[y1:y2, x1:x2]
# img1 = cv2.resize(img1,(360,580))

# 20 , 16, 12, 8,  4

if __name__ == "__main__":
    cv2.imwrite('Image/changed_image.jpg',bit_or())
