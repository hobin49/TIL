### 오류 정리

- 2/21
  
  - ESLint(Prettie)r에서는 `<style>`태그는 스타일을 지정하게 되면 콜론 뒤에 항상 space를 띄어야한다.
  
  - Figma export하는 법 
    - 두 개의 레이어를 한 개로 export하고 싶다면 group selection을 하면 된다.
    - 그리고 `.png`로 export해야 뒷배경 색깔이 먹힌다. 
  
  - Vue 파트
  
    - 이미지 바인딩
  
      ```vue
      <template>
        <div>
          <!--절대경로로 사용하고 require을 해서 이미지를 import 한다 파일 이름을 변수화 처리한다-->
           <img :src="require(`@/assets/${imgName1}.png`)" class="left-img" />
           <img :src="require(`@/assets/${imgName2}.png`)" class="right-img" />
        </div>
      </template>
      <script>
      	export default {
        data() {
          return {
            message: "",
            imgName1: "smile3",
            imgName2: "smile2",
          };
        },
      };
      </script>
      
      ```
  
    - 버튼 비활성화
  
      ```vue
      <template>
        <div>
          <button :disabled="isDisabled" class="btn btn-start">시작하기</button>
        </div>
      </template>
      <script>
      	export default {
        computed: {
          isDisabled() {
            return true;
          },
        },
      };
      </script>
      ```
  
      
  
  - CSS 파트
  
    - 문서 상에 요소를 배치하는 방법(position)
  
      - 자기보다 상위 태그에 `position: relative` 를 한 후에(**relative는 자기 자신의 원래 위치를 기준으로 배치**) 자기 자신에 `position: absolute`를 하면 된다. **absolute는 가장 가까운 위치에 있는 조상 요소를 기준으로 배치한다**
  
    - 이미지랑 글씨를 같은 선상에 배치하기
  
      ```html
      <!--div로 하나 묶는다-->
      <div>
        <span class="header">SM</span>
        <img :src="require(`@/assets/${imgName3}.png`)" class="title-img" />
        <span class="header">E</span>
      </div>
      ```
  
      ```css
      </*header의 font-size에 맞게 타이틀 img 높이랑 너비를 지정한다 */> 
      .header {
        color: #f59607;
        font-size: 2.5rem;
        margin-top: 0.67rem 0 0.67rem 0;
        font-weight: bold;
      }
      
      .title-img {
        margin-top: 5px;
        padding-left: 1px;
        width: 30px;
        height: 30px;
      }
      ```
  
    - 이미지 position 때문에  빈 공간을 채우기 
  
      ```html
      <!--2개의 div를 하나로 묶고 class를 준다-->
      <div class="slider">
         	<div class="main_content">
            <h3>
              주변 사람들의<br />
              <span class="orange">MBTI</span>를 저장해<br />한 눈에 확인하세요!
            </h3>
          </div>
          <div>
             <img :src="require(`@/assets/${imgName1}.png`)" class="left-img" />
             <img :src="require(`@/assets/${imgName2}.png`)" class="right-img" />
           </div>
      </div>
      ```
  
      ```css
      </*높이지정을 하면 공간이 생긴다*/>
      .slider {
        height: 600px;
      }
      ```
  
    - **em의 경우 실제 몇 px로 변환될지에 영향을 주는 변수가 많아지기 때문에, em을 사용해서 스타일된 요소의 경우 재사용이 어렵고 유지보수가 힘들어지는 경향이 있기 때문이다**
  
    



- 2/23

  - css 오류

    - h3에는 margin이 들어가 있어서 밑으로 움직이려면 margin을 제거하고 padding을 줘야한다.

  - vue 오류

    - 이미지 바인딩 할 때 이미지가 상황에 따라서 변하는 데이터가 아니라면 데이터에 값을 안 넣어도 된다.

      ```vue
      <!-- 변경 전-->
      <template>
      	<img :src="require(`@/assets/${img1}.png`)" class="left-img" />
      </template>
      <script>
        export default {
          data() {
            return {
              img1: "smile";
            }
          }
        }
        }
      </script>
      
      <!-- 변경 후 -->
      <template>
      	<img :src="require(`@/assets/first_smile7.png`)" class="left-img" />
      </template>
      ```

    - swiper 설치 오류

      - Vue-awesome-swiper 라이브러리를 사용하기 위해 설치 시도를 했지만 실패했다. 찾아보니 vue3에는 지원하지 않는다. 그래서 공식 사이트에 있는 `import { Swiper, SwiperSlide } from 'swiper/vue'` 사용
      - Swiper.css를 사용하기 위해 import 했지만 **Module not found: Can't resolve 'swiper/css** 에러 발생
        - 해결 방법: swiper 버전을 6버전으로 다운그레이드 하거나 아니면 `import swiper/swiper-bundle.min.css`(압축형태) 이나 `import swiper-bundle.css`사용한다.

      
    
    - swiper slide 기본 틀 
    
      ```vue
      <template>
      	<swiper
         :modules="modules"
      	<!--한 장씩 넘기자-->
         :slides-per-view="1"
      		<!-- 페이지네이션 컬러-->
         :style="{
         	'--swiper-pagination-color': '#f59607',        
         }"
      		<!--움직이는 speed-->
         :speed="1200"
      		<!--슬라이드 사이 여백-->
         :space-between="50"
      		<!-- pagination 클릭할 수 있게 처리 버튼 클릭 여부-->
         :pagination="{ clickable: true }"
         @swiper="onSiper"
         @slideChange="onSlideChange"
        >
        <swiper-slide>1</swiper-slide>
        <swiper-slide>2</swiper-slide>
        <swiper-slide>3</swiper-slide>
      </template>
      <script>
        import { Swiper, SwiperSlide } from "swiper/vue"
        import { Pagination } from "swiper";
        import "swiper/swiper-bundle.min.css"
        
        
        export default {
          components:{
            Swiper,
            SwiperSlide,
          },
          setup() {
            const onSwiper = (swiper) => {
              console.log(swiper);
            };
            const onSlideChange = () => {
              console.log("slide");
            };
            return {
              onSwiper,
              onSlidechange,
              modules: [Pagination],
            }
          }
        }
      </script>
      ```
    
      - `npm i swiper` 를 통해서 swiper을 설치한다.
    
      - [swiper 기본 설명](https://swiperjs.com/vue) 여기를 참고하자 
    
        
    
        
  
- 2/24

  -  css

    - 모달 버튼 눌렀을 시에 뜨게 하는 방법

      ```vue
      <template>
      	 <div class="add-tab">
              <h3 class="left-name">그룹</h3>
           		<!--모달 클릭시 메서드 실행 -->
              <button class="right-tab" @click="modalclick()">
                <img :src="require(`@/assets/plus.png`)" class="right-tab-img" />
              </button>
            </div>
      			<!-- true일때만 보일 수 있게-->
            <div class="black-bg box-sizing" v-if="modal == true">
                    <div class="radio-button-control">
                      <input
                        type="radio"
                        :model="radioValues"
                        value="MBTI 정보 추가"
                        class="radio-button"
                      />
                     <label for="MBTI 정보 추가" class="radio-name">MBTI 정보 추가</label>
                   </div>
                 </div>
             </div>
      </template>
      <script>
      export default {
        data() {
          return {
            //기본값은 false로 처리
            modal: false,
          };
        },
        methods: {
          modalclick() {
            <!--버튼을 클릭하면 true로 처리-->
            this.modal = true;
          },
        },
      };
      </script>
      <style scoped>
        .black-bg {
        width: 100vw;
        </* 높이랑 너비 설정할때는 vh, vw를 사용하면 편하다*/>  
        height: 100vh;
        background: rgba(0, 0, 0, 0.5);
         </* 모달 창은 absolute 처리해야지 나중에 우리가 원할때 띄울 수 있다.*/>
        position: absolute;
        top: 0;
        left: 0;
        padding: 20px;
      }
      
      .white-bg {
        width: 90vw;
        background: white;
        position: absolute;
        bottom: 20px;
        border-radius: 15px;
        padding: 20px;
        height: 150px;
      }
      </style>
      ```
  
    - 라디오 버튼 키웠을 시에 오른쪽 텍스트랑 줄 높이 맞추는 법
  
      ```vue
      <style scoped>
      .radio-button-control {
        display: flex;
        justify-content: left;
        margin: 10px 0 5px 0;
        </* vertical-align:middle이 아니고 align-items:center를 해서 정렬해준다 */>
        align-items: center;
      }
      </style>
      ```
  
    - input placeholder의 위치를 조정하는 법
  
      `text-indent`를 사용해서 들여쓰기를 사용하면 된다.



- 3/2 오류 정리

  - 버튼 클릭 시 해당 라우터 경로로 이동하기 

    ```vue
    <template>
    	<div class="dropbox">
          <button class="btn-more" @click="pageLink">더보기</button>
       </div>
    </template>
    <script>
    export default {
      methods : {
        pageLink() {
          this.$router.push( { path: "messagebox"})
        }
      }
    }
    </script>
    ```

- 3/8 오류 정리

  - 추가 버튼 누를 시 새로운 텍스트와 값을 보여주기

    ```vue
    <template>
    	<div>
        <button class="plus-btn" @click="changeName()">
           <img :src="require(`@/assets/plus.png`)" class="plus" />
        </button>
      </div>
    </template>
    <script>
    changeName() {
         this.content = "";
         this.title = this.mbti;
         this.isShow = true;
       },
    </script>
    ```

  - 값을 삭제하기

    ```vue
    <template>
    	<div class="mbti-cancel">
          <h3 class="mbti-title">{{ title }}</h3>
         	<button v-show="isShow" class="btn-cancel" @click="remove()">
           <img :src="require(`@/assets/close.png`)" class="close" />
         </button>
      </div>
    </template>
    <script>
    	remove() {
          if (confirm("삭제하시겠습니까?")) {
            for (let i in this.mbti_complete) {
              if (this.mbti_complete[i].id === this.mbti) {
                this.mbti_complete.splice(i, 1);
                break;
              }
            }
            localStorage.setItem("memos", JSON.stringify(this.memos));
         }
       },
    </script>
    ```
    
    

- 3/9 오류 정리

  - 첫 번째 문제

    - 글쓰기를 할 때 똑같은 중복 mbti를 임시저장 할 수 없게 고유의 4개의 서로 다른 mbti만 선택할 수 있게 처리하는 문제가 있었다 

  - 해결

    - 기존에 내가 값을 넣을때 배열을 사용했는데 객체로 바꿔서 처리했다. 그렇게 되면 같은 mbti에 글을 쓰게 되면 value 값에 계속 갱신이 된다. 
    - 이전 배열을 이용할때는 각각 `,` 를 기준으로 두 개의 값을 넣어주게 처리했었는데 객체를 사용하게 되면 key에는 mbti 값을 그리고 value에는 해당 내용을 한 번에 삽입할 수 있다. 

     

  - 기존 코드

    ```vue
    <script>
    export default {
      methods: {
        tempSave() {
          if (this.mbti_complete.length < 4) {
            this.mbti_complete.push({ id: `${this.mbti}`, content: this.content });
          } else {
            alert("4개 이상 만들 수 없습니다");
          }
        },
    
        remove() {
          if (confirm("삭제하시겠습니까?")) {
            for (let i in this.mbti_complete) {
              if (this.mbti_complete[i].id === this.mbti) {
                this.mbti_complete.splice(i, 1);
                break;
              }
            }
            localStorage.setItem("memos", JSON.stringify(this.memos));
          }
        },
      }
    }
    </script>
    ```

  - 새로운 코드

    ```vue
    <script>
    export default {
      methods: {
         tempSave() {
          if (Object.keys(this.mbti_complete).length < 4) {
            this.mbti_complete[this.mbti] = this.content;
          } else {
            alert("4개 이상 만들 수 없습니다");
          }
        },
    
        remove() {
          if (confirm("삭제하시겠습니까?")) {
            for (const key in this.mbti_complete) {
              if (`${key}` === this.mbti) {
                delete this.mbti_complete[key];
                this.title = "";
                this.content = "";
                this.isShow = false;
              }
            }
          }
        },
        call_btn(mbti) {
          for (const [key, value] of Object.entries(this.mbti_complete)) {
            console.log(value);
            if (key === mbti) {
              this.title = key;
              this.content = this.mbti_complete[key];
              this.isShow = true;
              this.mbti = key;
            }
          }
        },
      },
    };
    </script>
    ```

  - 두 번째 문제

    - 랜덤 질문을 하고 선택된 mbti들의 답변을 보기 위해서 mbti를 선택했을 때 다른 페이지로 이동할 시에 선택된 값의 데이터를 다른 컴포넌트에서 액세스 할 수 있게 처리

  - 해결

    - Vuex 상태관리를 통해서 다른 컴포넌트에서도 데이터를 액세스 할 수 있게 처리했다.

    ```js
    <!--store.js-->
    import { createStore } from "vuex";
    
    export default createStore({
      state: {
        selectMBTI: "",
        total_mbti: "",
      },
    });
    ```

    ```vue
    <!--randomQuestion.vue-->
    <script>
    export default {
      methods: {
        selectEIOption(option) {
          this.mbti1 = option;
          this.totalMbti += this.mbti1;
          this.$store.state.totalMbti = this.totalMbti;
        },
        selectNSOption(option) {
          this.mbti2 = option;
          this.totalMbti += this.mbti2;
          this.$store.state.totalMbti = this.totalMbti;
        },
        selectTFOption(option) {
          this.mbti3 = option;
          this.totalMbti += this.mbti3;
          this.$store.state.totalMbti = this.totalMbti;
        },
        selectPJOption(option) {
          this.mbti4 = option;
          this.totalMbti += this.mbti4;
          this.$store.state.totalMbti = this.totalMbti;
        },
      },
    }
    </script>
    ```

    ```vue
    <!--randomAnser.vue-->
    <template>
    	<div>
      	<h2>{{ $store.state.totalMbti }}들의 답변</h2>
      </div>
    </template>
    ```

- 3/13 오류 정리

  - 문제

    - 첫 화면 페이지에 Swiper-slide를 활용해서 화면을 구성했다. 총 4개의 페이지가 존재하는데 한 개의 시작하기 버튼이 존재하는데 마지막 페이지에서만 버튼 활성화 처리와 라우터 주소로 이동할 수 있게 처리를 하고 싶었다.

  - 해결 

    - 버튼 활성화 처리
  
      - 버튼을 활성화하기 위해서 `ref`(변수를 반응성 데이터로 만들어 데이터의 변경을 추적하고 이를 뷰에 반영하기 위한 역할)을 활용했고, `swiper.activeIndex`를 활용해서 현재 페이지의 위치를 받아오게끔 처리했습니다. 
      - 클래스 바인딩을 통해서 초기에 버튼을 `disabled` 처리를 하고 만약에 현재 페이지가 마지막 페이지라면 disabled를 true처리를 해줬습니다.

       

    - 마지막 페이지에서만 라우터 주소로 이동할 수 있게 
      - 만약에 현재 페이지가 마지막 페이지라면 `this.$router.push` 를 활용해서 라우터 주소로 이동할 수 있게 처리했다.
  
    ```vue
    <template>
        <button
          class="btn btn-start"
          @click="lastBtn()"
          :class="{ disabled: isDisabled }"
        >
          시작하기
        </button>
      </div>
    </template>
    <script>
    // Import Swiper Vue.js components
    import { Swiper, SwiperSlide } from "swiper/vue";
    import { Pagination } from "swiper";
    import "swiper/swiper-bundle.min.css";
    import { ref } from "vue";
    
    export default {
      components: {
        Swiper,
        SwiperSlide,
      },
      data() {
        return {
          currentIndex: 0,
        };
      },
      setup() {
        let currentSlide = ref(0);
        let isDisabled = ref(false);
        const onSwiper = (swiper) => {
          console.log(swiper);
        };
        const onSlideChange = (swiper) => {
          currentSlide.value = swiper.activeIndex + 1;
          if (currentSlide.value === 4) {
            isDisabled.value = true;
          } else {
            isDisabled.value = false;
          }
        };
        return {
          onSwiper,
          onSlideChange,
          currentSlide,
          modules: [Pagination],
          isDisabled,
        };
      },
      methods: {
        lastBtn() {
          if (this.currentSlide === 4) {
            this.$router.push({ path: "login" });
          }
        },
      },
    };
    </script>
    ```
  
- 3/14 오류 정리

  - 큰 문제

    - 그룹 추가페이지에서 하나의 컴포넌트를 재사용해서 그룹 추가 버튼과 그룹 수정 버튼이 하나의 UI에서 이뤄질 수 있게 처리해야 했습니다.	

  - 작은 문제

    - 1.수정 버튼을 누르면 추가 버튼이 동작하는 문제
  
    - 해결 방법
  
      - 현재 버튼이 추가버튼이라면 추가할 수 있게 로직을 바꿨고 그리고 정보를 담을 때 배열을 사용하지 않고 객체를 사용해서 중복된 key의 값에 다른 값이 저장되는 것을 방지했다. 
  
      ```vue
      <script>
      export default {
        data() {};
        methods: {
        	registerBtn() {
            if (this.button === "추가") {
              this.content = this.groupId;
              this.groups[this.keys] = this.content;
              this.keys++;
            }
          },
      	}
      }
      </script>
      ```
  
    - 2.수정 버튼을 누르면 값이 수정되지 않는 문제 
  
    - 해결 방법
  
      - 해당 그룹의 수정버튼을 누르면 그 그룹의 key값을 받아와야 하는데 그러지 못한 상황이었습니다. 따라서 해당 key값을 받아오기 위해서 template에서 해당함수에 argument를 넣어주고 이에 methods에서 파라미터로 key를 받아왔습니다. 
      - 그리고 객체를 돌면서 해당 객체의 key값과 일치하는 값이 있으면 해당 key값의 value를 불러오게 처리했습니다.
      - 불러오기까지 됐는데 수정이 되지 않아서 또 다른 함수를 만들어서 현재 입력된 내용이 저장될 수 있게 처리를 했습니다.
  
      ```vue
      <template>
        <div>
            <div class="group-name" v-for="(item, value) in groups" :key="value">
              <span class="name">{{ item }}</span>
              <div>
                <div class="add-delete-img">
                  <button class="fix-btn" @click="fixBtn(value)">
                    <img :src="require(`@/assets/pencil.png`)" class="pencil" />
                  </button>
                  <button class="delete-btn" @click="removeBtn(value)">
                    <img :src="require(`@/assets/trashcan.png`)" class="trashcan" />
                  </button>
                </div>
              </div>
            </div>
            <div class="btn-control">
                <button class="add-btn" @click="registerBtn(), saveBtn()">
                  {{ button }}
                </button>
                <button class="cancel-btn" @click="pageLink()">취소</button>
              </div>
         </div>
      </template>
      <script>
      	data() {};
        fixBtn(number) {
            this.button = "수정";
            this.category = "그룹 및 수정";
            this.prevKey = number;
            for (const [key, value] of Object.entries(this.groups)) {
              console.log(value);
              if (key === this.prevKey) {
                this.groupId = this.groups[key];
              }
            }
          },
        saveBtn() {
            if (this.button === "수정") {
              this.groups[this.prevKey] = this.groupId;
            }
          },    
      </script>

​				

- computed 속성

  - 일반 methods이랑 비슷하지만 Vue 인스턴스 데이터를 기반으로 자동으로 계산되는 의존적인 속성 즉 값이 변경되지 않으면 이전에 값들을 저장해 놓은것을 불러오기 때문에 계산 비용이 큰 작업을 수행할 때 성능 향상에 도움이 되고, 참조하는 데이터가 변경될 때만 속성이 다시 계산 된다. 반면에 methods는 캐싱되지 않고 매번 계속 계산하면서 호출하기 때문에 성능이 저하되는 문제가 발생한다.  

  ```vue
  <template>
  	<template>
    <div>
      <input v-model="firstName" type="text">
      <input v-model="lastName" type="text">
      <p>{{ fullName }}</p>
    </div>
  </template>
  <script>
  	<script>
  export default {
    data() {
      return {
        firstName: '',
        lastName: ''
      }
    },
    computed: {
      fullName() {
        return `${this.firstName} ${this.lastName}`
      }
    }
  }
  </script>
  ```

  

- watch 속성

  - 데이터의 변화를 감지하고 이에 대한 반응을 정의하는 방법이다. 특정 테이터를 감시하다가 데이터가 변경될 때 콜백 함수(이벤트 핸들러나 비동기 처리 등에서 사용)를 호출하는 기능 watch 속성은 데이터의 변화를 감지하고 이에 대한 적절한 처리를 할 수 있는 강력한 기능이다. 데이터의 유효성 검사, API 호출, 다른 데이터와의 연동 등 다양한 기능을 구현할 수 있다.
  - 객체 또는 배열의 형태로 정의하며, 객체 형태로 정의할 경우 키는 감시하고자 하는 데이터의 이름이고 값은 콜백 함수이다. 

  ```vue
  <template>
    <div>
      <input v-model="message" type="text">
      <p>{{ message }}</p>
    </div>
  </template>
  <script>
  export default {
    data() {
      return {
        message: "Hello, world"
      }
    }
    watch: {
    	message(newVal, OldVal) {
        this.messageChanged(newVal, oldVal)
      }	
  	},
    methods {
      messageChanged(newVal, oldVal) {
        console.log(`message changed from $[oldVal} to ${newVal}`)
      }
    }
  } 
  </script>
  ```

- ref 속성 

  - ref속성으로 지정된 요소는 Vue 인스턴스 내부에서 직접 접근이 가능하다. 필요한 경우에만 사용하자. `$refs`객체를 사용하여 Vue 인스턴스에서 직접 참조할 수 있다.

  ```vue
  <template>
    <div>
      <input type="text" ref="myInput">
      <button @click="focusInput">입력창에 포커스</button>
    </div>
  </template>
  
  <script>
  export default {
    methods: {
      focusInput() {
        this.$refs.myInput.focus()
      }
    }
  }
  </script>
  ```



```vue
import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    messages: [
      {
        name: '익명',
        content: '오늘은 날씨가 좋네요',
        date: '2022/02/16 14:36',
      },
      {
        name: '익명',
        content: '오늘은 날씨가 좋네요',
        date: '2022/02/16 14:36',
      },
    ],
  },
  mutations: {
    deleteMessage(state, index) {
      if (confirm('삭제하시겠습니까?')) {
        state.messages.splice(index, 1);
      }
    },
    deleteAllMessages(state) {
      if (confirm('전체 삭제하시겠습니까?')) {
        state.messages = [];
      }
    },
  },
});

export default store;

<template>
  <div class="title background">
    <h2>쪽지함</h2>
    <div class="total_delete_btn">
      <button class="total_delete" @click="deleteAllMessages()">
        전체삭제
      </button>
    </div>
    <div class="dropbox" v-for="(message, index) in messages" :key="index">
      <div class="name-img">
        <img :src="require(`@/assets/yellowsmile.png`)" class="smile" />
        <div class="name-content">
          <div class="name-left">
            <span class="name">{{ message.name }}</span>
          </div>
          <span class="content">{{ message.content }}</span>
        </div>
      </div>
      <div class="date">
        <span class>{{ message.date }}</span>
        <button class="cancel" @click="deleteMessage(index)">
          <img
            :src="require(`@/assets/cancelorange.png`)"
            class="cancel-image"
          />
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex';

export default {
  computed: {
    ...mapState(['messages']),
  },
  methods: {
    deleteMessage(index) {
      this.$store.commit('deleteMessage', index);
    },
    delete
```



#### Vuex 정리

- Vuex는 여러 컴포넌트에서 공유되는 상태 데이터를 중앙 집중적으로 관리하고 컴포넌트 간 통신을 쉽게 할 수 있도록 도와준다.
- State: Vuex의 상태 데이터를 의미한다. 애플리케이션 전체에서 공유되는 데이터를 중앙 집중적으로 관리하기 위해 사용됩니다.
- Mutaions: 상태 데이터를 변경하는 메서드를 정의합니다. 이 메서드는 동기적으로 상태를 변경한다.

```javascript
const store = new Vuex.Store({
  state: {
    count: 0
  },
  mutations: {
    increment(state) {
      state.count++
    },
    decrement(state) {
      state.count--
    },
    add(state, payload) {
      state.count += payload
    }
  }
})

// 카운터 컴포넌트에서
<button @click="increment">증가</button>
<button @click="decrement">감소</button>
<button @click="add(10)">10 증가</button>

export default {
  methods: {
    increment() {
      this.$store.commit('increment')
    },
    decrement() {
      this.$store.commit('decrement')
    },
    add(value) {
      this.$store.commit('add', value)
    }
  }
}
```

- Actions: 비동기 로직을 처리하거나 여러 뮤테이션을 호출하여 상태를 변경하는 메서드를 정의합니다.
- Getters: 상태 데이터를 가져오거나 연산하여 반환하는 메서드를 정의합니다.

```vue
<script>
export default {
  data() {
    return {
      memo: "",
      newMessage: null,
    };
  },
  methods: {
    pageLink() {
      this.$store.commit("updateMemo", this.newMessage);
      this.$router.push({ path: "messageconfirm" });
    },
    updateMemo() {
      this.newMessage = {
        content: this.memo,
        date: new Date().toLocaleDateString(),
      };
    },
  },
};
</script>
```

- 처음에 $store.commit의 위치를 updateMemo() 함수 밑에 처리했는데 그러면 `this.$store.commit`이 text가 변할때마다 객체에 들어가기 때문에 그것을 막기 위해서 보내기 버튼 클릭때 가장 최근 문자열만 반영할 수 있게 처리했다. 

- `$route`와 `$router` 의 차이
  - route는 현재 활성화된 라우트의 상태를 저장한 객체
  - router은 웹 어플리케이션 전체에서 딱 하나만 존재
  - 그렇기에 전반적인 라우터 기능을 관리한다.



- actions를 쓰는 이유

> 1. **비동기 작업 처리**: `actions`는 주로 비동기 작업을 처리하기 위해 사용됩니다. 예를 들어, API 호출, 타이머 설정, 웹 소켓 작업 등과 같은 비동기 작업을 수행할 때 사용합니다. `mutations`는 동기적으로 작동하므로 비동기 작업을 처리할 수 없습니다.
> 2. **복잡한 로직 분리**: `actions`를 사용하면 복잡한 로직을 분리하여 컴포넌트에서 직접 처리하지 않고 상태 관리를 위한 코드로 이동시킬 수 있습니다. 이렇게 함으로써, 컴포넌트는 뷰 렌더링과 사용자 상호작용 처리에 집중할 수 있으며, 상태 변경 로직은 Vuex에서 관리할 수 있습니다.
> 3. **재사용성**: `actions`를 사용하면 애플리케이션 전체에서 재사용 가능한 상태 변경 로직을 작성할 수 있습니다. 여러 컴포넌트에서 동일한 로직이 필요한 경우, 코드를 중복 작성하지 않고 `actions`를 사용하여 한 곳에서 관리할 수 있습니다.
> 4. **코드의 명확성**: `actions`를 사용하면 애플리케이션의 상태 변경 로직을 명확하게 표현할 수 있습니다. `actions`를 사용하면 어떤 상태 변경이 발생하는지, 어떤 `mutations`가 호출되는지 쉽게 파악할 수 있습니다.
> 5. **디버깅 및 테스트 용이성**: `actions`를 사용하면 디버깅 및 테스트하기 쉬운 코드를 작성할 수 있습니다. Vuex에서 제공하는 개발 도구를 사용하면 `actions`와 관련된 모든 정보를 확인할 수 있습니다. 또한, `actions`는 독립적인 함수로 작성되기 때문에 테스트하기가 더 쉽습니다.





```vue
<script>
	saveBtn() {
      if (this.button === "수정") {
        this.updateGroup({ key: this.prevKey, groupId: this.inputValue });
      }
    }
</script>  
```

- payload라는 객체를 사용하여 여러 데이터를 단일 인자로 전달하는 것이 Vuex의 일반적인 패턴이다. 이렇게 하면 액션 함수의 시그니처가 변경될 때마다 호출하는 코드를 수정할 필요가 없어지므로 유지보수가 더 용이해준다.



> `mounted()`를 사용하면, 해당 Vue 인스턴스의 모든 DOM이 생성되고 접근 가능한 상태입니다. 따라서 컴포넌트가 DOM에 마운트 된 후에 데이터를 불러오거나 DOM 조작을 수행하려면 `mounted()`가 가장 적절한 라이프사이클 훅입니다.
>
> 이 경우, 우리는 `route.params`로부터 데이터를 가져와 `groupItem`에 할당하려고 합니다. 라우터를 통해 전달된 데이터는 일반적으로 `mounted()` 훅에서 처리할 수 있습니다. 그 이유는 `mounted()`가 호출되는 시점에는 컴포넌트가 DOM에 마운트되어 있고, 라우터로부터 전달된 데이터에 접근할 수 있기 때문입니다.
>
> 만약 데이터를 더 일찍 처리하고 싶다면, `created()` 라이프사이클 훅을 사용할 수도 있습니다. 이 훅은 인스턴스가 생성된 직후에 호출되므로, DOM에 마운트되기 전에 데이터를 처리할 수 있습니다. 하지만 이 경우에는 DOM 조작은 할 수 없으며, 라우터로부터 전달된 데이터에 접근하는 것만 가능합니다. -다시 물어보기-





> Vue에서 컴포넌트를 사용할 때, 때로는 컴포넌트에 추가 속성을 전달하고 싶을 수 있습니다. 이 경우, 일반적으로 컴포넌트의 최상위 요소에 자동으로 이러한 속성이 상속됩니다. 그러나, 컴포넌트가 프래그먼트(fragment) 또는 텍스트 노드를 렌더링하면 이러한 속성을 자동으로 상속받지 못합니다.
>
> 프래그먼트(fragment)란 하나의 부모 요소 없이 여러 루트 노드를 가진 컴포넌트를 의미합니다. 즉, 최상위 요소가 없습니다.
>
> 이 경우, Vue는 경고 메시지를 표시하여 이러한 속성을 명시적으로 상속해야 함을 알려줍니다. 이를 위해 v-bind="$attrs"를 사용하여 컴포넌트의 최상위 요소에 모든 속성을 명시적으로 바인딩해야 합니다.
>
> 간단히 말해, 컴포넌트에 전달된 추가 속성이 있는데, 컴포넌트 구조 때문에 자동으로 상속되지 않는 것입니다. 그래서 v-bind="$attrs"를 추가하여 명시적으로 모든 속성을 최상위 요소에 바인딩하도록 설정하면 경고 메시지가 사라집니다.

> 앞서 언급한 대로, `content`를 computed property가 아닌 일반적인 data 속성으로 변경하거나, content에 대한 getter와 setter를 만들어야 합니다. 지금 코드에서는 `content`가 여전히 `mapState`를 사용하여 computed property로 정의되어 있습니다.





```vue
<template>
  <div class="add-group">
    <p class="category-name2">{{ category }}</p>
    <input
      type="text"
      :placeholder="placeholder"
      :value="localInputValue"
      @input="updateInputValue($event.target.value)"
      class="input-box"
      maxlength="10"
    />
    <br />
    <div class="btn-control">
      <button class="add-btn" @click="registerBtn()">
        {{ button }}
      </button>
      <button class="cancel-btn" @click="pageLink()">취소</button>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    category: {
      type: String,
      required: true,
    },
    placeholder: {
      type: String,
      required: true,
    },
    button: {
      type: String,
      required: true,
    },
    inputValue: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      localInputValue: this.inputValue,
    };
  },
  watch: {
    inputValue(newValue) {
      this.localInputValue = newValue;
    },
  },
  methods: {
    pageLink() {
      this.$router.push({ path: "/mbti" });
    },
    registerBtn() {
      if (this.localInputValue === "") {
        alert("그룹의 이름을 작성해주세요.");
        return;
      }
      this.$emit("register", this.localInputValue);
      this.localInputValue = "";
    },
    updateInputValue(value) {
      this.localInputValue = value;
    },
  },
};
</script>
```

- 그룹 추가에서 inputvalue를 변경했는데 다른 컴포넌트에 전달하려면 watch 속성을 보내자







- 그룹을 삭제하고 새로 추가했는데 groupId를 찾을 수 없다고 뜬다

```js
import { createStore } from "vuex";

export default createStore({
  state: {},
  getters: {},
  mutations: {

    ADD_GROUP(state, payload) {
      state.groups[state.keys] = payload;
      // key 그룹의 길이만큼 조정 
      state.keys = state.groups.length;
    },


    REMOVE_GROUP(state, index) {
      if (index > -1 && index < state.groups.length) {
        state.groups.splice(index, 1);
        state.keys--;
      } else {
        console.warn("Invalid index for removal:", index);
      }
    },

  
  },
  actions: {},
  modules: {},
});

```



- 하나라도 일치하는 문자열을 찾고 싶으면 some 메서드 활용

```vue
<script>
export default {
  computed: {
    filterMessages() {
      return this.messages.filter((item) =>
        item.name
          .split("")
          .some((char) => this.$store.state.totalMbti.includes(char))
      );
    },
  },
};
</script>
```







```vue
<template>
  <div class="background">
    <h1 class="title">
      <span class="header">SM</span>
      <img :src="require(`@/assets/first_smile1.png`)" class="title-img" />
      <span class="header">E</span>
    </h1>
    <swiper
      :modules="modules"
      :slides-per-view="1"
      :style="{
        '--swiper-pagination-color': '#f59607',
      }"
      :space-between="100"
      :pagination="{ clickable: true }"
      ref="swiper"
      @swiper="onSwiper"
      @slideChange="onSlideChange"
    >
      <swiper-slide class="wrap-swiper">
        <div class="slider">
          <div>
            <h3>
              주변 사람들의<br />
              <span class="mbti">MBTI</span>를 저장해<br />한 눈에 확인하세요!
            </h3>
          </div>
          <div>
            <img :src="require(`@/assets/first_smile3.png`)" class="img1" />
            <img :src="require(`@/assets/first_smile2.png`)" class="img2" />
          </div>
        </div>
      </swiper-slide>
      <swiper-slide class="wrap-swiper">
        <div class="slider">
          <div class="main_content">
            <h3>
              다른 사람들이<br />
              생각하는 <span class="mbti">MBTI</span>는<br />
              어떤지 같이 확인하세요!
            </h3>
          </div>
          <div>
            <img :src="require(`@/assets/first_smile5.png`)" class="mid-img" />
            <img :src="require(`@/assets/first_smile4.png`)" class="left-img" />
            <img
              :src="require(`@/assets/first_smile6.png`)"
              class="right-img"
            />
          </div>
        </div>
      </swiper-slide>
      <swiper-slide class="wrap-swiper">
        <div class="slider">
          <div class="main_content">
            <h3>
              일정을 기록하고<br />
              만나는 사람의 <span class="mbti">MBTI</span><br />
              대응법을 익혀요!
            </h3>
          </div>
          <div>
            <img
              :src="require(`@/assets/first_smile7.png`)"
              class="left-img2"
            />
            <img :src="require(`@/assets/first_info.png`)" class="right-info" />
          </div>
        </div>
      </swiper-slide>
      <swiper-slide class="wrap-swiper">
        <div class="slider">
          <div class="main_content">
            <h3>
              하루의 하나의 질문을 통해<br />
              다른 <span class="mbti">MBTI</span>의 생각을 확인해요!
            </h3>
          </div>
          <div>
            <img
              :src="require(`@/assets/first_smile8.png`)"
              class="left1-img"
            />
            <img
              :src="require(`@/assets/first_question.png`)"
              class="question-mark"
            />
            <img :src="require(`@/assets/exmark.png`)" class="ex-mark" />
            <img
              :src="require(`@/assets/first_smile11.png`)"
              class="right-img1"
            />
            <img
              :src="require(`@/assets/first_smile12.png`)"
              class="right-img2"
            />
            <img
              :src="require(`@/assets/first_smile9.png`)"
              class="right-img3"
            />
            <img
              :src="require(`@/assets/first_smile10.png`)"
              class="right-img4"
            />
            <img
              :src="require(`@/assets/first_smile14.png`)"
              class="right-img5"
            />
            <img
              :src="require(`@/assets/first_smile13.png`)"
              class="right-img6"
            />
          </div>
        </div>
      </swiper-slide>
    </swiper>
    <button
      class="btn btn-start"
      @click="lastBtn()"
      :class="{ disabled: isDisabled }"
    >
      시작하기
    </button>
  </div>
</template>
<script>
// Import Swiper Vue.js components
import { Swiper, SwiperSlide } from "swiper/vue";
import { Pagination } from "swiper";
import "swiper/swiper-bundle.min.css";
import { ref } from "vue";

export default {
  components: {
    Swiper,
    SwiperSlide,
  },
  data() {
    return {
      currentIndex: 0,
    };
  },
  setup() {
    let currentSlide = ref(0);
    let isDisabled = ref(false);
    const onSwiper = (swiper) => {
      console.log(swiper);
    };
    const onSlideChange = (swiper) => {
      console.log(swiper.activeIndex);
      currentSlide.value = swiper.activeIndex + 1;
      if (currentSlide.value === 4) {
        isDisabled.value = true;
      } else {
        isDisabled.value = false;
      }
    };
    return {
      onSwiper,
      onSlideChange,
      currentSlide,
      modules: [Pagination],
      isDisabled,
    };
  },
  methods: {
    lastBtn() {
      if (this.currentSlide === 4) {
        this.$router.push({ path: "login" });
        this.isDisabled = true;
      }
    },
  },
};
</script>
<style scoped>
.background {
  margin: 0;
  position: relative;
  width: 100%;
  background-color: #fff9c8;
  max-height: 100%;
}

.header {
  color: #f59607;
  font-size: 40px;
  font-weight: bold;
}

.swiper-slide {
  width: auto !important;
}

.slider {
  height: 75vh;
}

.title {
  padding-top: 30px;
  margin: 0;
}

.title-img {
  margin-top: 5px;
  padding-left: 1px;
  width: 30px;
  height: 30px;
}

h3 {
  font-weight: bold;
  font-size: 25px;
}

.mbti {
  color: #f59607;
}

@media (max-width: 767px) {
  .img1 {
    right: -12%;
    width: 40%;
  }

  .img2 {
    left: -12%;
    width: 40%;
  }

  h3 {
    font-size: 20px;
  }

  .header {
    font-size: 60px;
  }

  .title-img {
    width: 47px;
    height: 47px;
  }
  .left-img {
    position: absolute;
    left: 5%;
    top: 40%;
    width: 40%;
  }

  .mid-img {
    position: absolute;
    left: 33%;
    top: 40%;
    width: 40%;
  }

  .right-img {
    position: absolute;
    right: 1%;
    top: 40%;
    width: 40%;
  }

  .left-img2 {
    position: absolute;
    left: 15%;
    top: 35%;
    width: 40%;
  }

  .right-info {
    position: absolute;
    top: 33%;
    right: 18%;
    width: 20%;
  }

  /* 4*/
  .left1-img {
    position: absolute;
    width: 60%;
    top: 40%;
    left: -17%;
  }

  .question-mark {
    position: absolute;
    width: 20%;
    top: 25%;
    left: 15%;
  }

  .ex-mark {
    position: absolute;
    top: 20%;
    width: 8%;
    right: 10%;
  }

  .right-img1 {
    position: absolute;
    width: 30%;
    top: 40%;
    right: 17%;
  }

  .right-img2 {
    position: absolute;
    width: 30%;
    top: 45%;
    right: -5%;
  }

  .right-img3 {
    position: absolute;
    width: 30%;
    top: 27%;
    right: 13%;
  }

  .right-img4 {
    position: absolute;
    width: 30%;
    top: 31%;
    right: -8%;
  }

  .right-img5 {
    position: absolute;
    width: 30%;
    top: 59%;
    right: -5%;
  }

  .right-img6 {
    position: absolute;
    width: 30%;
    top: 54%;
    right: 18%;
  }
}

@media (min-width: 768px) and (max-width: 1023px) {
  .img1 {
    right: 1%;
    width: 50%;
  }

  .img2 {
    left: 20%;
    width: 50%;
  }

  h3 {
    font-size: 40px;
  }

  .header {
    font-size: 60px;
  }

  .title-img {
    width: 47px;
    height: 47px;
  }

  .left-img {
    position: absolute;
    left: 3%;
    top: 40%;
    width: 40%;
  }

  .mid-img {
    position: absolute;
    left: 30%;
    top: 40%;
    width: 40%;
  }

  .right-img {
    position: absolute;
    right: 4.5%;
    top: 40%;
    width: 40%;
  }

  .left-img2 {
    position: absolute;
    left: 18%;
    top: 35%;
    width: 40%;
  }

  .right-info {
    position: absolute;
    top: 35%;
    right: 23%;
    width: 15%;
  }

  /*4 */
  .left1-img {
    position: absolute;
    width: 350px;
    top: 300px;
    left: -70px;
  }

  .question-mark {
    position: absolute;
    width: 100px;
    top: 190px;
    left: 95px;
  }

  .ex-mark {
    position: absolute;
    top: 120px;
    width: 45px;
    right: 80px;
  }

  .right-img1 {
    position: absolute;
    width: 230px;
    top: 360px;
    right: 150px;
  }

  .right-img2 {
    position: absolute;
    width: 230px;
    top: 380px;
    right: -40px;
  }

  .right-img3 {
    position: absolute;
    width: 230px;
    top: 180px;
    right: 100px;
  }

  .right-img4 {
    position: absolute;
    width: 230px;
    top: 210px;
    right: -50px;
  }

  .right-img5 {
    position: absolute;
    width: 230px;
    top: 550px;
    right: -40px;
  }

  .right-img6 {
    position: absolute;
    width: 230px;
    top: 550px;
    right: 140px;
  }
}

@media (min-width: 1024px) {
  .img1 {
    right: -4.2%;
    width: 45%;
  }

  .img2 {
    left: -4.2%;
    width: 45%;
  }

  h3 {
    font-size: 35px;
  }

  .header {
    font-size: 60px;
  }

  .title-img {
    width: 47px;
    height: 47px;
  }

  .left-img {
    position: absolute;
    left: 37.5%;
    top: 40%;
    width: 11%;
  }

  .mid-img {
    position: absolute;
    left: 45%;
    top: 40%;
    width: 11%;
  }

  .right-img {
    position: absolute;
    right: 37%;
    top: 40%;
    width: 11%;
  }

  .left-img2 {
    position: absolute;
    left: 35%;
    top: 41%;
    width: 15%;
  }

  .right-info {
    position: absolute;
    top: 41%;
    right: 40%;
    width: 7%;
  }
  /*4 */
  .left1-img {
    position: absolute;
    width: 25%;
    top: 36%;
    left: -8%;
  }

  .question-mark {
    position: absolute;
    width: 7%;
    top: 23%;
    left: 8%;
  }

  .ex-mark {
    position: absolute;
    top: 15%;
    width: 3%;
    right: 5%;
  }

  .right-img1 {
    position: absolute;
    width: 13%;
    top: 46%;
    right: 8%;
  }

  .right-img2 {
    position: absolute;
    width: 13%;
    top: 52%;
    right: -2%;
  }

  .right-img3 {
    position: absolute;
    width: 13%;
    top: 26%;
    right: 7%;
  }

  .right-img4 {
    position: absolute;
    width: 13%;
    top: 32%;
    right: -2%;
  }

  .right-img5 {
    position: absolute;
    width: 13%;
    top: 70%;
    right: -2%;
  }

  .right-img6 {
    position: absolute;
    width: 13%;
    top: 66%;
    right: 8%;
  }
}

.btn-start {
  width: 180px;
  height: 52px;
  border-radius: 25px;
  color: #ffffff;
  background-color: #c8c8c8;
  font-size: 18px;
  font-weight: 700;
  border: none;
}

.btn-start.disabled {
  background-color: #f59607; /* 버튼 비활성화 시 적용될 색상 */
}
</style>
```

