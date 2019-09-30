# 1. Project
![젭](https://user-images.githubusercontent.com/50629716/65788145-6907b400-e195-11e9-913f-74caf29c40a7.PNG)




## 1. Introduction
> 최근 카메라의 화질이 향상되면서 지문까지 고화질로 찍히게 되었습니다.</br>
> 이를 통해 사용자가 V자를 하고 사진을 찍거나 손바닥이 향하게 찍은 사진을 SNS에 게시하게 되면,</br> 
> 사용자가 게시한 사진을 통해 지문을 해킹할 수 있게 되었습니다.</br>
> 본 팀에서는 이를 방지하기 위한 「????」을 설계하였습니다.




## 2. How to make this System
### 2-1. Hand Keypoint Detection
> 본 기법은 손의 마디를 인식하는 Open CV 기법입니다.</br>
> 손가락의 마디를 인식하여 사용자의 손가락 구부림 정도, 취하고 있는 자세 등을 list에 담습니다.</br>
> list에 담긴 번호와 이미지를 매칭합니다.</br>
### 2-2. Draw ellipses
> 본 기법은 손에 타원을 그려주는 기법입니다.</br>
> 먼저, 손 끝마디와 두번째 마디의 중심점을 잡습니다.</br>
> 손 끝마디와 두번째 마디 간격에 맞게 원의 크기를 정해줍니다.</br>
> 타원을 손에 맞춰서 기울여주기 위해서 적정 각도를 찾습니다.</br>
### 2-3. Fill ellipses with Black
> Draw ellipses를 통해 그려진 타원에 검은색을 채워줍니다.</br>
> 그 이유는 블라블라블라</br>
### 2-4. XOR the Original image with black
> 원본이미지와 검은색으로 채워진 이미지를 XOR연산을 통해</br>
> 처리하여 손가락의 지문이 있는 부분만 취합니다..</br>
### 2-5. Median Blur
> 2-4에서 처리한 이미지에 median blur를 적용합니다.</br>
### 2-6. Result
> 블러처리한 이미지와 원본이미지를 합칩니다.</br>
## n. Result
> 사진이나 동영상에 찍힌 손가락의 지문 부분만 Blur 처리하는 데 성공하였습니다.</br>
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


<img src="https://user-images.githubusercontent.com/50629716/65842742-96f12200-e368-11e9-887d-983ed18566fd.PNG" width="70%"></img>
