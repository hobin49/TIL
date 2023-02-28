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