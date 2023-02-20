`$router.push('이동위치')`: method를 등록하고 클릭시 해당 메소드를 호출하여 `$router`를 이동하는 방법, 현재 라우트를 변경 (`this.$router.push("place")`) URL 이동, 히스토리 스택에 추가되므로 뒤로가기 버튼 동작시 이전 URL로 이동

- 세션

  - 사용자가 브라우저를 닫아 서버와의 연결을 끝내는 시점

- 세션 스토리지

  - 웹페이지의 세션이 끝날 때 저장된 데이터가 지워진다
  - 브라우저에 같은 웹사이트를 여러 탭이나 창을 띄우면, 여러 개의 세션 스토리지의 데이터가 서로 격리되어 저장된다.
  - 데이터를 브라우저 상에서 저장한다

- 로컬 스토리지 

  - 웹페이지의 세션이 끝날 때 저장된 데이터가 지워지지 않는다.
  - 여러 탭이나 창 간에 데이터가 서로 공유되며 탭이나 창을 닫아도 데이터는 브라우저에 그대로 남아 있는다.
  - 이러한 영속성은 같은 브라우저 상에서만 가능하다.  
  - 데이터를 브라우저 상에서 저장한다

- 로컬 스토리지 사용하기

  ```js
  // 키에 데이터 쓰기
  localStorage.setItem("key", value)
  
  // 키로부터 데이터 읽기
  localStorage.getItem("key"),
   
  // 키의 데이터 삭제
  localStorage.removeItem("key")
  
  // 모든 키의 데이터 삭제
  localStorage.clear();
  
  // 저장된 키/값 쌍의 개수
  localStorage.length;
  ```

  - 웹 스토리지를 사용할 대 오직 문자형 데이터 타입만 지원한다
  - 그래서 JSON 형태로 데이터를 읽고 쓰는 것

  ```js
  localStorage.setItem('json', JSON.stringify({a: 1, b: 2}))
  JSON.parse(localStorage.getItem('json'))
  ```

- vuex-persistedstate

  - npm이고 vuex에 저장되는 값들을 사용하는 웹브라우저의 localstorage에 저장하며, 새로고침시 그 값이 있다면 localstorage의 값을 가져와 사용한다

    ```vue
    import createPersistedState from "vuex-persistedstate"
    
    export const store = new Vuex.Store({
    	plugins: [
    		createPersistedState({
    			paths: ["country", "place"],
    	}),
    ],
    })
    ```

  - State: 해당 파일에서 관리하는 상태값이다. State를 변경하기 위해서는 mutations 내부의 변수를 commit으로 실행시켜야 한다.

  - Mutation: state를 변경하기 위해 실행되는 것으로 비동기를 해야할 경우 action에서 실행하며, 그렇지 않을 경우 컴포넌트 내부 method에서 `commit(`변수`)`를 통해 실행 가능하다.

    > setCountry(context, country) {
    >
    > ​	context.commit("STORE_COUNTRY", country)
    >
    > }

  - Getters: 컴포넌트에서 store의 값을 가져올 때 어떠한 계산식 이후 가져오려할 때 사용한다. Computed 사이클에서 사용한다.

  - Action: state를 바꾸기 위해 사용되며 컴포넌트의 method에서 실행한다.

    - dispatch('함수명',  전달인자)

    `this.$store.dispatch("setCountry", text);`

  - mutations은 상태관리 자체가 한 데이터에 대해 여러 개의 컴포넌트가 관여하는 것을 효율적으로 관리하기 위함인데 Mutations에 비동기 처리 로직들이 포함되면 같은 값에 대해 여러 개의 컴포넌트에서 변경이 요청했을 때, 그 변경 순서 파악이 어렵기 때문다. 따라서 `setTimeout()`이나 서버와의 http 통신 처리 같이 결과를 받아올 타이밍이 예측되지 않은 로직은 Action에 선언한다. 

- Axios 사용

  - 전역으로 axios를 사용하기 위해서 `Vue.prototype.$axios`를 정의한다.

  - GET 

    - axios.get을 사용하여 서버의 데이터를 불러오는 것을 요청할 수 있다.
    - 첫 번째 parameter에는 axios에 전달할 서버의 url이 들어가게 된다. 두 번째 parameter에는 config 객체를 선택적으로 추가 전달을 할 수 있다.

    ```vue
    <script>
    
    export default {
      methods: {
        getData() {
          this.$axios..get(HOST + "/api/getData", {
              headers: { "X-AUTH-TOKEN": "인증 받음을 증명하는 토큰" },
            })
          .then((res) => {
            console.log(res.status);
            console.log(res.data);
          })
          .catch((error) => {
            console.log(error);
          })
          .finally(() => {
            console.log("마지막 실행")
          }) 
        }
      }
    }
    </script>
    ```

  - POST

    - axios.post를 사용하여 서버에 데이터에 입력을 할 수 있다. 첫 번째 parameter에는 axios에 전달할 서버의 url, 두 번째 parameter에는 입력할 데이터가 들어간다.

    ```js
    <script>
    const HOST = "";
    
    export default {
      methods: {
        postData() {
          let saveData = {};
          saveData.title = "axios POST request";
          saveData.index = 0;
    
          this.$axios
            .post(HOST + "/api/postData", JSON.stringify(saveData))
            .then((res) => {
              console.log(res.staus);
              console.log(res.data);
            })
            .catch((error) => {
              console.log(error);
            })
            .finally(() => {
              console.log("항상 마지막에 실행");
            });
        },
      },
    };
    </script>
    ```

  - PUT

    - 기존 데이터를 수정한다.
    - **첫 번째 parameter에는 axios에 전달할 서버의 url**, **두 번째 parameter에는 수정할 데이터가 들어간다**.

    ```vue
    <script>
    const HOST = "";
    
    export default {
      methods: {
        putData() {
          let number = "0";
          let updateData = {};
          updateData.title = "axios PUT request";
          updateData.index = 0;
    
          this.$axios
            .put(HOST + "/api/putData" + number, JSON.stringify(updateData))
            .then((res) => {
              console.log(res.staus);
              console.log(res.data);
            })
            .catch((error) => {
              console.log(error);
            })
            .finally(() => {
              console.log("항상 마지막에 실행");
            });
        },
      },
    };
    </script>
    ```

  - Delete

    - 첫 번째 파라미터에는 axios에 전달할 서버의 url이 들어간다. **보통 삭제할 경우 참고할 점은 url의 마지막에는 삭제할 객체를 구분할 수 있는 key가 들어간다.**

    ```vue
    <script>
    const HOST = "";
    
    export default {
      methods: {
        deleteData() {
          let deleteKey = "123";
          this.$axios
            .delete(HOST + "/api/deleteData" + deleteKey)
            .then((res) => {
              console.log(res.staus);
              console.log(res.data);
            })
            .catch((error) => {
              console.log(error);
            })
            .finally(() => {
              console.log("항상 마지막에 실행");
            });
        },
      },
    };
    </script>
    ```

  - Async/await

    - **기존의 axios는 처리 순서를 지정하지 않으면 request 요청을 보내고 나서 response 응답도 받기 전에 바로 다음 구문을 수행해 버리기 때문에 원하는 결과를 받아오지 못한다는 점이다. 그래서 async/await를 사용하여 처리 순서를 지정한다.**

    - **또한 오류 디버깅을 위해 try catch 구문을 사용해야 한다.**

  - Mixin

    - Mixin은 여러 컴포넌트 간에 공통으로 사용되고 있는 로직, 기능들을 재사용하는 방법을 의미한다
    - 코드의 재사용성을 위해 사용합니다. mixin은 상위 컴포넌트를 만들지 않고 단순히 공통 요소만 한 곳에 모아두는 것을 의미한다.

    ```vue
    import bus from '../utils/bus.js'
    
    export default {
    	created() {
    		bus.$emit('Start:spinner');
    		this.$store.dispatch('Fetch_list', this.$route.name)
    		.then(() => bus.$emit('end:spinner'))
    		.catch(err => console.log(err));
    }
    }
    ```

    ```vue
    <template>
        <list-item></list-item>
    </template>
    
    <script>
    import ListItem from '../components/ListItem.vue'
    import ListMixin from '../mixins/ListMixin.js';
    export default {
        components:{
            ListItem,
        },
        mixins: [ListMixin],
    }
    </script>
    ```

- vuex

  - 상태 관리를 위한 패턴이자 라이브러리이다. 

  - 컴포넌트 간의 통신이나 데이터 전달을 좀 더 유기적으로 관리할 필요성이 생긴다.

  - 여러 컴포넌트 간의 데이터 전달과 이벤트 통신을 한곳에서 관리하는 패턴을 의미한다.

  - 뷰의 컴포넌트 통신 방식인 props, event emit 때문에 중간에 거쳐할 컴포넌트가 많아지거나

  - 이를 피하기 위해 Event Bus를 사용하여 컴포넌트 간 데이터 흐름을 파악하기 어려운 것

  - 상태 관리 패턴

    - State: 컴포넌트 간에 공유할 data
    - view: 데이터가 표현될 template
    - Actions: 사용자의 입력에 따라 반응할 methods

  - 기존에 data 속성으로 선언한 값을 제거하고 

  - Child 컴포넌트로 값을 전달하지 않는다.

  -  그리고 **computed의 특징** 중 자잘한 몇가지는

    **호출할 때 괄호()를 사용할 필요가 없다**는것과, **파라미터를 받을수가 없다 라는 특징**을 가지고있다.

- 라우터 뒤로가기 

```vue
<template>
  <div class="nav">
    <div v-on:click="$router.go(-1)">
      <p>뒤로</p>
    </div>
    <img class="logo" src="../assets/logo.png" alt="" />
    <div>
      <p>더보기</p>
    </div>
  </div>
</template>
```

- 이미지 동적 데이터 바인딩

```vue
<img
  class="country__img"
  :src="require('@/assets/' + img + '.png')"
  alt=""
/>
```

- 동적 파일을 요구할 때 `require`을 사용해서 받을 수 있다.
- 클릭 함수를 정의한 태그를 확인하기 위해서는 `event.target`이 아닌 `event.currentTarget`을 사용해야 함

```js
// div 태그 안 p 태그의 text를 가져오기 위한 셀렉트
const text = event.currentTarget.querySelector("p").innerText;
console.log(text);
```

- API 노출하고 싶지 않을 때 환경변수를 사용

  - `npm i dotenv`, 최상위 root에서 `.env.local` 라는 파일이름으로 생성한다.그리고 `VUE_APP_<변수명>=<패스워드>` 의 공식으로 작성한다. 
  - 클릭하면 환경변수를 작동할 수 있게 vue 파일의 `<template>`에서 이렇게 작성한다

  ```vue
  <template>
    <div>
      <button @click="printLog">click me</button>
    </div>
  </template>
  <script>
  methods: {
      printLog() {
        console.log(process.env.VUE_APP_TEST_KEY);
      },
    },
  </script>
  ```

  `x-cors-api-key": process.env.VUE_APP_X_CORS_API_KEY,`로 사용하면 된다



- 복사하기 기능

  ```js
  import Vue from 'vue'
  import VueClipboard from 'vue-clipboard2'
  
  VueClipboard.config.autoSetContainer = true;
  Vue.use(VueClipboard)
  ```

- Methods

  ```js
  copyClipboard(event) {
    const text = event.currentTarget.parentElement.parentElement
      .querySelector(".result")
      .querySelector(".foreign__text").innerText;
  
    this.$copyText(text).then(() => {
      alert("복사 완료");
    });
  },
  ```

  

- payload

  - `state.place = payload`는 연결된 컴포넌트에서 넘겨주는 data값이다

  - payload는 상태 값을 변이시킬 때 사용할 수 있습니다.

    ```js
    STORE_TALKLIST(state, payload) {
          state.talkList = payload;
        },
    ```

    



- computed

  - 비동기적인 props를 전달받는 상황이라면 computed 속성을 사용한다. props가 객체가 아닌 기본값(불린, 숫자, 문자형, null, undefined)이면 반응형으로 잘 업데이트 되는데 만약 객체라면 computed를 사용해야한다.

  - 템플릿에서 사용할만한 복잡한 로직은 computed에서 사용하자(재사용성)

    ```vue
    <!--변경 전-->
    <div id="example">
      {{ message.split('').reverse().join('') }}
    </div>
    
    <!--변경 후-->
    <div id="example">
      {{ reversedMessage }}
    </div>
    <script>
    	var vm = new Vue({
      el: '#example',
      data: {
        message: 'Hello'
      },
      computed: {
        // 산출 getter 함수
        reversedMessage: function () {
          // `this`는 「vm」 인스턴스를 뜻한다
          return this.message.split('').reverse().join('')
        }
      }
    })
    </script>
    ```

  - Computed vs methods 

    - computed는 리액티브인 의존관계에 의해 캐쉬화 되어진다. `message`가 변하지 않는 한 `reversedMessage` 가 몇 번이고 불러져도 함수는 다시 실행되는 것이 아닌 이전에 계산되어진 결과를 즉시 돌려준다.
      - 캐싱을 사용하는 이유는 전에 계산되어 있던 결과를 그대로 반환되기 때문에 속도가 빠르다. 캐쉬를 사용해야 하는 경우에는 computed를 사용하자
    - 반면 `methods` 는 렌더링을 다시 할 때마다 항상 함수를 실행한다.

  - computed vs watch 차이점

    - watch가 필요한 경우가 있다
      - 데이터를 업데이트 할 때 비동기처리나 무거운 처리(많은 처리)를 실행하고 싶은 경우 편리하다.
      - 감시할 데이터를 지정하고 그 데이터가 바뀌면 선언한 함수를 실행하라는 방식으로 명령형 프로그래밍이다. but computed속성은 계산해야 하는 목표 데이터를 정의하는 방식으로 선언형 프로그래밍이다. 
        - 선언형 프로그래밍이 명령형 프로그래밍보다 코드 반복이 적은 등 우수하다고 평가하는 경향이 있다고 한다. 

    ```vue
    <script>
    export default {
      data: () => ({
        countrySelected: "",
        placeSelected: ""
      })
    }
    watch: {
        countrySelected(val) {
          //vuex의 상태변경이 감지되면 result에 값을 넣는다... 
          this.result = this.$store.dispatch("setCountryTalkList", val);
        },
        placeSelected(val) {
          this.result = this.$store.dispatch("setPlaceTalkList", val);
        },
      },
    };
    </script>
    ```

  - watch는 감시할 데이터를 지정하고 그 데이터가 바뀌면 어떠한 함수를 실행하라는 방식의 명령형 프로그래밍 방식이다.(실시간으로 값을 받아오는것)

    ```vue
    <script>
    	watch: {
        //firstName 바뀔 경우
        firstName: function(val){
          this.fullName=val+''+this.lastName
        },
        //lastName 바뀔 경우
        lastName: function(val){
          this.fullName=this.firstName+''+val
        }
      }
    </script>
    ```

    







`