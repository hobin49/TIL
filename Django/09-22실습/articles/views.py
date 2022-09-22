from re import L
from django.shortcuts import render
import random

# Create your views here.
#첫 번째 인자를(요청한 사람의 정보) 핸들링해야해서 적어야한다.
def index(request):
    # 환영하는 메인 페이지를 보여준다.
    # HTTP 요청을 수신하고 응답을 반환하는 함수 작성 보낸 사람의 정보를 담아야해서 request 
    # 정적페이지가 되기 위해서 딕셔너리를 활용하교 여기서 값을 변경한다.

    names = ['주세환', '오진수', '임수경', '조병진', '차화영', '최근영', '김선교']

    #하나를 랜덤에서 뽑으려면
    name = random.choice(names)

    context = {
      'name': name,
      'img': "https://cdn.crowdpic.net/detail-thumb/thumb_d_063DE2526E75F644AA2AE4BD774FE330.jpg",  
    }
    return render(request, 'index.html', context)

# urls.py 사용자가 랜덤으로 입력한 값을 다룰 변수와 같은 역할 - name
def welcome(request, name):
    #사람들이 /welcome/본인이름을 입력하면, 환영 인사와 이름을 동시에 보여준다.
    #터미널에 출력된다. 
    # print(name)

    context = {
        'name' : name,
        'greetings': [
            '안녕하세요', 'hello', 'bon jour',
        ],
        'images': [
            "https://cdn.crowdpic.net/detail-thumb/thumb_d_063DE2526E75F644AA2AE4BD774FE330.jpg",
            "https://cdn.crowdpic.net/detail-thumb/thumb_d_063DE2526E75F644AA2AE4BD774FE330.jpg",
            "https://cdn.crowdpic.net/detail-thumb/thumb_d_063DE2526E75F644AA2AE4BD774FE330.jpg",
        ]
    }

    return render(request, 'welcome.html', context)