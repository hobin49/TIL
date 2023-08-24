- html의 id로 접근해서 이름 바꾸기

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1 id="hello">안녕하세요</h1>
  <script>
    // 우측꺼를 왼쪽에 집어넣어라
    // 1.바꿀 요소를(셀렉터) 2.무엇을 3.어떻게?
    document.getElementById("hello").innerHTML = "안녕"
  </script>
</body>
</html>
```

- fontSize 변경

```html
<body>
  <h1 id="hello">안녕하세요</h1>
  <script>
    document.getElementById("hello").style.fontSize = "16px";
  </script>
</body>
```

- UI 만드는 step
  - HTML/CSS로 미리 디자인(필요하면 미리 숨김)
  - 필요할 때 보여달라고 코드 짬(자바스크립트로)
- 함수 영어 작명시엔
  - 소문자 시작
  - CamelCase
- 버튼 누르면 알림창 열리게 + 닫기 버튼 누르면 닫히게

```html
    <body>
       <div class="alert-box" id="alert">알림창임<button onclick="알림창닫기()">닫기</button></div>
       <button onclick="알림창열기()">버튼</button>
       <script>
           function 알림창열기() {
             document.getElementById('alert').style.display='block';
           }
           function 알림창닫기() {
             document.getElementById("alert").style.display="none";
           }
       </script>    
    </body>
```



- 근데 비슷한 함수를 굳이 다시 생성하지 말고 파라미터를 활용해서 더 줄일 수 있음

```html
    <body>
       <div class="alert-box" id="alert">알림창임<button onclick="알림창('none')">닫기</button></div>
       <button onclick="알림창('block')">버튼</button>
       <script>
           function 알림창(파라미터) {
             document.getElementById('alert').style.display=파라미터;
           }
           
       </script>    
    </body>
```



- getElementByClassName
  - 클래스 이름은 중복이 있을 수 있으니 
    - **getElementsByClassName('클래스명')[순서]**로 사용해야 한다. 



- addEventListener 함수 (onclick없어도 click시 동작 가능)

  ```js
  document.getElementById("id이름").addEventListener("event명", 콜백함수() {
    // 실행시킬 내용
    document.getElementById('alert').style.display = 'none'; 
  })
  ```

- event는 키입력, 클릭, 스크롤, 드래그 등 유저들이 내 페이지에 조작을 가하는 것들 언급한 거 이외에 더 많다.



- class부착식으로 개발하면
  - 애니메이션 추가 쉽고
  - 나중에 재사용 편리하다. 



- class에 새로운 요소를 추가하는 법 
  - classList를 사용하면 된다. 
  - toggle을 이용하면 boolean 형태로 show라는 것을 자동으로 보임/안보임 설정 가능하다. 

```html
<body>
  <nav class="navbar navbar-light bg-light">
   <div class="container-fluid">
     <span class="navbar-brand">Navbar</span>
     <button class="navbar-toggler" type="button">
       <span class="navbar-toggler-icon"></span>
     </button>
   </div>
 </nav>
 <ul class="list-group">
    <li class="list-group-item">An item</li>
    <li class="list-group-item">A second item</li>
    <li class="list-group-item">A third item</li>
    <li class="list-group-item">A fourth item</li>
    <li class="list-group-item">And a fifth one</li>
 </ul> 
    
    
  <script>
      document.getElementsByClassName('navbar-toggler')[0].addEventListener("click", function() {
        document.getElementsByClassName("list-group")[0].classList.toggle("show");
      })
  </script> 
```



- querySelector

  - 안에 css selector를 통해서 요소를 찾아서 사용한다. 
  - css 문법 그대로 쓴다.
  - 만약 똑같은 css selector가 존재하면 **가장 위에 나오는 한개만 찾아준다.**
    - 그래서 querySelectorAll()을 사용하면 다 찾아준다. 

  ```HTML
  document.querySelector(".list-group") 
  document.querySelectorAll(".list-group-item")[몇 번째 요소]



- jQuery

  - HTML 조작문법을 쉽게 바꿔주는 라이브러리
  - 함수명만 짧아짐
  - 거의 모든 자바스크립트 라이브러리는 `<body>` 끝나기 전에 넣는거 권장 
  - querySelector => $로 짧아짐
  - querySelctorAll() 처럼 자동으로 해당 css Selector를 다 선택해준다. 
  - jQuery 함수만 붙일 수 있다. 자바스크립트 코드(innerHTML)은 못 붙인다. 

  ```js
  // html 내용 교체
  $(".hello").html("바보");
  
  // css 변경
  $(".hello").css("color", "red");
  
  // class탈부착
  $('.hello').addClass('show')
  
  // 이벤트리스너 부착 
  $('#test-btn').on("click", function() {
    // 간단한 에니메이션도 가능
    $('.hello').hide();
    $('.hello').fadeout();
  })
  ```

- modal창 띄우기

  ```html
      <div class="black-bg">
          <div class="white-bg">
          <h4>로그인하세요</h4>
          <button class="btn btn-danger" id="close">닫기</button>
          </div>
      </div>
      <script>
  			$("#modal").on("click", function() {
           $(".black-bg").addClass("show-modal");
        })
  		</script>
  ```

- UI에 애니메이션 추가하려면 가능하면 CSS만으로 처리하는게 좋다(성능때문에)

- one-way UI 애니메이션 만드는 법

  - 1.시작스타일

  - 2.최종스타일

    - display:none 과 visibility: hidden의 차이는 display는 화면상에 없애는거고 visibility는 숨기는 역할을 하기 때문에 애니메이션 쓰려면 쓰자. 

  - 3.원할 때 최종스타일로 변하라고 코드짬

  - 4.transition 추가

    - `transition: all 1s` - 모든 css 속성이 1초에 걸쳐서 변하게 

    

- 모달창 안에 `<form>` 만들기

  - 전송하려면 type을 submit하고 아니면 button이라고 정의하자.

  ```html
   <div class="black-bg">
          <div class="white-bg">
          <h4>로그인하세요</h4>
          <form action="success.html">
            <div class="my-3">
              <input type="text" class="form-control" id="email">
             </div>
             <div class="my-3">
               <input type="password" class="form-control" id="password">
             </div>
             <button type="submit" class="btn btn-primary">전송</button>
             <button type="button" class="btn btn-danger" id="close">닫기</button>
          </form> 
          </div>
      </div> 
  ```

  - 만약 input이 빈값이라면? (아이디 입력해주세요 띄우기)

  ```js
  $('form').on('submit', function(e){
    // document.getElementById().value === 사용자가 입력한 값
    if (document.getElementById('#email').value == '') {
      alert('아이디 입력하쇼');
      e.preventDefault();
    }
  });
  ```





- input에서 발생하는 특별한 이벤트

  ```js
  // input 이벤트: 유저가 입력한 값이 변경될 때마다 실행
  document.getElementById("email").addEventListener('input', function() {
  })
  
  // change 이벤트: 유저가 입력한 값이 변경될 때마다 실행 
  document.getElementById("email").addEventListener('change', function() {
    console.log('안녕')
  })
  ```

  - **change 이벤트는 input에 입력한 값이 바뀌고 focus를 잃을 때 발생**





- var, let, const
  - var는 함수레벨 스코프
  - let, const는 블록레벨스코프이다. 



- setTimeout()

  - x초후에 실행하려면

    - setTimeout(콜백함수(){ 실행할코드 }, ms)

    ```js
    // 1초후에 alert 숨김
    setTimeout(function() {
       $(".alert").hide();
    }, 1000)
    
    
    // 함수가 길면 함수를 만들어서 넣으면 돼
    setTimeout(함수, 1000)
          
    function 함수() {
       console.log("안녕")
    }
    ```

- setInterval()

  - x초마다 실행하려면

    ```js
    setInterval(function() {
      console.log("안녕");
    }, 1000);
    ```

    

- if var function 같은 건 자바스크립트 문법 vs document.querySelector(), setTimeout(), alert() 브라우저 사용법(web Browser API)
  - 웹 개발을 잘하려면 자바스크립트 문법, 브라우저 사용법을 잘 알아야 한다. 





- 정규식으로 이메일형식 검증해보기
  - 문자 검사하는 쉬운 방법
    - .includes() 메서드 
  - 정규표현식을 사용하면 특정 패턴이 있는지 체크 확인 가능
    - /검사할문자/.test("검사당할 문자")
      - /a-zA-Z/.test("abcde") - 영어
      - /[ㄱ-ㅎ 가-힣]/.test("바보") - 한국어
      - /\S/.test("ㅋㅋㅋㅋ") - 아무 문자(특수기호 포함)
      - /^a/.test("asdfdfsa") - a로 시작하는지 체크
      - /(a|b)/.test('sfac') - a 또는 b 체크
  - 이메일 형식 검사하기
    - `/\S+\@\S+\.\S+/.test("aaa@bbb.ccc")`
      - `+` 기호는 문자 반복 검색 
      - `.` 은 정규식에서 특수한 문법이기 떄문에 진짜 마침표를 찾아달라는 의미로 백슬래시를 앞에 붙여야 한다. 



- 이미지를 왼쪽으로 이동시에 margin-left보다 transform이 부드럽다. 

- 캐러셀 구현

  ```html
  <div style="overflow: hidden">
      <div class="slide-container">
         <div class="slide-box">
           <img src="car1.png">
         </div>
         <div class="slide-box">
           <img src="car2.png">
         </div>
         <div class="slide-box">
           <img src="car3.png">
         </div>
      </div>
  </div>
  
  <button class="before">이전</button>
  <button class="slide-1">1</button>
  <button class="slide-2">2</button>
  <button class="slide-3">3</button>
  <button class="next">다음</button>
  
  <script>
     $(".slide-1").on("click", function() {
        $(".slide-container").css("transform", "translateX(0)");
     })
        
     $(".slide-2").on("click", function() {
        $(".slide-container").css("transform", "translateX(-100vw)");
     })
        
     $(".slide-3").on("click", function() {
        $(".slide-container").css("transform", "translateX(-200vw)");
     })
    
    	  $(".before").on("click", function() {
  		$(".slide-container").css("transform", "translateX(-" + 이전사진 + "00vw)");
  			이전사진--;
  		    if (이전사진 < 0) {
  				이전사진 = 2;
  			}
  	  });
  	  
  	  
        let 지금사진 = 1;
  	  
  	  $(".next").on("click", function() {
  			$(".slide-container").css("transform", "translateX(-" + 지금사진 + "00vw)");
  			지금사진++;
  		    if (지금사진 === 3) {
  				지금사진 = 0;
  			}
  	  });
  </script>
  ```

  ```css
  .slide-container {
      width: 300vw;
      transition: all 1s;
  }
  
  .slide-box {
      width: 100vw;
      float: left;
  }
  
  .slide-box img {
      width: 100%;
  }
  
  ```

  - toFixed는 소수점 반올림하는 법
  - parseFloat, parseInt 문자 => 숫자







- 스크롤 이벤트 

  - scroll 이벤트리스너

  ```js
  //windows는 html 페이지, 구조가 widow(document(html))
  	 window.addEventListener("scroll", function() {
       // 위로부터 얼마나 내렸는지 측정가능(pageYOFFset === scrollY)
  		 console.log(window.pageYOffset);
  		 // 강제로 스크롤하기(0~ 100px)
  		 window.scrollTo(0, 100);
  		 // 현재 위치에부터 강제로 스크롤하기
  		 window.scrollBy(x, y)
  });
  
  
  // JQuery 사용하면 스크롤바 위치 출력 + 이동 두 가지 동시에 가능
  $(window).on("scroll", function() {
  	console.log($(window).scrollTop(100))
  })
  
  ```

  - 스크롤 위치가 순간이동하지 않고 bootstrap을 설치했을 경우 천천히 이동할 수 있다.
    - 그게 싫으면 아래 코드를 넣어주자.

  ```css
  :root { 
    scroll-behavior : auto
  }
  ```

  

  - 문제 1. 스크롤바를 100px 내리면 폰트 사이즈 작게 반대로 100px 미만으로 내리면 크게 만들자

  ```js
  // 스크롤바를 100px 내리면 로고 폰트사이즈를 작게 만들고
  // 반대로 100px 미만으로 내리면 로고 폰트사이즈를 크게 만들자.
  	  
  $(window).on("scroll", function() {
    // scrollY를 이용해서 100px 보다 위면 작게 그리고 크면 크게했다.
  	if (window.scrollY > 100) {
  		 $(".navbar-brand").css("font-size", "5px")
  	} else {
  		 $(".navbar-brand").css("font-size", "30px")
  	}
  });
  ```

  - 문제2. 약관을 하나 만들었다. 이 약관을 끝까지 다 읽으면 alert창을 띄어주자

  ```js
  // <div> 스크롤바 내린 높이는 셀렉터.scrollTop
  // div의 스크롤바 내린 양 + 눈에 보이는 div 높이 == div의 실제높이
  $(".lorem").on("scroll", function() {
    // 스크롤 내리는 양
  	let 스크롤양 = document.querySelector(".lorem").scrollTop
    // 박스의 실제 높이
  	let 실제높이 = document.querySelector(".lorem").scrollHeight;
    // 눈에 보이는 높이
  	let 높이 = document.querySelector(".lorem").clientHeight;	
  	if (스크롤양 + 높이 == 실제높이) {
  			alert("약관 다 읽으셨습니다")
  	}
  })
  ```

  - scroll 다룰 때 주의할 점

    - scroll 이벤트리스너 안의 코드는 1초에 60번 이상 실행된다. (컴퓨터가 힘드니까 많이 쓰면 안 돼)
    - 스크롤 바닥까지 체크하는데 alert 창이 중복으로 실행된다. 

    ```js
    // <html> 높이
    // 페이지 로드 완료시 실행해야 정확하다.(bdoy 태그 안에 넣자)
    // querySelector("html") === documentElement
    document.querySelector('html').scrollHeight;
    document.querySelector('html').clientHeight;
    ```

  - 교훈

    - 스크롤바를 조작할 때마다 코드실행이 가능하다
    - 박스의 실제 높이/ 보이는 높이 구할 수 있다. 

- 탭기능

  - 반복문 사용해서 탭버튼 만들기

  ```html
  <div class="container mt-5">
    <ul class="list">
      <li class="tab-button">Products</li>
      <li class="tab-button orange">Information</li>
      <li class="tab-button">Shipping</li>
    </ul>
    <div class="tab-content">
      <p>상품설명입니다. Product</p>
    </div>
    <div class="tab-content show">
      <p>스펙설명입니다. Information</p>
    </div>
    <div class="tab-content">
      <p>배송정보입니다. Shipping</p>
    </div>
  ```

  

  ```js
  let 버튼 = $(".tab-button");
  let 내용 = $(".tab-content");
  
  for (let i = 0; i < 3; i++) {
     버튼.eq(i).on("click", function(){
     버튼.removeClass("orange");
     버튼.eq(i).addClass("orange");
     내용.removeClass("show");
     내용.eq(i).addClass("show");
   })
  }
  ```



- 이벤트 버블링

  - 모든 브라우저는 이벤트 버블링이 일어난다.(이벤트가 상위 html로 퍼지는 현상)
  - 유용한 이벤트관련 함수들
    - e.target
      - 이벤트 발생한 곳(유저가 실제로 누른거)
    - e.currentTarget
      - 이벤트리스너 달린 곳
    - e.preventDefault();
      - 이벤트 기본동작 막아줌
    - e.stopPropagation();
      - 내 상위요소로 이벤트 버블링 막아줌

  ```js
  	  $(".black-bg").on("click", function(e) {
  		  // JQuery랑 document.querySelector()결과가 다르다. 
        // 유저가 실제로 누른게 까만 배경이면 모달이 닫히게 설정한다. 
  		  if (e.target == document.querySelector(".black-bg")) {
  			document.querySelector(".black-bg").classList.remove("show-modal");	  
  		 }
  	  })
  ```

- Tab-button 함수화하기

  ```javascript
  let 버튼 = $(".tab-button");
  let 내용 = $(".tab-content");
  
  for (let i = 0; i < 버튼.length; i++) {
     버튼.eq(i).on("click", function(){
  	  탭열기(i)
   })
  }
  
  function 탭열기(i) {
     버튼.removeClass("orange");
     버튼.eq(i).addClass("orange");
     내용.removeClass("show");
     내용.eq(i).addClass("show");
  }
  ```

  

- dataset

  - html 태그에 몰래 정보숨기기 가능 (data-자료이름="값")

  ```html
    <ul class="list">
      <li class="tab-button" data-id="0">Products</li>
      <li class="tab-button orange" data-id="1">Information</li>
      <li class="tab-button" data-id="2">Shipping</li>
    </ul>
  ```

  - e.target을 활용해서 data-id에 접근

  ```html
  $(".list").click(function(e) {
  	탭열기(e.target.dataset.id);
  })
  ```

- object 자료

  ```js
  let car = { name : '소나타', price : 50000, year : 2030 };
  
  // 접근방법
  console.log(car['name']) || console.log(car.name)
  ```

- Array/object 차이점

  - 상품데이터가 많으면 object가 좋다.
  - array 자료간 순서가 존재 / object는 순서개념이 없다.
  - array 정렬, 자르기, 자료검색, 맨앞/맨뒤에 자료추가 가능
  - object안에는 아무거나 다 넣을 수 있음(object, array 가능)

- 데이터 바인딩

  ```html
  <div class="card-group container">
  	  <div class="card">
  		<img src="https://via.placeholder.com/600">
  		<div class="card-body">
  		  <h5>Card title</h5>
  		  <p>가격 : 70000</p>
  		  <button class="btn btn-danger">주문하기</button>
  		</div>
  	  </div>
  	  <div class="card">
  		<img src="https://via.placeholder.com/600">
  		<div class="card-body">
  		  <h5>Card title</h5>
  		  <p>가격 : 70000</p>
  		  <button class="btn btn-danger">주문하기</button>
  		</div>
  	  </div>
  	  <div class="card">
  		<img src="https://via.placeholder.com/600">
  		<div class="card-body">
  		  <h5>Card title</h5>
  		  <p>가격 : 70000</p>
  		  <button class="btn btn-danger">주문하기</button>
  		</div>
  	  </div>
  </div>
  ```

  ```javascript
  let products = [
  		{ id : 0, price : 70000, title : 'Blossom Dress' },
  		{ id : 1, price : 50000, title : 'Springfield Shirt' },
  		{ id : 2, price : 60000, title : 'Black Monastery' }
  	];
  	  
  for (let i = 0; i < products.length; i++) {
  	document.querySelectorAll('.card-body h5')[i].innerHTML = products[i].title;
  	document.querySelectorAll(".card-body p")[i].innerHTML = '가격: ' + products[i].price;
  }
  ```




- select

  ```js
  	let 셀렉터 = $(".form-select");
  		
  		
  	셀렉터.eq(0).on("input", function() {
      // e.currentTaget.value === this.value 똑같아.
  		 let value = this.value;
  		 if (value === "셔츠") {
  			 셀렉터.eq(1).removeClass("form-hide");
  		 } else {
  			 셀렉터.eq(1).addClass("form-hide");
  		 }
  	})
  ```



- 자바스크립트 html 생성법

  ```js
  // 방법1
  let a = document.createElement("p");
  a.innerHTML = "안녕"
  document.querySelector("#test").appendChild(a);
  
  
  // 방법2
  let b = "<p>안녕</p>"
  
  // beforeend 는 안쪽 맨 밑에 추가하라는 뜻이다.
  document.querySelector("#test").insertAdjacentHTML("beforeend", b);
    
   
  // 방법3 JQuery
  let c = "<p>안녕</p>"
  $("#test").append(c);
  
  // 방법 4 innerHTML
  document.querySelector("#test").innerHTML
  ```

  

```js
	셀렉터.eq(0).on("input", function() {
		 let value = this.value;
		 if (value === "셔츠") {
			 셀렉터.eq(1).removeClass("form-hide");
       //옵션 변경하기
		 } else  if (value == "바지") {
			 셀렉터.eq(1).removeClass("form-hide");
			 // 기존 select 비워주세요.
			 셀렉터.eq(1).html("");
			 let 템플릿 = `<option>28</option><option>30</option>`
			 
			 $(".form-select").eq(1).append(템플릿);
		 }
	})
```



- object를 사용할 때 for in 반복문 쓰면 된다. 

- arrow Function을 사용하면 함수 안의 this 뜻이 달라질 수 있다. 

  - function 안에서 쓰면 this가 알맞게 재정의됨.

- Ajax 새로고침 없이 GET, POST 요청하는 기능 

  - 서버와 유저는 문자자료만 주고받을 수 있다.

  - Object, array 보내고 싶으면 따옴표쳐서 문자처럼 만들어야 한다.

  - jQuery 활용

    ```js
    $.get("https://codingapple1.github.io/price.json")
    		// $.get은 JSON => object 자동변환 해준다. 
    	.done(function(data) {
    	console.log(data.price);
    })
    	.fail(function() {
    	console.log("fail");
    })
    ```

  - fetch 활용

    ```js
    fetch("https://codingapple1.github.io/price.json")
    	// 받아온 JSON을 object로 바꿔줘서 뽑기 쉽게
    	.then(res => res.json())
    	.then(data => {
    	console.log(data)
    })
    	.catch(error => {
    	console.log(error);
    })
    ```

    

- filter
  - filter()는 원본을 변형하지 않기 때문에 변수에 저장해서 써야한다. 
- sort
  - sort() 는 원본 변형을 한다. 그래서 따로 저장하지 않아도 된다.



- Document Object Model(DOM)

  - 자바스크립트가 어떻게 HTML을 조작할 수 있나? `<p></p>`  자바스크립트는 이런거 해석 못함

  - 그래서 HTML을 자바스크립트가 해석할 수 있는 문법을 변환해놓으면 된다. 

  - 예를 들어 

    ```html
    <div style="color : red">안녕하세요</div>
    ```

    - 브라우저는 이런 HTML을 발견하면 object 자료로 바꿔서 보관한다. 

    - 구체적으로 아래처럼 만들어 놓는다

      ```js
      var document = {
        div1 : {
          style : {color : 'red'}
          innerHTML : '안녕하세요'
        }
      }
      ```

      - 위 변수를 document object라고 부른다. 거기에 Model이라고  한다. 

  - 요약하면 자바스크립트가 HTML에 대한 정보들 (id, class, name, style, innerHTML 등)을 object 자료로 정리한걸 DOM이라고 부른다.

  - 브라우저는 HTML 문서를 위에서 부터 읽으며 DOM을 생성한다.

    - 그래서 자바스크립트 코드가 HTML 보다 아래에 있다. 

    - 자바스크립트 실행을 나중으로 약간 미루는 방법이 있다.
      - 둘 중에 아무거나 써도 된다. 

    ```js
    $(document).ready(function(){ 실행할 코드 })
    document.addEventListener('DOMContentLoaded', function() { 실행할 코드 }) 
    ```

- load 이벤트 리스너

  - load라는 이벤트리스너를 사용하면 DOM 생성뿐만 아니라 이미지, css, js파일이 로드가 됐는지 체크가능하다.
  - 이미지 같은게 로드되면 load라는 이벤트가 발생한다.

  ```js
  셀렉터로찾은이미지.addEventListener('load', function(){
    //이미지 로드되면 실행할 코드 
  })
  ```

  - document에 포함된 모든것들 찾기

  ```js
  // JQuery 방식
  $(window).on('load', function(){
    //document 안의 이미지, js 파일 포함 전부 로드가 되었을 경우 실행할 코드 
  });
  
  // Javascript 방식
  window.addEventListener('load', function(){
    //document 안의 이미지, js 파일 포함 전부 로드가 되었을 경우 실행할 코드
  })
  ```

  

- localStorage

  - 브라우저 안에 몰래 데이터 저장가능

  - 이름 : 값 형태로 저장가능 (sessionStorage)처럼

  - 5MB 문자/숫자만 저장가능

  - 로컬스토리지 사이트 재접속해도 유지

  - 세션스토리지는 사이트 나가면 자동삭제

  - localStorage.setItem() - 저장하기

  - localStorage.getItem() - 가져오기

  - localStoarge.removeItem() - 삭제하기

  - localStorage에 array,object 저장하려면

    - `JSON.stringify(arr)`

  - localStorage에 array, object 가져올 때는

    - `JSON.parse(arr)`

  - session 스토리지 사용법 똑같음

  - 수정하고 싶으면 

    - 데이터를 꺼내서

      - JSON.parse(배열); 

    - 수정해서 

      - Spread 연산자 활용

        ```js
        let cart = [...cart, name]
        ```

    - 다시 넣음

- IndexDB: 구조화된 대용량데이터 저장시

- Cookies: 보통 로그인정보 저장

- cache Storage: html css js 파일 저장하는 곳



- Position: sticky
  - 조건부로 fixed
  - 부모박스 넘어가면 해제

- clear: both
  - 사진 주위로 글자가 따라 붙지 않게 하기 



- 스크롤 위치에 따라 변하는 애니메이션

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <link rel="stylesheet" href="main.css">
</head>
<body>
  
  	<div class="card-background">
	  <div class="card-box">
		<img src="card1.png">
	  </div>
	  <div class="card-box">
		<img src="card2.png">
	  </div>
	  <div class="card-box">
		<img src="card3.png">
	  </div>
	</div>
	
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js" integrity="sha512-894YE6QWD5I59HgZOGReFYm4dnWc1Qt5NtvYSaNcOP+u1T9qYdvdihz0PPSiiqn/+/3e7Jo4EaG7TubfWGUrMQ==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
	
  <script>
	  //화면이 실행될 때마다 안에 코드를 실행해주세요
    $(window).scroll(function() {
		let 높이 = $(window).scrollTop();
		console.log(높이);
		
		// 1. opacity 조정
		// 700 ~ 1000까지 스크롤바를 내리면,
		// 첫번째 카드의 opacity를 1~0으로 서서히 변경한다.
		// 1차 함수 적용 y = ax + b
		let y1 = (1/-300) * 높이 + (1000/300);
		let y2 = (1/-300) * 높이 + (1950/300);
		
		// 변수가 서서히 변한. 
		$(".card-box").eq(0).css('opacity', y1);
		$(".card-box").eq(1).css('opacity', y2);
		
		// 2.scale 조정
		// 700 ~ 1000 까지 스크롤바를 내리면,
		// 첫번째 카드의 scale를 1 ~ 0.8으로 서서히 변경한다.
		
		let s1 = (-2/3000) * 높이 + (44/30);
		let s2 = (-2/3000) * 높이 + (630/300);
		
		if(높이 >= 700 && 높이 <= 1000) {
			$(".card-box").eq(0).css('transform', `scale(${s1})`);
		} else {
			$(".card-box").eq(0).css('transform', `scale(1)`);
			if (높이 >= 1650 && 높이 <= 1950) {
				$(".card-box").eq(1).css('transform', `scale(${s2})`);
			} else {
				$(".card-box").eq(1).css('transform', `scale(1)`);
			}
		}
		
	});	
  </script>	
</body>
</html>
```







- 캐러셀 스와이퍼 기능

  - Mousedown

    - 마우스를 눌렀을때 발생하는 이벤트
    - 마우스 좌표 구하는 법 `e.clientX`

  - mouseup

    - 마우스를 뗄 때

  - Mousemove

    - 마우스가 움직일 때 

    

- 사진을 drag 못하게 막으려면 
  - `draggable = "false" ` 처리하면 된다. 

- 캐러셀 스와이퍼 기능

```js
  <script>
	  let 시작좌표 = 0;
	  let flag = false;
	  
	  $(".slide-box").eq(0).on("mousedown", function(e) {
		  // 마우스 좌표 나옴
		  시작좌표 = e.clientX;
      // 마우스를 누를때 true로 변환
		  flag = true;
	  
	  })
	  
	  $(".slide-box").eq(0).on("mousemove", function(e) {
      // 마우스를 눌렀을때 좌표 구해서 transform을 이용해서 X만큼 이동
		  if (flag) {
			$(".slide-container").css('transform', `translateX(${e.clientX - 시작좌표}px)`)  
		  }
	  })
	  $(".slide-box").eq(0).on("mouseup", function(e){
      // 마우스를 떼면 false 처리
	     flag = false;
		  
		  if (e.clientX - 시작좌표 < -100) {
			  // 이동한 거리가 -100px이면 transform으로 왼쪽 이동
			  $('.slide-container').css("transition", "all 0.5s").css('transform', 'translateX(-100vw)');
			} else {
				// transition 줘숴 부드럽게 
			  $('.slide-container').css("transition", "all 0.5s").css('transform', 'translateX(0vw)');
			}
		  // 이동후에 transition 5초후에 사라지게 
		    setTimeout(()=> {
				$('.slide-container').css("transition", "none")
			},5000)
	  })
	
 </script>
```

- 모바일에서 터치했을 때 넘어가려면
  - touchstart
    - 그리고 좌표 구할때 `e.clientX()`가 아닌 `e.touches[0].clientX`가 되어야 한다.;
    - 터치시작시 발동
  - touchmove
    - 터지중일시 발동
  - touchend
    - 여기서는 `e.touches[0]`이 아닌 `e.changedTouches[0]`로 해야지 작동한다. 
    - 터치종료시 발동