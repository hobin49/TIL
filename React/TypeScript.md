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

  - Union Type(타입 2개 이상 합친 새로운 타입 만들기)

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
      // 파라미터로 들어올 수 있는 수는 숫자
      // return 되어야하는 값도 숫자
      function 함수(x : number) :number {
        return x * 2
      }
      
      함수(4)
      ```

    - 함수는 파라미터, return 값 타입지정가능

    - 함수에서 void 타입 활용가능

    - void 타입(텅 비었다는 뜻)을 쓰면 실수로 뭔가 return하는 것을 사전에 막을 수 있다. 

    ```typescript
    function 함수(x : number) :void {
      return x * 2
    }
    
    ```

    - 자바스크립트와 다른 점 

      - 타입지정된 파라미터는 필수이다.

      ```typescript
      function 함수(x : number) {
        return x * 2
      }
      //에러난다.
      함수()
      ```

      - 그래서 옵션파라미터를 쓰면된다. 변수 뒤에 ?만 넣으면 된다.

      ```typescript
      function 함수(x? : number) {
        return x * 2
      }
      
      함수()
      
      // object인 경우 => 옵션
      {age? : number}
      ```

      - 변수가 ? 연산자는 들어올 수도 있다라는 뜻이긴 한데 
        - 변수: number | undefined와 같다.(union type)
        - 즉 어떠한 값도 함수에 넣지 않으면 옵션파라미터 사용시 자동으로 변수의 값은 undefined가 된다. 
