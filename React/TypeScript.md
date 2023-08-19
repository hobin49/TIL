- TypeScript(JavaScript + Type 문법)

  - 왜 타입스크립트를 쓸까?

    - 기존 자바스크립트는 Dynamic Typing이 가능해서 5 - "3"을 하면 문자가 숫자로 바뀌어서 5-3= 2가 된다.
    - 프로젝트가 그켠 단점이다. 코드 길게 짤 땐 자유도 & 유연성은 쓰레기
    - TypeScript는 타입 엄격히 검사해준다. 
    - TypeScript는 에러메시지 퀄리티가 오진다. 
    - 그냥 코드 에디터 부가기능 역할로 봐도 된다. 

  - 설치

    - 코드짤 폴더 만들고 에디터로 폴더 오픈
    - 어쩌구.ts 파일 생성 후 코드 짜셈
    - tsconfig.json 생성 후 내용 작성

  - ts파일을 js로 변환해야 사용가능 

    - `tsc -w`를 하면 자동으로 자바스크립트 파일로 변환이 된다. 

    - 파일 사용시 당연히 변환된 js 파일 쓰셈

    - tsconfig.json은 ts => js 컴파일시 옵션설정 가능

      ```json
      {
        "compilerOptions": {
          // esnext 최신 자바스크립트
          "target": "es5",
          // module은 자바스크립트 파일간 import 문법을 구현할 때 어떤 문법을 쓸지 정하는 곳
          // commonjs는 require 문법
          // es2015, esnext는 import 문법을 사용합니다. 
          // 어느정도 호환성을 원하시면 es5, commonjs을 사용하자
          // BigInt() 이런 함수는 esnext 버전으로 올려야한다.
          "module": "commonjs",
        }
      }
      ```
      
      ```typescript
      //이 변수엔 string(문자) type만 들어올 수 있다.
      // 간단한 변수 타입지정가능
      let 이름 :string = "kim";
      
      // array 자료인데 string 담긴 array만 들어올 수 있다.
      let 이름 :string[] = ["kim", "park"];
      
      // object 타입지정
      let 이름 :{ name : string} = { name : "kim"};
      
      let 회원들 : {member1: string, member2: string} = { member1: "kim", member2: "park"}
      
      // 타입지정 원래 자동으로 됩니다. 타입지정 문법 생략가능
       
      // name? = name 속성은 옵션이다. 그럼 뒤에 값이 비어도 error가 뜨지 않는다.
      let 이름 :{ name? : string} = { };
      
      // 다양한 타입이 들어올 수 있게 하려면 Union type
      let 이름 :string | number = "kim";
      
      // 타입은 변수에 담아쓸 수 있다.(type alias) 이름 첫 글자는 대문자
      type Name = string | number;
      
      let 이름 :Name = 123;
      
      // 함수에 타입지정 가능 이 함수는 파라미터로 number, return 값으로 number
      function 함수 (x :number) :number {
        return x * 2
      }
      
      // array에 쓸 수 있는 tuple 타입(무조건 첫 째는 number, 둘 째는 boolean)
      type Member = [number, boolean];
      let john:Member = [123, true]
      
      
      // object에 타입지정해야할 속성이 너무 많으면
      // 글자로 된 모든 object 속성의 타입은 : string
      type Member = {
        [key :string] : string,
      }
      
      let john : Member = { name : "kim" }
      
      // class 타입지정 가능
      class User {
        name :string;
        constructor(name :string) {
          this.name = name;
        }
      }
      ```
      
  
- primitive types

  - JS 문법 그대로 TS에서 사용가능
  - 변수에 타입지정 = 변수에 실드씌우는 것이다.
  
  ```typescript
  // 문자
  let 이름 :string = "kim";
  // 숫자
  let 나이 :number = 50;
  let 결혼했니 :boolean = true;
  // 값이 없어
  let 결혼 :undefined = undefined;
  // 값이 비어있어
  let 결혼해 :null = null;
  // 배열 사용시 왼쪽에 배열에 들어갈 타입을 꼭 명시하자 아래는 문자만 담긴 array만 가능
  let 이름들 :string[] = ["kim", "park"];
  
  // 변수 하나에 여러자료 집어넣고 싶으면 object 자료형 써도 가능, object 자료에도 타입지정 가능
  let 회원들 :{ member1: string, member2: string}= { member1: "kim", member2 : "park" };
  
  // 오늘의 팁 타입지정 원래 자동으로 된다. 타입지정 문법 생략 가능
  
  let 이 = "string";
  ```
  
  





- 타입을 미리 정하기 애매할 떄 

  - Union Type(타입 2개 이상 합친 새로운 타입 만들기)-가변적인 타입 만들기

  ```typescript
  //Union Type(타입 2개 이상 합친 새로운 타입 만들기)
  let 회원 :(number | string | boolean) = 123;
  회원 = 123;
  
  
  
  // 숫자 or 문자가 가능한 array / object 타입지정은?
  let 회원들 : (number | string)[]  = [1, "2", 3];
  
  
  var 오브젝트: {data : string | number} = { data : '123' };
  
  
  // any 타입 모든 자료형 허용해준다. 그럼 타입 스크립트를 쓰는 이유가 없어진다.(타입실드 해제문법)-> 타입관련 버그가 나도 잡아주지 않는다.
  let 이름 :any;
  이름 = 123;
  이름 = true;
  
  
  // unknown 타입 모든 자료형 허용해준다.
  let 이름들 :unknown;
  이름들 = 123;
  이름들 = [];
  
  // any 보이면 실드 죽는다.
  let 변수1 :string = 이름;
  // 오염 방지
  // let 이름들 :string = 이름;
  
  
  
  let 나이 :string|number;
  // 왜 타입맞는데 +1이 안 되니?
  // 타입은 엄격한 거 좋아한다고 했다.
  // union type은 허용하지 않는다. (새로운 타입을 만드는 거니까)
  // string 타입 + 1(허용)| number 타입 + 1(허용), string | number타입 +1 (안돼)
  나이 + 1;
  
  // unknown이어도 안 된다.
  // 숫자타입이여야 숫자처럼 연산해준다.
  let 내나이 :unknown = 1;
  내나이 - 1;
  ```

  - 타입스크립트의 엄격함에 대해 - 간단한 수학연산도 타입맞아야한다.
  - any타입 보다 unknown 타입을 선호하는 이유는 타입 검사를 강제하기 때문에 더 안전한 타입이다. 이는 잠재적인 오류를 줄이고 더 견고한 코드를 작성할 수 있게 도와줍니다.
  - unknown 타입은 변수의 타입이 알려지지 않은 상태임을 나타낸다. 따라서 unknown 타입의 변수에 대해 어떠한 작업도 수행할 수 없고, 해당 변수를 사용하기 전에 타입을 명시적으로 검사해야 한다. 
  
- 함수에 타입 지정하는 법 && void 타입

  - 함수란

    - 길고 복잡한 코드 한 단어로 축약 가능

    - 숫자 집어넣으면 다른 숫자 나오는 블랙박스 역할

    - 파라미터 (숫자 input역할)

    - return할 값(output되는 값 = 뱉어주세요)

    - 파라미터 만드는게 변수 작명이랑 똑같음

    - 변수만 만들면 :any 자동할당된다.

      ```typescript
      // 파라미터로 들어올 수 있는 수를 타입지정
      // return 되어야하는 값도 타입지정
      function 함수(x : number) :number {
        return x * 2
      }
      
      함수(4)
      ```

    - 함수는 파라미터, return 값 타입지정가능

    - 함수에서 void 타입 활용가능

    - void 타입(텅 비었다는 뜻)을 쓰면 실수로 뭔가 return하는 것을 사전에 막을 수 있다. 

      - 함수를 쓰고 나서 뱉고싶지 않을 때 
    
    
    ```typescript
    function 함수(x : number) :void {
      x * 2
    }
    
    ```
    
    - 자바스크립트와 다른 점 
    
      - 타입지정된 파라미터는 필수이다.
    
      ```typescript
      function 함수(x : number) {
        return x * 2
      }
      // 파라미터 안 쓰면 에러난다.
      함수()
      ```
    
      - 파라미터를 넣지 않아서 발생하는 에러를 방지하기 위해서 옵션파라미터를 쓰면된다. 변수 뒤에 ?만 넣으면 된다.
    
      ```typescript
      function 함수(x? : number) {
        return x * 2
      }
      
      함수()
      
      // object인 경우 => 옵션
      {age? : number}
      ```
    
      ```typescript
      // 타입스크립트에선 변수의 타입이 number | string 이런 union type인 경우 자료 조작을 금지시킨다.
      function 자릿수세기(x :number | string) {
        return x + 1;
      }
      
      // 옵션 파라미터의 경우 number | undefined이기 때문에 확실하지 않아서 에러가 뜬다.
      function 내함수(x? :number) :number {
        return x * 2
      }
      ```
      
      
      
      
      
      - 변수가 ? 연산자는 들어올 수도 있다라는 뜻이긴 한데 
      
        - 변수: number | undefined와 뜻이 같다.(union type)
        - 즉 어떠한 값도 함수에 넣지 않으면 옵션파라미터 사용시 자동으로 변수의 값은 undefined가 된다. 
      
        ```typescript
        function 함수(월소득 :number, 집보유여부: boolean, 매력점수: string) :string {
          let 총점수 :number = 0;
          총점수 += 월소득;
          if (집보유여부 === true) {
              총점수 += 500;
            }
        
            if (매력점수 === "상") {
              총점수 += 100;
            }
        
            if (총점수 >= 600) {
              return "결혼가능"
            }
        }
        
        console.log(함수(100, true, "상"))
        ```
      
    - Narrowing && Assertion
    
      - Narrowing
    
        - Type이 아직 하나로 확정되지 않았을 경우 Type Narrowing 써야한다. 타입을 정한다.
        - typeof 연산자 활용
        - 어떤 변수가 타입이 아직 불확실하면 if 문 등으로 Narrowing 해줘야 조작가능
        - (주의) if문 썼으면 끝까지 써야 안전 else, else if 안쓰면 에러로 잡아줄 수도 있다.
        - Narrowing으로 판정해주는 문법들(현재 변수의 타입이 뭔지 특정지을 수 있기만 하면 다 인정해준다.)
          - `typeof` 변수
          - 속성명 In 오브젝트자료
          - 인스턴스 instanceof 부모
      
        ```typescript
        function 함수(a : string | number) {
          if (typeof a === 'string'){
            return a + "1"
          }
          return  + 1
        }
        
        함수(123);
        ```
      
        
      
      - Assertion 문법(타입 덮어쓰기)
      
        - 아무때나 쓰지말자
        - 언제 쓰나?
          - Narrowing 할 때 쓴다. (Union Type을 하나로 확정하고 싶을때 사용) 
            - 절대 타입을 A에서 B로 변경할 때 사용하지말자.
          - 무슨 타입이 들어올지 100% 확실할 때 쓰자.
            - As문법을 쓰면 as number해도 문자를 넣어도 아무일 없음 (이런 버그 캐치 못함)
            - 즉 남이 짠 코드 수정할 대 왜 타입에러가 나는지 모르겠을 때 비상용으로 사용하자.
      
        ```typescript
        function 내함수(x :number|string) {
        
          let array :number[] = [];
          // 왼쪽에 있는 변수를 number로 덮어쓰여요.(if문 필요없어)
          array[0] = x as number;
        
        }
        
        let 이름 :string = "kim";
        // Type a -> b (x)
        이름 as number;
        
        내함수(123);
        ```
      
      
      
      
      - type도 변수에 담아서 써라
      
        - type alias
      
        ```typescript
        
        //영어 대문자 국룰
        type AnimalType = {name : string, age: number}
        
        let 동물 : AnimalType = { name : "kim", age : 20}
        
        
        // const 변수는 등호로 재할당만 막는 역할이다
        // const로 담은 Object 수정은 자유롭게 가능
        const 출생지역 = { region : "seoul" };
        출생지역.region = "busan"
        
        //readonly 쓰면 object 자료 수정도 막을 수 있다.
        // 수정하면 에러가 뜬다.
        // object 속성 안에도 ? 사용가능
        type Girlfriend = {
          readonly name: string
          age? : number
        }
        
        // 타입스크립트 에러는 에디터 & 터미널에서만 존재함
        // 실제 Js코드는 문제없이 돌아가
        const 여친 :Girlfriend = {
          name : "엠버",
          age : 21
        }
        
        //옵션 파라미터는 object 속성 안에도 사용가능하다.
        type Girfriend = {
          name? : string | undefined
        }
        
        //type 변수 union type으로 합치기 가능
        type Name = string;
        type Age = number;
        type Person = Name | Age;
        
        // 연산자로 object 타입 extend
        type PositionX = { x : number };
        // 같은 이름의 type 변수 재정의 불가능
        type PositionX = number;
        
        type PositionY = { y : number };
        
        // {x: number, y: number}
        type NewType = PositionX & PositionY
        
        let position :NewType = { x: 10, y : 20 }
        ```
        
        - object 타입을 정의한 type alias 두개를 & 기호로 합칠 때 중복된 속성이 있으면 어떻게 될까요?
        
          ```typescript
          type A = {
            prop: string;
          };
          
          type B = {
            prop: number;
          };
          
          type C = A & B; // Error
          ```
        
        - ```typescript
          type A = {
            prop: string;
          };
          
          type B = {
            prop: string;
          };
          
          type C = A & B; // No error, C is { prop: string }
          
          ```
        
          

- Literal Types로 만드는 const 변수 유사품

  ```typescript
  // 더 엄격하게 타입지정 가능
  // 이 변수에 무조건 kim만 들어올 수 있다.
  // 변수에 뭐가 들어올지 더 엄격하게 관리가능
  // 자동완성 힌트 굿
  let 이름 :"kim"
  
  // 함수 파라미터에 hello가 무조건 들어가야함
  function 함수(a: "hello") : (1 | 0) {
    
  }
  함수("hello")
  
  //const 변수의 한계 객체 안의 값은 바꿀 수 있음
  //Literal type은 const 변수와 유사하게 사용가능하다.
  // 2개 이상 저장가능하다. 
  // Literal type은 const 변수 업글버전이라고 생각하면 된다. 
  
  
  //Literal type의 문제점
  var 자료 = {
    name: "kim"
  }
  
  
  function 내함수(a: "kim") {
  
  }
  
  // 에러가 나는 이유는 내함수 안에 파라미터에는 "kim"만 들어와야 하는데 위에 자료.name은 string이니까 불일치해서 오류를 반환 
  내함수(자료.name)
  
  // 솔루션 1. object 만들 때 타입지정 확실히 해라
  // 솔루션 2. as const를 사용하면 object value 값을 그대로 타입으로 지정해준다. 
  let 자료 = {
    name : 'kim'
  } as const;
  
  function 내함수(a : 'kim') {
  
  }
  내함수(자료.name)
  // 솔루션 3. as const 이상한 키워드 쓰던가 - 이 objectsms literal type 지정 알아서 해주셈
  // 1.as const를 사용하면 object value 값을 그대로 타입으로 지정해준다. 
  // 2. object 속성들에 모두 readonly 붙여준다. 
  // 결론 object 자료를 완전히 잠가놓고 싶으면 as const를 사용하자 .
  ```
  
  



- 함수와 methods에 type alias 지정하는 법 

```typescript
// 함수 type 저장해서 쓰는 법 
// arrow function 활용
// 함수 파라미터에는 string만 들어오고 return은 number형태만 올 수 있다. 

// 1.함수타입은 () => {}모양으로
// 2.함수선언식이 아닌 표현식에서만 type alias 사용가능하다.

type 함수타입 = (a :string) => number;

let 함수 :함수타입 = function () {

}

type plus = (a : number) => number;

type change = () => void;

type 회원 = {
  name : string,
  age : number,
  plusOne : ( x :number) => number,
  changeName : () => void,
}


let 회원정보 :회원 = {
		name : 'kim',
		age : 30,
		plusOne (x){
			return x + 1
		},
		changeName : () => {
		  console.log('안녕')
  	}
	}

회원정보.plusOne(10)



//콜백함수
// 함수 1 내부 코드 a()실행됨
// 근데 파라미터를 a 자리에 집어넣어서 함수2() 실행된다. 

function 함수1() {
  a()
}

function 함수2() {
  
}
// 함수 안에 함수가 들어가는 것을 콜백함수라고 부른다. 
함수1(함수2)


// 예제
// 맨 앞에 "0" 문자가 있으면 제거하고 type으로 return 해준다.
let cutZero :zero = function (x) {
  // 첫 번째 0과 매치되는지 1번이상 반복
  let result = x.replace(/^0+/, "");
  return result 
}
cutZero("01010")


type remove = (b: string) => number

// 문자를 하나 입력하면 대시기호 "-" 있으면 전부 제거해주고 그걸 숫자 type으로 Return 해준다. 
let removeDash :remove = function(b){
  let result = b.replace(/-/g, "");
  return parseFloat(result)
}  


function 만들함수(a:string, func1: zero, func2: remove) {
  let result = func1(a);
  let result2 = func2(result);
  console.log(result2);
}


만들함수('010-1111-2222', cutZero, removeDash)
```





- 타입스크립트로 HTML 변경과 조작할 때 주의점

```typescript
// h4 안의 글자를 바꿔보자
// null이 아니지 체크한다. 제목이라는 변수를 narrowing을 하면된다. 
let 제목 = document.querySelector("#title");
if (제목 !== null) {
  제목.innerHTML = "반가워요"
}

// narrowing 하는 방법 5개 
// 1.null

// 2.instanceof 연산자
if (제목 instanceof Element) {
  제목.innerHTML = "반가워요"
}

// 3.as로 사기치기
// 이 요소는 element라고 사기쳐주세요
// null이 들어와도 element type가능
// 비상시에 100%확신이 있을때
let 제목1 = document.querySelector("#title") as Element;
제목.innerHTML = "반가워요"


// 4. 오브젝트에 붙이는 ?.
// 제목에 innerHTML이 있으면 출력해주고
// 없으면 undefined 뱉어내 (optional chaing)
let 제목 = document.querySelector("#title");
if (제목?.innerHTML !== undefined) {
  제목.innerHTML = "반가워요"
}

//5. 무식한 방법 귀찮은 strict 모드 끄기



// a태그 href 속성내용을 바꾸자
// 기존의 Element는 속 빈 강정이다.
// 그래서 HTMLAnchorElement 타입을 사용하면
// 이 타입은 href, style, css 이런거 사용할 수 있다.
let 링크 = document.querySelector('#link');
if (링크 instanceof HTMLAnchorElement) {
  링크.href = "https://www.naver.com/"
}


let 버튼 = document.querySelector("button");
// 버튼에 addEventListener 가능하면 해주시고 아니면 undefined 뱉자.
버튼?.addEventListener("click", ()=> {
    console.log("안녕")
})

let 이미지 = document.querySelector("#image");

if (이미지 instanceof HTMLImageElement) {
  이미지.src = "./images/rose.jpg"
}


// 3개의 링크를 모두 바꾸는 법 

let 링크스 = document.querySelectorAll(".naver");

링크스.forEach((link) => {
  if (link instanceof HTMLAnchorElement) {
    link.href = "https://kakao.com"
  }
})
```





- class 키워드 알아보기

```js
{object} 자료형으로 LoL 캐릭터들의 정보를 정리하자

저렇게 비슷한 object 많이 만들일 있으면 class 만들어 쓰세요

기존코드
<script>

 let nunu = {
  q : "consume",
  w : "snowball",
 }

 let garen = {
  q : "strike",
  w : "courage",
 }


</script>
```

```js
function Machine(토끼1) {
      this.q = 토끼1;
      this.w = "snow";
    }

let nunu = new Machine("consume");
let garen = new Machine("strike");

//ES6 문법
class Hero {
  constructor(구멍) {
    this.q = 구멍;
    this.w = "snowball";
  }
}

new Hero("consume")
```



- prototype
  - 부모 자식생산하는 느낌
  - Prototype 이라는거 써도 자식 object에게 데이터 물려줄 수 있다. 
  - 기계는 자동적으로 prototype이라는 공간이 생긴다. 
  - 프로토타입은 유전자라고 인식하면 쉽다.
    - 기계의 유전자
      - prototype에 뭔가 추가하면 자식들이 사용가능

```js
// 여기다가 쓰면 자식이 직접 가진다.
function 기계() {
  this.q = "strike",
  this.w = "snowball",
}

// 여기다 쓰면 부모만 가지게 된다. 
기계.prototype.name = "kim"

let nunu = new 기계()
```

- 부모 유전자에 있는걸 자식이 사용가능한 이유는?
  - object에서 자료뽑을 때 일어나는 일
  - nunu가 name을 가지고 있지 않으면 nunu 부모유전자 뒤진다.(거기 name이 있으면 출력한다.)
    - 처음에 직접 자료를 가지고 있으면 그것을 출력하고 
    - 아니면 부모한테 물어봐서 가져옴
    - Prototype.chain의 원리이다. 

```javascript
let 어레이 = [4, 2, 1];
어레이.sort();
```

- 어레이에 length를 붙일 수 있는 이유가 뭔데

```js
// 인간방식
let 어레이 = [4, 2, 1];
// 컴퓨터방식
let 어레이 = new Array(1, 2, 4);
```





- Class 만들 때 타입지정 가능

```typescript
class Person {
  data = 0;
}

let 사람1 = new Person();
let 사람2 = new Person();

// 0
console.log(사람1.data);
// 0
console.log(사람2.data);



class Person {
  // TS & JS 다른 점이다.
  // name 형태 미리 지정해야한다.
  // TypeScript constructor()는 필드값에 어쩌구가 미리 있어야 this.어쩌구 가능
  name : string;
  // 복제되는게 object이라서 return 타입 지정할 이유는 없다.
  // 당연히 rest parameter, default parameter 등 가능
  constructor(a :string) {
    this.name = a
  }

  // prototype도 type 지정 가능
  함수(a :string)  {
    console.log("안녕" + a);
  }
}


let 사람1 = new Person("Kim");
let 사람2 = new Person("Lee");

사람1.함수("안녕");



Car 클래스를 만들고 싶습니다.

1. 대충 { model : '소나타', price : 3000 } 이렇게 생긴 object를 복사해주는 class를 만들어보십시오.

2. 그리고 복사된 object 자료들은 .tax() 라는 함수를 사용가능한데 현재 object에 저장된 price의 10분의1을 출력해주어야합니다. 

3. model과 price 속성의 타입지정도 알아서 잘 해보십시오. tax() 함수의 return 타입도요. 

class Car {
  name :string;
  price :number;

  constructor (a: string, b: number) {
    this.name = a
    this.price = b;
  }

  tax () :number {
    return this.price * 0.1;
  }
}

let car1 = new Car("소나타", 3000);
console.log(car1);
console.log(car1.tax());
```





- interface

```typescript
// object 만드는 법 유사함
// object 타입지정시 interface 사용 가능하다.
// class 만드는 법이랑 유사하다.
// 항상 첫 글자는 대문자
interface Square { color : string, width: number}

let 네모 :Square= { color : "red", width: 100}

interface Student { name : string}

interface Teacher { name : string, age: number}

let 학생 :Student = { name : "kim" }
let 선생 :Teacher = { name : "kim", age : 20}

// &기호 (intersection type)
// 왼쪽도 만족하고 오른쪽도 만족하는 타입을 생성해주세요 
type Animal = { name : string}
type cat = { age : number} & Animal


// type vs interface
// interface는 중복선언 가능
// type은 중복선언 불가능
// Student = { name :string, score :number}
// 자동으로 extends된다.
interface Student {
  name : string;
}

interface Student {
  score : number
}

// 에러 발생
type Animal = { name : string }
type Animal = { name : string }



// 주의사항1 .extends 쓸 대 중복속성 발생하면?
// 에러로 잡아준다.
interface Student {
  name : string
}

interface Teacher extends Student{
  name : number;
}

// 주의사항 2. & 기호 쓸 때 중복속성 발생하면?
// 에러가 발생한다. 다만 사용하기 전에 미리 에러가 안날 뿐이다. 
type Animal = { name : string}
type Cat = { name : number} & Animal

let 야옹이 :Cat = { name : "kim"}


interface Cart {
  product : string,
  price: number
}

let 장바구니 :Cart[] = [ { product : '청소기', price : 7000 }, { product : '삼다수', price : 800 } ];
```



