### Auth Q&A

- 자료를 숙지 
- account.User에 만들고 시작하는지? 왜 auth.User를 사용하지 않는지?
  - Model은 DB를 조작 밀접한 관계를 가지고 있다. 모델의 필도가 수정되거나 하는 것들은 마이그레이션 파일 등을 통해서 자동으로 관리 모델 자체가 변화하고 하면 별도의 수작업이 필요하다.
  - **우리는 django 내부가 아닌 accounts User 만들고 간다** 
- 왜 AbstractUser를 상속받나요? User를 상속받나?
  - User을 상속받는 것을 받으면 그게 똑같은 상황
- 모델의 필드가 수정되거나 하는 것들은 마이그레이션 파일 등을 통해서 자동으로 관리 

- UserCreationForm의 custom? 
  - UserCreationForm => ModelForm 상속 받아서 만들고 있다(슈퍼캡짱중요)
  - 우리가 ModelForm을 정의할 때 가장 중요했던 설정은 모델과 필드이다! 
- AUTH_USER_MODEL 다른 것을 쓰고 UserCreationForm 을 쓰면 오류가 발생한다.
- 클래스
  - 부모 클래스에 정의된 속성/메서드 (기능) 상속 받아서
- ModelForm
  - meta, 모델필드가 필요하고, is_valid, request.post를 할 수 있었다.
  - ArticleForm(필드 모델을 상속 받는다) - 같은 종족
  - UserCreationForm(필드 모델을 상속 받는다.)- 같은 종족

- passoword1, 2 는 결국 모델 필드에서의 필드를 정의한 것이다.
- 상속 받은것은 필드와 구성만 달라진다
- 비밀번호 변경은 다른 페이지에서 바꾼다. 암호화를 해서 저장해야한다. 
  - UserChangeForm(ModelForm)- 모델의 필드를 의미
  - SetPasswordForm(Forms.Form)- 모델과 연결되어 있지 않은 form(범용적)
- Get_user_model의 사용 이유?
  - User 모델이라는게 결국에는 변경이 가능한 친구이면서 django + 사용자 쓰는 것 결국에는 변경 가능한 것은 어찌 되었는지 변수화 등을 통해서 얘를 호출하도록 하는게 가장 좋다, 범개발영역에서의 핵심 관통하는 내용 url에 name을 붙여두고 함수로 해석해서 쓰자
  - {% url 'articles:index %'}-> 일종의 함수
  - 그래서 유저 모델 클래스는 어딘가에 있겠지만 이 것을 get_user_model() 호출해서 쓰자 그러면 알아서 AUTH_USER_MODEL에 정의된 클래스를 준다. 





### 로그인에 대한 이해 

- HTTP

  - Hyper Text Transfer Protocol

  - HTML 문서와 같은 리소스들을 가져올 수 있도록 해주는 프로토콜(규칙, 규약)

  - 웹(WWW)에서 이루어지는 모든 데이터 교환의 기초

  - 클라이언트 - 서버 프로토콜이라고도 부른다.

  - 요청

    - 클라이언트에 의해 전송되는 메시지

  - 응답

    - 서버에서 응답으로 전송되는 메시지

  - 비 연결 지향

    - 서버의 요청에 대한 응답을 보낸 후 연결을 끊는다
      - 예를 들어 우리가 네이버 메인 페이지를 보고. 있을 때 우리는 네이버 서버와 연결되어 있는 것이 아니다
      - 네이버 서버는 우리에게 메인 페이지를 응답하고 연결을 끊는 것

  - 무상태

    - 연결을 끊는 순간 클라이언트와 서버 간의 통신이 끝나며 상태 정보가 유지되지 않는다
    - 클라이언트와 서버가 주고받는 메시지들은 서로 완전히 독립적

  - 어떻게 로그인 상태를 유지할까?

    - 우리가 로그인을 하고 웹 사이트를 사용할 때 페이지를 이동해도 로그인 "상태"가 유지됨
    - 서버와 클라이언트 간 지속적인 상태 유지를 위해 쿠키와 세션이 존재한다. 

  - 쿠키

    - 서버가 사용자의 웹 브라우저(클라이언트)에 전송하는 작은 데이터 조각
      - 브라우저(클라이언트)는 쿠키를 로컬에 KEY-VALUE의 데이터 형식으로 저장
      - 동일한 서버에 재요청 시 저장된 쿠키를 함께 전송
    - 쿠키는 서로 다른 요청이 동일한 브라우저로부터 발생한 것인지 판단할 때 주로 사용된다
      - 상태가 없는 HTTP에서 상태 정보를 관리, 사용자는 로그인 상태를 유지할 수 있다.
    - 사용자가 웹사이트를 방문할 경우 해당 웹사이트의 서버를 통해 사용자의 컴퓨터에 설치되는 작은 기록 정보 파일

  - 쿠키 사용 목적

    - 세션 관리
      - 로그인, 아이디 자동완성, 공지 하루 안 보기, 팝업 체크, 장바구니 등의 정보 관리
    - 개인화
      - 사용자 선호, 테마 등의 설정

    - 트래킹
      - 사용자 행동 분석

  - 세션

    - 사이트와 특정 브라우저 사이의 state(상태)를 유지시키는 것

    - 클라이언트가 서버에 접속하면 서버가 특정 session id를 발급하고, 클라이언트는 session id를 쿠키에 저장

      - 클라이언트가 다시 동일한 서버에 접속하면 요청과 함께 쿠키를 서버에 전달
      - 쿠키는 요청 때마다 서버에 함께 전송 되므로 서버에서 session id를 확인해 알맞은 로직을 처리

    - 페이지 하루 안 보이면 브라우저에만 기록해서 다른 브라우저를 열면 다시 뜬다.

    - Session id는 세션을 구별하기 위해 필요하며, 쿠키에는 session id만 저장한다. 

    - Session cookie

      - 현재 세션이 종료되면 삭제된다
      - 브라우저 종료와 함께 세션이 삭제된다. 

    - Persistent cookies

      - Expires 속성에 지정된 날짜 혹은 Max-Age 속성에 지정된 기간이 지나면 삭제된다.

    - Session in Django

      - Django는 database-backed sessions 저장 방식을 기본 값으로 사용
        - Session 정보는 Django DB의 django_session 테이블에 저장
        - 설정을 통해 다른 저장방식으로 변경 가능
      - Django는 특정 session id를 포함하는 쿠키를 사용해서 각각의 브라우저와 사이트가 연결된 session을 확인한다.

    - 장고는 세션을 자동으로 해준다

      `django.contrib.sessions`

    - 요청이 들어오면 (세션->csrf->인증) 이 순서로 나간다. MIDDLEWARE은 요청과 응답을 처리하는 로직들이 담겨 있다.

### Login

- 로그인을 위한 built-in form
  - 로그인 하고자 하는 사용자 정보를 입력 받는다.(username, password)
  - ModelForm이 아닌 일반 Form을 상속 받고 있으며, request를 첫번째 인자로 취한다. 

- 로그인 기능

  - Article Create / User Create!
  - URL: GET/accounts/login/
  - 처리 
    - 사용자에게 Form을 제공한다.

  - URL : POST / accounts /login/
  - 처리
    - (로그인) 로직처리
      - 사용자인지 확인하고,  django_session 테이블에 저장, 쿠키 주기
    - (성공)게시글 목록 페이지로 redirect
    - (실패) 로그인 Form

- 로그인 로직 작성
  - 일반적인 ModelForm 기반의 Create 로직과 동일하지만,
    - ModelForm이 아닌 Form으로 필수 인자 구성이 다르다
    - DBd에 저장하는 것 대신 세션에 유저를 기록하는 함수 호출함
      - View 함수와 이름이 동일하며 변경하여 호출
      - 로그인 URL이 '/accounts/login/'에서 변경되는 경우 settings.py LOGIN_URL을 변경해야 한다.

```python
urlpattern = [
  path("login/", views.login, name = "login")
]

# views.py 
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
def login(request):
  if request.method == "POST":
    	# AuthenticationForm은 ModelForm이 아니다. 
    	form = AuthenticationForm(request, data=request.POST)
      if form.is_valid:
        #유저정보를 form으로부터 가져올 수 있다.
        #login 함수는 request, user 객체를 인자로 받는다
        #user 객체는 어디있어요? 바로 form에서 인증된 유저 정보를 받을 수 있다.
        	auth_login(request, form.get_user())
          return redirect("accounts:index")
  else:
    	form = AuthenticationForm()
  context = {
    	'form' : form
  }
  return render(request, "acocunts/login.html", context)
```

```html
{% extends 'base.html' %}

{% block content %}
	<h1>로그인</h1>
	<form action="" method="POST">
    {% csrf_token %}
    {% bootstrap_form form %}
    {% bootstrap_button button_type="submit" content="OK" %}  
	</form>
```

- login()

  - login(request, user, backend=None)
  - 인증된 사용자를 로그인
    - 유저의 ID를 세션에 저장하여 세션을 기록
  - HttpRequest 객체와 User 객체가 필요
    - 유저 정보는 반드시 인증된 유저 정보여야 한다.
      - authenticate()함수를 활용한 인증
      - AuthenticationForm을 활용한 is_valid

- get_user()

  - AuthenticationForm의 인스턴스 메서드
  - 유효성 검사를 통과했을 경우 로그인 한 사용자 객체를 반환한다. 

- 세션 데이터 확인하기

  - 로그인 후 개발자 도구와 DB에서 django로부터 발급받은 세션 확인
  - django_session 테이블에서 확인

  - 브라우저에서 확인
    - 개발자도구-Application-Cookies

- 로그인 링크 작성

  ```html
  <!-- base.html -->
  <body>
    <div class = "container">
      <a href="{% url 'accounts:login' %}">login</a>
      <hr>
      {% block content %}
      {% endblock content %}
    </div>
  </body>
  ```

### Authentication with User

- 현재 로그인 되어 있는 유저 정보 출력하기

- 템플릿에서 인증 관련 데이터를 출력하는 방법

  ```html
  <body>
    <div class = "container">
      <h3>Hello, {{ user }}</h3>
      <a href="{% url 'accounts:login' %}">login</a>
      <hr>
      {% block content %}
      {% endblock content %}
    </div>
  </body>
  ```

- 어떻게 base 템플릿에서 context 데이터 없이 user 변수를 사용할 수 있는 걸까?

  - Settings.py의 context processors 설정의 'Django.contrib.auth.context_processors.auth'

- Cotext processors

  - 템플릿이 렌더링 될 때 호출 가능한 컨텍스트 데이터 목록
  - 작성된 컨텍스트 데이터는 기본적으로 템플릿에서 사용 가능한 변수로 포함된다
  - 즉, django에서 자주 사용하는 데이터 목록을 미리 템플릿에 로드 해 둔 것

- Django.contrib.auth.context_processors.auth

  - 템플릿 변수 {{user}}
    - 클라이언트가 로그인한 경우 User 클래스의 인스턴스
    - 클라이언트가 로그인하지 않은 경우 AnonymousUser 클래스의 인스턴스 



### Logout

- logout()
  - logout(request)
  - 요청 유저에 대한 세션 정보를 삭제한다
    - DB에서 session data 삭제
    - 클라이언트의 쿠키에서 sessionid 삭제
  - HttpRequest 객체를 인자로 받고 반환 값이 없다
  - 사용자가 로그인하지 않은 경우 오류를 발생시키지 않는다.

```python
#urls.py
path('logout/', views.logout, name="logout")
#accounts/views.py
from django.contrib.auth import logout as auth_logout
def logout(request):
		auth_logout(request)
    return redirect('articles:index')
```

```html
<body>
  <div class = "container">
    <h3>Hello, {{ user }}</h3>
    <a href="{% url 'accounts:login' %}">login</a>
    <form action ="{% url 'accounts:logout'%}" method="POST">
      {% csrf_token %}
      <input type="submit" value="Logout">
    </form>
    <hr>
    {% block content %}
    {% endblock content %}
  </div>
</body>
```



### Limiting access to logged-in users

- 개요
  - 로그인 사용자에 대한 접근 제한하기
  - 로그인 사용자에 대한 접근을 제한하는 2가지 방법
    - is_authenticated attribute를 활용한 조건문
    - The login_required decorator를 활용한 view 제한

- is_authenticated
  - User Model의 속성(attributes) 중 하나
  - 사용자가 인증 되었는지 여부를 알 수 있는 방법
  - 모든 User 인스턴스에 대해 항상 True인 읽기 전용 속성
    - AnonymousUser에 대해서는 항상 False
  - 일반적으로 request.user에서 이 속성을 사용(request.user.is_authenticated)
  - 권한과는 관련이 없고, 사용자가 활성한 상태이거나 유효한 세션을 가지고 있는지도 확인하지 않았다. 

- is_authenticated

  - 인증된 사용자만 게시글 작성 링크를 볼 수 있도록 처리하기
    - URL을 직접 입력하면 게시글 작성 페이지로 갈 수 있다
    - View에서의 처리도 반드시 필요하다

  ```html
  {% extends 'base.html' %}
  
  {% block content %}
  	<h1>Articles</h1>
  	{% if request.user.is_authenticated %}
  		<a href="{% url 'articles:create' %}">CREATE</a>
  	{% else %}
  		<a href="{%url 'accounts:login' %}">새 글을 작성하려면 로그인하세요</a>
  	{% endif %}
  
  {% endblock content %}

- 인증된 사용자라면 로그인 로직을 수행할 수 없도록 처리

  ```python
  # accounts/views.py
  
  def login(request):
    	if request.user.is_authenticated:
        	return redirect('articles:index')
      ...
  ```

  

- 디버깅은 역순으로 
- Authentication은 modelform이 없어요. forms.Form를 상속 받고 있었다. 

- 모델폼이 없어서 form.save()는 없어 세션에 저장

```html
{% if request.user.is_authenticated %}
	<span>{{request.user}}</span>
	<a href="">로그아웃</a>
{% else %}
	<a href="{% url 'accounts:signup' %}">회원가입</a>
	<a href="{% url 'accounts:login' %}">회원가입</a>
```

- login_required

  - login_required decorator

    - 사용자가 로그인 되어 있으면 정상적으로 view 함수를 실행
    - 로그인 하지 않은 사용자의 경우 settings.py의 LOGIN_URL 문자열 주소로 redirect

  - 로그인 상태에서만 글을 작성/수정/삭제 할 수 있도록 변경

    ```python
    from django.contrib.auth.decorators import login_required
    
    @login_required
    def create(request):
      	pass
    
    ```

- login_required 적용 확인하기

  - /articles/create/로 브라우저에 직접 요청
  - 로그인 페이지로 리다이렉트 및 URL 확인
    - 인증 성공 시 사용자가 redirect 되어야하는 경로는 "next"라는 쿼리 문자열 매개 변수에 저장된다
    - 예시) /accounts/login/?next=/articles/create/

```python
# accounts/views.py
def login(request):
  	if request.user.is_authenticated:
      	return redirect('articles:index')
    if request.method == "Post":
      	form = AuthenticationForm(request, request.POST)
        if form.is_valid():
          	auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')
```

- "Next" query string parameter 주의 사항
  - 만약 login 템플릿에서 form action이 작성되어 있다면 동작하지 않는다
  - 해당 action 주소 next 파라미터가 작성 되어 있는 현재 url이 아닌 /accounts/login/으로 요청을 보내기 때문이다.

- 코드의 실행순서
  - 사용자가 어떠한 버튼 안 만들어놨는데, URL로 직접 접근할 수 있다
    - 어디서 막을 것이냐?
    - View에서 서버 막아두면 된다
  - 인증여부를 직접 조건문 => @login_required 데코레이터를 쓸 수 있다
    - 이 친구의 역할은 아래와 같은 URL로 로그인페이지로 보내줌
    - `http://127.0.0.1:8000/acocunts/login/?next=/articles/1/update/`
  - 사용자가 로그인 HTML Form을 보고 내용을 채우고 로그인 버튼을 누르겠죠
  - URL: POST `http://127.0.0.1:8000/acocunts/login/?next=/articles/1/update/`
  - View:login
  - redirect를 할 때 URL Get 파라미터로 보내준 값을 쓴다.
  - 단축 평가이다. 아까 if문이랑 똑같다.
    - 없으면 None or 'articles:index'
    - 있으면 /articles/1/update/ or ''articles:index"
  - Or은 하나만 True면 True임 즉 단축평가로 앞에 값이 True면 리턴하고 뒤는 X 앞에 값이 False면 뒤를 리턴함







