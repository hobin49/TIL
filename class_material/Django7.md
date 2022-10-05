- 서비스 기능을 만들기 위해 코드를 작성

- 클라이언트는 url을 요청(http 요청 메시지) - path, 메서드, 헤더, 프로토콜
- Variable rouing 이 버튼을 누르면 실행되게
- ModelForm
  - DB 필드가 사실상 HTML form(DB필드가 변하면 HTML form도 따라서 변화하면 좋지 않을까!)
  - input값 => DB 유효성 검사



- 글쓸래 -> 비어있는 form(요청- GET)
- form 입력 -> 유효성 검사 -> DB 저장(성공시) ->실패시(에러 + 입력 값)- POST
- 생성 부분에서 GET, POST를 같이 하나의 함수 안에서 작동, 수정 부분도 역시 하나의 함수 안에서 GET과 POST를 쓴다.
- 조회 부분에서 objects.get 요청을 orm으로 처리  

- 장고는 파이썬 기반 웹 프레임워크
- 가상환경을 사용하는 이유 어떤 언어를 선택하시더라도 언어별 프로젝트별 별도 패키지 관리
- 장고는 주요 기능 단위의 app구조, app별로 MTV를 구조를 가지는 모습 + 'urls.py'
- include에서 모듈(분리된 파일): 앱이름.urls->articles/urls.py를 의미
- Template에서 활용 예시
  - {% url ''앱이름:기능''%}

- 게시글 생성 전에 modelform을 생성
  - 선언된 모델에 따른 필드 구성 1. form 생성 2. 유효성 검사
- 만약 form action이 비워도(만약 동일한 URL이면) 상관이 없다. 
- 쿼리셋api는 sql을 파이썬 메소드 조작으로 하는것은 sql핵심은 필드에서 값을 찾는 것

### Django ModelForm

- 개요
  - DB 기반의 어플리케이션을 개발하다보면, HTML Form(UI)는 Django의 모델(DB)과 매우 밀접한 관계를 가지게 된다.
  - 사용자로부터 값을 받아 DB에 저장하여 활용하기 때문
  - 즉, 모델에 정의한 필ㄷ의 구성 및 종류에 따라 HTML Form이 결정된다.
- 사용자가 입력한 값이 DB의 데이터 형식과 일치하는지를 확인하는 유효성 검증이 반드시 필요하며 이는 서버 사이드에서 반드시 처리해야 한다.
- ModelForm Class
  - Model을 통해 Form Class를 만들 수 있는 helper class
  - ModelForm은 Form과 똑같은 방식으로 View 함수에서 사용
- ModelForm 선언
  - forms 라이브러리의 ModelForm 클래스를 상속받음
  - 정의한 ModelForm 클래스 안에 Meta 클래스를 선언
  - 어떤 모델을 기반으로 form을 작성할 것인지에 대한 정보를 Meta 클래스에 지정

```python
#articles/forms.py

from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
  
  	class Meta:
      model = Article
      fields = "__all__"
```

- ModelForm에서의 Meta Class (1/2)
  - ModelForm의 정보를 작성하는 곳
  - ModelForm을 사용할 경우 참조 할 모델이 있어야 하는데, Meta class의 model 속성이 이를 구성한다.
    - 참조하는 모델에 정의된 field 정보를 Form에 적용함.
- ModelForm에서의 Meta class(2/2)
  - fields 속성에 `'__all __'`를 사용하여 모델의 모든 필드를 포함할 수 있다
  - 또는 exclude 속성을 사용하여 모델에서 포함하지 않을 필드를 지정할 수 있다.

```python
#articles/forms.py

from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
  
  	class Meta:
      model = Article
      fields = ('title',)
```

- ModelForm 활용

```python
#articles/views.py
from .forms import ArticleForm

def new(request):
  	form = ArticleForm()
    context = {
      'form' : form,
    }
    
    return render(request, 'articles/new.html', context)
```

- Input Field 활용

  ```html
  <!-- articles/new.html -->
  {% extends 'base.html' %}
  
  {% block content %}
  	<h1>NEW</h1>
  	<form action = "{% url 'articles:create' %}" method="POST"> 
  		{% csrf_token %}
      {{ form.as_p }}
      <input type="submit">
  	</form>
  	<hr>
  	<a href="{% url 'articles:index' %}">[back]</a>
  {% endblock content %}
  ```

- From rendering options

  - `<label>` & `<input>`쌍에 대한 3가지 출력 옵션
    - as_p()
      - 각 필드가 단락(`<p>` 태그) 으로 감싸져서 렌더링
    - as_ul()
      - 각 필드가 목록 항목(`<li>` 태그) 으로 감싸져서 렌더링
      - `<ul>`태그는 직접 작성해야 한다
    - as_table()
      - 각 필드가 테이블(`<tr>`태그) 행으로 감싸져서 렌더링

```python
from django.forms import ModelForm
from .models import Article

class ArticleForm(ModelForm):
  	class Meta:
      	model = Article
        fields = "__all__"
        
form = ArticleForm()        
article = Article.obejects.get(pk=1)
form = ArticleForm(instance=article)
```



###  ModelForm with view functions 

- ModelForm 활용 로직

  - 요청 방식에 따른 분기
    - HTML Form 전달
    - 사용자 입력 데이터 수신
  - 유효성 검사에 따른 분기
    - 유효성 검사 실패시 Form으로 전달
    - 유효성 검사 성공시 DB 저장

- CREATE

  ```python
  # articles/views.py
  
  def create(request):
    	form = ArticleForm(request.POST)
      if form.is_valid():
        article = form.save()
        return redirect('articles:detail', article.pk)
     	return redirect('articles:new')
  ```

  - 유효성 검사를 통과하면

    - 데이터 저장 후 
    - 상세 페이지로 리다이렉트

  - 통과하지 못하면

    - 작성 페이지로 리다이렉트

  - "Is_valid()" method

    - 유효성 검사를 실행하고, 데이터가 유효한지 여부를 boolean으로 반환
    - 데이터 유효성 검사를 보장하기 위한 많은 테스트에 대해 Django는 is_valid()를 제공하여 개발자의 편의를 도움

  - The "save()" method

    - form 인스턴스에 바인딩 된 데이터를 통해 데이터베이스 객체를 만들고 저장

    - ModelForm의 하위 클래스는 키워드 인자 instance 여부를 통해 생성할 지, 수정할지를 결정한다

      - 제공되지 않은 경우 save()는 지정된 모델의 새 인스턴스를 만듦(create)

      - 제공되면 save()는 해당 인스턴스를 수정(UPDATE)

        ```python
        # CREATE
        form = ArticleForm(request.POST)
        form.save()
        
        # UPDATE
        form = ArticleForm(request.POST, instance=article)
        form.save()
        ```

        

  -  form 인스턴스의 errors 속성

    - 이 같은 특징을 통해 다음과 같은 구조로 코드를 작성하면 유효성 검증을 실패했을 때 사용자에게 실패 결과 메세지를 출력해줄 수 있다

    ```python
    # articles/views.py
    
    def create(request):
      	form = ArticleForm(request.POST)
        if form.is_valid():
          article = form.save()
          return redirect('articles:detail', article.pk)
       	context = {
          'form': form,
        }
        return render(request, 'articles/new.html', context)
    ```

  - UPDATE

    - ModelForm의 인자 instance는 수정 대상이 되는 객체(기존 객체)를 지정
    - request.POST
      - 사용자가 form을 통해 전송한 데이터(새로운 데이터)
    - instance
      - 수정이 되는 대상

    ```python
    # articles/views.py
    
    def edit(request, pk):
      	article = Article.objects.get(pk=pk)
        form = ArticleForm(instance=article)
        context = {
          'article': article,
          'form' : form,
        }
        return render(request, 'articles/edit.html', context)
    ```

    ```html
    <!-- articles/edit.html -->
    {% extends 'base.html' %}
    
    {% block content %}
    	<h1>EDIT</h1>
    	<form action = "{% url 'articles:update' article.pk%}" method="POST"> 
    		{% csrf_token %}
        {{ form.as_p }}
        <input type="submit">
    	</form>
    	<hr>
    	<a href="{% url 'articles:index' %}">[back]</a>
    {% endblock content %}
    ```

### Django admin

- `python manage.py createsuperuser`
  - 사용자이름: 입력
  - 이메일주소:입력 안해도 돼
  - 비밀번호: 1234하면 돼 

```python
#articles/admin.py 
from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
  fields = ['title', 'created_at', 'updated_at']
#admin.site.register(Article)
admin.site.register(Article, ArticleAdmin)
```



### Static files

- 웹 서버는 특정 위치에 있는 자원을 요청 받아서 제공하는 응답을 처리하는 것을 기본 동작으로 한다.

- 즉, 웹 서버는 요청 받은 URL로 서버에 존재하는 정적 자원을 제공

- static이라는 파일 안에 img, css파일 만들 수 있다.

- 정적 파일

  - img폴더를 앱 안에 생성후에 이미지 담기 

  ``` html
  {% load static %}
  <img src="{% stactic 'img.jpeg' %}"
  ```

  - Css 파일

  ```html
  <link rel="stylesheet"href="{% static 'css/style.css' %}"
  ```

  - 프로젝트 단위 폴더로 할떄는 DIR 설정해야한다. 
  - Load static은 import를 한다고 생각하자.

- 부트스트랩

  - `pip install django-bootstrap`
  - `pip freeze > requirements.txt`

  ```html
  {% load django_bootstrap5 %}
  {% bootstrap_css %}
  {% bootstrap_javascript %}
  
  {% bootstrap_form article_form %}
  
  {% bootstrap_button button_type="submit" content="OK" %}
  ```

  