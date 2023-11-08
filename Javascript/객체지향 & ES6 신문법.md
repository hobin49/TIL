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

  



#### 자바스크립트가 문자 다루는 신기한 방법(Template literals)

- 자바스크립트에서 문자를 다룰 때 어려웠던 점을 해결하기 위해 나온 문법이다.
- 따옴표 대신 backquote, backtick 이라는 "요런" 기호를 사용해서 문자를 만들 수 있다.
- 장점
  1. 문자 중간 엔터키 입력이 가능하다.
     - 문자열은 문자 중간에 엔터키 치면 안 된다. 
     - 하지만 백틱으로 문자를 만들면 엔터키가 자유롭게 가능하다
  2. 중간중간 변수넣기 쉬움
     - 특히 HTML 작성시 유용

```js
let 이름 = '손흥민';
let 문자 = `안녕하세요 ${이름} 입니다`;
let 템플릿 = `<div>${변수}</div>`
```

​	

- tagged literal

  - **ES6에서는 함수로 문자 해체분석기능을 만들어줄 수도 있다.**
    - 단어 순서를 변경하거나
    - 단어를 제거하거나
    - ${변수} 위치를 옮기거나(쉽게 가능)
    - `${}` 양옆 문자들을 Array화 해준다. 
  - 함수를 실행시킬 때 소괄호가 아니라 문자를 이용해서 함수를 실행시킬 수 있다.
  - 실행할 함수이름 쓰시고 **소괄호 대신 `백틱` 문자를 붙여주면 된다**.

  ```js
  let 변수 = '손흥민';
  
  // 분석용 함수를 만든 뒤에 파라미터 두개 넣기
  // 파라미터 1. 문자들을 Array화 해준다.
  // 파라미터 2. ${변수}를 뜻함
  function 해체분석기(문자들, 변수들){
    // ["안녕하세요", "입니다"]
    console.log(문자들);
    // 손흥민
    console.log(변수들);
  }
  
  해체분석기`안녕하세요 ${변수} 입니다`
  ```

  - 사용 예시 글자의 순서를 변경하고 싶을 때

  ```js
  let 변수 = '손흥민';
  
  function 해체분석기(문자들, 변수들){
    console.log(문자들[1] + 변수들 +문자들[0]);
  }
  
  해체분석기`안녕하세요 ${변수} 입니다`;
  ```

  

  

​      



#### Spread Operator

- 마침표를 연달아서 3개 찍으면 그게 Spread Operator문법이다.
- 괄호제거 해주는 연산자다.
- 뭔가 내용물을 빼고 싶을 때 쓰면 된다. 

```js
let 어레이 = ['hello', 'world'];
// hello world
console.log(어레이);

let 문자 = "hello";
// h e l l o
console.log(...문자);
```

- 어디에 쓰나?

  - **Array 합칠 때 자주 쓴다.**

  ```js
  let a = [1,2,3];
  let b = [4,5];
  
  // c = [1, 2, 3, 4, 5]
  let c = [...a, ...b];
  ```

  - 배열에 깊은 복사할 때 자주 사용한다.
    - 아래처럼 하면 a에만 값을 추가했는데 b에도 값이 추가된다. 
    - 이유는 등호로 복사하면 값을 공유하기 때문이다. 
      - reference data type(Array, Object)의 경우 해당 primitive data type과는 다르다.

  ```js
  let a = [1, 2, 3];
  // 잘못된 예시
  let b = a 
  // 옳은 예시
  let b = [...a]
  
  a[3] = 4
  
  // [1, 2, 3, 4]
  console.log(a);
  // [1, 2, 3]
  console.log(b);
  ```

  

  - 객체에 깊은 복사할 때 자주 사용한다.
    - 대괄호, 중괄호 다 벗겨준다.
    - 만약 값 중복이 일어나면?
      - 가장 뒤에 있는걸 적용한다. 순서가 중요

  ```js
  let o1 = { a : 1, b : 2 };
  let o2 = { ...o1, c : 3};
  
  // 	o1을 o2에 deep copy하려면
  let o2 = { ...o1 }
  
  // 값 중복 발생시
  let o2 = { a: 2, ...o1}
  // {a : 1, b: 2}
  console.log(o2)
  
  // { a : 1, b : 2, c: 3}
  console.log(o2)
  ```

  - 쓸곳3. 함수 파라미터 넣을 때 

    ```js
    function 더하기(a, b, c) {
      console.log(a + b + c)
    }
    
    let 어레이 = [10, 20, 30];
    // 1. 일일히 넣는다. 근데 이 방식 넘 귀찮다(주먹구구식)
    더하기(어레이[0], 어레이[1], 어레이[2])
    
    // 2.apply 메서드 활용(옛날방식), undefined(아무 뜻 없음)
    더하기.apply(undefined, 어레이);
    
    // 3.spread operator(요즘방식)
    더하기(...어레이)
    ```

  - apply, call 함수 개념 설명

    - apply는 함수를 옮겨와서 실행해주세요라는 뜻이다.
      - 함수 인자를 배열 형태로 넣을 수 있음
    - call은 함수 인자를 하나 하나씩 넣는다. 

    ```js
    let person = {
      인사 : function() {
        console.log(this.name + '안녕')
      }
    }
    
    person.인사();
    
    let person2 = {
      name: "손흥민"
    }
    
    // undefined안녕
    person.인사()
    
    // person2에도 인사 함수를 사용하고 싶다.
    // 1. apply(함수 인자를 array형태로 넣을 수 있다.)
    // 손흥민 안녕
    person.인사.apply(person2, [1, 2, 3])
    // 2. call(함수 인자를 하나씩 넣어야 한다.)
    person.인사.call(person2, 1)
    ```

    

    

#### 자바스크립트 함수 업그레이드하기 (default parameter/arguments)

- default parameter
  - 함수 파라미터에 2개가 필요한데 1개만 넣어도 에러가 뜨지 않음
  - 파라미터에 값을 미리 지정할 수 있어서 아무것도 안 넣을 경우 해당 값을 넣어주세요라고 처리 가능
  - 함수 넣거나 연산도 가능 (b = 2 * a)

```js
function 임시함수() {
  return 10
}

// 파라미터 한 개 깜빡하고 안 넣을경우 임시함수 발동
function 더하기(a, b = 임시함수()) {
  console.log(a + b)
}

// 1
더하기(1);
```



- 함수의 arguments(옛날 문법임)
  - 모든 파라미터를 배열 안에 넣은 변수

```js
function 함수(a, b, c) {
  console.log(arguments[0]);
  console.log(arguments[1]);
  console.log(arguments[2]);
}
// array[1, 2, 3] 
함수(1, 2, 3);
```

- 입력한 파라미터를 전부 콘솔창에 출력해주는 함수

  ```js
  function 함수(a, b, c) {
    for (let i = 0; i < arguments.length; i++) {
      console.log(arguments[i]);
    }
  }
  ```

  



#### Rest 파라미터

- Rest 파라미터를 쓰면 모든 파라미터를 배열 안에 보관해준다. 
  - 기존의 arguments랑 다른 것은 **특정 자리에 오는 파라미터를 배열에 담아준다.**

```js
// 3번째부터 배열로 들어감
function 함수2(a, b, ...파라미터들){
  console.log(파라미터들)
}

// 함수안에 들어온 파라미터를 전부 담은 array 출력
함수2(1,2,3,4,5,6,7);
```

- Rest vs Spread
  - 함수 파라미터 자리에 붙으면 rest
  - 나머지는 spread다.
- Q.모든 파라미터들을 하나씩 콘솔창에 출력해주는 함수는?

```js
function 함수2(...rest){
  for (let i = 0; i < rest.length; i++) {
    console.log(rest[i]);
  }
}

함수2(1,2,3,4);
```



- **주의사항**

  - 1.가장 뒤에 써야함
    - 아래처럼 중간에 쓰면 안 돼 오류 남

  ```js
  function 함수2(a, ...파라미터들, b){
    console.log(파라미터들)
  }
  ```

  - 2.2개 이상 사용할 수 없다.

  ```js
  function 함수2(a, ...파라미터들, ...파라미터들2){
    console.log(파라미터들)
  }
  ```

  





#### Reference data type

- 그냥 문자와 숫자는 Primitive data type
  - **변수에 값이 그대로 저장됨**
- 반면에 Array, Object는 변수에 값이 저장이 안 된다. 
  - 변수에 reference가 저장된다. 

```js
// { name: "Kim"}이 저쪽에 있습니다~라는 화살표가 들어있다.
let obj = { name : "Kim"};
```

- Primitive data type 다루기: 복사

```js
var 이름1 = "김";
var 이름2 = 이름1;
// 이름 1 = 박
이름1 = "박"
```

- Reference data type 다루기 : 복사
  - 데이터가 저기있어요라는 화살표가 저장된다. 
  - 새로운 중괄호를 할당할 대마다 새로운 화살표

```js
var 이름1 = { name : '김' };
var 이름2 = 이름1;
이름1.name = '박';
// { name : "박"}
// 이름2 안 바꿨는데 바뀜
console.log(이름2)
```



- 다루기 예시 2

```js
var 이름1 = { name : '김' };
var 이름2 = { name : '김' };

// false(object가 저장되지 않고 어디에 저장되어 있는지를 가리킨다.)
console.log(이름1 == 이름2)
```



- 다루기 예시 3
  - 파라미터는 변수생성 & 할당과 똑같다.
    -  변경(var obj = 이름1) 이거랑 똑같다. 
    - 새로운 object를 생성하면 새로운 화살표가 생기기 때문에 다른 메모리에 저장됨 
      - 따라서 파라미터 변수에 = {} 해봤자 원래 이름에는 변화가 없다.

```js
let 이름1 = { name : "김"};

function 변경(obj) {
  // object 재할당 (실패 안바뀜....)
  obj = { name : "park"}
  obj.name = "park"
}

변경(이름1);
```





#### Constructor

- object를 마구 복사하고 싶을 때 사용한다.

  - 비슷한 object 여러개 만들때

  ```js
  var 학생1 = { name : 'Kim', age : 15 };
  
  // 일반 함수랑 달라서 대문자로 적는다
  function 기계(이름) {
    // this가 필요해 새로생성되는 Object를 뜻함
    this.name = 이름;
    this.age = 15;
    // 함수도 넣을 수 있다. 
    this.sayHi = function(){
      console.log("안녕하세요" + this.name + "입니다")
    }
  }
  
  
  var 학생1 = new 기계("kim");
  var 학생1 = new 기계("park");
  ```

  - this : 기계에서 새로 생성되는 object(instance)
  - 기계: object생성기계(contructor, 생성자)
  - 학생1, 학생2가 부모한테서 상속 받았다고 표현한다. 





#### prototype

- 상속을 구현할 수 있는 또하나의 문법 자바스크립트만 있어

- prototype은 유전자
- constructor를 만들면 prototype이라는 공간이 자동으로 생긴다. 
- prototype에 값을 추가하면 모든 자식들이 물려받기 가능

```js
function 기계(이름) {
  // this가 필요해 새로생성되는 Object를 뜻함
  this.name = 이름;
  this.age = 15;
  // 함수도 넣을 수 있다. 
  this.sayHi = function(){
    console.log("안녕하세요" + this.name + "입니다")
  }
}

기계.prototype.gender = "남";

var 학생1 = new 기계("kim");
var 학생1 = new 기계("park");

//남
학생1.gender
```

- Prototype의 동작원리

  - 학생1.gender를 출력을 하려고 하면 

    - 일단 먼저 constructor를 검사한다. 
    - 그 다음을 검사한다. 학생1의 부모 유전자가 gender를 가지고 있는지 체크한다. 

  - 학생1.toString(); 

    - 객체를 문자열로 변환 

  - 자바스크립트 내장함수를 어떻게 사용할 수 있는가??

    - Prototype 동작원리를 생각하자. 

    ```js
    let arr = [1, 2, 3];
    // 실제 array가 만들어지는 방식(array 만드는 기계로부터 하나 뽑는다)
    let arr = new Array(1, 2, 3)
    
    arr.sort()
    ```

    - arr에 sort()가 있나?
    - 그럼 arr 부모의 유전자(prototype)에 sort()가 있나?





#### prototype의 특징 몇가지

- prototype은 contructor 함수에만 생긴다.
- 내 부모 유전자(부모의 prototype)를 검사하고 싶다면 `__proto__`

- `__proto__`를 이용해 부모님 강제 등록하기

```js
var 부모 = { name : "Kim"};
var 자식 = {};

// 부모님 강제 등록하기
자식.__proto__ = 부모;
```

- 콘솔창에서 알려주는 prototype chain 
  - 학생1에 부모 유전자를 담고있는 것
  - array, object, function 다 new 키워드로 생성된다. 

- 배열에서 3을 제거하는 함수 만들기

```js
function Student(이름, 나이){
  this.name = 이름;
  this.age = 나이;
}

Student.prototype.sayHi() {
	console.log('안녕 나는 ' + this.name + '이야');
}

var 학생1 = new Student('Kim', 20);
console.log(학생1.sayHi());
```







#### ES5 방식으로 쉽게 구현하는 상속기능

- Object.create()

```javascript
var 부모 = { name : 'Kim', age : 50 };
var 자식 = Object.create(부모);

// 빈 객체 출력
console.log(자식)
// 50(prototype 때문이다.)
console.log(자식.age);
// 자식 = { age: 20}
자식.age = 20;

var 손자 = Object.create(자식);
// Kim
console.log(손자.name);
```





#### ES6방식으로 안쉽게 구현하는 상속기능 (Class)

```js
class 부모 {
  constructor(파라미터) {
    this.name = 파라미터;
    // constructor에 함수 넣어도 되고(1.자식이 직접 함수를 갖고 싶은 경우)
    this.sayHi = function() {console.log("Hello")}
  }
  // 아니면 여기에 함수를 넣어도 된다.
  // 여기에 추가되는 함수는 
  // 2.부모.prototype에 추가된다.  
  sayYes() {
    console.log("nice")
  }
}

var 자식 = new 부모("파라미터");
// 얘의 부모 prototype(부모유전자)가 출력된다.
자식.__proto__

// class 안에 함수 추가
부모.prototype.sayHello = function(){}

```

- Object.getPrototypeOf(자식)
  - 부모님 prototype을 출력해주세요!
  - `자식.__proto__` 이거랑 같음

- 객체지향 문법은 왜 쓰나?
  - Object 여러개 만들어 쓰려고 하는 것이다. 





#### 객체지향5. class를 복사하는 extends / super

- extends
  - 유사한 class를 하나 더 만들고 싶으면?
  - 정확히 말하면 class를 상속한다. 
  - class 안에 복사/상속할 값이 많으면 힘들기 때문에 사용한다. 

```js
class 할아버지 {
  constructor(name) {
    this.성 = "Kim";
    this.이름 = name;
  }
}

var 할아버지1 = new 할아버지("만덕");


//extends해서 만든 class는 this 그냥 못 쓴다. 
class 아버지 extends 할아버지 {
  constructor(name) {
    super(name);
    this.나이 = 50;
  }
}


var 아버지1 = new 아버지('만수');
```

- extends해서 만든 class는 this 그냥 못 쓴다. 
- 그래서 대안이 super() 다음에 사용하면 사용 가능하다.
- **super()는 물려받는 class의 constructor라는 뜻이다.**
  - **물려받는 class에 파라미터로 값을 받는 게 있다면 똑같이 물려받을 class의 constructor와 super 파라미터에 전달해준다. **
  - 까먹고 파라미터 안 넣으면 undefined가 나온다. 
  - 파라미터 2개 이상이어도 잘 맞춰서 넣어주면 된다. 
- super()의 다른 용도

```js
class 할아버지 {
  constructor(name) {
    this.성 = "Kim";
    this.이름 = name;
  }
  sayHi() {
    console.log("안녕 저는 할아버지에요");
  }
}

class 아버지 extends 할아버지 {
  constructor(name) {
    super(name);
    this.나이 = 50;
  }
  
  sayHi() {
   console.log("안녕 저는 아버지에요");
   // 부모 prototype을 상속해주세요
   super.sayHi();
  }
}

var 아버지1 = new 아버지("만수");
아버지1.sayHi();
```

- 똑같은 함수가 부모랑 나한테 있다면 가장 가까운 프로토타입에 있는 함수를 출력한다. 
- super
  - 부모 class의 constructor를 의미
  - 부모 class의 prototype을 의미 === `__proto__`
  - 부모가 가진 함수들을 자유롭게 사용 가능





### getter, setter 왜 쓰나?

- 함수를 만들어  object 데이터를 다루는 이유

  - object 자료가 복잡할 때 이득이다
    - 코드가 복잡하지 않게 하기 위해
    - 데이터를 업데이트 수정
  - object 자료 수정시 편리
    - 안전장치 기능개발 가능 (잘못 입력해도)
    - 데이터를 꺼내거나 /수정하거나 그럴 때 편리 실수방지 & 관리가능

  ```js
  var 사람 = {
  	 name : "Park",
  	 age : 30
  	 nextAge() {
  	  return this.age + 1 
    	 }
       setAge(나이) {
  		this.age = parsInt(나이);
  	 }
    }	
  	
  사람.nextAge();
  사람.setAge(20);
  ```

  

- 복잡한 소괄호 꼴보기 싫다면 set/get

  - ES5 등장
  - 예시

  ```react
  var 사람 = {
  	 name : "Park",
  	 age : 30
  	 get nextAge() {
  	  return this.age + 1 
    	 }
       set setAge(나이) {
  		this.age = parsInt(나이);
  	 }
    }	
  	
  // set쓰면 괄호 안 쓰고 더 직관적으로 사용 가능
  사람.setAge = 20;
  사람.nextAge
  ```

  - 데이터 변경은 set, get은 데이터 꺼내쓰는 함수에 
    - property화 시켜서 소괄호 떼도 된다.
  - getter/setter은 문법을 좀 더 쉽게 다룬다. 
    - **get 함수들은 return이 있어야 한다.**
      - +파라미터도 없어야 한다.
    - set 함수들은 파라미터가 딱 1개 있어야 한다. 

- class에서 사용하는 get/set

  ```js
  class 사람 {
  	constructor() {
  		 this.name = "Park";
  		 this.age = 20;
  	}
  	get nextAge() {
  		return this.age + 1
  	}
  	set setAge(나이) {
  		this.age = 나이;
  	}
  }
  	
  var 사람1 = new 사람();	
  사람1.setAge = 200
  사람1.nextAge
  ```

  

- 데이터 출력/수정 함수를 만들어 쓰는 이유는 **데이터의 무결성** 때문이다. 

- 연습문제

```js
class 강아지 {
	 constructor(type, color) {
		 this.type = type;
		 this.color = color;
	 }
	 한살먹기() {
		 if (this instanceof Cat) {
		 this.age ++
	 }
	}
}
	
var 강아지1 = new 강아지("말티즈", "white");
var 강아지2 = new 강아지("진돗개", "brown");
	
console.log(강아지1, 강아지2)
	
class 고양이 extends 강아지 {
	 constructor(type, color, age) {
		super(type, color);
		this.age = age;
	}
}
  	
var 고양이1 = new 고양이("코숏", "white", 5);
var 고양이2 = new 고양이("러시안블루", "brown", 2);
console.log(고양이1, 고양이2)
	 
	
class Unit {
	 constructor() {
		this.공격력 = 5
		this.체력 = 10
	}
	get battlePoint() {
		 return this.공격력 + this.체력
	}
	set heal(stamina) {
		this.체력 += stamina
	}
}
  	
var 인스턴스 = new Unit();
console.log(인스턴스.battlePoint)
인스턴스.heal = 50;
  
  
var data = {
	odd: [],
	even: []
  // 들어오는 숫자가 많아서 spread operator 쓰면 배열로 묶어준다. 
	setter함수: function(...숫자들) {
	if (number % 2 === 0) {
	  this.even.push(number)
  } else {
		this.odd.push(number)
	}
	get getNumber() {
		return [...this.odd, ...this.even].sort((a, b) => a - b)
	 }
  }
}
```





### Destructuring 문법

```js
// 직관적으로 변수 만들 수 있다.
var [a, b, c] = [2, 3, 4]

// default 값 지정 가능
var [a, b, c = 10] = [2, 3]

var { name, age } = { name : "Kim", age: 30};

// 기본값 지정 가능
var { name, age = 10 } = { name : "Kim", age: 30};

// 이름도 바꿀 수 있다. (default 값도 가능)
var { name : 나이 } = { name : "Kim"}

// default 값도 넣을 수 있다.
var { name : 나이  = "Kim"} = {}
```

- **object는 순서를 보장하지 않기 때문에 반드시 key명과 똑같이 써야한다. **

- 많은 변수를 object에 집어넣고 싶은 경우

```js
var name = 'Kim';
var age = 30;

// key와 value가 똑같은 경우
var obj = { name : name, age : age }

// 이렇게 단순하게 바꿀 수 있음
var obj = { name, age }
```

- 함수 파라미터 만들 때 destucturing 문법 사용가능

```js
function 함수({name, age}) {
  console.log(name);
  console.log(age);
}

함수({ name : "Kim", age : 30 })

// array인 경우
function 함수([name, age]) {
  console.log(name);
  console.log(age);
}

함수([1, 2])
```



- 예제 문제

  - 다음과 같은 Object에서 데이터를 뽑아서 변수를 만들고 싶다

  ```js
  let 신체정보 = {
    body: {
      height: 190,
      weight: 70
    },
    size: ["상의 Large", "바지 30인치"],
  };
  
  let {
    body: {
      height,
      weight,
    },
    size: [상의, 하의]
  } = 신체정보;
  ```

  

### import/export를 이용한 파일간 모듈식 개발

- 기본적으로 import할 때 다 가져오지 않는다. 

```html
<script type= "module">
  // 가져올거 부분은 맘대로 작명 가능
  import 가져올거 from 경로 
</script>
```

- 내가 자바스크립트에서 작성한 코드는 `export default`라는 keyword를 통해서 내보낼 수 있다.
  - 참고로 `export default`는 파일당 1회 사용 가능하다. 

```js
var a = 10;
// export default 내보낼 거
export default a;
```

- 여러개를 export 할 수 있는 방법
  - 1.`export{내보낼것들}` 해야 한다. 
    - 그리고 import  할때도 `import{가져올 것들} from "경로"` 중괄호 필요하다.
  - 2.변수 앞에  export를 붙인다. 

```js
var a = 10;
var b = 20;
export c = 30;

export { a, b };
```

```html
<script type= "module">
	import {b} from 경로
</script>
```

- export와 export default는 동시 사용 가능하다.
  - Import 할 때 순서가  1.export default, 2. export이다.

```js
var a = 10;
var b = 20;
var c = 30;
export {a, b};
export default c;
```

```html
<script type= "module">
	import c, {a, b} from 경로
</script>
```

- 변수명이 마음에 안들면 새로 짓자
  - `import {변수 as 새변수명} from '경로'`

```html
<script type="module">
  import c, {a as 폭발} from 경로
</script>
```

- 모든걸 다 import 해오는 `*`  기호
  - `import * as 변수명들 from "경로"`

```html
<script type="module">
  import * as 변수모음 from 'library.js';
  console.log(변수모음.a);
</script>
```

- 프론트엔드 개발에선 호환성 떄문에`<script src="">`을 사용하자
- 반면에 React, Angular 쓰거나 또는  JS 파일 나눌 때 import/export 사용



### Stack, Queue를 이용한 웹브라우저 동작원리

```js
console.log(1+1)
setTimeout(function(){ console.log(2+2)}, 1000)
console.log(3+3)

// 출력 순서 2 => 6  => 4
```

- 웹 브라우저는 자바스크립트 실행해주는 애들이다. 
- 앱브라우저 내부 
  - 스택이라는 공간이 존재 
    - 나의 코드를 한 줄 한 줄 담는다. 
    - 그러다 변수를 만나면
      - 힙이라는 공간에 변수가 저장된다. 
    - 우리 코드 실행해주는 곳이다. (특징 하나밖에 없다. )
      - 그래서 자바스크립트는  single threaded 언어라고 한다. 
    - setTimeout 같은 코드는 바로 실행이 불가능하니 대기실로 잠시 이동
      - 대기실 보내는 코드들(기다림이 필요한 코드)
        - Ajax 요청 코드들, 이벤트 리스너, SetTimeout 등
      - 대기실로 보내진 코드들은 이벤트 큐라고 불리우는 곳으로 이동한다. 처리가 완료된 코드들을 줄을 세운다. 
        - 그리고 stack으로 하나씩 올려보낸다. 
        - 스택이 바쁘니까 큐 거쳐서 오는데 조건이 Stack이 비어있을 때만 올려보낸다. 
    - setTimeout은 0초 걸려도 무조건 대기실로 이동한다. 
- 반복문 안에서 너무 어려운 작업은 자바스크립트로 시키면 큰일난다.
  - 스택에서 오랫동안 머물면 queue에 있는 요청들이 스택이 비어있지 않아서 실행이 되지 않는다. 
  - 10초 걸리는 연산이 있을 때 버튼클릭, ajax요청 등 작동이 안 된다. 

- 절대 stack을 바쁘게 만들지말자. (응답 대기 뜸)
- 큐를 바쁘게 하면 사이트 안 좋음.(이벤트 리스너 많이 부착하지 말자) 

- 자바스크립트는 원래 동기적으로 처리된다. 
  - 한번에 한줄 순서대로 간다. 
  - 비동기적으로 처리도 가능
    - setTimeout, 이벤트리스너, ajax 함수 쓰면된다. 





### 동기/비동기처리와 콜백함수라는 용어 깔끔하게 정리

- 자바스크립트는 동기식 처리

  - 한번에 코드 한줄씩 차례로 실행

  ```javascript
  <script>
    console.log(1); 
    console.log(2); 
    console.log(3);
  </script>
  ```

  

- 비동기식 처리

  ```js
  <script>
    console.log(1);
    setTimeout(() => { console.log(2)}, 1000);
  	console.log(3);
  </script>
  ```

  - 오래걸리는 작업이 있으면 제껴두고 다른거부터 처리하는 방식
  - 자바스크립트가 아니라 자바스크립트 실행하는 브라우저 덕분에 가능 

- Web API

  - setTimeout 코드들, eventListener 코드, $.ajax()들은 실행 대기실에 있다. 
    - 이 문법들을 써야 비동기처리 가능하다. 
  - web API 덕분에 오래걸리는 작업이 있으면 제껴두고 다른거부터 처리하는 비동기식 처리가능
  - 그냥 자바스크립트는 오래걸리는 연산 만나면 멈추는데 Web API와 연관된 특수한 함수들을 쓰면 작업이 오래걸릴 때 다른거 부터 실행 가능하다.

- 콜백함수

  - 자바스크립트를 순차적으로 실행하려면 콜백함수를 사용한다. 
    - 함수 안에 함수가 들어가는게 콜백함수

  ```js
  // function을 쓰면 콜백함수
  setTimeout(function(){}, 1000);
  
  // 클릭하면 함수 발동
  addEventListener("click", function() {})
  ```

  

- 콜백함수를 이용한 함수 디자인

```js
function 첫째함수(구멍) {
  console.log(1);
 	구멍();
}

function 둘째함수() {
  console.log(2)
}

// 첫째함수() 다음에 둘째함수()를 실행하고 싶다. 
첫째함수(둘째함수);
```

- 콜백함수는 함수 디자인 패턴일 뿐이다.

- 콜백함수의 문제점

```js
첫째함수(function() {
  둘째함수(function() {
    셋째함수(function() {
      
    })
  })
})
```

- 콜백 지옥에 빠짐.. 그니까  Promise 패턴을 





### ES6 Promise

- 성공/실패 판정 기계

- then 사용법

```js
<script>
var 프로미스 = new Promise();


프로미스.then(function() {
  //프로미스가 성공일 경우 실행할 코드
}).then(function() {
  
})
</script>
```

- 콜백함수 만드는 거랑 비슷한데 콜백함수보다는 약간 기능이 많다. 

  

- catch 사용법
  - 실패할 경우 코드실행

```js
<script>
var 프로미스 = new Promise();

프로미스.catch(function() {
  //프로미스가 실패일 경우 실행할 코드
})
</script>
```



- 성공/실패 판정 기계 Promise 디자인

```js
var 프로미스 = new Promise(function(성공, 실패) {
  성공();
  실패();
})

프로미스.then(function() {
  //프로미스가 성공일 경우 실행할 코드
}).catch(function() {
  //프로미스가 실패일 경우
})
```



- Promise 예시 1

```js
var 프로미스 = new Promise(function(){
 	var 어려운 연산 = 1 + 1;
  성공(어려운연산);
});

프로미스.then(function(결과) {
  //프로미스가 성공일 경우 실행할 코드
  console.log(결과)
}).catch(function() {
  //프로미스가 실패일 경우
 console.log("실패했어요")
})
```

- promise의 장점
  - 콜백 대신 예쁜 코드 
  - 성공/실패의 경우 맞춰 각각 다른 코드 실행 가능 



- Promise 예시 2

```js
var 프로미스 = new Promise(function(){
 	// 1초 후에 성공하는 Promise
  setTimeout(function(){
    성공();
  }, 1000);
});

프로미스.then(function() {
  //프로미스가 성공일 경우 실행할 코드
  console.log("성공했어요")
}).catch(function() {
  //프로미스가 실패일 경우
 console.log("실패했어요")
})
```



- Promise의 3가지 상태
  - 성공하면 `<resolved>`
  - 판정 대기중이면 `<pending>`
  - 실패하면 `<rejected>`



- Promise에 대한 오해 
  - 동기를 비동기적으로 바꿔주는게 아니다. 
  - 그냥 콜백함수 디자인의 대체품일 뿐
- Promise가 적용된 곳들 
  - JQuery.ajax()
    - `$.ajax().done(function() {}).fail()`
  - fetch()
    -  `fetch().then().catch( )`





### async/await

- ES8문법
  - async가 promise의 역할을 대신한다. 함수 실행 후에 Promise 오브젝트가 남는다. 

```js
async function 더하기() {
  return 1 + 1;
}

더하기().then(function(결과) {
  console.log(결과);
});
```

- async는 성공만 가능
- 강제로 실패는 가능

```js
async function 더하기() {
  return Promise.reject("실패임")
}

더하기().then(function(결과) {
  console.log(결과)
})
```

- 함수 안에서 Promise 쓰기

```js
async function 더하기() {
  var 프로미스 = new Promise(function(성공, 실패) {
    var 힘든연산  = 1 + 1;
    성공();
  });
 	
  // 프로미스 해결까지 기다린다. 
  var 결과 = await 프로미스;
  console.log(결과);
}
더하기();
```

-   **await은 기다려라는 뜻** === then()과 똑같다.
  - 프로미스 실패시 에러나고 멈춘다. 
- try {이걸해보고에러나면} catch { 이걸 실행해주세요 }

```js
async function 더하기() {
  var 프로미스 = new Promise(function(성공, 실패) {
    var 힘든연산  = 1 + 1;
    성공(힘든연산);
  });
  
  try {
    var 결과 = await 프로미스
    // 2가 출력
    console.log(결과);
  } catch {
    console.log("프로미스 연산이 잘 안됩니다.")
  }
}
```

- 프로미스 연산결과는 변수에 저장 가능



- Q.button을 누르면 성공 판정하는 Promise & 성공시 "성공했어요를" 출력하려면?

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
  <button id="button">버튼</button>
</body>	
<script>
   async function 더하기() {
	 	var 프로미스 = new Promise(function(성공, 실패) {
		document.getElementById("button").addEventListener("click", function() {
		  성공("성공했어요");
	  })
	});
	
	try {
	  var 결과 = await 프로미스
	  console.log("성공했어요")
	} catch {
		console.log("실패했어요")
	}
}
 
  </script>  
</html>
```





### for in / for of 반복문

- forEach는 Array(전용)

  - 각 배열 요소에 대해 제공된 함수를 한 번씩 실행한다.

  ```js
  array1.forEach((el) => element * 2)
  ```

- for in 반복문 (Object 전용)

  - Object에 있던 값을 전부 하나식 꺼내서 사용할 때
  - enumerable(셀 수 있는)한 것만 반복해준다.
    - 일반 자료들은 항상 enumerable이 true가 기본값 

  ```js
  var 오브젝트 = { name: "Kim", age : 30};
  // 오브젝트.name의 숨겨진 정보 출력
  // {value: "Kim", writable: true, enumerable: true}
  Object.getOwnPropertyDescriptor(오브젝트, "name");
  
  
  for (var key in 오브젝트) {
    // Kim, 30
    console.log(오브젝트[key])
  }
  ```

  - 부모의 prototype도 반복해준다.

  ```js
  class 부모 {
    
  }
  부모.prototype.name = "Park";
  
  var 오브젝트 = new 부모();
  
  for (var key in 오브젝트) {
    // 내가 직접 가지고 있는 값만 반복시키고 싶으면
    if (오브젝트.hasOwnProperty(key)) {
     	// Park
    	console.log(오브젝트[key]) 
    }
  }
  ```

  

- for of 반복문 (iterable 전용) - 신문법

  - Array, 문자, arguments, NodeList, Map, Set에 사용 가능

  ```js
  var 어레이 = [2,3,4,5];
  // 변수명 작명
  for (var key of 오브젝트) {
    console.log(자료)
  }
  
  // Array Iterator {} => 내부 데이터 출력을 도와주는 함수같은 것 
  어레이[Symbol.iterator].next();
  ```

  - NodeList란

  ```js
  // 이거를 쓰고 난 자리에는 대괄호가 남는다.
  // [HTML1, HTML2]
  document.getElementByClassName();
  ```

  

### Symbol

- 심볼 만드는 법

```js
var 심볼 = Symbol("설명");
```

- **심볼은 Object 자료형의 비밀스런 key값**
  - 비밀스런 데이터를 저장하고 싶으면? 
  - 쉽게 말해, Object 안에 주석을 다는 것이다. 

```js
var weight = Symbol("내 시크릿 몸무게임");
var height = Symbol("내 키")

// Symbol 직접 집어넣어도 된다. 
var person = { name : "kim", [height] : 160 };
// 이 정보를 숨기고 싶다면? 
person.weight = 100;
// Symbol 사용
// { Symbol(내 시크릿 몸무게임): 100}
person[weight] = 100;
person[height] = 160;

// symbol은 반복문에서 출력이 안 된다 
for (var key of person) {
  console.log(person[key])   
}
```

- Symbol 특징

  - 설명이 같다고 Symbol이 아니다
    - Symbol을 만들 때 마다 유니크한 Symbol이 생긴다. 

  ```js
  var a = Symbol('설명1');
  var b = Symbol('설명1');
  // false
  console.log(a === b);
  ```

  - 전역 변수같은 전역 Symbol
    - `Symbol.for()`로 만든다
    - 같은 설명을 가지고 있는 심볼이 위에 있으면 기존 심볼을 복붙해준다. 

  ```js
  var a = Symbol.for('설명1');
  var b = Symbol.for('설명1');
  console.log(a === b);
  ```

  - 기본 내장 Symbol들

  ```js
  var 어레이 = [2, 3, 4];
  //자바스크립트 array 기본적으로 집어 넣는 기본 Symbol
  어레이[Symbol.iterator];
  ```

  



### Map, Set

- Map
  - key, Value로 저장 가능해
  - **자료간의 연관성을 표현하기 위해 쓴다.**
    - 화살표 기호를 사용
  - **기존의 Object 자료형은 자료 이름으로 글자만 가능하지만 Map 자료형은 다 가능하다**

```js
var person = new Map();
// Map {"name" => "Kim"}
person.set("name", "Kim");
person.set([1, 2, 3], "Kim");

// 자료 가져오기
person.get('age')
// 자료 삭제하기
person.delete("age")
// Map에 저장된 데이터의 개수
person.size

// 반복문 사용하기
for (var key of person.keys()) {}

// Map 자료형에 직접 자료 집어넣을 떈
var person = new Map([
  ["name", "Kim"],
  ["age", 20]
]);
```



- Set 
  - 중복자료를 허용하지 않는 Array 비슷한 것 

```js
var 출석부 = ["john", "tom", "andy", "tom"];

// Set() {"john", "tom", "andy"}
var 출석부2 = new Set(["john", "tom", "andy", "tom"]);

// Set 자료형에 자료추가하기
출석부2.add("sally");
// 자료 제거하기
출석부2.delete("sally");
// 자료 있는지 확인
출석부2.has("sally")

// Set 자료형 <=> Array 자료형
var 출석부 = new Set(["john", "tom", "andy", "tom"]);
// 중괄호 제거법 
출석부 = [...출석부2]
```





### Web Components : 커스텀 HTML 태그 만들기

- JS 문법으로 구현할 수 있는 브라우저 기본 기능임
- 브라우저 기능을 잘 알아야한다.

```html
<body>
  <custom-input></custom-input>
  <script>
    class 클래스 extends HTMLElement {
      // 우리가 만든 태그가 HTML에 장착될 때 실행할 코드 적는 곳이다. 
      connectedCallback() {
        // 1. html 생성하는 다른 방법
        document.createElement("label");
        this.appendChild(변수)
        // 2. this => 새로 생성될 <custom-input> 요소 
        this.innerHTML = `<label>이메일인풋이에요</label><input>`
      }
    }
    // 정의할 커스텀 HTMl
    customElements.define('custom-input', 클래스);
  </script>
</body>
```

- 커스텀태그의 장점은 html 중복제거, 다른 페이지에서 재활용 가능하다. 

- 파라미터문법같은거 구현 가능

  - 확장성 가능
  - 함수처럼 활용 가능

  - attribute 변경 감지하는 법 가능

```html
<body>
  <custom-input name="이메일"></custom-input>
	<custom-input name="비번"></custom-input>
  <script>
  	class 클래스 extends HTMLElement {

       connectedCallback() {
          let name = this.getAttribute('name');
          this.innerHTML = '<label>${name}을 입력하쇼</label><input>'
       }
       // attribute 변경 감지하는 법 => name이 바뀌는지 감시
       static get observedAttributes() {
         return ["name"]
       }
      // 바뀌면 이거 실행해준다.
       attributeChangedCallback() {
         console.log(this.getAttribute("name"));
       }
    }

    customElements.define("custom-input", 클래스);
  </script>
</body>
```

- 결론 Web Components 기능 쓰면 긴 HTML도 함수처럼 재사용 가능하다

- Lit, stencil 사용하면 된다. 



### shadow DOM과 template으로 HTML 모듈화하기

```html
<input type="range">
```

- 이런거 쓰면 대게 복잡한 레이아웃이 나온다. 
- 실제로 내부적으로도 여러개의 `<div>`를 이용해서 만들어진 것인데 
- 확인하고 싶으면 크롬 개발자도구 - 설정 - show user agent shadow DOM 켜기 이런거 체크해놓으면 된다. 
- 저 코드 안에 `div` 3개가 숨어있다. 이것을 **shadow DOM**이라고 한다.

- Shadow DOM 만드는법

```html
<body>
  <div id="mordor"></div>
  <script>
    // shadow Root 만들기
    document.querySelector("#mordor").attachShadow({mode : "open"})
    // 안에 내용 넣기
    document.querySelector("#mordor").shadowRoot.innerHTML = '<p>심연에서 왔도다</p>'
  </script>
</body>
```



- Web Components + shadow DOM = 완벽한 HTML 모듈
- 변경 전

```html
<body>
  <custom-input name="이메일"></custom-input>
  <script>
      class 클래스 extends HTMLElement {
         connectedCallback() {
           // 다른 label까지 오염 될 수 있다. 
           // 그래서 Shadow DOM 쓰면 좋음.(Shadow DOM에 넣은 것들은 외부에 영향을 주지 않는다.)
            this.innerHTML = `<label>이름을 입력하쇼</label><input>
      <style> label { color : red } </style>`
         }
      }
      customElements.define("custom-input", 클래스);
  </script>
  
</body>
```

- 변경 후

```html
<body>
  <custom-input name="이메일"></custom-input>
  <template id="template1">
   	<label>이메일을 입력하쇼</label><input>
    <style>label { color : red }</style>
  </template>
  <script>
      class 클래스 extends HTMLElement {
         connectedCallback() {
            this.attachShadow({mode: "open"});
           // 독립적인 공간을 생성했으니 다른 label 태그에 스타일 영향을 주지 않는다.
           // 그냥 짜면 드러움 
           // HTML 임시보관함 쓰자.
            this.shadowRoot.append(template1.content.cloneNode(true));
           	let el = this.shadowRoot.querySelector("label");
            el.addEventListener("click", function() {
              console.log("클릭함")
            })
         }
      }
      customElements.define("custom-input", 클래스);
  </script>
  
</body>
```







### ?./ ?? 연산자 (optional chaining)

- 여러 문자, 숫자를 한 변수에 저장하려면

````js
var user = {
    name : 'kim',
    age : 20
}

console.log(user.name);
// 왼쪽이 비어있으면 오른쪽 안해줌
console.log(user?.name);
````

- optional chaining 
  - 왼쪽이 null, undefined면 점 안 찍어주고 undefined 남겨줌

```js
var user = {
    name : 'kim',
    age : {value : 20};
}

// 코드 실행 중단되면서 아래 코드가 작동을 안하는거니까 미리 예방하자.
// optional chaining 사용한다.
console.log(user.age?.name);
// 이 경우에는 undefined.value라서 error를 발생시킨다. 
console.log(user.param.age)
```

- 간단한 object 자료에서는 데이터 뽑을 때는 optional chaining 사용하지 않아도 된다. 자동으로 undefined가 남기 때문이다.

- ?? nullish coalescing operator
  - 왼쪽이 null, undefined일 경우 오른쪽 보여달라는 뜻이다
  - **변수 안에 데이터가 있을 때 데이터가 늦게 도착하면 undefined말고 로딩중을 띄우고 싶을 때 사용하자.**

```js
var user;

console.log(user ?? '로딩중')
```

