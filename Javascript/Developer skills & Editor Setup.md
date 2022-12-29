#### Setting up Prettier and VS Code

- `.prettierrc`라는 파일을 만들어서 내가 원하는 것들을 변경한다. 

  ```js
  {
    "singleQuote": true,
    "arrowParens": "avoid"
  }
  
  ```

  

- 위에처럼 처리하면 자동저장 했을시에 자동으로 내가 요청한 것처럼 처리된다.

- Snippets 활용 

  ```js
  "Print to console": {
      "scope": "javascript,typescript",
      "prefix": "cl",
      "body": ["console.log();"],
      "description": "Log output to console"
  }
  ```

- 위에처럼 console.log를 cl만 입력하면 자동으로 뜨게 처리해준다. 



#### 4 steps to solve any problem

- make sure you 100% understand the problem. Ask the right questions to get a clear picture of the problem

  - ask questions more concretely

  >
  >
  >he: " We need a function that reverses whatever we pass into it"(x)
  >
  >he: "What does "whatever" even mean in this context? what should be reversed? Answer: only strings, numbers, ....(0)
  >
  >he: what to do if something else is passed in? 
  >
  >he: what should be returned? Should it always be a string, or should the type be the same as passed in?
  >
  >he: how to recognize whatever the argument is a number, a string, or an array?

- Divide and conquer: Break a big problem into smaller sub-problems.

  > Check if argument is a number, a string, or an array
  >
  > Implement reversing a number
  >
  > Implement reversing a string
  >
  > lmplement reversing an array
  >
  > Return reversed value

- Don't be afraid to do as much reserach as you have to 

- For bigger problems, write pseudo-code before writing the actual code
- genuine curiosity

- ex) 문제 발생: 온도계 이상 문제 

  - 문제 이해
    - 온도 진폭이 뭐냐
    - 진폭은 최고 온도와 최저 온도의 차이
    - 어떻게 최고 온도와 최저 온도를 계산할래?
    - 무슨 센서가 오류가 발생했는데

  - 작은 문제로 들어가기
    - 어떻게 오류를 무시할건데
    - 최고 온도를 찾기
    - 최저 온도를 찾기
    - 최고 온도와 - 최저 온도 그리고 return