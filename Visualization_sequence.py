from __future__ import division
import cv2
import numpy as np
import time
import math
import fingerprint_image

# caffe 모델과 가중치값 저장
#1. 손의 이미지에 마디의 라인을 그려주고 점을 찍어준다.
fingerprint_image.draw_line()
cv2.waitKey(0)

#2. 손의 지문 부위를 추출해 타원의 형태로 그려준다.
fingerprint_circle = fingerprint_image.draw_circle()[0]
cv2.imshow('fingerprint_circle',fingerprint_circle)
cv2.waitKey(0)

#3. 지문 부위를 검은색을 채워준다
fingerprint_darkframe = fingerprint_image.draw_circle()[1]
cv2.imshow('fingerprint_darkframe',fingerprint_darkframe)
cv2.waitKey(0)

#4. xor연산을 통해 손가락 부분만 추출한다. 나머지는 검은색으로
extraction_finger = fingerprint_image.bit_xor()
cv2.imshow('extraction_finger',extraction_finger)
cv2.waitKey(0)

#5. 원본 이미지와 합친다.
synthesis_images = fingerprint_image.bit_or()
cv2.imshow('synthesis_images',synthesis_images)
cv2.waitKey(0)