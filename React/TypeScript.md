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
  
  





