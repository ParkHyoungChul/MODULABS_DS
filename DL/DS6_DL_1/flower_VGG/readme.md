# 꽃분류 모델을 만들기 : VGG16 전이학습

https://www.tensorflow.org/datasets/catalog/tf_flowers?hl=ko
위 링크에서 데이터를 가져왔습니다

설명이 조금 불친절하다
총 3,670개의 데이터 

라벨은 총 5개   
0 (dandelion) - 민들레?     
1 (daisy) - 데이지    
2 (tulips) - 튤립   
3 (sunflowers) - 해바라기   
4 (roses) - 장미   

<img width="600" height="288" alt="image" src="https://github.com/user-attachments/assets/18d810bd-58bb-400e-9160-8e5596020e2c" />

# 실험결과
<img width="1281" height="711" alt="image" src="https://github.com/user-attachments/assets/333a7a61-721e-4577-8515-f9d1267680f7" />

4번째 튤립인데 장미로 예측함.. 사실 나도 보라 장미인줄
1행 마지막 사진도 어려움
3행의 맨오른쪽 두번째 = 꽃이 아니잖아..

## 회고
꽃을 분류하는건 사진 이슈가 좀있다 꽃이 아닌것같은것도있고 사진이 아닌것도있다 꽃이아니라 다른 오브젝트가 많은경우도있다
