### Django CRUD

1.가상환경 및 Django 설치

1. 가상환경 생성 및 실행

   - 가상환경 폴더를 `.gitignore` 로 설정을 해둔다.

   `python -m venv venv`

   `source venv/bin/activate` 

2. 장고 설치하고 기록을 남긴다

   `pip install django==3.2.13` 

   `pip freeze > requirements.txt`

3. 프로젝트를 만든다.

   `django-admin startproject [프로젝트 이름] [설치 경로]` 



2.app을 생성

`python manage.py startapp [앱 이름] `

- 앱을 등록한다
  - pjt -> settings.py -> `INSTALLED_APPS`. -> [앱 이름] 작성

- 메인 url로 이동해서 새로운 앱의 urls.py를 등록한다. 

```python
# pjt/urls.py 
from django.urls import path, include

urlpatterns = [
  path('articles/', include('articles.urls')),
]
```

- articles의 url을 만들어주고 설정을 해준다.

```python
# articles/urls.py
from django.urls import path
from . import views

app_name = "articles"
urlpatterns = [
  #초기 페이지 만들어주기
  path("", views.index, name="index"),
]
```

- articles의 views에 가서 함수를 만들어준다.

```python
# 초기 페이지 설정
def index(request):
    return render(request, "articles/index.html")
```

- base.html을 만들어준다.

```html
<!-- templates/base.html-->
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js"
    integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa"
    crossorigin="anonymous"></script>
</head>

<body>
  {% block content %}
  {% endblock %}
</body>

</html>

<!-- pjt/settings.py -->
Template = [
	{"DIRS": [BASE_DIR / "templates"],
	}
]
```



- templates 파일을 만들어준다. 

```html
<!--articles/templates/articles/index.html-->

{% extends "base.html" %}
<h1>안녕하세요!</h1>
{% block content %}

{% endblock %}
```



3.Model 정의(DB 설계)

- 클래스 정의

```python
#articles/models.py/Articles
# 게시판 기능
# 제목(30글자 이내에)
# 글 작성시간/수정시간(자동으로 기록, 날짜 시간/)
class Article(models.Model):
  title = models.CharField(max_length=30)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)
  
#articles/views.py
from .models import Articles 
```

- 마이그레이션 파일 생성

`python manage.py makemigrations`

- DB 반영

`python manage.py migrate`



4.CRUD 기능 구현

- 게시글 생성

```python
#articles/urls.py
path("new", views.new, name="new")

# HTML Form 제공 페이지 만들기
def new(request):
    return render(request, "articles/new.html", context)
```

```python
#articles/templates/articles/new.html

{% extends 'base.html'%}

{% block content %}
<!-- form: 사용자에게 양식을 제공하고 값을 받아서(input: name, value) 서버에 전송(form: action)-->
<form action="{% urls 'articles:create'%}">
  <label for="title">제목</label>
  <input type="text" name="title" id="title">
  <label for="content">내용</label>
  <textarea name="content" id="content" cols="30" rows="10"></textarea>
  <input type="submit" value="제출">
</form>

{% endblock %}
```

- 입력받은 데이터 처리

```python
#articles/urls.py
path('create', views.create, name="create")

# 게시글 DB 생성하고 index 페이지로 redirect
def create(request):
    title = request.GET.get("title")
    content = request.GET.get("content")
    Ariticle.object.create(title=title, content=content)
    return redirect("articles:index")

```

- 게시글 목록

```python
# 요청 정보(생성한 정보)를 받는다. 
def index(request):
    #게시글에 입력된 것을 다 가져오고
    article = Articles.objects.order_by('-pk')
    #template에 전달한다.
    context = {
        "articles": article
    }
    return render(request, "articles/index.html", context)
```

```html
<!-- 요청한 정보를 template에서 DTL을 이용해서 사용자에게 보여준다 -->
{% extends 'base.html' %}
{% block content %}
	<h1>게시판</h1>
	<!-- 글쓰기 버튼 누를시에 new로 이동-->
	<a href="{%url 'articles:new' %}">글쓰기</a>
	{% for article in articles %}
	<h3>{{articles.title}}</h3>
	<h3>{{articles.content}}</h3>
	<p>{{articles.created_at}} | {{articles.updated_at}}</p>
{% endblock %}
```

- Django modelform 활용

```python
from django import forms
from .models import Article

# forms 정의
class ArticleForm(forms.ModelForm):
    class meta:
        model = Article
        # 모든 데이터 사용
        field = "__all__"

    
    
# articles/views.py
from .forms import ArticleForm
def new(request):
  article_form = ArticleForm()
  context = {"article_form" : article_form}
  return render(request, "articles/new.html", context=context)
```

- form.as_p는 폼의 각 필드를 p 태그 안에서 레이블과 텍스트로 배치한다

```html
{% extends 'base.html'%}

{% block content %}
<!-- form: 사용자에게 양식을 제공하고 값을 받아서(input: name, value) 서버에 전송(form: action)-->
<form action="{% url 'articles:create'%}" method="POST">
  {% csrf_token%}
  {{ article_form.as_p}}
  <input type="submit" value="제출">
</form>

{% endblock %}
```

```python
# new와 create를 합쳐준다. 
def create(request):
  # post면 db에 저장하는 작업을 한다.
    if request.method == "POST":
        # 요청한 값의 데이터를 한꺼번에 받아올 수 있다.
        article_form = ArticleForm(request.POST)
        # 유효성 검사
        if article_form.is_valid():
            article_form.save()
            return redirect("articles:index")
    # post가 아니면
    else:
        article_form = ArticleForm()
    context = {"article_form": article_form}
    return render(request, "articles/new.html", context=context)
  
# articles/index.html에서 변경
	<a href="{%url 'articles:create' %}">글쓰기</a>
```

- 상세보기

```python
#articles/urls.py
path("<int:pk>/", views.detail, name="detail"),
```

```python
# 상세보기
def detail(request, pk):
    # 특정 글을 가져온다.
    article = Articles.objects.get(pk=pk)
    # 템플릿 객체 전달
    context = {
        "article": article,
    }

    return render(request, "articles/detail.html", context)
```

```html
<!--articles/detail.html-->
{% extends 'base.html' %}

{% block content %}

<h1>{{ article.pk }}번 게시글</h1>
<h2>{{article.created_at}} | {{articles.updated_at}}</h2>
<p>{{articles.content}}</p>
{% endblock %}

<!--articles/index.html-->
<h3><a href="{% url 'articles:detail' article.pk%}"></a>{{article.title}}</h3>
```

- 수정하기

```python
# 수정하기
path("<int:pk>/update", views.update, name="update"),
```

```python
#update.html
<h1>글 수정하기</h1>

<form action="" method="POST">
  {{ article_form.as_p}}
  <input type="submit" value="수정하기">
</form>
```

```python
# 업데이트하기
def update(request, pk):
    article = Article.objects.get(id=pk)
    # POST이면?
    if request.method == "POST":
        # 유효성 체크
        articleForm = ArticleForm(request.POST, instance=article)
        if articleForm.is_valid():
            articleForm.save()
            # 해당 글로 가야해
            return redirect("article:detail", article.pk)
    # GET이면?
    else:
        articleForm = ArticleForm(instance=article)
    context = {"articleForm": articleForm}
    return render(request, "articles/update.html", context)

```

- Django Staticfiles 활용한 정적 파일(css, image) 다루기

  - 앱 안에 static이라는 파일을 만들고 거기에 image 폴더를 만들어서 이미지를 넣어줬다.

  `{%load static %}` 

  `img src="{% static 'images/turtle.jpeg'%}" alt="">` 

  - 그리고 css 폴더를 만들고 그안에 파일 하나를 만들고 적용하기 위해 base.html에 가서 

  `{% load static%}` 

  `<link rel="stylesheet" href="{% static 'css/style.css' %}">` 

  이 두 가지를 추가해줬다.

- bootstrap을 사용하려면 

  `pip install django-bootstrap5`

  - settings로 이동
    - `INSTALLED_APPS ` 로 이동하고 `django_bootstrap5`를 등록한다.
  - 템플릿에서

  ```html
  <!-- bootstrap을 사용하기 위한 필수 코드 -->
  {% load django_bootstrap5 %}
  {% bootstrap_css %}
  {% bootstrap_javascript %}
  
  <!-- 사용 -->
  <form action="{% url 'articles:create'%}" method="POST">
    {% csrf_token%}
    {% bootstrap_form article_form %}
    <!-- 기본 form형식 주석처리 -->
    {# article_form.as_p #}
    
    {% bootstrap_button button_type="submit" content="OK" %}
  </form>
  
  ```

  
