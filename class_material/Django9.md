### DJango Auth

- 게시판과 무엇이 같고 무엇이 다를까요? 

- Django authentication system(인증 시스템)은 인증(Authentication)과 권한(Autorization) 부여를 함께 제공(처리)하고 있다.
  - User
  - 권한 및 그룹
  - 암호 해시 시스템(유저에 관한 정보는 민감하니 잘 관리해야한다.)
  - Form 및 View 도구
  - 기타 적용가능한 시스템
  
- 필수 구성은 settings.py의 INSTALLED_APPS에서 확인 가능
  - django.contrib.auth
    - 지난 주에 배운 superuser => admin(기본 내장된 auth)
  
- 개요
  - Authentication(인증)
    - 신원 확인
    - 사용자가 자신이 누구인지 확인하는 것
  - Authorization (권한, 허가)
    - 권한 부여 
    - 인증된 사용자가 수행할 수 있는 작업을 결정
  
- 우리가 app_name을 쓰는 이유는 기본적으로 URL을 모두 변수화해서 쓰고 있다.

- 사전 설정

  - 멀티 accounts app 생성 및 등록

    `python manage.py startapp accounts`

    ```python
    #settings.py 
    INSTALLED_APPS = [
      'accounts',
      	...
    ]
    # auth와 관련한 경로나 키워드들은 Django 내부적으로 accounts라는 이름으로 사용하고 있기 때문에 되도록 accounts로 지정하는 것을 권장
    # 다른 이름으로 설정해도 되지만 나중에 추가 설정을 해야 할 일들이 생기게 된다. 
    ```

  - url 분리 및 매핑

    ```python
    # accounts/urls.py
    
    from django.urls import path
    from . import views
    
    app_name = "accounts"
    urlpatterns = [
      
    ]
    
    #메인Pjt/urls.py
    urlpatterns = [
      ...,
      path('accounts/', include('accounts.urls')),
    ]
    ```


### User model 활용하기

- Django User Model

  - "Custom User Model"로 대체하기
  - Django는 기본적인 인증 시스템과 여러 가지 필드가 포함된 User Model을 제공, 대부분의 개발 환경에서 기본 User Model을 Custom User Model로 대체함
  - Django는 새 프로덱트를 시작하는 경우 비록 기본 User 모델이 충분 하더라도 커스텀 User 모델을 설정하는 것을 강력하게 권장(highly recommend)
  - 커스텀 User 모델은 기본 User 모델과 동일하게 작동 하면서도 필요한 경우 나중에 맞춤 설정을 할 수 있다. 
    - 단, User 모댈 데체 작업은 프로젝트의 모든 migrations 혹은 첫 migrate를 실행하기 전에 이 작업을 마쳐야 한다.
  - 개발자들이 작성하는 일부 프로젝트에서는 django에서 제공하는 built-in User model의 기본 인증 요구사항이 적절하지 않을 수 있다
    - 예를 들어, 내 서비스에서 회원가입 시 username 대신 email을 식별 값으로 사용하기 때문에 적합하지 않다
  - Django는 현재 프로젝트에서 사용할 User Model을 결정하는 AUTH_USER_MODEL 설정 값으로 Default User Model을 재정의 할 수 있도록 한다.

- AUTH_USER_MODEL

  - 프로젝트에서 User를 나타낼 때 사용하는 모델

  - 프로젝트가 진행되는 동안(모델을 만들고 마이그레이션 한 후) 변경할 수 없다

  - 프로젝트 시작 시 설정하기 위한 것이며, 참조하는 모델은 첫 번째 마이그레이션에서 사용할 수 있어야 한다.

    - 즉 첫번째 마이그레이션 전에 확정 지어야 하는 값이다

  - 다음과 같은 기본 값을 가지고 있다.

    ```python
    #settngs.py
    AUTH_USER_MODEL = 'auth.User'
    ```

  - AUTH_USER_MODEL은 global_settings.py를 상속받아 재정의하는 파일이다

- 대체하기 

  - AbstractUser를 상속받는 커스텀 User 클래스 작성
  - 기존 User 클래스도 AbstractUser를 상속받기 때문에 커스텀 User 클래스도 완전히 같은 모습을 가지게 된다

  ```python
  # accounts/models.py
  from django.contrib.auth.models import AbstractUser
  
  class User(AbstractUser):
    	pass
  ```

  - Django 프로젝트에서 User를 나타내는데 사용하는 모델을 방금 생성한 커스텀 User 모델로 지정

  ```python
  #settings.py
  
  AUTH_USER_MODEL = 'accounts.User'
  ```

  - admin.py에 커스텀 User 모델을 등록
    - 기본 User 모델이 아니기 때문에 등록하지 않으면 admin site에 출력되지 않는다

  ```python
  # accounts/admin.py
  from django.contrib import admin
  from django.contrib.auth.admin import UserAdmin
  from .models import User
  
  admin.site.register(User, UserAdmin)
  ```

- 데이터베이스 초기화 (실습용)

  - 수업 진행을 위한 데이터베이스 초기화 후 마이그레이션(프로젝트 중간일 경우)
  - Migrations 파일 삭제
    - migrations 폴더 및 `__init__.py` 는 삭제하지 않는다
    - 번호가 붙은 파일만 삭제한다
  - db.sqlite3 삭제
  - migrations 진행
    - makemigrations
    - migrate 

- User 객체 활용

  - User 객체는 인증 시스템의 가장 기본
  - 기본 속성
    - username
    - password
    - email
    - first_name
    - last_name

- 암호 관리

  - 회원은 가입시 일반적으로 암호(password)를 저장이 필수적이며, 별도의 처리가 필요
  - Django에서는 기본으로 PBKDF2를 (Password-Based Key Derivation Function) 사용하여 저장
    - 단방향 해시함수를 활용하여 비밀번호를 다이제스트로 암호화하며, 이는 복호화가 불가능하다
      - Django는 SHA256을 활용한다
    - 단방향 해시함수의 경우 레인보우 공격 및 무차별 대입 공격 등의 문제가 발생 가능하다
    - 이를 보완하기 위하여 아래의 기법을 추가적으로 활용한다
      - 솔팅: 패스워드에 임의의 문자열인 salt를 추가하여 다이제스트를 생성
      - 키 스트레칭(Key Stretching): 해시를 여러 번 반복하여 시간을 늘린다.

- User 객체 활용

  - User 생성

    `User = User.objects.create_user('john', 'john@google.com', '1q2w3e4r!')`

  - User 비밀번호 변경

    ```python
    user = User.objects.get(pk=2)
    User.set_password('new password')
    User.save()
    ```

  - User 인증(비밀번호 변경)

    ```python
    from django.contrib.auth import authenticate
    user = authenticate(username="john", passowrd="secret")
    ```

    

- 회원가입기능 구현

  ```python
  #accounts/urls.py
  
  app_name = "accounts"
  urlpatterns = [
    ...
    path('signup/', views.signup, name="signup"),
  ]
  ```

  ```python
  #from django.contrib.auth.forms import UserCreationForm
  import redirect
  from .forms import CustomUserCreationForm
  
  
  def siginup(request):
    	#post 요청 처리
      if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
          	form.save()
          	return redirect('articles:index')
      else:
        form = CustomUserCreationForm()
      context = {
        	'form' : form
      }
      return render(request, 'accounts/signup.html', context)
  ```

  ```html
  <!-- accounts/signup.html -->
  {% extends 'base.html' %}
  {% block content %}
  <h1>회원가입</h1>
  <form action= "{% url 'accounts:signup'%}" method="POST">
    {{% csrf_token %}}
    {{ form.as_p}}
    <input type="submit">
  </form>
  {% endblock content %}
  ```

  ```html
  <!-- base.html -->
  
  <div class="container">
    <a href="{% url 'accounts:signup' %}">Signup</a>
    <hr>
    {% block content %}
    {% endblock content %}
  </div>
  ```

  - 위에 작성만 했을시 발생하는 에러

    - AttributorError at /accounts/signup/

      - Manager isn't available; 'auth.User' has been swapped for 'account.User' 

        - 매니저는 ORM에서 models.Model을 상속 받는 이유다. Article(objects)

      - 해결 방법

        - 회원가입에 사용하는 UserCreationForm이 우리가 대체한 커스텀 유저 모델이 아닌 기존 유저 모델로 인해 작성된 클래스이기 때문

        ```python
        #forms.py
        #기존 UserCreationForm을 상속받아 User 모델 재정의
        from django.contrib.auth.forms import UserCreationForm
        from django.contrib.auth import get_user_model
        def CustomUserCreationForm(UserCreationForm):
          	
            class Meta:
              	#모델 부분을 수정해야한다. user은 원래 auth.user으로 인식되어 있어서
                #바꿔야해서 상속을 받는다. account에 정의한것을 의미하게끔 변경한다.
                #그래서 get_user_model()함수를 통해서 유저 클래스를 참고하자! 
                #언제든지 바뀔 수 있으니 직접 참조하지 말자.
              	model = get_user_model()
                fields = ('username', 'password')
        ```
        
        ```python
        #admin.py
        from django.contrib import admin
        from django.contrib.auth.admin import UserAdmin
        #언제든지 바뀔 수 있으니 직접 참조하지 말고 user클래스 참조
        from django.contrib.auth import get_user_model
        
        # admin.site.register(Article)
        admin.site.register(get_user_model , Useradmin)
        ```
        
        ```html
        <!--signup.html-->
        [%extends 'base.html' %]
        {% load django_bootstrap5 %}
        
        {% block body %}
        <h1>회원가입</h1>
        <form action = "" method ="POST">
          {% csrf_token %}
          {% bootstrap_form form %}
        	{% bootstrap_button button_type="submit" content="OK"%}
        </form>
        
        {% endblock body %}
        ```

- get_user_model()

  - 현재 프로젝트에서 활성화된 사용자 모델을 반환
  - Django에서는 User 클래스는 커스텀을 통해 변경 가능하며, 직접 참조하는 대신 get_user_model()을 사용할 것을 권장

- 프로필 페이지 만들기

  - URL : /accounts/`<int:pk>`/
  - View:detail
  - template반환: 사용자 정보(username)
  - from .models import User 사용 금지

  ```python
  # views.py 
  def detail(request, pk):
    	user = get_user_model().objects.get(pk=pk)
      context = {
        "user", uesr
      }
      return render(request, 'accounts/detail.html', context)
  ```

  - Django.contrib: 장고가 좀 도와주는 기능, 