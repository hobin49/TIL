#### 초기 세팅

- Vue/Vue CLI 설치

  `sudo npm install -g vue`

  `sudo npm install -g @vue/cli`

  - 만약에 설치가 되지 않을 경우 

    `sudo npm uninstall -g vue-cli` 삭제 후 다시 설치

- Vue version 체크

  `vue --version`

- Vue 프로젝트 생성하기

  `vue create 프로젝트 이름`

  - 많은 오픈소스를 활용하기 위해서 vue2로 설정한다.



- 앱을 처음 실행하면

  ```js
  import { createApp } from "vue";
  // 이름은 app이라는 것으로 쓸 것이다.
  import App from "./App.vue";
  
  // App.vue를 생성하겠다  #app =>index.html 여기에 Vue 객체에 컴포넌트 인스턴스(= 컴포넌트 객체)를 부착한다. 페이지 하나가지고 뷰 애플리케이션이 구동된다.
  createApp(App).mount("#app");
  ```

  - App.vue를 생성(app은 또 hello.vue를 import한다.) -> index.html에 있는 #app에 컴포넌트 인스턴스를 부착한다.
  - 뷰는 SPA(single webpage application)이라서 index.html 하나만 가진다.
  - 자바스크립트로 동적으로 작동하기 때문에 소스코드는 노출이 되지 않는다.
  - id app에서 계속 동적으로 변한다.

- manually selected 할때 고려할 부분들

  - 우리가 추가적으로 새로 만들어야한다. default로는 할게 없다.
  
  - 바벨은 우리가 ES6 짠 코드를 구 브라우저에서도 동작에서도 동작할 수 있도록 구 자바스크립트 코드로 변환해준다.
  
  - pwa (모바일처럼 웹을 구현)
  
  - 라우터
    - 만들면 웹페이에 메뉴 탭이 생긴다.
    - 마치 화면이 이동하는 것처럼 메뉴를 구성한다.
    
  - 뷰에서 메뉴를 구성하고 메뉴를 클릭했을 떄 화면 이동할 수 있게 

  - Vuex(store)

    - 모든 우리의 뷰 컴포넌트 내에 공통으로 접근 가능한 저장소를 만들어서 데이터를 저장하고 상태관리까지 할 수 있게

    - Lint

      - 자바스크립트 문법 체크용, 코딩 컨벤션 
  
      - eslint-standard로 설정해서 그거에 맞게 `.prettierrc`에서 재조정 해줘야한다.
  
        >{
        >
        >  "semi": false,
        >
        >  "bracketSpacing": true,
        >
        >  "singleQuote": true,
        >
        >  "useTabs": false,
        >
        >  "trailingComma": "none",
        >
        >  "printWidth": 80
        >
        >}
  
      - package.json에서 `rules`에  추가해준다.
  
        > "eslintConfig": {
        >
        > ​    "root": true,
        >
        > ​    "env": {
        >
        > ​      "node": true
        >
        > ​    },
        >
        > ​    "extends": [
        >
        > ​      "plugin:vue/vue3-essential",
        >
        > ​      "@vue/standard"
        >
        > ​    ],
        >
        > ​    "parserOptions": {
        >
        > ​      "parser": "@babel/eslint-parser"
        >
        > ​    },
        >
        > ​    "rules": {
        >
        > ​	//standard는 기본적으로 함수 정의시에 한 칸 띄는 것을 쓰지 않겠다.
        >
        > ​	//eslint-standard에서 나는 쓰지 않겠다.
        >
        > ​      "space-before-function-paren": "off"
        >
        > ​    	"eol-last" :"off"
        >
        > ​    }
        >
        > },
  
    - unit 테스팅
      - 작은 단위마다 테스팅
  
    - E2E 테스팅
      - 전체 테스팅

  - EsLint + Airbnb
  
    - 에어비엔비 팀에서 정한 코드 컨벤션
  
  - App.vue
  
    ```js
    <template>
      <nav>
        <router-link to="/">Home</router-link> |
        <router-link to="/about">About</router-link>
      </nav>
    	//정확히 탭 메뉴를 클릭하면 이 부분 태그가 교체가 되는것이다.
      <router-view/>
    </template>
    
    <style>
    #app {
      font-family: Avenir, Helvetica, Arial, sans-serif;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      text-align: center;
      color: #2c3e50;
    }
    
    nav {
      padding: 30px;
    }
    
    nav a {
      font-weight: bold;
      color: #2c3e50;
    }
    
    nav a.router-link-exact-active {
      color: #42b983;
    }
    </style>
    ```

    
  
  - router.js
  
    - App.vue에서 to 부분 == router에서 path부분, 즉 경로부분이 같아야한다.
  
    ```js
    import { createRouter, createWebHistory } from 'vue-router'
    import HomeView from '../views/HomeView.vue'
    
    const routes = [
      {
        path: '/',
        name: 'home',
        component: HomeView
      },
      {
        path: '/about',
        name: 'about',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
      }
    ]
    
    const router = createRouter({
      history: createWebHistory(process.env.BASE_URL),
      routes
    })
    
    export default router
    ```

    

    #### 라우터

    - 메뉴는 브라우저에 독립적인 url 접근 가능한 모든 페이지

    - name는 독립적인 값이 필요합니다

    - 컴포넌트는 실제로 path로 접근할 때 갖고와서 연결해줄 컴포넌트

    - `.vue` 는 컴포넌트라고 부른다
  
    - **라우터에 컴포넌트를 연결하는 방식 세 가지**
  
      - import해서 사용하는 방식
  
      ```vue
      import HomeView from '../views/HomeView.vue'
      
      const routes = [
        {
          path: '/',
          name: 'home',
          component: HomeView
        }
      ]
      ```
  
      - Lazy-loaded방식 나중에 추가되는 방식
  
      ```vue
      {
          path: '/about',
          name: 'about',
          // route level code-splitting
          // this generates a separate chunk (about.[hash].js) for this route
          // which is lazy-loaded when the route is visited.
          component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
        }
      ```
  
      - Lazy-loaded방식인데 Prefetch 방식
  
      ```vue
       {
          path: '/about',
          name: 'about',
          // route level code-splitting
          // this generates a separate chunk (about.[hash].js) for this route
          // which is lazy-loaded when the route is visited.
          component: () => import(/* webpackChunkName: "about", webpackPrefetch:true */ '../views/AboutView.vue')
        }
      ```

      

    - Chunk-vendors.js에는 우리가 설치한 참조하고 있는 외부 자바스크립트 라이브러리 스크립트 코드가 다 들어가게 된다.

    - app.js에는 라우터를 만들어준 애들이 들어간다
  
    - **`webpackPrefetch:true ` : 이걸 컴포넌트 안에 넣으면 당장 쓸거는 아닌데 미래에 사용될 가능성이 높은 리소스를 브라우저 캐시 안에 저장한다.**(라우터 설계에서 핵심)
  
      `<link rel="prefetch" as="script" href="/js/about.js"> ` 
  
      - as는 파일의 형태이다.
      
      - 프리패치를 하지 않으면 about.js를 about 버튼을 눌러야 서버로부터 받아온다. 사이즈가 작으면 문제가 되지 않는데 크면 사용자가 느리다고 느낄 수 있다. 
      
      - 그래서 프리패치를 쓰면 아무리 복잡하고 크더라도 사용자 입장에서 빨리 열리게 된다
      
      - 프리패치가 꼭 좋은건 아니다. 사용자가 메뉴를 사용하지 않고 서버로부터 받아와 브라우저에 캐시에 저장이 되는 시간이 꽤 걸린다. 라우터에 등록한 애들이 많으면 처음에 접속하는 순간에 시간이 오래걸린다. 
      
      - **1.접속할 확률이 높을 경우. 2. 사이즈가 너무 커서 미리 서버에서 받아오고 싶은 경우 프리패치를 설정한다. **
      
      - 그 반대인 경우에는 쓰지 않아도 된다.
      
        
    
    #### 데이터 바인딩
    
    - 재사용 가능한 컴포넌트(다른 곳에서도 사용)
    
    - 화면 전체를 차지하는 컴포넌트는 views 폴더
    
    - 재사용가능한 컴포넌트는 component 파일 안에 만든다
    
    - html에 작성할 떄 항상 상위 태그가 존재해야한다. 같은 레벨의 태그가 있으면 안 된다. 보통 `div`를 많이 사용한다. 루트태그라고도 불린다.
    
    - 단방향 데이터 바인딩(한 쪽 방향)- 자바스크립트에서 html태그로 한 방향으로 데이터 바인딩
    
      - data함수에서 작성된 애들만 자바스크립트 함수 혹은  html에서 사용할 수 있다.
    
      - key, value 형태로 작성하자.
    
      - 문자열 바인딩-단방향 데이터 바인딩
    
        ```vue
        <template>
         <div>
          <h1>Hello <span id="userName"></span>{{ userName }}</h1>
          <p>{{ message }}</p>
         </div>
        </template>
        
        <script>
        export default {
          data() {
            return {
              userName: 'John Doe',
              message: 'welcome 개발자의 품격',
              arr: [],
              obj: {}
            }
          }
        }
        </script>
        ```
    
      - 라우팅 추가
    
        ```js
        //만약 chunkname이 똑같으면 databinding.js 파일 하나로 합쳐지는 것이다.-그룹핑을 통해서
        //어떤 메뉴를 클릭하면 내려받는 과정 없이 바로 보여준다. 연관성 있는 애들을 같이 처리해준다.
        {
            path: '/databinding/string',
            name: 'DataBindingStringView',
            component: () => import(/* webpackChunkName: "databinding", webpackPrefetch:true */ '../views/1_databinding/DataBindingStringView.vue')
          }
        
        {
            path: '/databinding/html',
            name: 'DataBindingHtmlView',
            component: () => import(/* webpackChunkName: "databinding", webpackPrefetch:true */ '../views/1_databinding/DataBindingHtmlView.vue')
          }
        ```
    
      - 연관성이 있는 메뉴들은 webpack-chunk를 같이 만들어주면 효율적인 방법 중에 하나다.
    
      - 양방향 데이터 바인딩
    
        - 자바스크립트에서 정의한 데이터를 정의해도 화면에서 바로 반응이 되고 사용자가 어떤 값을 입력해도 자동으로 반응이 된다. 
    
      - Html 바인딩-단방향 데이터 바인딩
    
        ```vue
        <template>
          <div>
            <!--자바스크립 코드를 사용하기 위해서 추가되는 애들은 디렉티브라고 한다.-->
            <!--innerhtml로 여기안에 값을 넣어준다-->
            <div v-html="htmlString"></div>
          </div>
        
        </template>
        
        <script>
        export default {
          data() {
            return {
              htmlString: '<p style="color:red;">빨간색 문자</p>'
            }
          }
        }
        </script>
        
        <style>
        
        </style>
        ```
    
      - Input 바인딩 - 양방향 데이터 바인딩()
    
        ```vue
        <template>
          <div>
            <!--v-model은 data에 어떤 값이 들어가거나 들어오면 input type에 Value값으로 자동으로 바인딩 돼서 들어가게 된다 -->
            <input type='text' v-model='userId'/>
          </div>
        </template>
        
        <script>
        export default {
        
          data() {
            return {
              //사용자가 값을 입력하면 자바스크립트 값은(서로 연결되어 있다.)
              userId: ''
            }
          }
        }
        </script>
        
        <style>
        
        </style>
        ```
    
        - 사용자가 어떤 값을 입력했는지 변경했는지 자바스크립트를 작성하지 않아도 key값만 읽으면 된다.
    
        ```vue
        <template>
          <div>
            <!--v-model은 data에 어떤 값이 들어가거나 들어오면 input type에 Value값으로 자동으로 바인딩 돼서 들어가게 된다 -->
            <!--v-model이라는 directive를 이용해서 양방향으로 데이터를 연결할 데이터에 선언되어 있는 key를 넣어주면 서로 양방향으로 이미 연결된 것이다-->
            <input type='text' v-model='userId'/>
            <!--onclick-> @click 이벤트 발생시 그리고 파라미터로 넣어줄 값이 없어도 생략 가능하다.-->
            <button @click='myFunction'>클릭</button>
            <button @click='changeData'>변경</button>
          </div>
        </template>
        
        <script>
        export default {
        
          data() {
            return {
        
              userId: ''
            }
          },
          methods: {
            //데이터, 함수들의 메소드는 결국 나중에 vue에서 다루고 있는 vue.object 안에 등록이 된다. object 안에 있는 key 값을 접근할 때 this를 사용해야 한다.객체 안에서 특정 Key값을 접근할때는 this를 사용한다.
            myFunction() {
              console.log(this.userId)
            },
            changeData() {
              this.userId = "hobin"
            }
          }
        }
        
        </script>
        
        <style>
        
        </style>
        ```
    
        - 숫자형 바인딩(input)-양방향 데이터 바인딩
    
        ```vue
        <template>
          <div>
            <br>
            <input type="text /" v-model='num1'/>
            <input type="text /" v-model='num2'/>
            <!-- 아래처럼 입력하면 문자열 바인딩이니까 숫자를 더해도 원하는 값이 출력되지 않는다-->
            <span>{{ num1 + num2 }}</span>
            <br>
            <!-- 그래서 아래처럼 v-model.number 붙여서 작성하면 형변환 후에 값이 출력된다-->
            <input type="text /" v-model.number='num3'/>
            <input type="text /" v-model.number='num4'/>
            <span>{{ num3 + num4 }}</span>
          </div>
        </template>
        ```
    
        - select 바인딩-양방향 데이터 바인딩
    
        ```vue
        <template>
          <div>
            <select name='' id='' v-model='selectedCity'>
              <option value=""></option>
              <option value="02">서울</option>
              <option value="051">부산</option>
              <option value="064">제주</option>
            </select>
          </div>
        </template>
        
        <!-- input처럼 양방향이어서 사용자가 선택하면 data에 저장된다-->
        <script>
        export default {
          data() {
            return {
              selectedCity: '051'
            }
          }
        }
        </script>
        
        <style>
        
        </style>
        ```
    
        - Checkbox(양방향 데이터 바인딩)
    
        ```vue
        <template>
          <div>
            <div>
              <!--document 객체를 이용해서 접근하는 개념이 아니기 때문에 ID를 사용-->
              <input type="checkbox" name="" id="html" value='HTML' v-model='favoriteLang'>
              <!--label 태그랑 연결하기 위해서 id를 사용-->
              <label for='html'>HTML</label>
            </div>
            <div>
              <!--document 객체를 이용해서 접근하는 개념이 아니기 때문에 ID를 사용-->
              <input type="checkbox" name="" id="css" value='CSS' v-model='favoriteLang'>
              <!--label 태그랑 연결하기 위해서 id를 사용-->
              <label for='CSS'>CSS</label>
            </div>
            <div>
              <!--document 객체를 이용해서 접근하는 개념이 아니기 때문에 ID를 사용-->
              <input type="checkbox" name="" id="js" value='JS' v-model='favoriteLang'>
              <!--label 태그랑 연결하기 위해서 id를 사용-->
              <label for='js'>Javascript</label>
            </div>
            <div>선택한 지역: {{ favoriteLang }}</div>
          </div>
        
        </template>
        
        <script>
        export default {
          data() {
            return {
              //체크 박스는 여러개 선택할 수 있으니까 배열 형태로 선언하다.
              favoriteLang: []
            }
          }
        }
        </script>
        
        <style>
        
        </style>
        ```
    
        - checkbox의 경우에는 사용자가 체크를 해도 value값이 바뀌지 않는다 이전에 input, select와는 다르다. 
        - 여기서 v-model은 checked라는 속성과 연결되어 있다.
        - 체크 박스는 여러개를 선택할 수 있으니까 **반드시 배열 형태로** 선언한다.
    
        
    
        - 라디오(양방향 데이터)
    
        ```js
        <template>
          <div>
            <div>
              <!--document 객체를 이용해서 접근하는 개념이 아니기 때문에 ID를 사용-->
              <input type="radio" name="" id="html" value='HTML' v-model='favoriteLang'>
              <!--label 태그랑 연결하기 위해서 id를 사용-->
              <label for='html'>HTML</label>
            </div>
            <div>
              <!--document 객체를 이용해서 접근하는 개념이 아니기 때문에 ID를 사용-->
              <input type="radio" name="" id="css" value='CSS' v-model='favoriteLang'>
              <!--label 태그랑 연결하기 위해서 id를 사용-->
              <label for='CSS'>CSS</label>
            </div>
            <div>
              <!--document 객체를 이용해서 접근하는 개념이 아니기 때문에 ID를 사용-->
              <input type="radio" name="" id="js" value='JS' v-model='favoriteLang'>
              <!--label 태그랑 연결하기 위해서 id를 사용-->
              <label for='Js'>Javascript</label>
            </div>
            <div>선택한 지역: {{ favoriteLang }}</div>
          </div>
        
        </template>
        
        <script>
        export default {
          data() {
            return {
              //라디오는 하나만 선택할 수 있으니까 문자열로 받아준다.
              favoriteLang: ''
            }
          }
        }
        </script>
        
        <style>
        
        </style>
        ```
    
        - HTML 가지고 있는 다양한 속성을 바인딩
    
        ```vue
        <template>
          <div>
            <!--읽기 모드이니까 단방향만 데이터 바인딩이니까 v-bind를 사용해서 값을 지정해준다-->
            <input type="text" v-bind:value='userId' readonly />
            <!-- 위랑 똑같은 의미-->
            <input type="text" :value='userId' readonly />
            <br>
            <!-- 이미지도 데이터 바인딩 가능-->
            <img src="imgSrc" alt="" style="width:100px; height:auto;">
            <br>
            <!-- 양방향 데이터 바인딩 -->
            <input type='search' name='' id='' v-model='txt1'>
            <!-- 아무것도 입력되지 않은 상태면 비활성화 처리-->
            <button :disabled="txt1 === '' ">조회</button>
          </div>
        
        </template>
        
        <script>
        export default {
          data() {
            return {
              userId: 'hobin'
              imgSrc: 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Vue.js_Logo_2.svg/1200px-Vue.js_Logo_2.svg.png',
              txt1: ''
            }
          }
        }
        </script>
        
        <style>
        
        </style>
        ```
    
        
    
        - List (데이터 바인딩)
        
        ```vue
        <template>
          <div>
            <div>
              <select name="" id="" >
                <!--아무것도 선택 안 한것을 옵션으로 넣고 싶다면-->
                <option value=""></option>
                  <!-- 반복문 돌리고 싶을때 v-for-->
                  <!--v-for을 사용시에는 반드시 key를 데이터 바인딩 되어야 한다. key는 항상 유일한 값이 와야 한다. -->
                <option :value="city.code" :key="city.code" v-for='city in cities'>{{ city.title}}</option>
              </select>
            </div>
          </div>
        
        </template>
        
        <script>
        export default {
          data() {
            return {
              cities: [
                { title: '서울', code: '02' },
                { title: '부산', code: '051' },
                { title: '제주', code: '064' }
              ]
            }
          }
        }
        </script>
        
        <style>
        
        </style>
        ```
        
        -  테이블 바인딩(마땅한 key값이 마땅하지 않는 경우)
        
        ```vue
        <div>
              <table>
                <thead>
                  <tr>
                    <th>제품번호</th>
                    <th>제품명</th>
                    <th>가격</th>
                    <th>주문수량</th>
                    <th>합계</th>
                  </tr>
                </thead>
                <!--만약 마땅한 key값이 존재하지 않으면 인덱스를 넣는다.-->
                  <tr :key='idx' v-for='(drink,idx) in drinkList'></tr>
                </tbody>
              </table>
            </div>
        ```
        
        - 테이블 바인딩(key 값이 마땅한 경우)
        
        ```vue
        			<tbody>
                  <tr :key= 'drink.drinkId' v-for='drink in drinkList'>
                    <td>{{ drink.drinkId }}</td>
                    <td>{{ drink.drinkName }}</td>
                    <td>{{ drink.price }}</td>
                    <!--주문 수량은 사용자가 바꿀 수 있게끔 처리한다.(양방향 데이터 바인딩)-->
                    <td><input type='number' name='' id='' v-model='drink.qty'></td>
                    <!--자동 계산한 값이 출력 되도록-->
                    <td>{{ drink.price * drink.qty }}</td>
                  </tr>
                </tbody>
              </table>
            </div>
        
          </div>
        
        </template>
        
        <script>
        export default {
          data() {
            return {
        
        
              drinkList: [
                {
                  drinkId: '1',
                  drinkName: '코카롤라',
                  price: 700,
                  qty: 1
                },
                {
                  drinkId: '2',
                  drinkName: '오렌지주스',
                  price: 1200,
                  qty: 1
                },
                {
                  drinkId: '3',
                  drinkName: '커피',
                  price: 900,
                  qty: 2
                },
                {
                  drinkId: '4',
                  drinkName: '포카리',
                  price: 1100,
                  qty: 3
                }
              ]
            }
          }
        }
        </script>
        
        <style>
        
        </style>
        ```
        
        - 클래스바인딩
        
        ```vue
        <template>
          <div>
            <!-- class{class이름: value(true or false) }-->
            <!-- 클래스가 한 단어로 이루어져 있다면 single quote를 빼도 된다-->
            <!-- 사용자의 action에 따라서 클래스를 넣다뺐다 해야하니까 object를 만들어서 true/false로 제어한다.-->
            <div :class="{'text-red': hasError, active: isActive}">클래스 바인딩</div>
            <!-- 배열로 나타낸다. 잘 쓰지 않는다.-->
            <div :class="class2">클래스 바인딩2</div>
          </div>
        </template>
        
        <script>
        export default {
          data() {
            return {
              isActive: false,
              hasError: true,
              class2: ['active', 'hasError']
            }
          }
        }
        </script>
        
        <style scoped>
          .active {
            background-color: greenyellow;
            font-weight: bold;
          }
          .text-red {
            color:red;
          }
        </style>
        ```
        
        - 스타일 바인딩하기
        
        ```vue
        <template>
          <div>
            <!--style object 바인딩-->
            <div :style="style1">스타일 바인딩: 글씨는 green, 폰트크기:30px</div>
            <!-- object로 접근해서 값을 바꿔주기-->
            <button @click="style1.color='blue'">색상바꾸기</button>
          </div>
        
        </template>
        
        <script>
        export default {
          data() {
            return {
              //style은 무조건 object 형태로 선언하고
              style1: {
                color: 'green',
                fontSize: '30px'
              }
            }
          }
        }
        </script>
        
        <style>
        
        </style
        ```
        
        #### 이벤트
        
        - 가장 많이 쓰이는 곳 (Input type-chckbox, input type-radio, selectbox)
        
        - change event
        
          ```js
          <template>
            <div>
              <!--change 이벤트 통해서 함수를 구현한다.-->
            	<!-- change이벤트를 가지고 만들어야 가독성이 좋다--> 
              <select name="" id="" @change='changeCity' v-model='selectedCity'>
                <option value="">==도시선택==</option>
                <!--속성 바인딩-->
                <option :value="city.code" :key='city.code' v-for='city in cityList'>{{ city.title }}</option>
              </select>
              <select name="" id="">
                <option :value="dong.dongcode" :key="dong.dogncode" v-for='dong in selectedDongList'>{{ dong.dongTitle }}</option>
              </select>
          
              <!--템플릿 안에서 직접 fillter 함수 사용해서 적용하기-->
              <select name="" id="">
                <option :value="dong.dongcode" :key="dong.dogncode" v-for='dong in dongList.filter(dong => dong.cityCode === selectedCity)'>{{ dong.dongTitle }}</option>
              </select>
            </div>
          </template>
          
          <script>
          export default {
            data() {
              return {
                selectedCity: '',
                cityList: [
                  { code: '02', title: '서울' },
                  { code: '051', title: '부산' },
                  { code: '064', title: '제주' }
                ],
                dongList: [
                  { cityCode: '02', dongCode: '1', dongTitle: '서울 1동' },
                  { cityCode: '02', dongCode: '2', dongTitle: '서울 2동' },
                  { cityCode: '02', dongCode: '3', dongTitle: '서울 3동' },
                  { cityCode: '02', dongCode: '4', dongTitle: '서울 4동' },
                  { cityCode: '051', dongCode: '1', dongTitle: '부산 1동' },
                  { cityCode: '051', dongCode: '2', dongTitle: '부산 2동' },
                  { cityCode: '051', dongCode: '3', dongTitle: '부산 3동' },
                  { cityCode: '064', dongCode: '1', dongTitle: '제주 1동' },
                  { cityCode: '064', dongCode: '2', dongTitle: '제주 2동' }
                ],
                selectedDongList: []
              }
            },
          
            methods: {
              changeCity() {
                this.selectedDongList = this.dongList.filter(dong => dong.cityCode === this.selectedCity)
              }
            }
          }
          </script>
          
          <style>
          
          </style>
          ```
        
          - `v-on:change` == `@:change` 같다. 
        
          - 만약 함수를 호출하면서 이벤트를 전달하고 싶다면
        
            `v-on:change($event)` : 달러 + 이벤트 이름
        
            - 받을 때는 이름 바꿔도 된다.
        
          - key event
        
          ```js
          <template>
            <!-- <input type="search" name="" id="" @keyup='checkEnter($event)' v-model='searchText'> -->
            <input type="search" name="" id="" @keyup.enter='doSearch' v-model='searchText'>
            <button @click="doSearch">조회</button>
            <button type='submit' @click.prevent='dosearch'></button>
          </template>
          
          <script>
          // .enter
          // .tab
          // .delete
          // .esc
          // .space
          // .up
          // .down
          // .left
          // .right
          // .stop - event.stopPropagation()
          // .prevent - event.preventDefault()
          export default {
            data() {
              return {
                searchText: ''
              }
            },
            methods: {
              doSearch() {
                console.log(this.searchText)
              },
              checkEnter(event) {
                if (event.keyCode === 13) {
                  this.doSearch()
                }
              }
            }
          }
          </script>
          
          <style>
          
          </style>
          ```
        
          



​								







​		     



​			

​					

