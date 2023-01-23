

### An High-Level Overview of Javascript

- 저수준 언어(c)는 개발자가 자원들을 수동적으로 관리를 해야한다. 반면 고수준 언어(파이썬, 자바스크립트)는 모든 것들이 자동적으로 일어나니까 걱정하지 않아도 된다. 그래서 쉽게 배울 수 있지만 단점으로는 빠르거나 최적화 할 수 없다.

- 자바스크립트는 불필요한 것들 때문에 막히는 것을 방지하기 위해서 내부에서 자동적으로 오래되거나 사용하지 않는 객체들을 컴퓨터 메모리에서 제거한다. 이걸 Garbage-collected(쓰레기 수집)라고 한다.

- 컴퓨터는 오직 0과 1만 이해할 수 있다. 모든 프로그램은 0과 1로만 쓰여져야 한다. 이걸 기계 코드라고 불린다. 우린 사람이 읽을 수 있는 코드를 간단하게 쓴다. 추상화 작업을 하는데 따라서 기계 코드로 변환하는 작업이 필요하다 이게 컴파일링이거나 인터프리터 작업이다. 이 작업은 모든 프로그래밍 언어에서 필수적이다.

  - 인터프리터는 변환과 실행을 동시에 진행 속도가 느리죠(실시간 코드 수정이 가능-에러를 바로 알려준다.)
    - 인터프리터 오류발생 -> 코드 수정 -> 실행 후 확인
  - 컴파일러는 이미 기계어로 변환된 목적 파일을 실행만 하면 되므로 속도가 빠르다
    - 컴파일 오류발생 -> 코드 수정 -> 컴파일 -> 실행 후 확인

- 멀티 패러다임
  - 프로그래밍에서 패러다임은 코드 구조화에 대한 접근 방식과 사고 방식은 코딩 스타일이나 기술로 향한다.
  - 선언적 vs 명령적인
  - 절차지향 프로그래밍(우리가 해왔던 것들)
    - 우리가 코드를 구성할때 매우 선형적인 방식을 사용했다.
  - 객체지향 프로그래밍
    - 실세계에 존재하고 있는 객체를 소프트웨어의 세계에서 표현하기 위해 객체의 핵심적인 개념 또는 기능만을 추출하는 추상화를 통해 모델링하려는 프로그래밍 패러다임
      - 추상화란 구체적인 것은 감추고, 대략적이고 전체적인 그림만 드러내는 것을 의미한다. 
  - 함수형 프로그래밍
  - 보통 많은 언어들은 절차지향 or 객체지향을 둘 중에 하나만 가지고 있는데 자바스크립트는 둘 다 가지고 있다.
  
- 프로토타입(시제품) 기반 객체 지향

  - 자바스크립트에 있는 거의 모든 것들은 원시적인 값(문자형, 숫자형)들을 제외하고는 객체이다. 

  - 배열은 객체다 

  - Array(프로토타입)

    - Array.prototype.push
    - Array.prototype.indexOf

    - 위에 array 프로토 타입을 바탕으로 우리는 배열을 만든다.

- 퍼스트클래스 함수

  - 함수는 간단하게 변수처럼 여겨진다. 함수는 다른 함수의 일부분이 되기도하고 함수를 다른 함수로부터 리턴할 수도 있다.

  ```html
  const closeModal = () => {
  	modal.classList.add("hidden");
  	overlay.classList.add("hidden");
  };
  
  <!--passing a function into another function as an argument: First-class functions-->
  overlay.addEventListener("click", closeModal)
  ```

  

- 동적 언어

  - 값을 재할당 할 수 있다.

  ```js
  //No data type definitions. Types becomes known at runtime
  let x = 23;
  let y = 19;
  // Data type of variable is automatically changed
  x = "Jonas"
  ```

  

- 동시실행 모델
  - 어떻게 자바스크립트 엔진은 많은 일들을 동시에 다룰 수 있나
  - 왜 우리한테 필요할까?
    - 자바스크립트는 하나의 싱글 스레드로 동작하는데, 이것은 한 번에 한가지 일만 할 수 있다.
    - 스레드는 컴퓨터에서 명령어의 집합과 같다. 그건 컴퓨터 CPU에서 실행된다. 그래서 우리 컴퓨터에서 기계 과정에서 실행된다.
  - Long-running task는 뭘까
    - 우리의 코드에서 싱글 스레드를 막는다 근데 우리는 어떠한 행동들을 막고 싶지 않다.
  - 그래서 우리는 어떻게 할 수 있을까?
    - 이벤트 루프를 활용하면 시간이 오래 걸리는 작업들을 뒤에서 실행을하고 작업이 끝나면 메인 스레드에 제자리에 갖다 놓는다.





#### The Javascript Engine and Runtime

- 자바스크립트 엔진은 call stack과 Heap이라는 것을 가지고 있다.
- call stack은 실제로 코드가 실행되는 곳이다.

- heap은 체계화되어 있지않는 메모리 pool이다. 우리 어플에 필요한 모든 객체들이 저장된다. 

- 편집: 전체 코드를 머신코드로 한 번에 변환화고, 0과 1로 이루어진 파일(사용하기 좋은)로 변환되어서 컴퓨터에 의해 실행될 수 있게 한다.

  - 소스 코드(편집) -> 머신코드 -> 프로그램 실행(실행)

- 인터프리터는 편집과 실행이 동시에 줄마다 일어나지만 반대로 컴파일러는 편집이 먼저 된다. 

- 모던 자바스크립트나 fully fledged websited(완전히 작동하는 웹 사이트)의 경우에는 더 이상 낮은 속도를 받아들이지 않는다

- 모던 자바스크립트 엔진은 컴파일러와 인터프리터가 섞여있다. 우리는 이걸 Just-in-time compiliation이라고 부른다

- Just-in-time compilation: 전체 코드들은 머신코드로 한 번에 변환되고 그리고 즉시 실행된다.

- Parsing(reading a code): 구문을 해석하는 과정에서 데이터 구조 안에서 분석된다. 이것을 **AST(abstract syntax tree)**라고 불린다.

  - 이것은 각각의 코드의 줄을 조각들로 나누는데 이것은 const나 함수 키워드처럼 말이다. 그리고 모든 조각들을 구조화 되어있는 트리에 저장한다.

    - 여기서 syntax error을 체크한다. 그리고 결과 트리는 후에 머신코드로 사용되어진다.

    - AST example 

      - `const x = 23;`

      ```js
      VariableDeclaration {
        start: 0
        end: 13
        declarations: [
          VariableDeclarator {
          	start: 6
          	end: 12
          	id: Identifier {
          		start: 6
          		end: 7
          		name: "X"
          }
      		init: LIteral {
            start: 10
            end: 12
            value: 23
            raw: "23"
          	}
          }
        ]
        kind: "const"
      }
      ```

​			



- AST 트리는 DOM 트리랑 아무런 관련이 없다. 그냥 엔진 안에 있는 모든 코드들을 대표한다.

- parsing 후에 compilation 그리고 실행하는 과정(콜 스택이 일어난다.) 그리고 뒤쪽에서 코드는 이미 최적화된 상태이며 프로그램이 이미 실행되고 있을때 재편집된다. 
- 최적화 되어 있지 않은 코드들은 실행이 멈추지 않은 상태에서 다 최적화된 코드로 바꾼다. 이런 과정은 모던 엔진이 V-Eight처럼 매우 빠르다.
- 특정 스레드에서 일어나는 일들은 우리는 코드에서 접근할 수 없다.
- 브라우저에 있는 런타임
  - 엔진이 없으면 런타임이랑 자바스크립트가 없다. 그러나 엔진 혼자서는 충분하지 않다. 정상적으로 작동하려면 web APIs(dom, timers, fetch api)에 접근해야한다.
  - Fetch api란?
    -  HTTP 파이프라인을 구성하는 요청과 응답 등의 요소를 JavaScript에서 접근하고 조작할 수 있는 인터페이스를 제공한다.
  - Web APIs의 기능들이 엔진에게 제공되고 그건 자바스크립트의 부분이 아니다. 자바스크립트는 apis을 전역 객체를 통해서 접근한다. 
  - Web APIs는 런타임의 부분이다.
  - 런타임은 자바스크립트와 관련된 것들이 담겨져 있다. 
  - 콜백 큐라고 하는 것이 포함되어 있는데 이것은 데이터 구조인데 모든 콜백 함수들은 이미 실행될 준비가 되어있다.
    - 우리가 만약 이벤트 핸들러 기능인 버튼같은 기능들을 특별한 상황에서 반응할 수 있게 작동시킨다. 이벤트 핸들러 기능을 콜백 함수라고 불린다. 
    - 만약 클릭하면 콜백 함수는 실행될 것이다.
      - 누르면 콜백 기능들이 콜백 큐에 들어가게 된다. 그리고 그리고 콜스택이 비어있으면 콜백 함수들은 스택을 통해서 통과되고 실행된다. 이러한 과정들은 이벤트루프라고 불리는 과정에 의해서 발생된다.
      - 이벤트 루프는 콜백 큐로부터  콜백 기능들은 가지게 되는데 그것을 콜스택에 넣는다.
      - 이벤트루프는 자바스크립트에서 비폐색 동시 실행 모델에 있어서 필수적이다.

- 자바스크립트는 브라우저 밖에서도 존재한다.



#### Execution Contexts and The call stack

- 기계 코드로 변환 후 실행

  - 전역 실행 context(최상위 코드를 위해서) 생성- 함수 내부가 실행되지 않고 바깥쪽에 있는 함수들이 실행된다.

    - 함수 안에 있는 것들은 함수가 실행되어야 작동을한다 그것 말고 함수 밖에 있는 것들은 전역 실행 context가 된다.

    - 예시

      ```js
      // global exection context
      const name = "Jonas";
      
      const first = () => {
        let a = 1;
        const b = second();
        a = a + b;
        return a;
      }
      
      function second() {
        var c = 2;
        return c;
      }
      ```

      

- 실행 context 

  - 자바스크립트의 일부가 실행되고 있는 환경인데 어떠한 코드가 실행되기 위해서 필요한 모든 정보들이 저장되어 있다.

    - 로컬 변수라든지 아니면 함수 안에 있는 구문들

     

  - 자바스크립트 코드는 항상 실행 context 안에서 실행된다.
    - 예시 피자 박스는 피자를 먹기 위한 환경(실행 context)이고 피자는 자바스크립트 코드이다. 그리고 피자를 먹기 위한 포크 같은 것은 코드를 실행하기 위한것이다.
  - **자바스크립트 프로젝트가 아무리 커도 오직 하나의 전역 실행 context를 가지고 있다. 디폴트 context는 항상 있다.** 

- 글로벌 실행 context를 만들고 나서 최상위 코드를 실행하게 된다.
- 그리고 나서 함수들이 실행된다.
  - 함수마다 하나의 실행 context가 있는데 각각의 함수 호출마다 하나의 새로운 실행 context가 만들어진다.
- 콜백함수는 click event와 관련이 있다.
  - 이벤트루프는 이러한 새로운 콜백 함수들을 제공한다.



- 실행 context 내부에는 무엇이 있을까?

  - 변수 환경
    - let, const, and var declarations
      - 함수 안에서 실행되는 것들은 결국 변수 한경 안에 속한다.
    - functions
      - 밖에 있는 함수의 변수에도 접근할 수 있다.
    - Arguments 객체
      - 모든 객체들은 함수의 일부분인데 현재 실행 context에 속한다.
        - 이유는 각각의 함수 호출마다 하나의 새로운 실행 context가 만들어진다.

  - 스코프 체인
    - 스코프 체인은 일종의 리스트로서 전역 객체와 중첩된 함수의 스코프의 레퍼런스를 차례로 저장하고 의미 그대로 각각의 스코프가 어떻게 연결 되고 있는지 보여주는 것 
    - 각각의 실행 context에 저장되어 있다.
  -  `this` keyword
    - 각각의 context는 특별한 변수를 가지게 된다.

- 위에 3가지 모두 생성단계라고 불러지는 곳에서 생성된다. 실행 바로 전에 일어난다.

- 실행 context들은 arrow 함수에 속한다. Argument, this keywords는 arrow 함수에 속하지 않는다.

  - 하지만 arguemnt, this keyword는 일반적인 그들의 가장 가까운 부모함수에 의해서 사용할 수 있다.



```js
// global exection context
const name = "Jonas";

const first = () => {
  let a = 1;
  // second 함수가 실행될때까지 멈추고 실행되어야 작동한다.
  const b = second(7, 9);
  a = a + b;
  return a;
}

function second(x, y) {
  var c = 2;
  return c;
}

const x = first();
```

- global 

  > name = "Jonas"
  >
  > first = <function> - 말 그대로 실행코드다.
  >
  > second = <function>
  >
  > x = <unknown>- 첫 번째 함수의 실행이 필요하다

- First()

  > a = 1
  >
  > b = <unknown> - 두 번째 함수의 실행이 필요하다.

- second()

  > c = 2
  >
  > Arguments = [7, 9] - 이 배열은 구문을 통과한 배열이다. 모든 일반적인 함수에서 이용가능하다. (arrow 함수를 제외하고)





- 콜 스택 실행 순서
  - global -> first -> second
  - **자바스크립트는 하나의 실행의 스레드를 가질 수 있다. 한 번에 하나만 할 수 있다**
  - 두 번째 부분이 실행되면 콜스택에서 사라지고 첫 번째 부분이 다시 실행된다.
  - 콜스택은 절때 실행 순서를 잊지 않는다.
  - 우리가 생각하는 스택의 구조와 같다. 



#### Scope and The Scope Chain

- scoping: 어떻게 우리 프로그램의 함수들은 만들어지고 접근되는지
- lexical scoping: scoping은 함수의 배치나 코드 안에 있는 블럭에 의해 움직인다.
- scope: **특정한 변수들이 선언되는 공간이나 환경을 말한다.**  전역 범위, 함수 범위, 그리고 블럭 범위가 있다.
  - 함수의 경우에는 필수적으로 함수 실행 context에 저장되는 변수 환경이다. 
- 스코프와 변수 환경은 함수면에서만 보면 똑같다.
- 변수의 범위: 특정 변수가 접근이 되는 우리 코드의 지역이다.

- 위의 4가지는 미묘하게 다르다 

- 3가지의 스코프 타입

  - 전역 스코프

    - 탑 레벨 코드 
      - 함수 밖에 있는 코드나 블럭
      - 전역 범위에 있는 변수들은 어디서든지 접근할 수 있다.

  - 함수 스코프(지역 스코프)

    - 각각 그리고 모든 함수는 범위를 만든다.
    - 변수들은 오직 함수 안에서만 접근 가능하다. **밖이 아니다**

  - 블록 스코프(ES 6)

    ```js
    if (year >= 1981 && year <= 1996) {
      const millenial = true;
      const food = 'Avocado toast';
    }
    
    //referenceError
    console.log(millenial)
    ```

    - 변수들은 오직 블록 안에서 접근 가능하다
    - 그러나 오직 let and const에만 적용할 수 있다
      - 블럭 안에 갇혀있다.
      - 만약 var를 사용하면 밖에서도 접근할 수 있다.
    - **함수들은 ES6부터 모두 블록스코프 되어있다.**(오직 스트릭 모드에서)
    - 스코프 체인은 말 그래도 아래로부터 위를 접근한다는 것이 아니고 아래에 있는 함수는 자신이 원하는 변수를 위에서 찾아서 활용하기 위해 스코프 체인을 활용한다.
    - var는 블록 스코프이 적용되지 않는다. 그래서 함수 안에 있으면 지역 변수로 인식된다.
    - 스코프 체인은 함수가 실행된 순서와는 관련이 없다. 달리 말하면 콜스텍에 있는 실행 context의 순서와는 상관 없다.
      - 모든 스코프는 항상 모두 바깥에 있는 범위로 부터 모든 변수들을 접근 할 수 있게 한다. 이게 스코프 체인
      - 특정 범위에 있는 스코프 체인은 모든 부모 범위의 모든 변수 환경들을 함께 추가
      - 함수 호출과 관련이 없다.
      - 자기 자신의 스코프(scope)를 제외한 자신과 가장 가까운 변수 객체의 모든 스코프들을 스코프 체인이라 할 수 있다.
      - 오직 안에 있는 스코프만 밖에 있는 스코프의 변수들을 접근할 수 있다- 스코프 체인은 하나의 길만 존재한다.





#### Scoping in Practice 

- 호이스팅
  - 인터프리터가 변수와 함수의 메모리 공간을 선언 전에 미리 할당하는 것을 의미합니다.

```js
'use strict';

function calcAge(birthYear) {
  const age = 2037 - birthYear;

  function printAge() {
    const output = `${firstName}, You are ${age}, born in ${birthYear}`;
    console.log(output);

    if (birthYear >= 1981 && birthYear <= 1996) {
      var millenial = scope;
      // same block, same block, in according to scope chain, they're looking for current scope.
      // reassigning outer scope's variable. below console.log(output) value is New output
      output = 'NEW OUTPUT!';
      const firstName = 'Steven';
      const str = `Oh, and you're a millenial, ${firstName}`;
      console.log(str);

      function add(a, b) {
        return a + b;
      }
      // original output is working if without const the variable is redefined. and printout New output
      // const output = 'NEW OUTPUT';
    }
    // we cannot access block scope
    // console.log(str)
    // var is not passed into block scoped it can access in the local scope.
    console.log(millenial);
    // we should see add being called if we don't it won't be working
    // console.log(add(2, 3));
    console.log(output);
  }
  printAge();

  return age;
}

const firstName = 'Jonas';
calcAge(1991);

//스코프 체인은 오직 하나의 길만 존재한다.
//오직 안에서 밖에만 접근할 수 있다
console.log(age);

//전역 범위에서는 우리는 다른 범위에서 정의한 어떠한 변수도 접근할 수 없다.
printAge();
```







#### Variable Environment: Hosting and The TDZ

- 호이스팅은 코드가 실행하기 전 변수선언/함수선언이 해당 스코프의 최상단으로 끌어 올려진 것 같은 현상을 말한다(형식적인 정의). 인터프리터가 변수와 함수의 메모리 공간을 선언 전에 미리 할당한다.
- 함수/변수가 선언되기 전에 호출되는 것을 호이스팅이라고 한다.
  - 영어적인 표현에서는 코드들이 선언되기 전에 접근가능하고 사용가능한 변수들의 형태를 만드는 것 + 변수들은 그들의 범위의 최상단으로 이동된다.
  - 뒤쪽에서 실행하기 전에, 코드는 변수 선언을 위해서 스캔이 되어 있고 그리고 각각의 변수는 새로운 즉 새로운 프로퍼티는 변수환경객체에서 생성된다.

- 자바스크립트는 나중에 선언되는 변수를 미리 접근할 수 있다.

  ```js
  cosole.log(value); //undefined
  
  var value = 'Hello'
  
  console.log(value); // Hellow
  
  ```

- **JavaScript는 초기화가 아닌 선언만 호이스팅한다** 

- 다음 같은 경우에는 호이스팅이 발생하지 않는다

  ```js
  show();
  
  //에러가 발생하는 이유는 변수 show는 호이스팅 되지만, 함수를 할당(=초기화)하는 것은 호이스팅 되지 않습니다. 따라서 인터프리터는 변수 show를 함수가 아닌 일반변수로 취급하므로 TypeError가 발생한다.
  var show = function showFunc() {
    console.log('showFunc() Call');
  }
  
  show();
  ```

- 변수 할당이 함수 선언보다 우선순위이며, 함수 선언은 변수 선언보다 우선 순위이다.

  ```js
  // 변수 할당이 함수 선언보다 우선순위다.
  var msg = 'Hello';
  
  function msg() {
    console.log('msg() Call');
  }
  
  console.log(typeof msg); // string
  ```

  ```js
  var msg;
  
  function msg() {
    console.log('msg() Call!');
  }
  
  console.log(typeof msg); //function
  
  ```

|                                 | Hoisted | Initial value                         | scope    |
| ------------------------------- | ------- | ------------------------------------- | -------- |
| Function declarations           | Yes     | Actual function                       | Block    |
| var variables                   | Yes     | undefined                             | Function |
| let and const variables         | No      | `<uninitialized>`, Temporal Dead zone | Block    |
| Function expressions and arrows |         | depending if using var and let/const  |          |

- Temporal Dead Zone은 우리가 범위의 시작과 변수가 선언된 위치의 변수에 접근할 수 없고

  ```js
  const myName = 'Jonas';
  
  if (myName === 'Jonas') {
    console.log('Jonas is a ${job}'); // TDZ(job variable)
    const age = 2037 - 1989; // TDZ(job variable) - ReferenceError: cannot access 'job' before initialization 
    console.log(age); // TDZ(job variable)
    const job = 'teacher';
    console.log(x);
  }
  ```

- TDZ가 존재하는 이유는 쉽게 피하고 에러를 잡기 위해서다(선언 전에 변수에 접근하는 것은 잘못된 관례이며 피해야한다.)

- 또 다른 이유는 `const` 변수가 실제로 작동할 수 있게 만들기 위해서다. 우리는 const 변수에 값을 재할당 할 수 없다. 오직 실행되면서 할당해야한다.

- 호이스팅을 사용하는 이유

  - 실제로 선언되기 전에 함수를 사용하기 위해서
  - var는 실제로 호이스팅 함수의 부산물이다. 
  - 자바스크립트는 절대 큰 프로그래밍 언어가 될 의도가 없었다.