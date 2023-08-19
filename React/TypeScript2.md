- 함수 rest 파라미터, destructuring 할 때 타입지정

```typescript

// rest 파라미터 어떻게 지정?
// 함수안에 ... 쓰면 rest parameter
// array나 object에 쓰면 벗겨주세요 뜻
function 함수(...a : number[]) {
  console.log(a);
}
함수(1, 5, 3, 5, 6, 6)


// destructuring object
let { student, age } = { student : true, age : 20}
let 오브젝트 = {student : true, age : 20 }

// destructuring 타입지정
//파라미터 만들기 == 변수 만들기
type New = {student: boolean, age: number}
function 함수1({student, age} : New) {
  console.log(student, age)
}

함수1({ student : true, age: 20})


// 연습 문제
// 1. 최댓값 찾기
function 최댓값(...a : number[]) {
  let result = 0;
  a.forEach((i) => {
    if (result < i) {
      result = i
    }
  })
  return result;
}

console.log(최댓값(6, 3, 7, 2));

// 문제2.object 자료들 파라미터로 입력할 수 있는 방법
type User = { user : string, comment : number[], admin : boolean}


function 유저({user, comment, admin} : User) :void{
  console.log(user, comment, admin);
}

유저({ user : 'kim', comment : [3,5,4], admin : false })

// 문제3.array 자료를 파라미터로 입력할 수 있는 함수
type 어이 = (number | string | boolean)[]

function 어레이([a, b, c]:어이) {
   console.log(a, b, c)
}

어레이([40, 'wine', false])
```

- narrowing

```typescript
// Narrowing할 때  typeof 연산자로 부족할 때가 존재

// null & undefined 타입체크하는 경우가 잦음

function 함수(a : string | undefined) {
  // 1.&&연산자로 이렇게 하면 null & undefined인지 체크할 수 있다. 
  // case1. undefined이면 코드가 실행되지 않다
  // case2. a가 string이면 코드가 실행된다.
  if (a && typeof a === "string" ) {

  }
}

type Fish = {swim : string}
type Bird = {fly : string}

function 함수1(animal :Fish | Bird) {
  // type of 연산자는 number string, boolean, object 이런 식으로만 판정가능하다.
  // in 키워드로 object narrowing 가능
  // 2. 서로 가진 속성명이 다르면 in 써보자. 키값 in object
  if ("swim" in animal) {
    animal.swim
  }
}

// 3. instanceof 연산자로 object narrowing 가능.
// 오브젝트 instanceof 부모 클래스
// object 두개가 비슷하면 부모 class가 누군지 물어봐서 narrowing 가능
let 날짜 = new Date();

if (날짜 instanceof Date) {

}

// 속성명 in 오브젝트자료 (불가능) - 둘 다 똑같은 속성을 가지고 있음
// 오브젝트 instanceof 부모 (불가능)
// 4. 비슷한 구조를 가진 object 두 개를 구분하려면 literal type 강제로 만들어두면 나중에 도움됨
// cars- wheel: 4개, bike- wheel: 2ro

type Cars = {
  wheel : '4개',
  color : string
}
type Bike = {
  wheel : '2개',
  color : string
}

function 함수2(x :Cars | Bike) {
  // Cars type
  if (x.wheel === "4개") {
    console.log("X는 Cars 타입이이에요")
  }
}
```



- Never type

```typescript
// function return 값에 붙일 수 있는 never type
// 조건 1. return 값이 없어야한다.  
// 조건 2. 함수가 끝나면 안 된다.(endpoint)가 없어야 한다.
// 모든 함수는 return undefined를 몰래 가지고 있다.
// 모든 함수는 return 값을 가진다.
// 끝나지 않는 함수를 만드는 법
// 1. error를 낸다.
// 2. while (true)
function 함수() :never {
  // 에러를 강제로 내서 코드 실행이 중단된다. - 함수 실행이 끝나지 않음
  throw new Error()
  while (true) {

  }
}


// never 타입 어디다 쓰냐? - 대부분 쓸데없음 ㅅㄱ. void쓰면 돼
// 코드 이상하게 짜면 등장하기 때문에 알아야 한다. 
// 1. 뭔가 이상한 narrowing
// 아래 예시는 else가 말이 안 돼 string만 들어올 수 있는데 그럴 때 never속성이 들어가면서 있을 수 없다는 뜻이다.
function 함수2(parameter :string) {
  if (typeof parameter == 'string') {
    console.log(parameter)
  } else {
    console.log(parameter)
  }
}

// 2. 어떤 함수표현식은 return 타입이 자동으로 never
// 여기에 error 강제로 내면 쓰고나면 아무것도 남지 않기 때문에 never타입을 return 
let 함수3 = function () {
  throw new Error()
}
```







- public, private 

```typescript
// public 붙으면 모든 자식들이 이용가능하다.
class User {
  public name = "kim";
  constructor(a) {
    this.name = a
  }
  // 당연히 함수에도 사용가능
  public 함수() {

  }
}

let 유저1 = new User("park")
// 수정도 가능 사실 없어도 돼
// public 키워드는 항상 숨겨져 있다.
// public 인스턴스들 새로 뽑을 object에 속성을 부여하고 싶으면 사용가능
유저1.name = "안뇽"


// private은 수정이 불가능하다.
// private 붙으면 class 안에서만 수정, 이용가능하다.
class User2 {
  name :string;
  private familyName :string = "kim";
  constructor(a) {
    this.name = a + this.familyName
  }
  // 자식들이 familyName을 밖에서 바꾸고싶으면?
  // class 안에 familyName 변경 함수를 제작해야한다.
  // 그러면 자식들이 사용가능하다.
  이름변경함수() {
    this.familyName = "park"
  }
}

let 유저2 = new User2("민수")
// 얘가 실수로 familyName 속성 바꾸면 안 돼
// 그럴 때 private를 사용한다. class 안에서만 사용해야하는 필드값
// private은 수정불가가 아니다. class 안에서만 수정, 사용가능하다.
// 데이터를 외부로부터 보호하고 싶을 때 자주 사용하는 패턴이다.
유저2.이름변경함수()
console.log(유저2)


// public 키워드 쓰면 this.어쩌구 생략가능
class Person1 {
  // 이 자리에 들어온 파라미터는 자식의 Name 속성에 기입해주세요.
  constructor (public name : string) {

  }
}

let 자식 = new Person1("kim")
console.log(자식);
```





- protected, static

```typescript
// protected 붙이면 class {} 안에서만 사용가능하다.
// private의 경우에는 NewUser 클래스에서 사용 불가능 반면에 protected는 사용 가능
// 현재 class {} 안에서 + extends 된 class {} 안에서 사용가능하다.
// protected: extends된 class는 사용가능(클래스 공유기능), 자식들 사용 불가능
class User {
  protected x = 10;
}

// NewUser에 User의 값을 복사함
// class를 복사하고 싶으면 extends를 사용하면 된다.
class NewUser extends User {
  doThis() {
    this.x = 20;
  }
}

let 사람 = new NewUser();
console.log(사람);

// static 키워드 붙이면 부모 class에 직접 부여됨(자식에게 안 물려줌, extends하면 잘 따라온다.)
// private/protected/public + static 가능
class User1 {
  static x = 10;
  y = 20;
}

let 자식 = new User1();
// static 키워드에 붙은 것을 사용하려면 직접 부모를 불러서 사용해야해
console.log(User1.x)
console.log(자식.y)

class User2 {
  // 못 물려받게 감추고 싶음
  static skill = "js";
  intro =  User2.skill + "전문가입니다"
}

let 철수 = new User2();
console.log(철수)
// 근데 사실 숨기고 싶으면 protected, private이게 낫다.
User2.skill = "ts"

let 철수2 = new User2();
console.log(철수2);

// 1.x는 User클래스 내에서 접근할 수 있고 static x도 클래스 내에서 클래스.x로만 접근 가능 인스턴스 생성해서 접근 불가능
// 2. y는 어디에서나 사용가능하다. 다만 static 속성 때문에 클래스.y로 접근 인스턴스 생성해서 접근 불가능
// 3. z는 클래스끼리만 공유가능 인스턴스 생성해서 접근 불가능, 클래스.z로도 접근 불가능
class User3 {
  private static x = 10;
  public static y = 20;
  protected z = 30;
}


// 숙제 1.x속성에 숫자를 더해주는 함수가 필요하다.
class User3 {
  private static x = 10;
  public static y = 20;

  static addOne(a:number) {
    User3.x += a;
  }

  static printX() {
    console.log(User3.x);
  }
}

let newUser = new User3();
newUser.addOne(3) //이렇게 하면 x가 3 더해져야함
newUser.addOne(4) //이렇게 하면 x가 4 더해져야함
newUser.printX()


// 숙제2. 무작위로 배치된 박스 만들기
class Square {
  constructor(public width :number, public height :number, public color :string){}
  draw() {
    let a = Math.random();
    let box = `<div style = "position: relative;
    top: ${a * 400}px;
    left: ${a * 400}px;
    width: ${this.width}px;
    height: ${this.height}px;
    background : ${this.color};
    ">
    </div>`
    document.body.insertAdjacentHTML("beforeend", box);
  }
}

let 네모 = new Square(30, 30, 'red');
네모.draw()
네모.draw()
네모.draw()
네모.draw()
```





- generic

```typescript
// 함수에 타입파라미터를 넣을 수 있다(generic)

// 기존 코드
function 함수(x :unknown[]) {
  return x[0];
}

let a = 함수([4, 2]);
// 문제 발생. 문제가 x 자체가 unknown이어서 1을 더할수가 없다.
console.log(a + 1);


// 적용 코드

// type 여러개 지정가능 아무곳에서나 쓸 수 있다.
// 장점: 확장성이 조금 있어 보인다.
function 함수<MyType>(x: MyType[]) :MyType {
  return x[0];
}

let a = 함수<number>([4,2])
let b = 함수<string>(['4', '2'])
console.log(a);



// MyTypes가 우측에 있는 속성을 가지고 있는지 체크한다.
function 함수2<MyTypes>(x : MyTypes) {
  // 에러가 남 뭐가 들어올지 불확실해서 미리 걱정하는 중
  return x - 1
}

let c = 함수2<number>(100)
//해결법
// 타입 파라미터 제한두기
function 함수2<MyTypes extends number>(x : MyTypes) {
  return x - 1
}

let c = 함수2<number>(100)

// 커스텀 타입으로도 타입파라미터 제한가능 
interface LengthCheck {
  length : number
}

function 함수3<MyTypes extends LengthCheck>(x : MyTypes) {
  return x.length
}

let d = 함수3<string[]>(["100"])


// class에더 타입파라미터 넣을 수 있다.
class 클래스 <T> {
  content: T;

  constructor(content: T) {
    this.content = content
  }

  getContent(): T {
    return this.content;
  }
}

let numberBox = new 클래스<number>(123);
//123
console.log(numberBox.getContent());
```





- React + Ts 쓰는 법

  - 설치

    - `npx create react-app 프로젝트명 --template typescript`

  - 기존 프로젝트에 타입스크립트 더하고 싶을 때

    - `npm install --save typescript @types/node @types/react @types/react-dom @types/jest`

  - 일반변수, 함수 만들 때 타입지정 잘해라

  - JSX 표현하는 타입 있음

    ```react
    // html 리턴하려면 JSX.Element
    let 박스 :JSX.Element = <div></div>;
    ```

  - component 만들 때 타입지정 함수 타입지정은 파라미터 & return 값

    ```typescript
    function Profile() :JSX.Element{
      return (
        <>
         프로필입니다.
        </>
      )
    }
    ```

  - Component props 타입지정

    - props는 object 형식이니까 아래처럼 작성해야한다.
    - 맨날 props 잘못 전달해서 에러가 잦다.

    ```react
    function App() {
      return (
        <div>
          <h4>안녕하십니까</h4>
          <Profile name="철수" age="20"></Profile>
        </div>
      );
    }
    
    
    function Profile(props : {name : string, age: string}) :JSX.Element{
      return (
        <>
         {props.name}프로필입니다.
        </>
      )
    }
    
    export default App;
    ```

  - useState 타입지정

    - useState은 타입지정 (알아서 해준다.)
    - 근데 그럴 일이 별로 없지만 state에 stirng | number를 쓰고 싶으면? 
      - Generic 문법을 이용하자

    ```react
    let [user, setUser] = useState<string | number>("kim")
    ```

    

- Redux + TypeSciript 사용할 때 알아야할 점 2 : redux tookit.
  - action 사용할 때 PayloadAction을 필수적으로 사용하고 그 뒤에 어떤 타입을 dispatch할 때 붙일 것인지 정해준다.
  - reudcers의 함수나 state 안 건드려도 된다.
  - state 타입을 export 한다.

```react
//index.tsx
import { createSlice, configureStore, PayloadAction } from '@reduxjs/toolkit';
import { Provider } from 'react-redux';

const 초기값 :{count : number, user: string} = { count: 0, user : 'kim' };

const counterSlice = createSlice({
  name: 'counter',
  initialState : 초기값,
  reducers: {
    // state 건들 필요 없고
    // return type도 적지 않아도 된다.
    increment (state){
      state.count += 1
    },
    decrement (state){
      state.count -= 1
    },
    // action 사용할 때 PayloadAction을 필수적으로 사용하고 그 뒤에 어떤 타입을 dispatch할 때 붙일 것인지 정해준다.
    incrementByAmount (state, action :PayloadAction<number>){
      state.count += action.payload
    }
  }
})

let store = configureStore({
  reducer: {
    counter : counterSlice.reducer
  }
})

//state 타입을 export 해두는건데 나중에 쓸 데가 있음
export type RootState = ReturnType<typeof store.getState>

//수정방법 만든거 export
export let {increment, decrement, incrementByAmount} = counterSlice.actions
```



```react
// App.tsx

import React from 'react';
import { useDispatch, useSelector } from 'react-redux'
// dispatch() 타입지정 끝
import { Dispatch } from 'redux'
import {RootState, increment} from './index'

function App() {
  // index.tsx에 정의한 RootState 가져와서 사용
  const state = useSelector((state: RootState) => state);
  const dispatch: Dispatch = useDispatch();

  return (
    <div className="App">
      {state.counter.count}
      <button onClick={()=>{dispatch(increment())}}>button</button>
    </div>
  );
}

export default App;
```





- array 자료에 붙일 수 있는 tuple type 

  - 첫 자료는 무조건  string, 둘째 자료는 무조건 boolean(위치까지 고려한 타입지정 가능)

  ```typescript
  // 첫 자료는 무조건 string, 둘째 자료는 무조건 number인 array
  // tuple 타입 사용
  // 튜플 타입은 정확히 명시된 개수 만큼의 원소만을 가질 수 있다. 
  let 멍멍 :[string, boolean] = ["dog", true]
  
  
  // 옵션 항상 뒤에서 부터 시작해야한다.
  let 멍멍2 : [string, boolean?, number?] = ["dog", true]
  
  // rest parameter 타입지정시 tuple 가능(좀 더 엄격한 rest parameter 만들 수 있음)
  // 일반 타입지정과 다른건 tuple을 이용하면 전부 배열에 값이 담겨져서 온다.
  function 함수(...x :[number, string]) {
    console.log(x)
  }
  함수(111, "222")
  
  let arr = [1,2,3];
  // 뒤에 값이 spread operator이면 ...number[] 이런식으로 작성하자
  let arr2 :[number, number, ...number[]]= [4, 5, ...arr];
  
  // rest 형식은 배열 형식이어야 한다.
  function 함수(...x :[string, boolean, ...(string | number)[]]) {
    console.log(...x)
  }
  
  함수('a', true, 6, 3, '1', 4)
  
  // 문제 
  // 함수('b', 5, 6, 8, 'a') 이렇게 사용할 경우 이 자리에 [ ['b', 'a'], [5, 6, 8] ] 이 return 되어야한다.
  function 함수2(...rest : [...(string | number)[]]) {
  
    let result :[string[], number[]] = [[], []]
  
    rest.forEach((i) => {
      if (typeof i === "string") {
        result[0].push(i)
      } else {
        result[1].push(i);
      }
  
    })
    return result
  }
  
  함수2('b', 5, 6, 8, 'a')
  ```



- 외부 파일 이용시 declare & 이상한 특징인 ambient module 

```typescript
//data.js
// .js에 있는 변수를 .ts에 이용하고 싶다면?
// 이대로 typeScript에 쓰면 빨간불 뜸 
let a = 10;
let b = {name : "kim"}

// 그래서 변수 재정의가 가능한 declare 문법 사용해라
declare let a;
// 어딘가에 분명 a변수 있으니까 에러내지 말아주세요라는 뜻이다.
// 일반 js파일 등에 있던 변수쓸 때 에러나지 않도록 재정의할 때 쓴다.
console.log(a + 1);

// 특히 .js로 만든 라이브러리 사용할 때 변수, 함수같은걸 declare로 재정의하기도 한다. 

// ts 파일 -> ts 파일로 변수를 가져다 쓰고 싶으면?
// ts 이상한 특징 모든 ts은 ambient module(글로벌 모듈)
// console.log(a + 1);

// ts파일을 ambient 모듈이 아니라 로컬 모듈로 만드는 법
// import export 있으면 자동으로 로컬 모듈이다.

export {}

let b = 10;

// (현재 로컬 모듈이다) 근데 갑자기 글로벌 변수가 만들고 싶다면?
// declare global 사용하면 돼
declare global {
  type Dog = string;
}
```

- d.ts 파일 이용하기

```typescript
// tsconfig.json
{
  "compilerOptions": {
    // 이러면 ts 파일마다 d.ts 파일 자동생성된다. 
    "declaration": true
  }
}

// 어쩌구 .d.ts파일
// 타입정의 보관용 파일
// 다른 ts파일에서 import 가능
export type Age = number;
export interface Person { name : string}

// 혹은 import * as a from "./test" 하면 모든 것들을 가져다 사용 가능하다.
import {Age} from "./test"
let 이름 :string = "김";

// 1. ts 파일에 타입정의가 너무 길면 d.ts 파일 만들기도 한다.
// 2. 모든 타입을 정리해놓은 레퍼런스용으로 d.ts 파일 쓰기
// d.ts 자동생성되는 경우 d.ts 파일 수정 하면 안 된다.


// d.ts 파일은 자동으로 글로벌 모듈이 아니다.
// d.ts 파일 글로벌 모듈 만들기
// !!. 단 정말 귀찮은 거 아님 쓰짐 말기
// tsconfig.jso에 typeRoots 추가
{
  "compilerOptions": {
    "typeRoots" : ["./types"]
  }
}
// 그리고 types라는 폴더 안에 common 폴더 생성 후에 그 안에 d.ts파일을 넣으면 글로벌 모듈화가 가능해진다. 

// 외부라이브러리 쓸 때 타입정의 안되어 있다면?
// 타입스크립트 홈페이지 들어가서 검색해서 설치하면 된다.
// node_modules/@types 폴더에 있는 타입들은 글로벌 모듈이다.
// typeRoots 따로 설정해놓으면 자동으로 @types 포함 안 해준다. 
```

- Implements 키워드

```typescript
// class가 model, price를 가지고 있는지 타입으로 확인하고 싶으면 어떻게 해야하나?
// interface + implements 키워드로 확인하면 된다. 
interface CarType {
  model : string,
  price : number
}

// 이렇게 하면 현재 이 클래스가 CarType의 속성을 다 들고 있는지 확인한다. 
// 빠졌으면 에러로 알려주고 다 갖고 있으면 별말 안해준다. 
// 주의: implements는 타입지정문법이 아니다. 
// implements라는건 interface에 들어있는 속성을 가지고 있는지 확인만하라는 뜻이다.
// class에다가 타입을 할당하고 변형시키는 keyword는 아니다. 
class Cars implements CarType {
  model : string;
  price : number = 1000;
  constructor(a :string){
    this.model = a
  }
}
let 붕붕이 = new Cars('morning');
```



- object index signature

```typescript
// index signature 쓰면 object 타입지정 한번에 가능
interface StringOnly {
  // index signature와 중복되는 속성은 말이 안 된다.
  age: number,
  // 이렇게 짜는건 허용
  [key: string]: string | number
}

let objs :StringOnly = {
  name : 'kim',
  age : 20,
  location : 'seoul'
}

// 배열에서도 똑같이 적용
// object에서 숫자를 지정해도 문자화가 된다.
interface StringOnly2 {
  [key: number]: string,
}

let num :StringOnly2 = {
  0 : 'kim',
  1 : '20',
  2 : 'seoul'
}

interface MyType {
  //recursive 하게 타입 만드는법
  // {'font-size' : {'font-size' : MyType }}
  'font-size' : MyType | number;
}


// object 중첩 타입지정은?
let obj3 :MyType = {
  'font-size' : {
    'font-size' : {
      'font-size' : 14
    }
  }
}

// 숙제1 타입지정
interface 해결 {
  [key : string] : string | number;
}


let 숙제1 :해결 = {
  model : 'k5',
  brand : 'kia',
  price : 6000,
  year : 2030,
  date : '6월',
  percent : '5%',
  dealer : '김차장',
}


// 숙제 2 중첩문 타입지정
interface 해결2 {
  "font-size" : number,
  [key :string] : number | 해결2, 
}

let 숙제2 :해결2 = {
  'font-size' : 10,
  'secondary' : {
    'font-size' : 12,
    'third' : {
      'font-size' : 14
    }
  }
}
```



- object 타입 변환기

```typescript
interface Person {
  age :number,
  name :string,
}

// key 값을 전부 가져오는 keyof 
// age | name => union type으로 설정해줌 
type PersonKeys = keyof Person;
// name1은 안 돼 Literal 타입이라서 
let b :PersonKeys = "name" 


// index signature에다가 keyof 쓰면;
interface Person1 {
  [key :string] : number;
}
// object자료는 숫자를 key값에 넣어도 문자열로 치환한다. 
type PersonKeys2 = keyof Person1;
let c :PersonKeys2 = "name";


// 언제 사용하나?
// 타입으로 전부 String 으로 바꾸려면
type Car2 = {
  color: boolean,
  model : boolean,
  price : boolean | number,
};

// 타입 변환기 
type TypeChanger<MyType> = {
  // 파라미터로 들어온 object 타입의 key값
  // "color" | "model" | "price"
  // 전문용어로(mapping) 
  [key in keyof MyType] :string
}

type 새로운타입 = TypeChanger<Car2>


//숙제 1 Bus 안의 속성을 String or number로 만들기
type Bus = {
  color : string,
  model : boolean,
  price : number,
}

type Changer<meType> = {
  [key in keyof meType] : string | number
}

type a = Changer<Bus>

// 숙제 2 내가 원하는 타입으로 바꿔주기
type Bus2 = {
  color : string,
  model : boolean,
  price : number,
}

type Changer2 <MeType2, T> = {
  [key in keyof MeType2] : T
}

type b = Changer2<Bus2, boolean>
type c = Changer2<Bus2, string>
```





- 조건문으로 타입만들기 & infer

```typescript
// <>이건 일반 타입변수에도 사용가능
// 파라미터로 String 집어넣으면 string 남겨주시고 그게 아니면 unknown 남겨주세요
// type if문을 쓰자
// 왼쪽이 오른쪽에 있는지(조건식에 extends가 들어감)
type Age2<T> = T extends string ? string : unknown;
let b :Age2<string>
let b2 : Age2<unknown>


type FirstItem<T> = T extends any[] ? T[0] : any

//어레이를 입력하면 첫번째 아이템의 타입 array 첫 자료의 타입을 남기고 아니면 any 남김
let age1 : FirstItem<string[]>;
let age2 : FirstItem<number>;


// infer 키워드
// 조건문에서 쓸 수 있는 infer 키워드 타입을 왼쪽에서 추출해준다.
// T에서 타입을 뽑아주세요 R이라는 변수에 담아주세요(R(type) -string)
type Person1<T> = T extends infer R ? R : unknown;

// 새 타입은 string이다.
type 새타입 = Person1<string>

// array 내부에 있는 타입을 뽑을 수 있다.
type 타입추출<T> = T extends (infer R)[] ? R : unknown;
type NewType = 타입추출< boolean[] >

// 함수를 넣으면 함수의 return 타입만 뽑고 싶다.
type 타입추출1<S> = S extends (infer R)[] ? R : unknown;
type a = 타입추출<() => void>

//ReturnType이라는 기본 함수 쓰면 알아서 해준다.
type b = ReturnType<() => void>

```

