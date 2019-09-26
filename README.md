# 시작해보자
markdown 작성팁
https://gist.github.com/ihoneymon/652be052a0727ad59601


환경 설정하는 순서
1. Anaconda3(콘다 깔면 파이썬 알아서 깔림)
1. conda환경에서 파이썬 3.6ver으로 환경 새로 만들어 줘야함http://blog.naver.com/PostView.nhn?blogId=baek2sm&logNo=221378601592&categoryNo=0&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=postView
1. 필수 라이브러리 설치
cv2 - https://dejavuqa.tistory.com/228
pip install numpy,pandas,matplotlib,pillow 여러가지 있었는데 까먹.. 하다가 필요한거 부르는 것만 깔자 이거는

tensorflow는 필요할지 모르겠음, 여기선 일단 caffe 쓰니까 이것도 보류
----------------------
## Model 다운 받는 곳 http://posefs1.perception.cs.cmu.edu/OpenPose/models/hand/pose_iter_102000.caffemodel


여기서부터 하는 걸로 할께염


이미지나 동영상의 지문 지우기
============================

## 1. 기능
 최근 카메라의 화질이 좋아지면서 지문이 해킹을 당할 수 있는 상황에 놓여져 있다.
 
