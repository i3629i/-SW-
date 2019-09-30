from __future__ import division
import cv2
import numpy as np
import time
import math

protoFile = "Model/pose_deploy.prototxt"
weightsFile = "Model/pose_iter_102000.caffemodel"
nPoints = 22

POSE_PAIRS = [ [0,1],[1,2],[2,3],[3,4],[0,5],[5,6],[6,7],[7,8],[0,9],[9,10],[10,11],[11,12],[0,13],[13,14],[14,15],[15,16],[0,17],[17,18],[18,19],[19,20] ]
net = cv2.dnn.readNetFromCaffe(protoFile, weightsFile)

threshold = 0.3

cap = cv2.VideoCapture(0)
hasFrame, frame = cap.read()

frameWidth = frame.shape[1]
frameHeight = frame.shape[0]

aspect_ratio = frameWidth/frameHeight

inHeight = 368
inWidth = int(((aspect_ratio*inHeight)*8)//8)

vid_writer = cv2.VideoWriter('Video/output.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 15, (frame.shape[1],frame.shape[0]))

net = cv2.dnn.readNetFromCaffe(protoFile, weightsFile)
k = 0
while 1:
    k+=1
    t = time.time()
    hasFrame, frame = cap.read()
    frameCopy = np.copy(frame)

    line_frame = np.copy(frame)
    fingerprint_circle_frame = np.copy(frame)
    dark_frame = np.copy(frame)
    if not hasFrame:
        cv2.waitKey()
        break

    inpBlob = cv2.dnn.blobFromImage(frame, 1.0 / 255, (inWidth, inHeight),
                              (0, 0, 0), swapRB=False, crop=False)

    net.setInput(inpBlob)

    output = net.forward()

    print("forward = {}".format(time.time() - t))

    # Empty list to store the detected keypoints
    points = []

    for i in range(nPoints):
        # confidence map of corresponding body's part.
        probMap = output[0, i, :, :]
        probMap = cv2.resize(probMap, (frameWidth, frameHeight))

        # Find global maxima of the probMap.
        minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)

        if prob > threshold :
            # cv2.circle(frameCopy, (int(point[0]), int(point[1])), 6, (0, 255, 255), thickness=-1, lineType=cv2.FILLED)
            # cv2.putText(frameCopy, "{}".format(i), (int(point[0]), int(point[1])), cv2.FONT_HERSHEY_SIMPLEX, .8, (0, 0, 255), 2, lineType=cv2.LINE_AA)

            # Add the point to the list if the probability is greater than the threshold
            points.append((int(point[0]), int(point[1])))
        else :
            points.append(None)

    # Draw Skeleton
    for pair in POSE_PAIRS:
        partA = pair[0]
        partB = pair[1]

        if points[partA] and points[partB]:
            cv2.line(frameCopy, points[partA], points[partB], (0, 255, 255), 2, lineType=cv2.LINE_AA)
            cv2.circle(frameCopy, points[partA], 5, (0, 0, 255), thickness=-1, lineType=cv2.FILLED)
            cv2.circle(frameCopy, points[partB], 5, (0, 0, 255), thickness=-1, lineType=cv2.FILLED)


    f1 = [points[20], points[16], points[12], points[8], points[4]]
    f2 = [points[19], points[15], points[11], points[7], points[3]]

    finger = []
    finger_second = []


    def draw_circle():
        for i, v in enumerate(f1):
            if f1[i] != None and f2[i] != None:
                finger.append(f1[i])
                finger_second.append(f2[i])

        for i in range(len(finger)):
            # 손가락 마디의 중심좌표 X,Y
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
            radius = int(Z / 2)
            half_radius = int(radius / 2)
            acos = math.acos(X / Z) * 57.3

            # 타원그리는 함수
            # Y축을 기준으로 각도를 지정해줌 손가락이 위를 향할 경우 각의 마이너스, 손가락이 아래를 향할 경우 각의 플러스
            if first_Y >= second_Y:
                acos = acos
            else:
                acos = -acos
            print(acos)
            cv2.ellipse(fingerprint_circle_frame, (fingerprint_X, fingerprint_Y), (radius, half_radius), acos, 0, 360,
                        (255, 255, 125), 2)
            cv2.ellipse(dark_frame, (fingerprint_X, fingerprint_Y), (radius, half_radius), acos, 0, 360, (0, 0, 0), -1)
        return fingerprint_circle_frame, dark_frame


    def bit_xor():
        # 원본이미지와 지문부분만 검정색으로 칠한 이미지를 Xor연산(같은 색일 경우 검정색으로 다른색은 흰색)
        go_xor = cv2.bitwise_xor(draw_circle()[1], frame)
        # medianblur사용해서 지문 부위만 흐림효과 추가
        go_xor = cv2.medianBlur(go_xor, 3)
        return go_xor

        # 원본 이미지와 xor이미지를 합성함


    def bit_or():
        changed_image = cv2.bitwise_or(bit_xor(), frame)
        return changed_image


    cv2.imshow('original',frameCopy)
    cv2.imshow('changed', bit_or())

    # cv2.imwrite("video_output/{:03d}.jpg".format(k), frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    print("total = {}".format(time.time() - t))

    vid_writer.write(bit_or())
vid_writer.release()