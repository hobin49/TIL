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

  