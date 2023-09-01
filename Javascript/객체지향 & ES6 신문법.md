### this keyword

- 그냥 쓰거나 일반(전역)함수에서 쓰면 this는 window를 뜻한다. 

  ```js
  // window라는 전역객체가 감싸고 있다. 
  window: {
   	function solution() {
    	console.log(this);
  	} 
  }
  
  // window
  solution()
  ```

  

- Strict mode에서는 일반함수 안에서 this 키워드를 불렀을 때 undefined라는 값으로 지정해준다. 

  ```js
  'use strict';
  
  function solution(){
    // undefined
     console.log(this)
  }
   solution()
  ```

  

- Object 내 함수 안에서 this를 쓰면?

  - 나를 포함한 그 함수를 가지고 있는 오브젝트

  ```js
  let object = {
    data : "Kim",
    함수 : function() {
      console.log(this);
    }
  }
  
  object.함수();
  ```

  

- arrow function에서 this를 쓰면?

  ```js
  let object = {
    data : {
      // 상위 요소에 있는 this를 물려 받아서 쓰겠습니다 뜻
     	 함수 : () => {
      	console.log(this);
    	} 
    }
  }
  
  object.함수();
  ```



- Object 안에 함수 넣을때 신문법

  - 함수 `: function`안 써도 된다. 

  ```js
  let object = {
    함수() {
      console.log(this);
    }
  }
  
  object.함수();
  ```

  

- **함수나 변수를 전역공간에서 만들면 {window}에 보관한다.**





- this의 3번째 뜻 

  - 기계 안에서 쓰면 새로 생성되는 object를 뜻한다.

  ```js
  let 어쩌구 = {}
  
  function 기계() {
    // 새로 생성되는 object === instance
    this.이름 = "kim"
  }
  
  // 기계 {이름: "kim"}
  let object = new 기계();
  ```



- this의 4번째 뜻

  - 이벤트 리스너

  ```js
  <button id="버튼">버튼</button>
  
  
  document.getElementById("버튼").addEventListener("click", 
  function(e) {
    // 여기서 this === e.currentTarget
    console.log(this)
    // 지금 이벤트가 동작하는 곳
    console.log(e.currentTarget);
  })
  ```

  - case1.이벤트 리스너 안에서 콜백함수를 쓴다면 this는?
    - Window

  ```js
  document.getElementById('버튼').addEventListener('click', function(e){
    let 어레이 = [1,2,3];
    어레이.forEach(function(){
      // 이렇게 썡으로 있는 콜백함수는 일반함수랑 똑같아서 window가 출력된다. 
      console.log(this)
    });
  });
  ```

  - **함수가 쓰인 위치에 따라 this 값이 변한다.**

  - case2. 오브젝트 내에서 콜백함수를 쓴다면 this는?
    - Window

  ```js
  var 오브젝트 = {
    이름들 : ['김', '이', '박'];
    함수 : function(){
        // 오브젝트 출력
        console.log(this)
        오브젝트.이름들.forEach(function(){
          // window 근본없는 일반함수라
          console.log(this)
        });
    }
  }
  ```

  - Case3. 오브젝트 내에서 콜백함수를 arrow function으로 쓰면 this는?
    - arrow function은 내부의 this값을 변화시키지 않는다.
    - 위에 있는 외부 this값 그대로 재사용가능

  ```js
  var 오브젝트 = {
    이름들 : ['김', '이', '박'];
    함수 : function(){
        오브젝트.이름들.forEach(() => {
          console.log(this)
        });
    }
  }
  ```

  



### Arrow Function 

- ES6부터 등장한 문법
  - function 키워드 대신 사용

```js
let 함수 = (a) => {
  return a + 10
}

함수(5)
```

- 함수는 코드들을 기능을 묶고 싶을 때, 입출력 기계를 만들고 싶을 때 사용

- 장점

  - 입출력 기계 만들 때 보기 쉽다

  - 파라미터 1개면 소괄호 생략 가능

    ```js
    let 함수 = a => {return a + 10}
    ```

  - 코드가 한줄이면 중괄호도 생략 가능

    ```js
    let 함수 = a => return a + 10
    ```

    

- 사용예시

  - 1.forEach 콜백함수

  ```js
  // 원래 코드
  [1,2,3,4].forEach(function(a) => {
    console.log(a)
  })
  
  // 변경 코드
  [1,2,3,4].forEach(a => console.log(a))
  ```

  - 2.eventListener

  ```js
  document.getElementById('버튼').addEventListener('click', (e) => {
  	// 함수 내에 this값을 변경하지 않아서 e.currentTarget이 나오지 않고 window 나옴
    // 그래서 this 쓰고 싶으면 arrow function 쓰면 안 돼 
    // 아니면 e.currentTarget을 쓰자
    e.currentTarget
  });
  ```

  - 3.Object안의 함수

  ```js
  var 오브젝트 = {
    함수 : () => {
      // window
      return this
    }
  }
  
  오브젝트.함수()
  ```






### var, let, const 선언, 할당, 범위

- 변수이름 = 저장할값

- var

  - 재선언 가능
  - 재할당 가능
  - 범위는 function

  ```js
  var 이름 = "kim"
  var 이름 = "Park"
  
  // function 안에서만 효과 발동
  function 함수() {
    var 이름 = "kim";
  }
  
  
  // not defined
  console.log(이름)
  ```

  

- let

  - 재선언 불가능
  - 재할당 가능
  - 범위는 블록

  ```js
  let 나이 = 20;
  let 나이 = 30; (x)
  // 재할당 가능
  나이 = 30; (o)
  
  // 블록레벨 스코프
  if (true) {
    let 이름 = "Park"
  }
  
  ```

  

- const

  - 재선언 불가능
  - 재할당 불가능
  - 범위 블록

  ```js
  const 나이 = 20;
  const 나이 = 30(x)
  // 재할당 불가능
  나이 = 30(x)
  
  // 블록레벨
  if (true) {
    const 이름 = "Park"
  }
  ```

  

- 재할당 불가능한 불변의 Object 만드려면

  - 객체 내부 값 변경해도 에러 안 난다.

  ```js
  const 사람 = { 이름 : 'Kim' }
  
  // const 변수 자체를 재할당한게 아니다. 
  사람.이름 = "Park"
  ```

  - 그럼 어떻게 만드나?
    - `Object.freeze()`사용

  ```js
  const 사람 = { 이름 : 'Kim' }
  
  Object.freeze(사람);
  
  사람.이름 = "park";
  ```





### Hoisting, 전역변수, 참조

- Hoisting

  - 변수의 선언을 변수 범위 맨 위로 끌고 오는 현상
  - 변수를 만나면 선언부분을 강제로 맨 위로 끌어올린다. 
  - 함수선언도 Hoisting 일어난다. 

  ```js
  // undefined(아직 할당이 되지 않은 변수에 들어감)
  console.log(이름);
  var 이름 = 'Kim';
  // 30
  console.log(이름);
  ```

- 변수 여러개 만들기

  ```js
  let 나이 = 20, 이름 = "hobin", 성별 = "man"
  ```

  



- 전역변수와 변수의 참조

  - 전역변수

    - 모든 곳에서 쓸 수있는 변수

    ```js
    // 전역변수
    let 나이 = 20;
    
    function 함수() {
      // 20
      console.log(나이);
      // 지역변수
      let 이름 = "Hobin";
    }
    ```

  - window로 전역변수 만들기

    ```js
    window.이름 = "kim";
    // 함수도 가능
    window.나이 = function(){};
    // 김 
    console.log(window.이름);
    ```

    

- 문제 1

  ```js
  // 왜 동작하지 않고 i는 5만 찍히나?
  // 그리고 var = 5 게 전역변수처럼 나와있다. 
  for (var i = 1; i < 6; i++) { 
    // 반복문과 동시에 실행되지 않고 나중에 실행된다. 
    setTimeout(function() { console.log(i); }, i*1000 ); 
  }
  
  // 해결책 : var => let으로 변경
  for (let i = 1; i < 6; i++) { 
    // 반복문과 동시에 실행되지 않고 나중에 실행된다. 
    setTimeout(function() { console.log(i); }, i*1000 ); 
  }
  ```

- 문제 2

  ```js
  var 버튼들 = document.querySelectorAll('button');
  var 모달창들 = document.querySelectorAll('div');
  
  for (var i = 0; i < 3; i++){
    
    // 이벤트리스너 내부 코드는 나중에 실행한다. 
    버튼들[i].addEventListener('click', function(){
      // 좀 있다가 버튼을 클릭하면 내부 코드 실행한다. 
      모달창들[i].style.display = 'block';
    });
  
  }
  
  // 해결책
  for (let i = 0; i < 3; i++){
    
    // 이벤트리스너 내부 코드는 나중에 실행한다. 
    버튼들[i].addEventListener('click', function(){
      // 좀 있다가 버튼을 클릭하면 내부 코드 실행한다. 
      모달창들[i].style.display = 'block';
    });
  
  }
  ```

  