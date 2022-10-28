### 비동기처리 블로그 정리 

- 비동기 처리란 무엇일까요? 

  - 특정 코드의 연산이 끝날 때까지 코드의 실행을 멈추지 않고 다음 코드를 먼저 실행

- 비동기 처리의 첫 번째 사례

  - 제이쿼리의 ajax이다. 제이쿼리로 실제 웹 서비스를 개발할 때 ajax 통신을 빼놓을 수가 없다. 보통 화면에 표시할 이미지나 데이터를 서버에서 불러와 표시해야 하는데 이때 ajax 통신으로 해당 데이터를 서버로부터 가져올 수 있기 때문이다. 

  ```js
  function getData() {
    var tableData;
    $.get('https://www.naver.com', function(response)) {
          tableData = response;
    });
  	return tableData;
  }
  
  console.log(getData()); // undefined
  ```

  - 결론부터 `$.get()` 로 데이터를 요청하고 받아올 때까지 기다려주지 않고 다음 코드인`return tableData;`를 실행했다. getData()의 결과 값은 초기 값을 설정하지 않은 tableData의 값 undefined를 출력한다. 
  - 핵심 **특정 로직의 실행이 끝날 때까지 기다려주지 않고 나머지 코드를 먼저 실행하는 것이 비동기 처리다.** 화면에서 서버로 데이터를 요청했을 때 서버가 언제 그 요청에 대한 응답을 줄지도 모르는데 마냥 다른 코드를 실행 안 하고 기다릴 순 없다.  

  ```js
  // #1
  console.log("Hello");
  
  // #2
  setTimeout(function()) {
    console.log("Bye");         
  }, 3000);
  
  // #3
  console.log("Hello Again");
  ```

  - 실제 결과 값 출력은 #1 -> #3 -> #2이다. setTimeout() 역시 비동기 방식으로 실행되기 때문에 3초를 기다렸다가 다음 코드를 수행하는 것이 아니라 일단 setTimeout()을 실행하고 나서 바로 다음 코드인 `console.log("Hello Again")` 으로 넘어갔다. 따라서 "Hello", "Hello Again"를 먼저 출력하고 3초가 지나면 'Bye'가 출력된다. 

  #### 콜백 함수로 비동기 처리 방식의 문제점 해결

  ```js
  function getData(callbackFunc) {
    	$.get("https://www.naver.com", function(response)) {
         callbackFunc(response); // 서버에서 받은 데이터 response를 callbackFunc() 함수에 넘겨준다.  
      });
  }
  
  getData(function(tableData)) {
     console.log(tableData); //$.get()의 response값이 tableData에 전달된다.     
  });
  ```

  - 콜백 함수의 동작 방식은 식당 자리 예약. 대기자 명단에 등록을 하면 주변에 있다가 연락을 받고 식당을 다시 가는데 연락을 받는 시점이 콜백 함수가 호출되는 시점과 같다. 즉 데이터가 준비된 시점에서만 저희가 원하는 동작을 수행할 수 있다.

  ```js
  function findUserAndCallBack(id, cd) {
    const user = {
      id:id,
      name: "User" + id,
      email: id + "@test.com",
    };
    cb(user); => function(user) { console.log("user:", user);}
  }
  
  findUserAndCallBack(1, function (user) {
    console.log("user:", user);
  });
  
  # 결과
  user: {id : 1, name: "User1", email: "1@test.com"}
  ```

  - cb 매개 변수는 콜백 함수를 할당 받으며, `cb(user);`가 실행될 떄, 이 콜백 함수가 실행되게 된다. `findUserAndCallBack`함수는 결과값을 이용해 해야할 작업까지 함수 내부에서 수행해주기 떄문에 결과값을 굳이 리턴할 필요가 없다. 

  ```js
  unction findUserAndCallBack(id, cb) {
    setTimeout(function () {
      console.log("waited 0.1 sec.");
      const user = {
        id: id,
        name: "User" + id,
        email: id + "@test.com",
      };
      cb(user);
    }, 100);
  }
  
  findUserAndCallBack(1, function (user) {
    console.log("user:", user);
  });
  ```

  - **비동기 함수를 호출할 떄는 결과값을 리턴 받으려고 하지말고, 결과값을 통해 처리할 로직을 콜백 함수로 넘기는 스타일로 코딩을 해줘야 예상된 결과를 얻을 수 있다** 



### AJAX(에이젝스)



- 비동기식
  - 병렬적 Task 수행
  - 요청을 보낸 후 응답을 기다리지 않고 다음 동작이 이루어짐(non-blocking)
  - 요청을 보내고 응답을 기다리지 안혹 다음 코드가 실행됨
  - 
- 동기식
  - 동기적으로 움직이다(지금 온라인 수업)- 영상 수업이면 질문 올려 놓고 다른 걸 한다. 



- Event Loop 기반 동시성 모델
- AJAX란?
  - Asynchronous JavaScript And Json
  - 비동기 웹 통신을 위한 라이브러리 



### Axios

- "Promise(도착하면 실행을 시켜주겠다는 약속) based HTTP client for the browser and Node.js"

- 브라우저를 위한 Promise 기반의 클라이언트

- 원래는 "XHR"이라는 브라우저 내장 객체를 활용해 AJAX 요청을 처리하는데, 이보다 편리한 AJAX 요청이 가능하도록 도움을 준다. 

  - 확장 가능한 인터페이스와 함께 패키지로 사용이 간편한 라이브러리를 제공한다. 

  ```html
  axios.get('https://jsoplaceholder.typicode.com/todos/1') // Promise return
  	.then(..)
  	.catch(..)
  ```

  

- Promise

  - 비동기 작업을 관리하는 객체 

    - 미래의 완료 또는 실패와 그 결과 값을 나타낸다
    - 미래의 어떤 상황에 대한 약속

  - 성공(이행)에 대한 약속

    - .then()
      - 이전 작업(promise)이 성공했을 때(이행했을 때) 수행할 작업을 나타내는 callback 함수
      - 그리고 각 callback 함수는 이전 작업의 성공 결과를 인자로 전달받음
      - 따라서 성공했을 때의 코드를 callback 함수 안에 작성

  - 실패(거절)에 대한 약속

    - .catch()

      - .then이 하나라도 실패하면(거부 되면) 동작 (동기식의 'try-except' 구문과 유사)
      - 이전 작업의 실패로 인해 생성된 error 객체는 catch 블록 안에서 사용할 수 있다.

    - 각각의 .then() 블록은 서로 다른 promise를 반환

      - 즉, .then()을 여러 개 사용(chaining)하여 연쇄적인 작업을 수행할 수 있다
      - 결국 여러 비동기 작업을 차례대로 수행할 수 있다는 뜻

    - .then()과 .catch()메서드는 모두 promise를 반환하기 때문에 chasing 가능

    - 주의

      - 반환 값이 반드시 있어야 한다
      - 없다면 callback 함수가 이전의 promise 결과를 받을 수 없다.

    - .finally(callback)

      - Promise 객체를 반환
      - 결과와 상관없이 무조건 지정된 callback 함수가 실행
      - 어떠한 인자도 전달받지 않음
        - Promise가 성공되었는지 거절되었는지 판단할 수 없기 때문
      - 무조건 실행되어야 하는 절에서 활용
        - .then()과 .catch() 블록에서의 코드 중복을 방지 

    - callback Hell -> Promise(2/2)

      ```js
      work1().then(function(result1) {
        return work2(result1)
      })
      .then(function(result2) {
        return work3(result2)
      })
      .then(function(result3){
        console.log("최종결과:" + result3) 
      })
      .catch(failureCallback)
      ```

      - .then()을 여러 번 사용하여 여러 개의 callback 함수를 추가할 수 있다(Chaining)
      - Callback 함수는 JavaScript의 Event Loop가 현재 실행 중인 Call Stack을 완료하기 이전에는 절대 호출되지 않는다
        - Promise callback 함수는 Event Queue에 배치되는 엄격한 순서로 호출된다
        - 비동기 작업이 성공하거나 실패한 뒤에 .then() 메서드를 이용한 경우도 마찬가지

  ```js
  const myPromise = axios.get(URL)
  // console.log(myPromise) // Promise Object
  
  myPromise
  	.then(response => {
    	return response.data
  	})
  // chaining
  axios.get(URL)
  	.then(response => {
    	return response.data
  	})
  	.then(response => {
    	return response.title
  	})
  	.catch(error => {
    	console.log(error)
  	})
  	.finally(function () {
  		console.log("나는 마지막에 무조건 시행!!!")  
  	})
  ```



### 비동기 적용하기

- 팔로우

  - 각각의 템플릿에서 script 코드를 작성하기 위한 block tag 영역 작성

    ```html
    <!-- base.html -->
    <body>
    	{% block script %}
      {% endblock script %}	
    </body>
    </html>
    ```

  - axios CDN 작성

    ```html
    <!-- accounts/profile.html -->
    {% block script %}
    	<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
    	<script>
    	</script>
    {% endblock script %}
    ```

  - form 요소 선택을 위해 id 속성 지정 및 선택

  - 불필요해진 action과 method 속성은 삭제 (요청은 axios로 대체되기 때문이다.)

    ```html
    <!--accounts/profile.html -->
    <!-- url에 작성할 user pk 가져오기 (HTML -> JavaScript)-->
    <form id="follow-form" data-user-id="{{ person.pk }}">
      ...
    </form>
    ```

    ```html
    <!-- accounts/profile.html -->
    <script>
    	const form = document.querySelector("#follow-form")
      <!--AJAX로 csrftoken을 보내는 방법-->
      const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
      form.addEventListener("submit", function (event) {
        <!-- sumbmit 이벤트 취소 -->
        event.preventDefault()
        <!-- url에 작성할 user pk 가져오기 (HTML -> JavaScript)-->
        const userId = event.target.dataset.userId
        <!-- axios 요청 준비-->
        axios({
          method: "post",
          <!--url 작성 마치기 -->
          url: "/accounts/${userId}/follow"
          <!--AJAX로 csrftoken을 보내는 방법-->
          headers: {'X-CSRFToken': csrftoken,}
        })
        	.then((response)) => {
          	const followersCountTag = document.querySelector("#followers-count")
            const followingsCountTag = document.querySelector("#followings-count")
            <!-- view함수에서 응답한 연산 결과를 사용해 각 태그의 인원 수 값 변경하기 -->
            followersCountTag.innerText = followersCount
          	followingsCountTag.innerText = followingCount
          	const isFollowed = response.data.is_followed
            const followBtn = document.querySelector("#follow-form > input[type=submit]")
            if (isFollowed == true) {
              followBtn.value = '언팔로우'
            }	else {
              followBtn.value = "팔로우"
            }
        }
      })
    </script>
    ```

  - data-*attributes

    - **사용자 지정 데이터 특성을 만들어 임의의 데이터를 HTML과 DOM사이에서 교환 할 수 있는 방법**

    - 사용 예시

      ```html
      <div data-my-id="my-data"></div>
      <script>
      	const myId = event.target.dataset.myId
      </script>
      ```

    - 예를 들어 data-test-value 라는 이름의 특성을 지정했다면 JavaScript에서는 element.dataset.testValue로 접근할 수 있다.

    - 속성명 작성 시 주의사항

      - 대소문자 여부에 상관없이 xml로 시작하면 안 된다
      - 세미콜론을 포함해서는 안 된다
      - 대문자를 포함해서는 안 된다. 

  - 팔로우

    - 팔로우 버튼을 토글하기 위해서는 현재 팔로우가 된 상태인지 여부 확인이 필요

    - axios 요청을 통해 받는 response 객체를 활용해 view 함수를 통해서 팔로우 여부를 파악 할 수 있는 변수를 담아 JSON 타입으로 응답하기

    - 팔로우 여부를 확인하기 위한 is_followed 변수 작성 및 Json 응답

      ```html
      <!-- accounts/profile.html -->
      {% extends 'base.html' %}
      
      {% block content %}
      	<h1>{{person.username}}님의 프로필</h1>
        <div>
          <!-- 해당 요소를 선택할 수 있도록 span태그와 id 속성 작성-->
          팔로워: <span id = "followers-count">{{person.followers.all|length}}</span> /
          팔로잉: <span id = "followers-count">{{person.followers.all|length}}</span>
      </div>
      ```

      - 팔로워, 팔로잉 인원 수 연산은 view 함수에서 진행하여 결과를 응답으로 전달

        ```python
        # accounts/views.py
        @required_POST
        def follow(request, user_pk):
          	context = {
              	"is_followed": is_followed,
              	"followers_count": you.followers.count(),
              	"followings_count": you.followings.count(),
            }
            return JsonResponse(context)
          return redirect("accounts:profile", you.username)
        return redirect("accounts:login")
        ```

      - HTML 코드

        ```html
        <!-- accounts/profile.html -->
        {% extends 'base.html' %}
        
        {% block content %}
        	<h1>{{ person.username}} 님의 프로필</h1>
        	<div>
          팔로워: <span id="followers-count">{{ person.followers.all|length}}</span>
          팔로잉: <span id="followings-count">{{ person.followings.all|length}}</span>
        	</div>
        	
        	{% if request.user != person %}
        	<div>
          	<form id="follow-form" data-user-id="{{ person.pk }}">
              {% csrf_token %}
              {% if request.user in person.followers.all %}
              	<input type="submit" value="언팔로우">
              {% else %}
              	<input type="submit" value="팔로우">
              {% endif %} 
            </form>  
        	</div>
        {%endif %}
        ```

        - Python 코드

        ```python
        #accounts/views.py
        from django.http import JsonResponse
        
        @require_POST
        def follow(request, user_pk):
          	if request.user.is_authenticated:
              User = get_user_model()
              me = request.user
              you = User.objects.get(pk=user_pk)
              if me != you:
                	if you.followers.filter(pk=me.pk).exists():
                    	you.followers.remove(me)
                      is_followed = False
                  else:
                    	you.followed.add(me)
                      is_followed = True
                 	context = {
                    'is_followed': is_followed,
                  }
                  return JsonResponse(context)
              return redirect("accounts:profile", you.username)
          	return redirect("accounts:login")
        ```

- 좋아요

  ```html
  {% extends 'base.html' %}
  
  {% block content %} 
  	<h1>Articles</h1>
  	{% if request.user.is_authenticated %}
  		<a href="{% url 'articles:create' %}">CREATE</a>
  	{% endif %}
  	<hr>
  	{% for article in articles %}
  	<p>
    	<b>작성자: <a href="{% url 'accounts:profile' article.user%}">{{article.user}}</a></b>  
  	</p>
  	<p>글 번호 : {{article.pk}}</p>
  	<p>제목 : {{article.title}}</p>
  	<p>내용 : {{article.content}}</p>
  	<div>
      <form class="like-forms" data-article-id="{{article.pk}}">
        {% csrf_token %}
        {% if request.user in article.like_users.all %}
        	<input type="submit" value="좋아요 취소" id="like-{{article.pk}}">
        {% else %}
        	<input type="submit" value="좋아요" id="like-{{article.pk}}">
       	{% endif %}
      </form>
  	</div>
  	<a href="{% url 'articles:detail' article.pk %}">상세 페이지</a>
  	<hr>
  	{% endfor %}
  {% endblock content %}
  ```

  ```python
  # articles/views.py
  
  from django.http import JsonResponse
  
  @require_POST
  def likes(request, article_pk):
    	if request.user.is_authenticated:
        	article = Article.objects.get(pk=article_pk)
          
          if article.like_users.filter(pk=request.user.pk).exists():
            	article.like_users.remove(request.user)
              is_liked = False
          else:
            	article.like_users.add(request.user)
              is_liked = True
          context = {
            "is_liked": is_liked,
          }
          return JsonResponse(context)
      return redirect("accounts:login")
  ```

  



- 매번 새로운 html을 주는게 아니라 리소스를 줄일 수 있고 클라이언트가 조작한다. 데이터가 오면 데이터를 붙여준다. 
- 웹 브라우저 상에서 자바스크립트가 실제 화면을 고쳐주는 역할을 하고 그걸 필요한 json 데이터를 전송해주는게 핵심

- CSS, JS 항상 CDN 혹은 해당 파일을 불러와야한다. JS -> 브라우저 조작
- axios는 URL로 요청을 보내준다. 요청 보내서 처리가 완료되면 실행시켜주겠다는 약속
- 성공적이면 then, 실패면 catch
- 성공해서 받은 응답 객체를 활용한 조작 
- 비동기 요처을 보내는 것!
- Json으로 무엇을 보내줘야 내가 DOM 조작을 할 수 있을 것인가? (Boolean)
- Json은 문자열이다. Js에서는 배열 안에 객체(parsing) import json을 하면 
- 데이터는 json을 많이 사용 epoch time
- Js는 비동기적으로 실행 (이벤트루프기반)  -> 콜백함수, promise, then에 있는 함수 실행 실패하면 catch -> axios 
- 링크, 버튼, url 등등을 누르면 이벤트가 발생하여 axios 요청
- Json(2) - then 메서드 안에서(3) 수작업(Dom조작) => 화면 일부 변경









#### 27일 추가

### Django query 심화

- aggregate는 db에서 처리한다. 
- Annotate(주석처리)
- Selected_related(반복적으로 활용되고 있는 모습에서 쿼리를 효율적으로 사용 가능 쿼리가 10개에서 1개로 줄었다. ) -> N+1 문제를 해결 
- Prefetch_related(역참조에서 사용된다. )- 역참조 대상은 join을 하지 않는다. 

- Custom template tag 





#### 28일 추가

- 헤로쿠 설치하고 터미널이나 vscode를 재부팅
- 