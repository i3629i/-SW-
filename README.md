# 1. Project

## 1. Introduction
> 최근 카메라의 화질이 향상되면서 지문까지 고화질로 찍히게 되었습니다.</br>
> 이를 통해 사용자가 V자를 하고 사진을 찍거나 손바닥이 향하게 찍은 사진을 SNS에 게시하게 되면,</br> 
> 사용자가 게시한 사진을 통해 지문을 해킹할 수 있게 되었습니다.</br>
> 본 팀에서는 이를 방지하기 위한 「????」을 설계하였습니다.


## 2. How to make this System
### 2-1. Hand Keypoint Detection
> 본 기법은 손의 마디를 인식하는 Open CV 기법입니다.</br>
### 2-2. // 타원 그린거 → 타원 부분을 blur 처리 하는 거 → noise 줄인 거
> 본 기법은 손의 마디를 인식하는 Open CV 기법입니다.</br>

## n. Result
> 사진이나 동영상에 찍힌 지문을 Blur 처리하는 것을 성공하였습니다.</br>
</br>
<hr/>
</br>

# 00. 환경 설정하는 순서
## 2-1. Anaconda3
>1. conda환경에서 파이썬 3.6ver으로 environment를 새로 만들어 줘야합니다.</br>
>//Anaconda 3를 설치하면 Python도 함께 설치되어 별도 설치할 필요가 없습니다.</br>
> → 아래 사이트를 참고하시면 됩니다.</br></br>
>http://blog.naver.com/PostView.nhn?blogId=baek2sm&logNo=221378601592&categoryNo=0&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=postView</br></br>
>2. 필수 라이브러리를 설치해야 합니다.</br></br>
>[Open CV 설치하는 법] </br>
>https://dejavuqa.tistory.com/228 </br></br>
>ps.pip install numpy,pandas,matplotlib,pillow 등 여러가지 설치할 라이브러리가 많습니다.</br>해당 부분은 필요한 부분만 선택하여 설치하면 됩니다.</br>

## 2-2. 본 프로젝트에서는 caffe를 사용합니다.</br>
>1. 해당 프로젝트에서 사용되는 Model을 다운받습니다.</br>
> → 아래의 사이트를 참고하시면 됩니다.</br></br>
>    [Model 다운 받는 곳] </br>
>http://posefs1.perception.cs.cmu.edu/OpenPose/models/hand/pose_iter_102000.caffemodel

</br></br>
