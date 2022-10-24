### 이미지 업로드(기본 설정)



- 미디어 파일

  - 사용자가 웹에서 업로드하는 정적 파일 (user-uploaded)
  - 유저가 업로드 한 모든 정적 파일

- Media 관련 필드

  - ImageField
    - 이미지 업로드에 사용하는 모델 필드
    - FileField를 상속받는 서브 클래스이기 때문에 FileField의 모든 속성 및 메서드를 사용 가능하며 더해서 사용자에 의해 업로드 된 객체가 유효한 이미지인지 검사한다.
    - ImageField 인스턴스는 최대 길이가 100자인 문자열로 DB에 생성되며, max_length 인자를 사용하여 최대 길이를 변경 할 수 있다.
    - **사용하려면 반드시 Pillow 라이브러리가 필요하다!**

- Media 관련 필드

  - FileField 

    - 파일 업로드에 사용하는 모델 필드
    - 2개의 선택 인자를 가지고 있다
      - upload_to
      - Storage

  - URL 설정

    - settings.py에 MEDIA_ROOT, MEDIA_URL 설정

    - upload_to 속성을 정의하여 업로드 된 파일에 사용 할 MEDIA_ROOT의 하위 경로를 지정

    - 업로드 된 파일의 경로는 django가 제공하는 'url'속성을 통해 얻을 수 있다.

      ```html
      <img src ="{{article.image.url}}" alt = "{{article.image}}">
      ```

  - URL 설정

    - MEDIA_ROOT

    - 사용자가 업로드 한 파일(미디어 파일)들을 보관할 디렉토리의 절대 경로

    - django는 성능을 위해 업로드 파일은 데이터베이스에 저장하지 않음

      - 실제 데이터베이스에 저장되는 것은 파일의 경로

      ```python
      # settings.py
      MEDIA_ROOT = BASE_DIR / 'media'
      ```

    - MEDIA_ROOT에서 제공되는 미디어를 처리하는 URL

    - 업로드 된 파일의 주소(URL)를 만들어 주는 역할

      - 웹 서버 사용자가 사용하는 public URL

    - 비어 있지 않은 값으로 설정 한다면 반드시 slash(/)로 끝나야 함

      ```python
      # settings.py
      MEDIA_URL = '/media/'
      ```

    - 개발 단계에서 사용자가 업로드 한 파일 제공하기

      ```python
      # urls.py
      from django.conf.urls.static import static
      
      urlpatterns = [
        	path('admin/', admin.site.urls),
        	path("articles/", include('articles.urls')),
      ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
      ```

### 이미지 업로드(create)

- ImageField

  - Upload_to = "images/"

    - 실제 이미지가 저장되는 경로를 지정

  - blank=True

    - 이미지 필드에 빈 값(빈 문자열)이 허용되도록 설정 (이미지를 선택적으로 업로드 할 수 있도록)

    ```python
    # models.py
    
    class Article(models.Model):
      	title = models.CharField(max_length = 20)
        image = models.ImageField(blank= True, upload_to = "images/")
    ```

- 모델 설정

  - Model field option - "blank"

    - 기본 값 : False
    - True인 경우 필드를 비워 둘 수 있다
      - DB에는 "(빈 문자열)이 저장된다"
    - 유효성 검사에서 사용 됨(is_valid)
      - 필드에 blank = True가 있으면 form 유효성 검사에서 빈 값을 입력할 수 있다

  - Model field option - "null"

    - 기본 값: False
    - True인 django는 빈 값을 DB에 NULL로 저장
    - 주의 사항
      - CharField, TextField와 같은 문자열 기반 필드에는 사용하는 것을 피해야 한다
      - 문자열 기반 필드에 True로 설정 시 '데이터 없음(no data)'에 "빈 문자열(1)"과 "NULL(2)"의 2가지 가능한 값이 있음을 의미하게 된다
      - 대부분의 경우 "데이터 없음"에 대해 두 개의 가능한 값을 갖는 것은 중복되며, Django는 Null이 아닌 빈 문자열을 사용하는 것이 규칙

  - 모델 설정

    - Blank & null 비교

      - blank
        - Validation - related
      - null
        - Database- related
      - 문자열 기반 및 비문자열 기반 필드 모두에 대해 null option은 DB에만 영향을 미치므로, form에서 빈 값을 허용하려면 blank=True를 설정해야 한다.

    - 마이그레이션 실행

      `python manage.py makemigrations `

      `pip install Pillow`  and 마이그레이션과 마이그레이트를 진행 

      `pip freeze > requirements.txt`

      

    - HTML 설정

      ```html
      <!--create.html-->
      <form action = "{% url 'articles:create'%} " method="POST" enctype="multipart/form-data">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit" value="작성">
      </form>
      ```

    - form 요소 - enctype(인코딩) 속성

      - Multipart/form-data
        - 파일/이미지 업로드 시에 반드시 사용해야 한다(전송되는 데이터의 형식을 지정)
        - `<input type="file">` 을 사용할 경우에 사용
      - Application/x-www-form-urlencoded
        - (기본값) 모든 문자 인코딩
      - text/plain
        - 인코딩을 하지 않은 문자 상태로 전송
        - 공백은 "+" 기호로 변환하지만, 특수 문자는 인코딩 하지 않는다. 

    - view 설정

      - 업로드 한 파일은 request.FILES 객체로 전달됨

      ```python
      def create(request):
          # 만약 요청 방법이 post라면
          if request.method == "request":
              # 유효성 검사
              articleForm = ArticleForm(request.POST, request.FILES)
              if articleForm.is_valid():
                  # 저장
                  articleForm.save()
                  return redirect("articles:index")
          else:
              articleForm = ArticleForm()
      
          context = {
            "articleForm": articleForm,
          }
      
          return render(request, "articles/create.html", context=context)
      ```

    - img 태그 활용

      - article.image.url == 업로드 파일의 경로

      - article.image == 업로드 파일의 파일 이름

        ```html
        {% extends 'base.html' %}
        
        {% block content%}
        <!--헷갈리지 말것은 모든 데이터를 도는게 아니야-->
        <h2>{{article.pk}}</h2>
        <h3>{{article.created_at}} | {{article.updated_at}}</h3>
        <p>{{article.content}}</p>
        <img src ="{{article.image.url}}" alt="{{article.image}}"> 
        <!--수정페이지로 이동 !수정할 글만 이동해야한다.-->
        <a href="{% url 'articles:update' article.pk%}">수정하기</a>
        {% endblock %}
        ```



### 이미지 수정하기(update)

- 이미지는 바이너리 데이터(하나의 덩어리)이기 때문에 텍스트처럼 일부만 수정 하는 것은 불가능하고, 새로운 사진으로 덮어 씌우는 방식을 사용

  ```html
  {% extends 'base.html' %}
  
  
  {% block content %}
  
  <form action="" method="POST" enctype = "multipart/form-data">
    {% csrf_token %}
    {% articleForm.as_p %}
    <input type="submit" value="수정하기">
  </form>
  
  {% endblock %}
  ```

  ```python
  #views.py
  def update(request, pk):
      article = Article.objects.get(id=pk)
      # POST이면?
      if request.method == "POST":
          # 유효성 체크
          articleForm = ArticleForm(request.POST, request.FILES, instance=article)
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

### 이미지 Resizing

- Django-imagekit

  - 실제 원본 이미지를 서버에 그대로 업로드 하는 것은 서버의 부담이 큰 작업
  - <img> 태그에서 직접 사이즈를 조정할 수도 있지만 (width 와 height), 업로드 될 때 이미지 자체를 resizing 하는 것을 사용해 볼 것
  - django-imagekit 라이브러리 활용
  - `pip install django-imagekit`
  - `pip freeze > requirements.txt`
  - `Settings.py => INSTALLED_APP = ['imagekit']`

- 이미지 크기 변경하기

  ```python
  #models.py
  from imagekit.models import ProcessedImageField
  from imagekit.processors import Thumbnail
  
  class Article(models.Model):
    	image = ProcessedImageField (
      		blank=True,
        	processors=[Thumbnail(200, 300)],
        	format = "JPEG",
        	options={"quality" : 90},
      
      )
      
  ```

  - 마이그레이션과 마이그레이트를 해주고 
  - **ProcessedImageField()의 parameter로 작성된 값들은 변경이 되더라도 다시 makemigrations를 해줄 필요없이 즉시 반영 된다** 

- Pillow 라이브러리 설치(이미지 관리하기 위해서(Python Image library- django가 python이라서))

  - `pip install Pillow`
  - `pip freeze > requirements.txt`

- models.py로 이동

  ```python
  class Article(models.Model):
    	image = models.ImageField(upload_to ="images/", blank = True)
  ```

- migrations, migrate을 진행 

- forms.py로 이동
  - form을 조정하기 위해서 
  - fields에 `image` 를 추가
  - 근데!! 게시글을 저장이 되는데 image는 저장이 되지 않고 있다
  - 그래서 html에서 나는 file을 받을거야
    - `enctype = "multipart/form-date"`
  - 그리고 views.py에서 create에서 파일을 별도로 모델폼에 넣어서 보내준다.
    - `form = ArticleForm(request.POST, request.FILES)`  
  - 이미지를 보여주고 싶으면
    - Settings.py 
      - `MEDIA_ROOT = BASE_DIR / "images" ` (이미지 파일을 서버에서 보여주는 방법)
      - `MEDIA_URL = '/media/'`
    - urls.py
      - `from django.conf import settings`
      - `from django.conf.urls.static`
      - urlspatters = [] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
- 이미지 업로드
  - 저장: 텍스트/숫자 + 이미지(HTML Form(enctype)) - VIEW에서 별도의 설정이 필요하다(request.FIELS) + MEDIA ROOT + URL





#### 이미지 Resizing

- Django-imagekit

  - 이미지 자체를 바꾼다. 
  - `pip install django-imagekit`
  - Settings.py로 이동 INSATLLED_APPS = ['imagekit']

- 에러 발생 - The image attribute has no file associated with it. 

  - 500 instenal server error 

  ```html
  {% if article.image %}
  	<img src = "{{article.img.url}}">
  {% endif %}
  ```

  - 수정하려면 updated에 request.FILES을 form 인자에 넣어준다. 

- Django-widget-tweak - 부트스트랩 폼 커스텀화



### 메시지 프레임워크

- settings.py  => `MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'`을 해준다.

```python
#views.py
from django.contrib import messages

def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "글 작성이 완료되었습니다")
            return redirect("articles:index")
    else:
        form = ArticleForm()
    context = {
        "form": form,
    }
    return render(request, "articles/create.html", context)
  
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
      			messages.success(request, "글 수정이 완료되었습니다")
            return redirect("articles:detail", article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        "form": form,
    }
    return render(request, "articles/update.html", context)
```

```html
<!--base.html-->
{% if messages %}
          {% for message in messages %}
          <div class="alert alert-{{ message.tags }}">
          {{ message }}
          </div>
          {% endfor %}
{% endif %}
```

