- 뷰 CLI 

  - 뷰  CLI 설치 -> 프로젝트 생성 -> 관련 라이브러리 설치 -> 프로젝트 구동

- 생성 방법

  - 내가 만든 폴더 내에서 명령 프롬프트 창을 열고 `vue init webpack-simple`을 입력하고 실행한다

  > Generate project in current directory? Yes
  >
  > Project name: vue-todo
  >
  > Project description: A Vue.js project
  >
  > Author: id<mail>
  >
  > License: MIT
  >
  > Use sass? No

  - 그리고 `npm install`과 `npm run dev`을 입력하여 실행한다.





- 반응형 웹 디자인 태그 설정

  ```html
  <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
  </head>
  ```

  - viewport 메타 태그를 추가하면 PC 웹 화면뿐만 아니라 모바일 웹에서도 레이아웃이 깨지지 않고 잘 보인다
  - `width=device-width` 속성은 기기의 너비만큼 웹 페이지의 너비를 지정하라는 의미이다.
  - 그리고 `initial-scale=1.0`은 페이지의 배율로, 페이지가 로딩되었을 때 줌 레벨을 의미한다.

- 어썸 아이콘 CSS 설정

  ```html
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"/>
  ```

  - 어썸 아이콘은 구글의 머터리얼 아이콘보다 더 많은 종류를 제공하며 대중적으로 사용되는 아이콘 CSS입니다.

- 폰트/파비콘 설정

  ```html
  <link rel="shortcut icon" href="src/assets/favicon.ico" type="image/x-icon"/>
  <link rel="icon" href="src/assets/favicon.ico" type="image/x-icon" />
  <link href="https://fonts.googleapis.com/css?family=Ubuntu" rel="stylesheet"/>
  ```

  

- 컴포넌트 생성

  - Src 폴더 밑에 components 폴더를 생성하고 그 아래에 TodoHeader.vue, TodoInput.vue, TodoList.vue, TodoFooter.vue를 생성한다.
  - 애플리케이션 규모가 클 경우에는 `component/기능/컴포넌트.vue` 와 같은 형식으로 관리하는게 좋다. 

- 컴포넌트 구분

  - 컴포넌트를 한눈에 구분할 수 있도록 아래와 같이 간단한 코드를 삽입한다.

    ```vue
    <template>
      <div>각 컴포넌트 이름</div>
    </template>
    
    <script>
    export default {};
    </script>
    
    <style></style>
    ```

    

- 컴포넌트 등록

  - 애플리케이션에서 사용할 컴포넌트는 모두 최상위 컴포넌트인 App.vue에 등록한다

    ```vue
    <template>
      <div id="app"></div>
    </template>
    
    <script>
    export default {};
    </script>
    
    <style></style>
    ```

    

- 지역 컴포넌트 등록

  - 지역 컴포넌트 등록 형식을 App.vue 파일에 적용한다.

    ```vue
    <template>
      <div id="app"></div>
    </template>
    
    <script>
    export default {
      components: {
        'TodoHeader': TodoHeader,
        'TodoInput': TodoInput,
        'TodoList': TodoList,
        'TodoFooter': TodoFooter,
      }  
    };
    </script>
    
    <style></style>
    ```

    

- 싱글 파일 컴포넌트 체계에서는 특정 컴포넌트에서 다른 위치에 있는 컴포넌트의 내용을 불러올 때 아래 형식을 사용한다.

  ```vue
  import TodoHeader from './components/TodoHeader.vue';
  import TodoInput from './components/TodoInput.vue';
  import TodoList from './components/TodoList.vue';
  import TodoFooter from './components/TodoFooter.vue';
  ```

  

- ES5와 ES6의 차이점은 import 구문으로 컴포넌트의 내용을 불러와 담고 넘겨 주느냐, var로 선언한 객체에 컴포넌트의 내용을 담아 넘겨 주느냐의 차이다. 



- 컴포넌트 등록이 완료하였으니 마지막으로 컴포넌트 태그 4개를 App.vue의 `<div id="app">`태그 안에 추가합니다.

  ```vue
  <template>
    <div id="app">
      <TodoHeader></TodoHeader>
      <TodoInput></TodoInput>
      <TodoList></TodoList>
      <TodoFooter></TodoFooter>
    </div>
  </template>
  ```

- 컴포넌트 내용 구현하기

  - TodoHeader: 애플리케이션 이름 표시
  - TodoInput: 할 일 입력 및 추가
  - TodoList: 할 일 목록 표시 및 특정 할 일 삭제
  - TodoFooter: 할 일 모두 삭제 

- 애플리케이션 제목 추가하기

  ```vue
  <template>
  	<header>
    	<h1>TODO it!</h1>
    </header>
  </template>
  ```

- CSS로 제목 꾸미기

  ```vue
  <!--App.vue-->
  <style>
  body {
    text-align: center;
    background-color: #f6f6f8;
  }
  input {
    border-style: groove;
    width: 200px;
  }
  button {
    border-style: groove;
  }
  .shadow {
    box-shadow: 5px 10px 10px rgba(0, 0, 0, 0.03);
  }
  </style>
  
  <!--TodoHeader.vue -->
  <style scoped>
    h1 {
      color: #2F3B52;
      font-weight: 900;
      margin: 2.5rem 0 1.5rem;
    }
  </style>
  ```

  - `<style>` 태그에 사용된 scoped는 뷰에서 지원하는 속성이며, 스타일 정의를 해당 컴포넌트에만 적용하겠다는 의미입니다.



- 할 일을 입력하는 TodoInput 컴포넌트

  - 인풋 박스와 버튼 추가하기

    ```vue
    <template>
      <div>
        <input type="text" v-model="newTodoItem" />
        <button>추가</button>
      </div>
    </template>
    
    <script>
    export default {
      data() {
        return {
          newTodoItem: ''
        };
      }
    };
    </script>
    ```

  - 인풋 박스에 텍스트를 입력했을 때 뷰 인스턴스에서 텍스트 값을 인식할 수 있게 v-model 디렉티브와 데이터 속성 newTodoItem을 다음과 같이 추가한다.

    - 인풋 박스에 텍스트를 입력하며넛 newTodoItem의 값을 지켜보면 텍스트를 입력함에 따라 newTodoItem 값도 같이 갱신된다.

  - 텍스트를 저장하기 위한 버튼 이벤트 추가하기