- 장고는 웹 서버를 만든다. 
- URL을 요청을 받아서 처리하고(views.py)->DB 활용(model) 응답을 해준다.(Template)
- 가상환경을 설치해야하는 이유는 패키지를 별도로 다르게 가져가기 위해서
- pip freeze > requirements.txt를 통해 내가 활용하고 패키지를 기록지에 남긴다. 특정한 가상환경에서 버전에 맞춰서 설치 가능
- MTV패턴은 앱 단위로 가지고 있게 된다.앱 별로 별도의 MTV 패턴을 가지게 된다. 앱은 일반적으로 복수형 
- urlpatterns를 urls.py에서 만들어야 서버가 작동한다. 그리고 app_name을 지정해주고
- include를 사용하는 이유는 url설정을 하기 위해서 
- 요청 정보를 받아서 페이지를 render( 요청 받고 해당 처리 정보들을 사용자한테 보내짐) views.index 거기에 요청받으면 대응하는 함수를 만들자
- 장고는 소프트웨어 개발, UI(기능)/ DB 이 둘은 밀접한 연관관계가 있다. 
- models.Model를 상속받는 이유는 우리가 설계를 해놓으면서 기능 자체는 상속 받아 쓰고 싶어서
- 데이터베이스의 스키마를 만드는 행위가 model에서 한다. 
- auto_now_add = True는 추가 될때마다 날짜를 추가하고 auto_now는 수정될때마다 날짜를 추가
- 1.클래스 저의 -> 마이그레이션 파일 생성 -> db 반영 
- python maange.py showmigraions 테이블이 만들어졌는지 확인 
- **각 기능별로 url을 mapping되는 view 함수는 무조건 1개가 필요하다**
- form: 사용자에게 양식을 제공하고 값을 받아서(input: name, value) 서버에 전송(action)하는 역할을 한다.

- 길게 받으면 textarea를 사용한다. 
- 수많은 정보를 객체로 담아서 준다(request), view 함수를 통해서 다양하게 조작 가능
- 쿼리셋(Article 객체를 가진)
- 전송하는 form에 method를 ="POST" and 
- `{% csrf_token %}`-사용자로부터 form을 받는다. Input type = 'hidden' 사이트간의 요청 위조. 다른 사이트에서 요청이 변조된 거 아닌지 체킹하는 로직(보안적 이슈) 
- post은 http 요청 메시지의 데이터로서 전송이 되기 때문에 url 주소에 뜨지 않는다.
- post는 저장하거나 기록하는 역할을 한다. 내 정보를 데이터베이스를 저장하기 위해서는 POST  
- 이제부터 post로 한다. 클라이언트에서 서버로 주로 수정, 생성 위해 전송할 때 쓰는 메소드, Body 라는 응답 몸통에 넣어서 보낸다.

- get 정보를 조회할때 사용하고(검색) , post는 저장하거나 기록할떄 사용한다.



### Django ModelForm

- DB 기반의 어플리케이션을 개발하다보면, HTML Form(UI)은 Django의 모델과 매우 밀접한 관계를 가지게 된다. 

  - 사용자로부터 값을 받아 DB에 저장하여 활용하기 때문이다. 

- 서버 쪽에서도 유효한 데이터인지 검증을 해야한다. 

- forms.py

  ```python
  from django import forms
  from .models import Article
  
  class ArticleForm(forms.ModelForm):
    
    class Meta:
      	model = Article
        fields = '__all__' 
        ### or fields = ['내가 원하는 데이터']
        
  ### new.html
  {{article_form.as_p}}
  def new(request):
    article_form = ArticleForm(request.POST)
    conetext = {
        'article_form': article_form
      }
      return render(reuqest, 'articles/new.html', context=context)
  
  def create(request):
      if request.method == 'POST':
      	article_form = ArticleForm(request.POST)
        #valid
      	if article_form.is_valid():
         		article_form.save()
          	return redirect('articles:index')
    	else:
      		article_form = ArticleForm()
      conetext = {
        'article_form': article_form(사용자 인풋을 다 받아서, 검증까지해서 에러메시지를 만든 article_form)
      }
      #유효하지 않을때 어떻게 해주면 좋을까요? 웹 사이트들은.. 어떻게 처리하죠?
      #invalid 
      return render(reuqest, 'articles/new.html', context=context)
    	
  		#return이랑 context를 절대 들여쓰기 하면 안 돼 return 값이 없어서 오류가 뜬다. 
    
  ```

  

- 수정하기 버튼을 누르면 이전 글을 가져와야해 

```python
# update.html#



# views.py # 
def update(request, pk):
  if request.method == 'POST':
    # POST: input 값 가져와서 검증하고, DB에 저장 기존에 있는 것을 
    # create랑 다른것은 instance를 꼭 지정해야해 내가 수정하는 행위는 기존에 있는 글을 수정하는것이니까
    article_form = ArticleForm(request.POST, instance=article)
    if article_form.is_valid():
      #유효성 검사 통과하면 상세보기 페이지로
      article_form.save()
      return redirect('articles:detail', articles.pk)
     # 유효성 검사 통과하지 않으면 => context 부터해서 오류메시지 담긴 article_form을 렌더링
  else:
    	#GET : Form을 제공
   		article = Article.objects.get(pk=pk)
  		article_form = ArticleForm(instance=article)
  context = {
    'article_form' : article_form (create와 다르게 기존의 인스턴스의 값을 가진 상태)
  }
  return render(request, 'articles/update.html', context)
```

- Create 
  - 1.ui 제공(GET) 2. db저장(POST)
- Read(detail)
  - db에서 특정 가져와서 조회
- delete
  - db에서 특정 가져와서 삭제
- update
  - 1.ui 제공(GET) 2.db저장(POST) - url 동일 같은 함수에서 처리 - invalid 할 때 form 전달할 떄 단순하게 전달하기 위해서

- model form은 model에 정의된 필드된대로 UI를 그려주고 유효성 검사하고 db에 저장된다. 