- 최종완성본




![Large GIF (780x602)](https://github.com/hobin49/TIL/assets/67423191/d4997c83-f330-4ba5-8d04-97207b5c854e)



#### 스크롤 위치에 따라 opacity가 변하는 애니메이션 만들기

일정 스크롤 위치를 기준으로 이전 이미지가 fade되어야 한다.

여기서 1차 방정식을 사용해야 한다. 2번째 이미지가 등장하는 시점을 650이라고 하면 그때 opacity는 1이다.

그리고 최종적으로 완벽하게 덮히는 시점은 1150이다. 이 때의 opacity는 0이다.

2개의 방정식 그리고 a, b 구해야될 2개의 값

2차 방정식을 풀어서 답을 찾아낸 다음에, 



여기에 대입하면 된다.

1 = 650a + b

0 = 1150a + b

그리고 해당 y값을 opacity에 대입해주면 된다. 




