d=[]
for i in range(20) :
  d.append([]) # 쓰지 않으면 out of range 뜬다
  for j in range(20) : 
    d[i].append(0) 

n = int(input())
for i in range(n) :
  x, y = map(int, input().split())
  d[x][y] = 1 #흰 돌이 위치한 곳에 1을 넣는다

for i in range(1, 20) : 
  for j in range(1, 20) : #for 중첩문을 돌고
    print(d[i][j], end=' ') #공백을 두고 한 줄로 출력하고
  print() # 줄바꿈을 해준다.
