- 조회수 기능

  -   유저클래스 가져오기

    ```python
    
    
    from django import forms
    from .models import Article, Comment
    
    class ArticleForm(forms.ModelForm):
    
        class Meta:
            model = Article
            # fields = '__all__'
            fields = ('title', 'content',)
            
            
            
    #views.py 
    def create(request):
        if request.method == 'POST':
            form = ArticleForm(request.POST)
            if form.is_valid():
                article = form.save(commit=False)
                article.user = request.user
                article.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm()
        context = {
            'form': form,
        }
        return render(request, 'articles/create.html', context)
    
    
    def delete(request, pk):
       article = get_object_or_404(Article, pk=pk)
       if request.user.is_authenticated:
           if request.user == article.user: 
               article.delete()
               return redirect('articles:index')
       return redirect('articles:detail', article.pk)
    
    
    def update(request, pk):
        article = get_object_or_404(Article, pk=pk)
        if request.user == article.user:
            if request.method == 'POST':
                form = ArticleForm(request.POST, instance=article)
                if form.is_valid():
                    form.save()
                    return redirect('articles:detail', article.pk)
            else:
                form = ArticleForm(instance=article)
        else:
            return redirect('articles:index')
        context = {
            'article': article,
            'form': form,
        }
        return render(request, 'articles/update.html', context)
     
    
    
    ```

    ```html
    
    {% if user == article.user %}
      <a href="{% url 'articles:update' article.pk %}">[UPDATE]</a>
      <form action="{% url 'articles:delete' article.pk %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="DELETE">
      </form>
    {% endif %}
    ```

    

    - 본격적 수업

      ```python
      #models.py
      from django.conf import settings
      
      #문자열로 더 정확하게 표현하기 위해서
      user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
      
      #만약에 마이그레이션과 마이그레이트 하면 디폴트 값 설정해달라고 요청
      #기존 정보에 새로운 속성이 추가가 되어서 여기에 값을 추가해 주어야 한다
      1치고 3치면 돼
      ```

      - Not Null constraint failed:뜨면 db의 문제이다!

      - 유저 정보를 어떻게 넣을까요?

        - Views.py 함수정의이된 곳에서 내가 사용자로부터(요청) 받을 수 있는 정보는 무엇이 있을까요?
          - request(request.POST/request.GET)
          - URL(varaible routing) 
        - 사용자는 어떻게 요청으로 서버에 값을 전달할까요?
          - request => Form
            - Form에서 값 입력해줘서
          - URL => 내가 깔아놓은 길
            - 게시글 보기(버튼 누르면 내가 URL에 값 넣어놨지)

        ```python
        #views.py 
        def create(request):
            if request.method == 'POST':
                form = ArticleForm(request.POST)
                if form.is_valid():
                    article = form.save(commit=False)
                    #로그인한 유저 => 작성자네!~
                    article.user = request.user
                    article.save()
                    return redirect('articles:detail', article.pk)
            else:
                form = ArticleForm()
            context = {
                'form': form,
            }
            return render(request, 'articles/create.html', context)
        ```

        ```html
        <!-- index.html -->
        <h3>
          {{article.pk}}
        </h3>
        <h3>
          <a href="{% url 'accounts:detail' article.user.id%}"{{article.user.username}}
        </h3>
        
        or 
        <p>
          {{article.user.username}}
        </p>
        
        
        <!--detail.html-->
        
        user가 작성한 모든 글!!
        <h3>작성한 글</h3>
        <p class="text-muted">{{user.article_set.all | length}}</p>
        {% for article in user.article_set.all %}
          <p>
           {{forloop.counter}}
        <a href="{% url 'articles:detail'article.pk%}"> {{article.title}}</a>
         </p>
          
        {% if request.user == article.user %}  
        <P>
         <a href="{% url 'articles:update' article.pk %}">수정하기</a>  
        </p>
        ```

        ```python
        #업데이트에서 수정해야 각자 자기글만 수정 가능
        def update(request, pk):
            article = Article.objects.get(pk=pk)
            if request.user == article.user:
                if request.method == 'POST':
                    form = ArticleForm(request.POST, instance=article)
                    if form.is_valid():
                        form.save()
                        return redirect('articles:detail', article.pk)
                else:
                    form = ArticleForm(instance=article)
            else:
              
                return redirect('articles:index')
            context = {
                'article': article,
                'form': form,
            }
            return render(request, 'articles/update.html', context)
          
        ## (1)403 에러메시지를 던져버리고 
        # 
        ```

        ```python
        #models.py
        class Comment(models.Model):
          	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        
        #마이그레이션 마이그레이트 진행(1, 3)
        #NOT NULL constraint faild
        
        #views.py
        @login_required
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
                #httpRequest obejct => 요청정보 담겨져 있는 객체 
                comment.user = request.user
                comment.save()
            return redirect('articles:detail', article.pk)
        ```
        
        ```html
        <!--detail.html-->
        <!-- set.all()하면 에러난다 --> 
        {% if request.user.is_authenticated %}
        <form action="{% url 'articles:comment_create' article.pk%}" method="POST">
          {% csrf_token %}
          {% bootstrap_form comment_form layout="inline"%}
          {% bootstrap_butoon button_type="submit" content+"OK"}
        </form>
        {% endif %}
        {% for comment in comments %}
        <p> {{ comment.user.username}}|{{ comment.content}} </p>
        <hr>
        {% empty %}
        	<p>댓글이 없어요 </p>
        {% endfor %}
        ```
        
        - user가 작성한 글 중 첫번째 글의 댓글 중에 첫번째의 user
          - user.article_set.all() # article로 이뤄진 Queryset
          - user.article_set.all()[0] # article 인스턴스
          - user.article_set.all()[0].comment_set.all() # article 인스턴스의 댓글(comment로 이뤄진 Queryset)
          - user.article_set.all()[0].comment_set.all()[0] # 그 댓글들 중에 첫번쨰
          - user.article_set.all()[0].comment_set.all()[0].user # 그 첫번째 댓글의 유저~ 
          
        -   request.user - 로그인시(User 객체), (비로그인시) AnomynousUser 객체 
          
          - Article.user # User 객체 (게시글 쓴 사람)
          - Comment.user # User 객체 (댓글 쓴 사람)
          - User.objects.get(pk=1) # User 객체 (pk가 1인 사람)
          - User.objects.all()[0] # User객체(User들 중에 첫번째 있는 사람)
          
        - Article.id vs article.pk
          
          - 지금 우리가 개발하는 방법으로는 id == pk 이다. 
          
        - Request.user는 로그인할때 발생하고, article.user는 데이터 베이스에서 가져 오는데 이 둘이 같은 객체인가?
          
          - 모두 User 클래스의 인스턴스인 것은 맞다
          - 완전 같은 인스턴스일지도 근데 아닐지도 모른다. 
          - (홍길동으로 로그인해서 이호빈이 쓴 글을 보면)
            - request.user는 홍길동이고
            - article.user은 이호빈이다.
              - 둘 다 같은 유저 객체니까 삭제 버튼/수정 버튼을 조건문을 써서 보여주기도 안보여주기도 했다. 
          - 만약 request.user에 객체가 없으면 annymous로 리턴해준다.
          - DB는 모델의 영향을 받는다. 모델폼을 활용해서 폼을 만들어 사용자가 내용을 써서 서버에 요청을 보낸다. 
          - 요청한 것은 request.POST에 들어가있다. User_id가 없으면(image, content 등 필드에 저장된게 저장이 되지 않아) Notnull이 있으면 안 돼 그래서 user_id가 있어야 db에 저장된다. 
          - form.save()를 하는 시점이 리턴 해당 모델인스턴스 그 인스턴스를 save 메서드를 호출한다.(이걸 안 하기 위해 commit=False를 한다.) 
          - article.user(user_id) = request.user(로그인한 유저) 
          
          - 모델/DB 변경 점이 있다면 => Pull 받고 migrate 국룰
          - 패키지 추가 설치했다 =? Pull 받고 requirements.txt 설치