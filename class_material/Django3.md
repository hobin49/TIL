 

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

- 변수는 "<>"에 정의하며 view 함수의 인자로 할당됨
- 기본 타입은 string이며 5가지 타입으로 명시할 수 있다.
- str
  - '/'를 제외하고 비어 있지 않은 모든 문자열
  - 작성하지 않을 경우 기본 값
- int
  - 0 또는 양의 정수와 매치

```python
#urls.py

urlpatterns = [
  ...,
  # path('hello/<str:name>/', views.hello),
  path('hello/<name>/', views.hello),
]
```

- variable routing으로 할당된 변수를 인자로 받고 템플릿 변수로 사용할 수 있다

```html
 <!-- 이건 html의 공통적인 부분을 하나로 묶어서 사용한다-->
{% extends 'base.html' %}


<!-- 내용만 채워 넣는다-->
{% block content %}
	<h1>만나서 반가워요 {{name}}님!</h1>
{% endblock %}
```



### Template inheritance

- 템플릿 상속

  - 템플릿 상속은 기본적으로 코드이 재사용성에 초점을 맞춘다.

  - 템플릿 상속을 사용하면 사이트의 모든 공통 요소를 포함하고, 하위 템플릿이 재정의(override) 할 수 있는 블록을 정의하는 기본 'skeleton' 템플릿을 만들 수 있다

  - 만약 모든 템플릿에 부트스트랩을 적용하려면 어떻게 해야 할까?

    - 모든 템플릿에 부트스트랩 CDN을 작성해야 할까?

  - 템플릿 상속에 관련된 태그

    ```html
    {% extends '' %}
    ```

    - 자식(하위)템플릿이 부모 템플릿을 확장한다는 것을 알림
    - 반드시 템플릿 최상단에 작성 되어야 한다. (즉, 2개 이상 사용할 수 없다)

    ```python
    {% block content %}{% endblock content %}
    ```

    - 하위 템플릿에서 재지정(override)할 수 있는 블록을 정의
    - 즉, 하위 템플릿이 채울 수 있는 공간
    - 가독성을 높이기 위해 선택적으로 endblock 태그에 이름을 지정할 수 있다
    - Index 템플릿에서 base 템플릿을 상속받음
    - Bootstrap이 적용되었는지 확인한다

    ```html
    <!-- index.html -->
    {% extends 'base.html' %}
    
    {% block content %}
    	<h1>만나서 반가워요</h1>
    	<a href="/greeting/">greeting</a>
    	<a href="/dinner/">dinner</a>
    {% endblock content %}
    ```

    













### Sending and Retrieving form data

- 데이터를 보내고 가져오기
- 웹은 다음과 같이 가장 기본적으로 클라이언트-서버 아키텍처를 사용
  - 클라이언트가 서버에 요청을 보내고, 서버는 클라이언트에 요청에 응답한다.
- 클라이언트 측에서 HTML form은 HTTP 요청을 서버에 보내는 가장 편리한 방법
- 이를 통해 사용자는 HTTP 요청에서 전달할 정보를 제공할 수 있다.
- HTML `<form>` element
  - 데이터가 전송되는 방법을 정의
  - 웹에서 사용자 정보를 입력하는 여러 방식을 제공하고, 사용자로부터 할당된 데이터를 서버로 전송하는 역할을 담당한다.
  - 데이터를 어디로 어떤 방식으로 보낼지
  - 핵심 속성
    - action 
      - 입력 데이터가 전송될 URL을 지정
      - 데이터를 어디로 보낼 것인지 지정하는 것이며 이 값은 반드시 유효한 URL이어야 한다.
      - 만약 이 속성을 지정하지 않으면 데이터는 현재 form이 있는 페이지의 URL로 보내진다.
    - Method
      - 데이터를 어떻게 보낼 것인지 정의
      - 입력 데이터의 HTTP request methods를 지정
      - HTML form 데이터는 오직 2가지 방법으로만 전송 할 수 있는데 바로 GET 방식과 POST 방식

- HTML `<input>` element

  - 사용자로부터 데이터를 입력 받기 위해 사용한다.

  - "type"속성에 따라 동작 방식이 달라진다

    - Input 요소의 동작 방식은 type 특성에 따라 현격히 달라지므로 각각의 type은 별도로 MDN 문서에서 참고하여 사용하도록 한다
    - type을 지정하지 않은 경우, 기본값은 'text'

  - 핵심 속성

    - name

      - form을 통해 데이터를 제출했을 때 name 속성에 설정된 값을 서버로 전송하고, 서버는 name 속성에 설정된 값을 통해 사용자가 입력한 데이터 값에 접근할 수 있다

      - 주요 용도는 GET/POST 방식으로 서버에 전달하는 파라미터(name은 key, value는 value)로 매핑하는 것

        - GET 방식에서는 URL형식으로 데이터를 전달

          `?Key=value&key=value/`

      - HTML `<input>` element 작성

        ```html
        {% extends 'base.html' %}
        
        {% block content %}
        	<h1>Throw</h1>
        	<form action="#" method="#">
        		<label for="message">Throw</label>
            <input type="text" id="message" name="message">
            <input type="submit">
        	</form>
        {% endblock %}
        ```

- HTTP request methods (1 / 2)

  - HTTP
    - HTML 문서와 같은 리소스(데이터, 자원)들을 가져올 수 있도록 해주는 프로토콜(규칙, 규약)
  - 웹에서 이루어지는 모든 데이터 교환의 기초
  - HTTP는 주어진 리소스가 수행 할 원하는 작업을 나타내는 request methods를 정의

- HTTP request methods(2/2)

  - 자원에 대한 행위(수행하고자 하는 동작)을 정의
  - 주어진 리소스(자원)에 수행하길 원하는 행동을 나타낸다
  - HTTP Method 예시
    - GET, POST, POST, DELETE
  - GET이 아닌 다른 method는 추후 다시 알아볼 예정

- GET

  - 서버로부터 정보를 조회하는 데 사용
    - 즉, 서버에게 리소스를 요청하기 위해 사용
  - 데이터를 가져올 때만 사용해야 함
  - 데이터를 서버로 전송할 때 Query string parameters를 통해 전송
    - 데이터는 URL에 포함되어 서버로 보내짐
  - GET과 get 모두 대소문자 관계없이 동일하게 동작하지만 명시적 표현을 위해 대문자 사용을 권장
  - 데이터를 입력 후 submit 버튼을 누르고 URL의 변화를 확인한다.

- Query String Parameters

  - 사용자가 입력 데이터를 전달하는 방법 중 하나로, url 주소에 데이터를 파라미터를 통해 넘기는 것
  - 이러한 문자열은 앰퍼샌드(&)로 연결된 key=value 쌍으로 구성이며 기본 URL과 물음표(?)로 구분된다
    - 예시
      - http://host:port/path?key=value&key=value
  - Query String이라고도 함
  - 정해진 주소 이후에 물음표를 쓰는 것으로 Query String이 시작함을 알린다
  - "key=value"로 필요한 파라미터의 값을 적는다
    - "="로 key와 value가 구분된다
  - 파라미터가 여러 개일 경우 "&"를 붙여 여러 개의 파라미터를 넘길 수 있다

### Retrieving the data (Server)

- "데이터 가져오기(검색하기)"
- 서버는 클라이언트로 받은 key-value 쌍의 목록과 같은 데이터를 받게 됨
- 이러한 목록에 접근하는 방법은 사용하는 특정 프레임워크에 따라 다르다
- 우리는 Django 프레임워크에서 어떻게 데이터를 가져올 수 있을지 알아볼 것이다.
  - throw가 보낸 데이터를 catch에서 가져오기
- throw 페이지에서 form의 action 부분을 마저 작성하고 데이터를 보낸다.
- 실습 편의를 위해 index 페이지에 throw 하이퍼 링크를 작성한다.

```html
<!--throw.html-->
{% extends 'base.html' %}

{% block content %}
	<h1>Throw</h1>
	<form action="/catch/" mehtod="GET"> 
		<label for="message">Throw</label>
    <input type="text" id="message" name="message">
    <input type="submit">
	</form>

	<a href="/index/">뒤로</a>

{% endblock %}

<!--index.html-->
{% extends 'base.html' %}

{% block content %}
	...
	<a href="/throw/">throw</a>
{% endblock %}
```



- 주소(누구에게) => https://search.naver.com
- 주문서(무엇을) => /search.naver?query=아이유
- https://search.naver.com/search.naver?query=아이유
  - ? 는 쿼리 파라미터라고 부르며 form에 input창을 통해서 전달되는 데이터가 ?뒤에 여러개가 올 수 있다.
- `code .`  Manage.py 가 있는 곳에 실행된다.

- 구글은 검색어를 받아서 /search로 보낸다. 

- 어떤 정보가 넘어오는지 장고 자체가 request라는 객체라는 정보 안에 담겨져 있다.
- Method:GET 아무것도 쓰지않으면 디폴트값으로 get하는 함수를 통해서 정보를 가져온다.
- `pip install black` => 코드 스타일 통일