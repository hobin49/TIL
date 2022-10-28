  

#### A one-to-many relationship

- RDB(관계형 데이터베이스) 복습
  - 데이터를 테이블, 행, 열 등으로 나누어 구조화하는 방식
  - RDB의 모든 테이블에는 행에서 고유하게 식별 가능한 기본 키라는 속성이 있으며, 외래 키를 사용하여 각 행에서 서로 다른 테이블 간의 관계를 만드는 데 사용할 수 있다
- 고객 정보(id)를 기록
  - 외래키 :관계형 데이터베이스에서 다른 테이블의 행을 식별할 수 있는 필드(키)
- RDB에서의 관계
  - 1:1
    - One-to-one relationships
    - 한 테이블의 레코드 하나가 다른 테이블의 레코드 단 한 개와 관련된 경우
    - Ex) 프로필 
  - 1:N
    - One-to-many relationships
    - 한 테이블의 0개 이상의 레코드가 다른 테이블의 레코드 한 개와 관련된 경우
    - 기준 테이블에 따라(1:N, One-to-many relationships) 이라고도 함
    - 댓글 사용자의 글/댓글
  - M:N 
    - Many-to-many relationships
    - 한 테이블의 0개 이상의 



### Foreign key 

- 외래 키(외부 키)
- 관계형 데이터베이스에서 다른 테이블의 행을 식별할 수 있는 키
- 참조되는 테이블의 본 키(Primary Key)를 가리킴
- 참조하는 테이블의 행 1개의 값은, 참조되는 측 테이블의 행 값에 대응된다.
  - 이 때문에 참조하는 테이블의 행에는, 참조되는 테이블에 나타나지 않는 값을 포함할 수 없다.
- 참조하는 테이블 행 여러 개가, 참조되는 테이블의 동일한 행을 참조할 수 있다.
- 키를 사용하여 부모 테이블의 유일한 값을 참조(참조 무결성)
  - 참조 무결성: 데이터베이스 관계 모델에서 관련된 2개의 테이블 간의 일관성
    - 외래 키가 선언된 테이블의 외래 키 속성(열)의 값은 해당 테이블의 기본 키 값으로 존재
- 외래 키의 값이 반드시 부모 테이블의 기본 키 일 필요는 없지만 유잃나 값이어야 한다.





### 1:N (Article - comment)

### Model 관계 설정

- 게시판의 게시글과 1:N 관계를 나타낼 수 있는 댓글 구현

- 1:N 관계에서 댓글을 담당할 Article 모델은 1, Comment 모델은 N이 될 것

  - 게시글은 댓글을 0개 이상 가진다
    - 게시글(1)은 여러 개의 댓글(N)을 가진다
    - 게시글(1)은 댓글을 가지지 않을 수도 있다. 
  - 댓글은 반드시 하나의 게시글에 속한다. 

- 만약 comment 테이블에 데이터가 다음과 같이 작성되었다면

- 1번 게시글에는 1개의 댓글이, 3번 게시글에는 2개의 댓글이 작성된 것

- ForeignKey(to, on_delete, **options)

  - A one-to-many relationship을 담당하는 Django의 모델 필드 클래스
  - Django 모델에서 관계형 데이터베이스의 외래 키 속성을 담당
  - 2개의 필수 위치 인자가 필요
    - 참조하는 model class
    - On_delete 옵션

- ForeignKey arguments - on_delete

  - 외래 키가 참조하는 객체가 사라졌을 때, 외래 키를 가진 객체를 어떻게 처리할 지를 정의
  - 데이터의 무결성을 위해서 매우 중요한 설정
  - on_delete 옵션 값
    - CASCADE : 부모 객체(참조 된 객체)가 삭제 됐을 때 이를 참조하는 객체도 삭제
    - PROTECT, SET_NULL, SET_DEFAULT 등 여러 옵션 값들이 존재
    - 수업에서는 CASCADE 값만 사용할 예정

- Comment 모델 정의

  - 외래 키 필드는 Foreign 클래스를 작성하는 위치와 관계없이 필드의 마지막에 작성됨
  - ForeignKey() 클래스의 인스턴스 이름은 참조하는 모델 클래스 이름의 단수형(소문자)으로 작성하는 것을 권장 (이유는 이어지는 모델 참조에서 확인 예정)
  - 게시글을 담당하는 곳은 게시판에서 담당

  

- 댓글 기능 구현

  - 댓글목록:게시글 상세(articles: detail)
  - 댓글작성: 게시글 상세(article:detail)
  - 생성: DB에 저장
    - 생성 완료 후: 상세 페이지로 이동(article.detail)

  - Model
    - 생성시간
    - 내용
    - article Fk

``` python
#models.py

class Comments(models.Model):
  	content = models.TextField()
    created_at = models.DateTImeField(auto_now_add=True)
    #Article입장에서는 역참조, 직접 클래스가 정의 되지 않음, comments는 article은 직접 참조한다.
    article = models.ForeignKey(Article, on_delete=mdodels.CASCADE)
    
#forms.py
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments 
        fields = ['content',]
```

`python manage.py makemigrations` `python manage.py migrate`

- ForeignKey 모델 필드로 인해 작성된 컬럼의 이름이 article_id인 것을 확인
- 만약 ForeignKey 인스턴스를 article이 아닌 abcd로 생성 했다면 abcd_id로 만들어짐
  - 이처럼 명시적인 모델 관계 파악을 위해 참조하는 클래스 이름의 소문자(단수형)로 작성하는 것이 권장 되었던 이유

```python
# comment 클래스의 인스턴스 comment 생성
comment = Comment()

#인스턴스 변수 저장
comment.content = 'first comment'

#DB에 댓글 저장
comment.save()

#에러 발생
django.db.utils.IntegrityError: NOT NULL, constraint faild: articles_comment.article_id
#aritlces_comment 테이블의 ForeignKeyField, article_id 값이 저장시 누락되었기 때문

#게시글 생성 및 확인
article = Article.objects.create(title="title", content="content")
article
=> <Article:title>

# 외래 키 데이터 입력
# 다음과 같이 article 객체 자체를 넣을 수 있다
comment.article = article
# 또는 comment.article_id = article.pk 처럼 pk 값을 직접 외래 키 컬럼에
# 넣어 줄 수도 있지만 권장하지 않음

# DB에 댓글 저장 및 확인
comment.save()
comment
=> <Comment: first comment>

comment.pk
=> 1

comment.content
=> 'first comment'

#클래스 변수명인 article로 조회 시 해당 참조하는 게시물 객체를 조회할 수 있다
comment.article
=> <Article: title>
 
# aritcle_pk는 존재하지 않는 필드이기 때문에 사용 불가
comment.article_id
=> 1

# 1번 댓글이 작성된 게시물의 pk 조회
comment.article.pk
=> 1

# 1번 댓글이 작성된 게시물의 content 조회
comment.article.content
=> 'content'

comment = Comment(content="second comment", article=article)
comment.save()

comment.pk
=> 2
comment
=> <Comment: second comment>

comment.article_id
=> 1
```



```python
# admin.py
from .models import Article, Comment
class CommentAdmin(admin.ModelAdmin):
  	list_display = ('content', 'created_at', 'article' )

admin.site.register(comment, commentAdmin)
```

```python
#댓글 생성 연습하기
python manage.py shell_plus

Article.objects.create(title='제목1', content="내용1")

article = Article.objects.create(title='제목1', content="내용1")

#게시글 13번에 내용이 111인 댓글을 생성하는 코드를 작성하세요
Comment.obejcts.create(content = '111', article=article) # 객체로 출력
or Comment.obejcts.create(content = '111', article_id= 13) # Integer출력
# comment.article_id == 13
# 13번 게시글의 모든 댓글을 알고자 한다면 어떻게 해야할까요?
Comments.objects.fillter(article_id = 13)
or article.comments_set.all() #객체가 담긴 set으로 받는다 

#참조 대상은(직접 참조) comment.article
#역참조는 article.comment_set

# 만약에 A라고 하는 모델에 B모델의 FK를 정의했어요 그러면 B모델은 A를 어떻게 쓰나?
b.a_set
```



### 관계 모델 참조

- Related manager
  - Related manager는 1:N 혹은 M:N 관계에서 사용 가능한 문맥(context)
  - Django는 모델 간 1:N 혹은 M:N 관계가 설정되면 역참조할 때에 사용할 수 있는 manager를 생성 
    - 우리가 이전에 모델 생성 시 objects라는 매니저를 통해 queryset api를 사용했던 것처럼 related manger를 통해 queryset api를 사용할 수 있게 된다
  - 지금은 1:N 관계에서의 related manager 만을 학습할 것
- 역참조
  - 나를 참조하는 테이블(나를 외래 키로 지정한)을 참조하는 것
  - 즉, 본인을 외래 키로 참조 중인 다른 테이블에 접근하는 것
  - 1:N 관계에서는 1이 N을 참조하는 상황
    - 외래 키를 가지지 않은 1이 외래 키를 가진 N을 참조

- `article.comment_set.method()`

  - Article 모델이 Comment 모델을 참조(역참조)할 때 사용하는 매니저
  - article.comment 형식으로는 댓글 객체를 참조 할 수 없다
    - 실제로 Article 클래스에는 Comment와의 어떠한 관계도 작성되어 있지 않다
  - 대신 Django가 역참조 할 수 있는 comment_set manager를 자동으로 생성해 article.comment_set 형태로 댓글 객체를 참조할 수 있다
    - 1:N 관계에서 생성되는 Related manager의 이름은 참조하는 "모델명_set" 이름 규칙으로 만들어진다
  - 반면 참조 상황(Comment -> Article)에서는 실제 ForeignKey 클래스로 작성한 인스턴스가 Comment 클래스의 클래스 변수이기 때문에 comment.article 형태로 작성 가능

- ForeignKey arguments - related_name

  - ForeignKey 클래스의 선택 옵션
  - 역참조 시 사용하는 매니저 이름(model_set manager)을 변경할 수 있다
  - 작성 후, migration 과정이 필요
  - 선택 옵션이지만 상황에 따라 반드시 작성해야 하는 경우가 생기기도 하는데 이는 추후 자연스럽게 만나볼 예정
  - 작성 후 다시 원래 코드로 복구

  ```python
  # articles/models.py
  
  class Comment(models.Model):
    	article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name = "comments")
  
  #위와 같이 변경하면 기존 article.comment_set은 더 이상 사용할 수 없고, article.comments로 대체됨
  ```

  

- M: Model Class 정의(python)
- T: Django Template language {% %} {{}}
- V: 모든 파이썬 코드

```python
# veiws.py
def detail:
  context = {
    'article': article,
    "comments" : article.comment_set.all(),
  }
```





```html
<!--detail.html-->
<!-- set.all()하면 에러난다 --> 
<form action="{% url 'articles:comment_create' article.pk%}" method="POST">
  {% csrf_token %}
  {% bootstrap_form comment_form layout="inline"%}
  {% bootstrap_butoon button_type="submit" content+"OK"}
</form>
{% for comment in comments %}
<p> {{ comment.content}} </p>
<hr>
{% empty %}
	<p>댓글이 없어요 </p>
{% endfor %}
```

```python
# models.py
from .models import Article, comment

class CommentForm(forms.ModelForm):
  	class Meta:
      model = comment
      exclude = ('article',)
      fields = "__all__"
      

#views.py
from .forms import ArticleForm, CommentForm
def detail:
  article = Article.objects.get(pk=pk)
  comment_form = CommentForm()
  context = {
    'article': article,
    "comments" : article.comment_set.all(),
    'comment_form': comment_form, 
  }
  return render(request, 'articles/detail.html', context)
```

```python
# urls.py
path('<int:pk>/comments', views.comment_create, name="comment_create")

#views.py
def comment_create(request, pk):
  	article = Article.obejcts.get(pk=pk)
    #모델폼의 역할은 특정 모델 필드를 만들고 받는다
    comment_form = CommentForm(request.POST)
    #comment_form은 CommentForm의 인스턴스
    if comment_form.is_valid():
      #save하기 전에 잠깐 멈추고 return하는 객체를 내가 조작해서 저장할래 너가 직접 db에 세이브하지말고 내가 직접 넣을 값들이 필요한데 내가 				직접 세이브 할게 ! 모델폼을 쓰면서 내가 객체를 리턴받아서 쓸 수 있다 
      	#save 한 후에 return 받은 이 친구들은 Comments 클래스의 인스턴스이다. 모델폼의 save메서드는 리턴 값이 그 모델의 인스턴스이다.
      	comment = comment_form.save(commit=false)
        comment.article = article
        comment.save()
    return redirect('articles:detail', article.pk)
```

- 출력에서 제외된 외래 키 데이터는 어디서 받아와야 할까? 
- detail 페이지의 url을 살펴보면 path('`<int:pk>`/', views.detail, name='detail') url에 해당 게시글의 pk 값이 사용 되고 있음
- 댓글의 외래 키 데이터에 필요한 정보가 바로 게시글의 pk값
- 이전에 학습했던 url을 통해 변수를 넘기는 variable routing을 사용
- The save() method
  - save(commit=False)
    - "create, but don't save the new instance"
    - 아직 데이터베이스에 저장되지 않은 인스턴스를 반환
    - 저장하기 전에 객체에 대한 사용자 지정 처리를 수행할 때 유용하게 사용
- comment.article # article 객체다
- article.comment_set.all()(모델이름_set) # comment 쿼리셋(N개)- 1대 N관계를 만들고 있다. 
- Foreignkey
  - 대상 모델 - 누구 참조?
  - 삭제시 - 대상 사라지면?
- ModelForm 활용한 정의
  - 요청데이터(request.POST)를 모델 폼에 넣고
  - 유효성검사(is.valid())
  - 저장(DB에 저장) 추가 값을 포함해서 하고 싶어 save(commit=False)
  - save()-> 모델 인스턴스  .save(commit-false) => 모델폼 인스턴스

- DELETE

  ```python
  #articles/urls.py
  urlpatterns = [
    ...,
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name="comments_delete"),
  ]
  ```

  ```python
  #articles/views.py
  
  def comments_delete(request, article_pk, comment_pk):
    	comment = Comment.objects.get(pk=comment_pk)
      comment.delete()
      return redirect('article:detail', article_pk)
    
  ```

  ```html
  <!-- articles/detail.html-->
  {% block content %}
  	...
  	<h4>댓글 목록</h4>
  	<ul>
      {% for comment in comments %}
      <li>
        {{comment.content}}
        <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST">
          {% csrf_token %}
          <input type="submit" value="DELETE">
        </form>
      </li>
      {% endfor %}
      </ul>
  		<hr>
  {% endblock content %}
  ```



### Comment 추가 사항

- 개요

  - 댓글에 관련된 아래 2가지 사항을 작성하면서 마무리하기

    - 댓글 개수 출력하기
      - DTL filter - length 사용
      - Queryset API - count() 사용
    - 댓글이 없는 경우 대체 컨텐츠 출력하기

  - 댓글 개수 출력하기

    - DTL filter - length 사용

      ```python
      {{ comments|length}}
      {{ article.comment_set.all |length}}
      ```

    - Queryset API - count()사용

      ```python
      {{ comments.count }}
      {{ article.comment_set.count}}
      ```

  - detail 템플릿에 작성하기

    ```html
    <!-- articles/detail.html -->
    
    <h4>댓글 목록</h4>
    {% if comments %}
    	<p><b>{{ comments|length }} 개의 댓글이 있습니다.</b></p>
    {% endif %}
    ```

    