# 1. Project
![젭](https://user-images.githubusercontent.com/50629716/65788145-6907b400-e195-11e9-913f-74caf29c40a7.PNG)
</br>

# 2. Introduction
> 최근 카메라의 화질이 향상되면서 지문까지 고화질로 찍히게 되었습니다.</br>
> 이를 통해 사용자가 V자를 하고 사진을 찍거나 손바닥이 향하게 찍은 사진을 SNS에 게시하게 되면,</br> 
> 사용자가 게시한 사진을 통해 지문을 해킹할 수 있게 되었습니다.</br>
> 본 팀에서는 딥 러닝 기반 비전인식 기술을 사용해 이를 방지하기 위한 이미지 지문 보호 프로그램을 설계하였습니다.
</br>


# 3. Environment and Installation
### OS
* OS는 Windows 환경에서 개발되었습니다.
* Server는 Ubuntu 환경을 통해 구축했습니다.

### 3.1 개발 환경
* Anaconda3 설치  
  * <a href ="http://blog.naver.com/PostView.nhn?blogId=baek2sm&logNo=221378601592&categoryNo=0&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=postView">Python3.6x 버젼을 가상환경으로 추가.</a>
* Pycharm 설치
  * Pycharm에서 <a href="https://user-images.githubusercontent.com/50629716/65853370-3bd52480-e394-11e9-9d83-050eef6cd25a.PNG">Settings-> Project Interpreter</a>에서 경로를 Anaconda3의 가상환경으로 추가한 Python3을  경로를 설정
  
### 3.2 설치 프로그램
* Python 3.6x Version(추천), ※ 3.7x같은 경우는 때에 따라 불편한 경우가 많음.
* <a href="https://dejavuqa.tistory.com/228">Opencv-conrtib 4.1.1v</a>
* Numpy 1.17.1v

### 3.3 Model 설치
Caffe로 만든 신경망 모델을 설치해 Model폴더에 추가</br>
http://posefs1.perception.cs.cmu.edu/OpenPose/models/hand/pose_iter_102000.caffemodel
</br>

> 3.1 ~ 3.3 순서대로 필수 환경을 구축해 주시기 바랍니다.<br>
> 구축시 문제가 생기면 언제든 메일 주세요(wonseok3629@gmail.com)

# 4. Manual
### 1. Server에서 실행하기.
1. 웹에서 http://cdy235.iptime.org:5000/test 사이트를 들어갑니다. 

2. Local환경에서 자신이 변환 하고자 하는 이미지를 올립니다.<br>

3 쿼리전송 버튼을 눌러 서버에서 변환된 이미지를 받습는다.<br>

### 2. Pycharm에서 Compile하기.
1.환경을 구축한후 다운받은 모델을 프로젝트의 Model폴더에 넣습니다.<br>
<img src="https://user-images.githubusercontent.com/50629716/65876724-e2391e00-e3c4-11e9-8e89-1c75c537fdd3.PNG" width="40%"></img></br>

2.원하는 이미지를 Image폴더에 넣습니다.<br>

3. fingerprint_Image.py에 path변수를 자신이 넣은 이미지의 이름으로 변경해 줍니다.
<img src="https://user-images.githubusercontent.com/50629716/65876971-87ec8d00-e3c5-11e9-8309-28f59e09b637.PNG" width="40%"></img></br>

4. Compile 합니다.
 


# 5. How to make this System
## 5.1 Download Model and weights
> 본 기법은 손의 마디를 인식하는 Open CV 기법입니다.</br>
> 손가락의 마디를 인식하여 사용자의 손가락 구부림 정도, 취하고 있는 자세 등을 list에 담습니다.</br>
> list에 담긴 번호와 이미지를 매칭합니다.</br>
## 5.2 apply the model
> 손 끝마디와 두번째 마디 간격에 맞게 원의 크기를 정해줍니다.</br>
> 타원을 손에 맞춰서 기울여주기 위해서 적정 각도를 찾습니다.</br>
<img src="https://user-images.githubusercontent.com/50629716/65854563-f4e92e00-e397-11e9-8310-2cc8085899db.PNG" width="40%"></img>
## 5.3 Draw ellipses in fingers
> Draw ellipses를 통해 그려진 타원에 검은색을 채워줍니다.</br>
## 5.4 XOR the Original image with black
> 원본이미지와 검은색으로 채워진 이미지를 XOR연산을 통해</br>
> 처리하여 손가락의 지문이 있는 부분만 취합니다..</br>
<img src="https://user-images.githubusercontent.com/50629716/65855168-7b523f80-e399-11e9-9982-1a6ecdba1fd9.PNG" width="40%"></img>
## 5.5 Median Blur
> 2-4에서 처리한 이미지에 median blur를 적용합니다.</br>
## 5.6 Synthesis original and blur images
> 블러처리한 이미지와 원본이미지를 합칩니다.</br>
</br>

# 6. Result
> 사진이나 동영상에 찍힌 손가락의 지문 부분만 Blur 처리하는 데 성공하였습니다.</br>
<img src="https://user-images.githubusercontent.com/50629716/65875074-abadd400-e3c1-11e9-844f-a7508da791d4.PNG" width="70%"></img>
</br>

# 7. References
* <a href="https://answers.opencv.org/question/105994/blurred-mask-on-image/">Image bitmapping</a>
* <a href="https://www.learnopencv.com/hand-keypoint-detection-using-deep-learning-and-opencv/">Hand Landmark</a>
* <a href="https://webnautes.tistory.com/1255">Image Blur</a>
</br>

# 8. Inquiry
Email : wonseok3629@gmail.com로 문의해 주시거나 Issue를 달아주시면 감사하겠습니다.
</br>


