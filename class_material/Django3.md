 

### Variable routing

- 필요성
  - 템플릿의 많은 부분이 반복
  - URL 주소를 변수로 사용하는 것을 의미한다. 
  - URL의 일부를 변수로 지정하여 view 함수의 인자로 넘길 수 있다.
  - 즉, 변수 값에 따라 하나의 path()에 여러 페이지를 연결 시킬 수 있다.



```html
<body>
  <!--fake.naver.html-->
  <h1>Naver</h1>
  <form action="https://www.naver.com">
    검색어: <input type="text">
    <input type="submit">
  </form>
  <!-- fake.html-->
  <h1>fake 궁합앱</h1>
  <form action="">
    당신의 이름: <input type="text"><br>
    그분의 이름: <input type="text">
    <input type="submit">
  </form>
</body>
```







### Sending and Retrieving form data

- 데이터를 보내고 가져오기
- 웹은 다음과 같이 가장 기본적으로 클라이언트-서버 아키텍처를 사용
  - 클라이언트가 서버에 요청을 보내고, 서버는 클라이언트에 요청에 응답한다.
- HTML `<form>` element
  - 데이터가 전송되는 방법을 정의
  - 웹에서 사용자 정보를 입력하는 여러 방식을 제공하고, 사용자로부터 할당된 데이터를 서버로 전송하는 역할을 담당한다.
  - 데이터를 어디로 어떤 방식으로 보낼지
  - 핵심 속성
    - action 
    - Method



- 주소(누구에게) => https://search.naver.com
- 주문서(무엇을) => /search.naver?query=아이유
- https://search.naver.com/search.naver?query=아이유
  - ? 는 쿼리 파라미터라고 부르며 form에 input창을 통해서 전달되는 데이터가 ?뒤에 여러개가 올 수 있다.
- `code .`  Manage.py 가 있는 곳에 실행된다.

- 구글은 검색어를 받아서 /search로 보낸다. 

- 어떤 정보가 넘어오는지 장고 자체가 request라는 객체라는 정보 안에 담겨져 있다.
- Method:GET 아무것도 쓰지않으면 디폴트값으로 get하는 함수를 통해서 정보를 가져온다.
- `pip install black` => 코드 스타일 통일