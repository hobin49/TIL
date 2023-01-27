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

    ```vue
    <template>
      <div>
        <input type="text" v-model="newTodoItem" />
        <button v-on:click="addTodo">추가</button>
      </div>
    </template>
    
    <script>
    export default {
      data() {
        return {
          newTodoItem: ''
        };
      },
      methods: {
        addTodo() {
          // 인풋 박스에 입력하고 추가 버튼을 클릭하면 다음과 같이 콘솔에 텍스트 값이 표시된다.
          console.log(this.newTodoItem);
        }
      }
    };
    </script>
    ```

  - 입력받은 텍스트를 로컬 스토리지에 저장하기

    ```vue
    methods: {
    	addTodo() {
    		localStorage.setItem(this.nowTodoItem, this.newTodoItem);
    	}
    }
    ```

    - 입력받은 텍스트를 로컬 스토리지의 setItem() API를 이용하여 저장한다. `setItem()`는 로컬 스토리지에 데이터를 추가하는 API다. API의 형식은 키, 값 형태이며 저장 기능을 최대한 단순하게 하기 위해 키, 값 모두 입력받은 텍스트로 지정한다. 

  - 로컬 스토리지에 저장된 것을 확인하려면 크롬 개발자 도구의 [Application -> Local Storage -> http://localhost:8080]
  
  - addTodo() 안에 예외 처리 코드 넣기
  
    ```vue
    methods: {
        addTodo() {
          //인풋 박스의 입력 값이 있을 때만 저장
          if (this.newTodoItem !== '') {
            //인풋 박스에 입력된 텍스트의 앞뒤 공백 문자열 제거
            var value = this.newTodoItem && this.newTodoItem.trim();
            localStorage.setItem(value, value);
            //인풋 박스의 입력 값을 초기화
            this.clearInput();
          }
        },
        clearInput() {
          this.newTodoItem = '';
        }
      }
    ```
  
    - addTodo() 메서드 안에서 `this`를 사용하면 해당 컴포넌트(여기서 App)를 가리킵니다. clearInput() 메서드는  App 컴포넌트에 정의되어 있으므로 addTodo() 에서 `this` 사용하며 clearInput() 메서드에 접근할 수 있다. data 속성에 정의의 newTodoItem을 addTodo()에서 ``this.newTodoItem` 으로 접근한 것과 같은 원리이다.
  
    > 디자일 패턴: 단일 책임 원칙
    >
    > 단일 책임 원칙이란 함수 하나가 하나의 기능만 담당하도록 설계하는 객체 지향 프로그래밍의 디자인 패턴입니다. clearInput()의 this.newTodoItem = "", 코드를 그냥 addTodo()에 넣고, 인풋 박스의 내용을 비우는 코드는 clearInput()에 넣었습니다. 만약 다른 메서드에서 인풋 박스의 내용을 비우는 코드가 필요할 경우 this.newTodoItem = ""; 코드 대신에 this.clearInput();을 호출하면 된다. 
  
  - 아이콘 이용해 직관적인 버튼 모양 만들기
  
    ```vue
    <template>
      <div class="inputBox shadow">
        <!-- v-on:keyup.enter: 인풋 박스에 enter를 눌렀을 때 동작하는 속성-->
        <input type="text" v-model="newTodoItem" placeholder='Type what you have to do' v-on:keyup.enter='addTodo'>
        <!--button 대신 클릭 이벤트를 받을 태그-->
        <span class='addContainer' v-on:click='addTodo'>
          <i class='addBtn fa fa-plus' aria-hidden='true'></i>
        </span>
      </div>
    </template>
    
    <style scoped>
    input:focus {
      outline: none;
    }
    .inputBox {
      background: white;
      height: 50px;
      line-height: 50px;
      border-radius: 5px;
    }
    
    .inputBox input {
      border-style: none;
      font-size: 0.9rem;
    }
    
    .addContainer {
      float: right;
      background: linear-gradient(to right, #6478fb, #8763fb);
      display: inline-block;
      width: 3rem;
      border-radius: 0 5px 5px 0;
    }
    
    .addBtn {
      color: white;
      vertical-align: middle;
    }
    </style>
    
    ```
  
  - 할 일 목록 만들기
  
    - 로컬 스토리지 데이터를 뷰 데이터에 저장 -> 뷰 데이터의 아이템 개수 만큼 리스트 아이템 표시
  
  - 로컬 스토리지 데이터를 뷰 데이터에 저장하기
  
    ```vue
    <script>
    export default {
      data() {
        return {
          todoItems: []
        };
      },
      created() {
        if (localStorage.length > 0) {
          //로컬 스토리지에는 저장된 모든 아이템을 한 번에 불러오는 API는 없기 때문에 반복문으로 아이템을 모두 불러와야 한다.
          for (var i = 0; i < localStorage.length; i++) {
            //push를 이용해 배열에 배열아이템을 추가한다.
            this.todoItems.push(localStorage.key(i));
          }
        }
      }
    };
    </script>
    ```
  
  - 뷰 데이터의 아이템 개수만큼 화면에 표시하기
  
    ```vue
    <template>
      <section>
        <ul>
          <li v-for="todo in todoItems">{{ todo }}</li>
        </ul>
      </section>
    </template>
    ```
  
  -  TodoList.vue에 할 일 삭제 기능 추가하기
  
    - 선택한 할 일을 뷰에서 인식 -> 선택한 할 일을 로컬 스토리지에서 삭제 -> 선택한 할 일을 뷰 데이터에서 삭제
    
    - 할 일 목록 & 삭제 마크업 작업하기
    
      ```vue
      <!--TodoList-->
      <template>
        <section>
          <ul>
            <li v-for="todo in todoItems" class="shadow">
              <i class="checkBtn fa fa-check" aria-hidden="true"></i>
              {{ todo }}
              <span class="removeBtn" type="button" @click="removeTodo(todoItem, index)">
                <i class="fa fa-trash-o" aria-hidden="true"></i>
              </span>
            </li>
          </ul>
        </section>
      </template>
    
    - style 작성
    
      ```vue
      <!--TodoList-->
      <style>
      ul {
        list-style-type: none;
        padding-left: 0px;
        margin-top: 0;
        text-align: left;
      }
      
      li {
        display: flex;
        min-height: 50px;
        height: 50px;
        line-height: 50px;
        margin: 0.6rem 0;
        padding: 0 2.3rem;
        background: white;
        border-radius: 10px;
      }
      
      .checkBtn {
        line-height: 50px;
        color: #62acde;
        margin-right: 5px;
      }
      
      .removeBtn {
        margin-left: auto;
        color: #de4343;
      }
      </style>
      ```
    
    - 할 일 삭제 버튼에 클릭 이벤트 추가하기
    
      ```vue
      <!--TodoList-->
      <span class="removeBtn" type="button" @click="removeTodo"></span>
      
      <script>
      	methods: {
          removeTOdo() {
            console.log('clicked');
          }
        }
      </script>
      ```
    
    - 선택한 할 일을 뷰에서 인식하도록 만들기
    
      - 아이콘을 클릭했을 때 선택한 할 일의 텍스트 값과 인덱스를 가져오는 코드를 추가한다. Template 코드와 removeTodo()코드를 수정하여 텍스트 값과 인덱스(목록에서 순서, 배열 인덱스와 동일)를 반환한다.
      - v-for 디렉티브에 index가 추가되었다. index는 임의로 정의한 변수가 아니라 v-for 디렉티브에서 기본적으로 제공하는 변수이다. 특정 할 일의 아이콘을 클릭하면 할 일의 텍스트 값과 인덱스 값이 콘솔에 표시된다.
    
      ```vue
      <!--TodoList-->
      <template>
        <section>
          <ul>
            <li v-for="(todoItem, index) in todoItems" :key="todoItem" class="shadow">
              <i class="checkBtn fa fa-check" aria-hidden="true"></i>
              {{ todoItem }}
              <span class="removeBtn" type="button" @click="removeTodo(todoItem, index)">
                <i class="fa fa-trash-o" aria-hidden="true"></i>
              </span>
            </li>
          </ul>
        </section>
      </template>
      ```
    
    - 선택한 할 일을 로컬 스토리지와 뷰 데이터에서 삭제하기
    
      - Splice()는 자바스크립트에 기본적으로 내장되어 있는 API이다. 배열의 특정 인덱스에서 부여한 숫자만큼 인덱스를 삭제한다
      - 로컬 스토리지의 데이터를 삭제하려면 `localStorage.removeItem()`과 배열의 특정 인덱스를 삭제하는 `this.배열.splice(인덱스, 삭제할 개수)`
    
      ```vue
      <!--TodoList-->
      methods: {
          removeTodo(todoItem, index) {
            localStorage.removeItem(todoItem);
            this.todoItems.splice(index, 1);
          }
        }
      ```
    
      - 제거하면 바로 뷰에서 자동으로 화면을 다시 갱신한다는 점이다. 이는 **데이터의 속성이 변하면 화면에 즉시 반영하는 뷰의 반응성 때문이다**. 
    
    - 모두 삭제하기 버튼을 포함하는 TodoFooter 컴포넌트
    
      - 모두 삭제하기 버튼 추가하기
        - 로컬 스토리지의 데이터를 모두 삭제하는 `localStorage.clear()`를 정의한다. 
    
      ```vue
      <!--TodoFooter-->
      <template>
        <div class="clearAllContainer">
          <span class="clearAllBtn" @click="clearTodo">Clear All</span>
        </div>
      </template>
      
      <script>
      export default {
        methods: {
          clearTodo() {
            localStorage.clear();
          }
        }
      };
      </script>
      
      <style scoped>
      .clearAllContainer {
        width: 8.5rem;
        height: 50px;
        line-height: 50px;
        background-color: white;
        border-radius: 10px;
        margin: 0 auto;
      }
      
      .clearAllBtn {
        color: #e20303;
        display: black;
      }
      </style>
      ```
    
    - 기존 애플리케이션 구조의 문제점 해결하기
    
      - 현재 애플리케이션의 구조의 문제점
    
        - 할 일을 입력했을 때 할 일 목록에 바로 반영되지 않는 점 
    
        - 할 일을 모두 삭제했을 때 할 일 목록에 바로 반영되지 않는 점
    
        - 종합해보면 4개의 영역으로 분리해 놓았기 때문에 한 영역의 처리 결과를 다른 영역에서 감지하지 못한다는 문제가 있다. 
    
          
    
      - 문제 해결을 위한 애플리케이션 구조 개선
    
        - 만약 모든 컴포넌트가 같은 데이터 속성을 조작한다면 최상위 컴포넌트인 App 컴포넌트에 todoitems라는 데이터를 정의하고, 하위 컴포넌트 TodoList에 props로 전달한다. 
          - 이전 구조 ( todoInput(삭제),  todoFooter(삭제) -> 로컬스토리지에 반영 -> 최신 데이터 미반영)
          - 개선된 구조(App에 todoItems를 정의하고 - 추가이벤트 및 삭제 이벤트를 받고 - 로컬스토리지에 보내주고 - todoList에 propsdata를 보내준다. 
    
      - props와 이벤트 전달을 이용해 할 일 입력 기능 개선하기
    
        ```vue
        export default {
        	<!--데이터 속성 todoItems 선언-->
          data() {
            return {
              todoItems: []
            };
          },
          methods: {
        	<!--로컬 스토리지에 데이터를 추가하는 로직-->
            addTodo() {
        
        }
          },
          components: {
            TodoHeader: TodoHeader,
            TodoInput: TodoInput,
            TodoList: TodoList,
            TodoFooter: TodoFooter
          }
        };
        </script>
        ```
    
      - App.vue 파일의 컴포넌트 태그에 props와 이벤트 전달을 위한 v-on 디렉티브 속성 추가
    
        ```vue
        <template>
          <div id="app">
            <TodoHeader></TodoHeader>
            <TodoInput v-on:add Todo="addTodo"></TodoInput>
            <TodoList v-bind:propsdata="todoItems"></TodoList>
            <TodoFooter></TodoFooter>
          </div>
        </template>
        ```
    
      - TodoInput 컴포넌트와 TodoList 컴포넌트 수정하기
    
        ```vue
        addTodo() {
              if (this.newTodoItem !== '') {
                var value = this.newTodoItem && this.newTodoItem.trim();
                localStorage.setItem(value, value);
        				<!-- 이벤트를 전달할 때 할 일 텍스트 값인 value 객체를 인자 값으로 전달했다-->
                this.$emit('addTodo', value);
                this.clearInput();
              }
            },
        ```
    
        

