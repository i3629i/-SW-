from __future__ import division
import cv2
import numpy as np
import time
import math
from PIL import Image

protoFile = "Model/pose_deploy.prototxt"
weightsFile = "Model/pose_iter_102000.caffemodel"
nPoints = 22
#https://www.learnopencv.com/hand-keypoint-detection-using-deep-learning-and-opencv/
#저 사이트에 나온 손 사진 번호를 리스트에 담음
POSE_PAIRS = [ [0,1],[1,2],[2,3],[3,4],[0,5],[5,6],[6,7],[7,8],[0,9],[9,10],[10,11],[11,12],[0,13],[13,14],[14,15],[15,16],[0,17],[17,18],[18,19],[19,20] ]
net = cv2.dnn.readNetFromCaffe(protoFile, weightsFile)

#원하는 이미지를 로드한다
frame = cv2.imread("Image/00.jpg")
frame_handlandmark = np.copy(frame)
color_frame = np.copy(frame)
frameCopy = np.copy(frame)
frameWidth = frame.shape[1]
frameHeight = frame.shape[0]
aspect_ratio = frameWidth/frameHeight

#임계값 설정. 작을 수록 좋게 나옴. 하지만 너무 작을 시에는 이상한 것을 감지함
threshold = 0.1

t = time.time()
# input image dimensions for the network
inHeight = 368
inWidth = int(((aspect_ratio*inHeight)*8)//8)
inpBlob = cv2.dnn.blobFromImage(frame, 1.0 / 255, (inWidth, inHeight), (0, 0, 0), swapRB=False, crop=False)

net.setInput(inpBlob)

output = net.forward()

print("time taken by network : {:.3f}".format(time.time() - t))

points = []

#아마 이부분이 이미지에서 손을 추출하는 부분인듯해용
for i in range(nPoints):
    # confidence map of corresponding body's part.
    probMap = output[0, i, :, :]
    probMap = cv2.resize(probMap, (frameWidth, frameHeight))
    # Find global maxima of the probMap.
    minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)

    if prob > threshold :
        cv2.circle(frameCopy, (int(point[0]), int(point[1])), 2, (0, 255, 255), thickness=-1, lineType=cv2.FILLED)
        cv2.putText(frameCopy, "{}".format(i), (int(point[0]), int(point[1])), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, lineType=cv2.LINE_AA)

        points.append((int(point[0]), int(point[1])))
    else :
        points.append(None)

#원하는 이미지에서 손 부분에 리스트 값을 매칭시키는 부분
for pair in POSE_PAIRS:
    partA = pair[0]
    partB = pair[1]
    # print(partA,partB)
    # print(points[partA], points[partB])

    if points[partA] and points[partB]:
        cv2.line(frame_handlandmark, points[partA], points[partB], (0, 255, 255), 2)
        cv2.circle(frame_handlandmark, points[partA], 2, (0, 0, 255), thickness=-1, lineType=cv2.FILLED)
        cv2.circle(frame_handlandmark, points[partB], 2, (0, 0, 255), thickness=-1, lineType=cv2.FILLED)

#매칭시킨 이미지에서 손 끝과 두번째 마디를 리스트에 담음
finger = [points[20],points[16],points[12],points[8],points[4]]
finger_second = [points[19],points[15],points[11],points[7],points[3]]

#리스트에 None값이 담길수 있어서 제거
#why?브이모양을 한 경우 모든 손가락을 감지해주지 못함
if None in finger:
    finger.remove(None)

if None in finger_second:
    finger_second.remove(None)


print(finger)
print(finger_second)



for i in range(len(finger)):
    #원을 그리기 위해서 중간값을 찾는 과정
    fingerprint_X = int((finger[i][0] + finger_second[i][0]) / 2)
    fingerprint_Y = int((finger[i][1] + finger_second[i][1]) / 2)
    print(fingerprint_X,fingerprint_Y)
    
    #원의 크기를 정하기 위해서 값을 구하는 과정
    circle_size = finger[i][0] - fingerprint_X +  fingerprint_Y - finger[i][1]
    print(circle_size)
    # cv2.circle(frame_handlandmark, (fingerprint_X, fingerprint_Y), circle_size, (255, 255, 0), thickness=1)
    first_X =finger[i][0]
    first_Y = finger[i][1]
    second_X = finger_second[i][0]
    second_Y = finger_second[i][1]
    
    #원을 기울여주기 위해서 각도를 찾는 과정
    X = first_X - second_X
    Y = first_Y - second_Y
    
    B = math.sqrt(math.pow(X,2) + math.pow(Y,2))
    print(B)
    radius = int(B / 2)
    half_radius = int(radius / 2)
    acos = math.acos( X/B ) * 57.3 # 1 radian 곱
    print('acos : ',acos)
    # cos = math.acos()
    #원을 그려줌
    cv2.ellipse(frame_handlandmark,(fingerprint_X, fingerprint_Y),(radius,half_radius),-acos,0,360,(255,255,125),1)
    #원을 검은색으로 채워줌
    cv2.ellipse(color_frame,(fingerprint_X, fingerprint_Y),(radius,half_radius),-acos,0,360,(0,0,0),-1)

#원을 검은색으로 채운 그림과 원본 사진을 XOR함
img = cv2.bitwise_xor(color_frame,frame)

# blue_threshold = 0
# green_threshold = 0
# red_threshold = 0
# bgr_threshold = [blue_threshold, green_threshold, red_threshold]
#
# thresholds = (color_frame[:,:,0] <= bgr_threshold[0]) \
#             | (color_frame[:,:,1] <= bgr_threshold[1]) \
#             | (color_frame[:,:,2] <= bgr_threshold[2])
#
# img[thresholds] = [255,255,255]

#지문있는 이미지를 블러처리
img = cv2.medianBlur(img,3)
cv2.imshow('test',img)

#블러처리한 이미지와 원본이미지를 합쳐줌
img = cv2.bitwise_or(img,frame)
print(img.shape)
# img = cv2.bitwise_or(img,frame2)
# frame = cv2.bitwise_and(frame,color_frame)


# cv2.circle(frame,finger[1])

# ycrcb = cv2.cvtColor(frame,cv2.COLOR_BGR2YCrCb)
# mask_hand = cv2.inRange(ycrcb, np.array([0,133,77]), np.array([255,173,127]))

# cv2.imshow('hands',mask_hand)
# frame = cv2.resize(frame,(480,680))
# cv2.imshow('Output-Keypoints', frameCopy)
frame_handlandmark = cv2.medianBlur(frame_handlandmark,15)
cv2.imshow('frame_handlandmark',frame_handlandmark)
cv2.imshow('color_frame',color_frame)
cv2.imshow('Output', img)
# 20 , 16, 12, 8,  4
print("Total time taken : {:.3f}".format(time.time() - t))

cv2.waitKey(0)
