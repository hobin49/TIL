### URL namespace

- 개요 

  - URL namespace를 사용하면 서로 다른 앱에서 동일한 URL 이름을 사용하는 경우에도 이름이 지정된 URL을 고유하게 사용 할 수 있다

  - app_name attribute를 작성해 URL namespace를 설정

    ```python
    #articles/urls.py
    
    app_name = "articles"
    urlpatterns = [
      ...,
    ]
    ```

- URL tag의 변화

  `{% url   'index'%}`  => `{%url 'articles:index' %}` 

- **반드시!! app_name을 지정한 이후에는 url 태그에서 반드시 app_name:url_name 형태로만 사용해야 한다. 그렇지 않으면 NoReverseMatch 에러가 발생한다. ** 

- ":" 연산자를 사용하여 지정

  - 예를 들어, app_name이 articles이고 URL name이 index인 주소 참조는 **aritcles:index**가 된다

### Naming URL patterns

- Naming URL patterns

  - 이제는 링크에 URL을 직접 작성하는 것이 아니라 "path()" 함수의 name 인자를 정의해서 사용
  - DTL의 Tag 중 하나인 URL 태그를 사용해서 "path()" 함수에 작성한 name을 사용할 수 있다
  - 이를 통해 URL 설정에 정의된 특정한 경로들의 의존성을 제거할 수 있다
  - Django는 URL에 이름을 지정하는 방법을 제공함으로써 view 함수와 템플릿에서 특정 주소를 쉽게 참조할 수 있도록 도움

- 예

  - `path('index/', views.index, name="index")`

- Built-in tag - "url"

  `{% url ' %'}`

  - 주어진 URL 패턴 이름 및 선택적 매개 변수와 일치하는 절대 경로 주소를 반환한다
  - 템플릿에 URL을 하드 코딩하지 않고도 DRY 원칙을 위반하지 않으면서 링크를 출력하는 방법

### App URL mapping

- 변수화를 잘하면 재사용성이 좋아져서 url의 변수화가 매우 중요하다 문제가 될 점은 name이 중복되면 그래서 namespace를 통해서 해결 

- `app_name: '앱이름'`: 장고가 정한 약속 어떤의 앱은 인덱스인지 확인하고 넘어가는 역할

- 그러나 위에만 작성하면 에러가 발생!!! 

- 그래서 `{% url ' app_name: app's url' %}`

- DRY 원칙
  - Don't repaet yourself 약자
  - 더 품질 좋은 코드를 작성하기 위해서 알고, 따르면 좋은 소프트웨어 원칙들 중 하나로 "소스 코드에서 동일한 코드를 반복하지 말자"라는 의미
  - 동일한 코드가 반복된다는 것은 잠재적인 버그의 위협을 증가 시키고 반복되는 코드를 변경해야 하는 경우, 반복되는 모든 코드를 찾아서 수정해야 함
  - 이는 프로젝트 규모가 커질수록 애플리케이션의 유지 보수 비용이 커짐

- Django의 설계 철학 (Templates System)

  - 표현과 로직을 분리

    - 템플릿 시스템은 표현을 제어하는 도구이자 표현에 관련된 로직일 뿐

    - 즉 템플릿 시스템은 이러한 기본 목표를 넘어서는 기능을 지원하지 말아야 함

  - 중복을 배제

    - 대다수의 동적 웹사이트는 공통 header, footer, navbar 같은 사이트 공통 디자인을 갖음
    - Django 템플릿 시스템은 이러한 요소를 한 곳에 저장하기 쉽게 하여 중복 코드를 없애야 한다.
    - 템플릿 상속의 기초가 되는 철학

  - Convention over configuration. 설정 보다는 관례

- Framework의 성격

  - 독선적(opinionated)
    - 독선적인 프레임워크들은 어떤 특정 작업을 다루는 '올바른 방법'에 대한 분명한 의견(규약)을 가지고 있다
    - 대체로 특정 문제내에서 빠른 개발방법을 제시
    - 어떤 작업에 대한 올바른 방법이란 보통 잘 알려져 있고 문서화가 잘 되어있기 때문에
    - 하지만 주요 상황을 벗어난 문제에 대해서는 그리 유연하지 못한 해결책을 제시할 수 있다
  - 관용적(unopinionated)
    - 관용적인 프레임워크들은 구성요소를 한데 붙여서 해결해야 한다거나 심지어 어떤 도구를 써야 한다는 '올바른 방법'에 대한 제약이 거의 없다
    - 이는 개발자들이 특정 작업을 완수하는데 가장 적절한 도구들을 이용할 수 있는 자유도가 높다
    - 하지만 개발자 스스로가 그 도구들을 찾아야 한다는 수고가 필요



### Django 구조 이해하기(MTV Design Pattern)

- SW란
  - 문제 해결(세상의 문제가 너무 복잡하다)
  - 추상화(요약) 
- Design pattern
  - 설계한다
- 소프트웨어에서의 관점
  - 각기 다른 기능을 가진 다양한 응용 소프트웨어를 개발할 대 
- 소프트웨어 디자인 패턴
  - 소프트웨어도 수십년간 전 세계의 개발자들이 계속 만들다 보니 자주 사용되는 구조와 해결책이 있다는 것을 알게 됨
  - 앞서 배웠던 클라이언트--서버 구조도 소프트웨어 디자인 패턴 중 하나
- MVC 소프트웨어 디자인 패턴
  - MVC는 Model - View - Controller의 준말 데이터 및 논리 제어를 구현하는데 널리 사용되는 소프트웨어 디자인 패턴
  - 하나의 큰 프로그램을 세가지 역할로 구분한 개발 방법론
  - Model: 데이터와 관련된 로직을 관리
  - view: 레이아웃과 화면을 처리
  - Controller:명령을 model과 view 부분으로 연결
- MVC 소프트웨어 디자인 패턴의 목적
  - 더 나은 업무의 분리와 향상된 관리를 제공
  - 각 부분을 독립적으로 개발할 수 있어, 하나를 수정하고 싶을 때 모두 건들지 않아도 된다.
    - 개발 효율성 및 유지보수가 쉬워진다
    - 다수의 멤버로 개발하기 용이하다.
- Django에서의 디자인 패턴
  - Django는 MVC 패턴을 기반으로 한 MTV 패턴을 사용한다. 두 패턴은 서로 크게 다른 점은 없으며 일부 역할에 대해 부르는 이름이 다르다
- Model
  - MVC 패턴에서 model의 역할에 해당
  - 데이터와 관련된 로직을 관리
  - 응용프로그램의 데이터 구조를 정의하고 데이터베이스의 기록을 관리
- Template
  - 레이아웃과 화면을 처리
  - 화면상의 사용자 인터페이스 구조와 레이아웃을 저으이
  - MVC 패턴에서 View의 역할에 해당한다.
- View
  - Model& Template과 관련된 로직을 처리해서 응답을 반환
  - 클라이언트의 요청에 대해 처리를 분기하는 역할
  - 동작 예시
    - 데이터가 필요하다면 model에 접근해서 데이터를 가져오고 가져온 데이터를 template로 보내 화면을 구성하고 구성된 화면을 응답으로 만들어 클라이언트에게 반환
  - MVC 패턴에서 Controller의 역할에 해당



- Django는 MTV 디자인 패턴을 가지고 있다
  - Model: 데이터 관련
  - Template: 화면 관련
  - View: Model & Template 중간 처리 및 응답 반환



### Database

- 모델은 데이터베이스를 관리하는 것이다

- 체계화된 데이터의 모임

- 검색 및 구조화 같은 작업을 보다 쉽게 하기 위해 조직화된 데이터를 수집하는 저장 시스템

- Database의 가장 기초적인 키워드에 대해 알아보고 자세한 내용은 추후 Database에서 다룰 예정

- 기본구조

  - 스키마
    - 뼈대
    - 데이터베이스에서 자료의 구조, 표현 방법, 관계 등을 정의한 구조
  - 테이블
    - 필드와 레코드를 사용해 조직된 데이터를 요소들
    - 관계라고도 부름
  - 필드
    - 속성, 컬럼
  - 레코드
    - 튜플, 행
  - PK
    - 기본 키
    - 각 레코드의 고유한 값(식별자로 사용)
    - 주민등록번호

  - 쿼리 
    - 데이터를 조회화기 위한 명령어
    - 조건에 맞는 데이터를 추출하거나 조작하는 명령



### Model

- 개요
  - Django는 Model을 통해 데이터에 접근하고 조작
  - 사용하는 데이터들의 필수적인 필드들과 동작들을 포함
  - 저장된 데이터베이스의 구조
  - 일반적으로 각각의 모델은 하나의 데이터베이스 테이블에 매핑
- 매핑
  - 하나의 값을 다른 값으로 대응시키는 것
- CharField(max_length=None, **options)
  - 길이의 제한이 있는 문자열을 넣을 때 사용
  - max_length
    - 필드의 최대 길이(문자)
    - CharField의 필수 인자
    - 데이터베이스와 Django의 유효성 검사(값을 검증하는 것)에서 활용된다.
- TextField(**options)
  - 글자의 수가 많을 때 사용
  - max_length 옵션 작성 시 사용자 입력 단계에서는 반영 되지만, 모델과 데이터베이스 단계에는 적용되지 않는다
    - 실제로 저장될 때 길이에 대한 유효성을 검증하지 않는다.

### Migrations

- makemigrations

  - 모델의 변경사항에 대한 새로운 migration을 만들 때 사용

  `python manage.py makemigrations`

- migrate

  - makemigrations로 만든 설계도를 실제 데이터베이스에 반영하는 과정
  - 결과적으로 모델의 변경사항과 데이터베이스를 동기화

  `python manage.py migrate`

- DateTimeField()

  - python의 datetime.datetime 인스턴스로 표시되는 날짜 및 시간을 값으로 사용하는 필드
  - DateField를 상속받는 클래스
  - 선택 인자
    - auto_now_add
      - 최초 생성 일자
      - 데이터가 실제로 만들어질 때 현재 날짜와 시간으로 자동으로 초기화 되도록 한다
    - auto_now
      - 최종 수정 일자
      - 데이터가 수정될 때마다 현재 날짜와 시간으로 자동으로 갱신되도록 한다.

### ORM

- Object-Relational-Mapping
- 객체 지향 프로그래밍 언어를 사용하여 호환되지 않은 유형의 시스템 간에 (Django <-> DB) 데이터를 변환하는 프로그래밍 기술
- 객체 지향 프로그래밍에서 데이터베이스을 연동할 때, 데이터베이스와 객체 지향 프로그래밍 언어 간의 호환되지 않는 데이터를 변환하는 프로그래밍 기법
- Django는 내장 Django ORM을 사용
- 한마디로 SQL을 사용하지 않고 데이터베이스를 조작할 수 있게 만들어주는 매개체

- 오늘 한 내용
- 첫 번째 앱을 만들어주고 `settings.py` 가서 등록을 하고 
- 메인 관리자한테 가서 `urls` 사용을 허락을 받는다. (include) `앱이름.urls`
- 그리고 `urls.py` 에 가서 `from . Import views`을 해주고
- `app_name`을 지정해주고 보통은 앱이름을 따라간다. 그리고 오늘 더 배운건 `name`을 지정한다.
  - name을 지정하면 템플릿에서 바로 url을 적용할 수 있다. 
  - `<a href="{% url '앱이름:사용할 함수' %}"></a>` 
- 유의할 점은 url include지정을 했으니까 항상 render를 할때 `앱이름/템플릿.html` 이 형태로 작성해야한다.
- 입력한 데이터를 저장하기 위해서는 `models.py` 를 조작한다
  - 첫 번째 클래스를 만들고 `class 이름(models.Model)`
  - 두번째 데이터들의 글자를 지정? 이건 하나의 예시
  - `title = models.CharField(max_length = 50)` 타이틀의 길이는 최대 50글자까지 지정
  - `content = models.TextField()` 내용은 따로 길이를 지정하지 않는다.
- `models.py`에서 작성한 클래스를 살기 위해서는 import를 해준다.
  - `from .models import 클래스이름` 
- 항상 파라미터로 날라온 데이터를 받기 위해서!!
  - `request.GET.get("input name")`
- **날라온 데이터를 DB에 저장하려면** DB구성에서도 우리가 만들어야할 항목들을에 날라온 데이터가 들어갈 수 있게 조작해준다.
  - Ex)
  - `class이름.objects.create(title = title, content = content)` 

- render은 템플릿을 받는데 redirect는 `redirect("앱: 바로 이동하고 싶은페이지")` 

  - redirect를 사용하려면 render와 함께 import 해야한다.

- redirect 

  - 사용자가 create 요청
  - 서버에서 index 요청
  - 사용자에게는 index 응답

- 게시판에 등록할 때

  - view에서 `model.object.all()`으로 받은 값을 context로 넘겨주고 객체로 받기 때문에 데이터를 뽑기 위해서는 DTL을 활용, for문을 활용해서 `{% for _ in context %}` 다음에 `{{ _.얻고 싶은 값}}` 

- 삭제

  - `path("delete/<int:pk>", views.delete, name="delete"),`

  - primary key를 활용해서 지워준다. 

  - 함수를 정의할 때는

    ```python
    #우리는 primary key를 사용하기로 했으니까 파라미터로 받아오고
    def delete(pk):
      	클래스이름.objects.get(id=고유값).delete()
      	return redirect("앱이름: 바로 이동할 페이지")
    ```

    

  - html에서는 `<a href="/앱/기능/{{ model.class.id}}" `



### UPDATE

- 2개의 view 함수가 필요
- 사용자의 





### 오늘 오전 복습

- 1. 가상환경 생성

  2. 가상환경 실행

  3. 장고 설치 (3.2.12)

  4. 장고 프로젝트 만들기

  5. 장고 숏츠 설치

     `pip install Django-shorctuts`

  6. 앱 생성

  7. 앱 등록

  8. 모델 정의

  9. 필드 정의(장고는 pk(id)는 자동으로 만들어준다.)

     1. default는 데이터를 생성할 때 값을 안 넣으면 자동으로 값을 채워서 데이터를 생성해

  10. 설계도(db.sqlite3에 새로운 테이블을 생성)

      1. python manage.py makemigrations.
      2. python manage.py migrate

  11. Url 분리(각 앱에 url을 만들어)

  12. 메인 urls에 import include해주고  앱의 경로를 include를 해준다.

  13. 앱 urls로 가줘 views를 import 해고 urlpattern 하고 namespace를 활용해서 app name 써줘

  14. views를 이동해서 함수를 만들어줘 

      1. 경로를 `todos/index.html`

  15. 템플릿 폴더를 만들고 그 안에 앱이름과 같은 폴더를 또 만들고 그 안에 템플릿을 만들어줘

  16.  `index.html`사용자에게 정보를 입력받을 떄 form 태그를 사용해야한다.

      1. `<input type="submit" value = "할 일 추가">` 

  17. html에서 글자수 지정

      1. `input type=text name="" id="" maxlength="80"`

  18. 어떤 url을 요청할까?

      1. `<form action="{% url 'todos:create' %}">`
      2. url이랑 다음글자랑 반드시 띄어야 한다.

  19. todo에 url로 가서 create를 만든다

  20. views로 가서 create함수를 만들어

  21. index.html로 가서  name에 이름을 지정한다.

  22. request.GET.get("index_html의 input 네임")해서 값을 가져와

  23. 모델을 import 해줘 `from .models import Todo`

  24.  db에 저장하기 위해  `Todo.objects.create(표의 구성 = 내가 넣을 값 )` 를 만든다.

  25. 우리가 만들어 놓은 데이터를 불러오자

      1. `Todo.objects.all()` 꼭 이것을 변수에 넣어줘야해 
      2. 템플릿에서 사용해야하니까 context를 사용

  26. 템플릿에서 dtl을 이용해서 출력 **꼭 출력하고 싶은 데이터를 작성해**

  27. 삭제 버튼을 만들자 

      1. `<a href="{% url 'todos:delete' todo.pk %}"></a>`

      2. int타입으로 지정하고
      3. 함수를 만든다