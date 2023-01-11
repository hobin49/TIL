### Vue란 무엇인가?

- 뷰는 웹 페이지 화면을 개발하기 위한 프론트엔드 프레임워크이다.
- 뷰는 화면단 라이브러리이자 프레임워크라고도 볼 수 있다.
- 뷰의 창시자는 Evan You다.
- 뷰 코어 라이브러리는 화면단 데이터 표현에 관한 기능들을 중점적으로 지원하지만 프레임워크의 기능인 라우터, 상태 관리, 테스팅 등을 쉽게 결합할 수 있는 형태로도 제공된다. 즉 라이브러리 역할뿐만 아니라 프레임워크 역할도 할 수 있다.
- 공식 사이트에서도 뷰를 Progressive framework라고 부르고 있다. 
- 뷰의 창시자 에반은 앵귤러의 명시적 데이터 바인딩과 같은 필수적인 요소들만 가지고 화면을 구현하기 시작했고, 오픈 소스화하면서 많은 사람들이 참여하여 프레임워크의 기능을 붙여 나가기 시작했다. 그래서 뷰가 탄생했다. 
- 뷰는 2014년 2월에 처음 배포됐다. 
- 뷰의 장점
  - 배우기가 쉽다
  - 리액트와 앵귤러에 비해 성능이 우수하고 빠르다
  - 리액트의 장점과 앵귤러의 장점을 갖고 있다 
    - 앵귤러의 데이터 바인딩 특성과 리액트의 가상 돔 기반 렌더링 특징을 모두 가지고 있다



### Vue.js의 특징

- 뷰는 UI화면 개발 방법 중 하나인 MVVM 패턴의 뷰 모델에 해당하는 화면단 라이브러리입니다. 

- 뷰는 화면의 요소가 변경되거나 조작이 일어날 때 즉각적으로 반응하여 화면의 데이터를 갱신하여 보여 주는 역할을 한다.

- 화면의 표현에 주로 관여하는 라이브러리이기 때문에 화면단 라이브러리라고도 한다.

- MVVM 패턴이란?

  - 모델 - 뷰 - 뷰 모델로 구조화하여 개발하는 방식을 의미한다. 
  - 마크업 언어나 GUI 코드를 비즈니스 로직 또는 백엔드 로직과 분리하여 개발하는 소프트웨어 디지인 패턴 
  - 이러한 방식은 화면의 요소들을 제어하는 코드와 데이터 제어 로직을 분리하여 코드를 더 직관적으로 이해할 수 있다. 
  - 추후 유지 보수가 편하다. 
  - **프론트엔드의 화면 동작과 관련된 로직과 백엔드의 데이터베이스 데이터 처리 로직을 분리하여 더 깔끔하게 코드를 구성**

- 간단한 용어

  - 돔
    - HTML 문서에 들어가는 요소(태그, 클래스, 속성 등)의 정보를 담고 있는 데이터 트리
  - 돔 리스너
    - 돔의 변경 내역에 대해 즉각적으로 반응하여 특정 로직을 수행하는 장치 
  - 모델
    - 데이터를 담는 용기, 보통은 서버에서 가져온 데이터를 자바스크립트 객체 형태로 저장
  - 데이터 바인딩
    - 뷰에 표시되는 내용과 모델의 데이터를 동기화 
    - 검색 버튼이 동작하면 검색 결과를 보여주는 로직이 동작하는데 이 과정에서 데이터 바인딩이 관여하는데, 검색 결과에 해당하는 데이터를 모델에서 가져와 화면에 나타내 줍니다. 
  - 뷰 모델
    - 뷰와 모델의 중간 영역, 돔 리스너와 데이터 바인딩을 제공하는 영역

  

- 컴포넌트 기반 프레임워크
  - 컴포넌트는 레고 블록과 같다. 레고 블록을 잘 조합해서 쌓으면 원하는 모형을 만들 수 있듯이 뷰의 컴포넌트를 조합하여 화면을 구성할 수 있다. 
  - header, content, footer 크게 세 가지로 구성
  - 컴포넌트 기반 방식으로 개발하는 이유는 코드를 재사용하기 쉽기 때문이다. (리액트, 앵귤러 모두 컴포넌트 기반)
  - 뷰의 경우는 컴포넌트를 썼을 때 HTML 코드에서 화면의 구조를 직관적으로 파악할 수 있다.
- 리액트와 앵귤러의 장점을 가진 프레임워크
  - 뷰는 앵귤러 의 양방향 데이터 바인딩과 리액트의 단방향 데이터 흐름의 장점을 모두 결합한 프레임워크다. 
  - 양방향 데이터 바인딩이란?
    - 화면에 표시되는 값과 프레임워크의 모델 데이터 값이 동기화 되어 한쪽이 변경되면 다른 한쪽도 자동으로 변경되는 것을 말한다. 
  - 단방향 데이터 흐름은?
    - 컴포넌트의 단방향 통신 즉 컴포넌트 간에 데이터를 전달할 때 항상 상위 컴포넌트에서 하위 컴포넌트 한 방향으로만 전달하게끔 프레임워크가 구조화되어 있는 게 바로 단방향 데이터 흐름이다.
  - 빠른 화면 렌더링을 위해 리액트의 가상 돔 렌더링 방식을 적용하여 사용자 인터렉션이 많은 요즘의 웹 화면에 적합한 동작 구조를 갖추고 있다. 
    - 가상돔을 활용하면 특정 돔 요소를 추가하거나 삭제하는 변경이 일어날 때 화면 전체를 다시 그리지 않고 프레임워크에서 정의한 방식에 따라 화면을 갱신한다. 따라서 브라우저 입장에서는 성능 부하가 줄어들어 일반 렌더링 방식보다 더 빠르게 화면을 그릴 수 있다. 



### Vue 기술 살펴보기 

- 크롬 익스텐션을 통해서 Vue를 설치했음에도 불구하고 익스텐션을 다운로드하라는 로그가 뜬다면 그것은 현재 예제를 서버에서 띄운 것이 아니라 파일 시스템에서 접근하여 브라우저로 실행했기 때문이다. 쉽게 말해 file:// 형태로 접근한 파일과 http://로 접근한 파일에 대해서 뷰 개발자 도구가 각기 다른 설정을 적용한다. 
  - 그래서 확장 프로그램 설정에서 파일 URL에 대한 액세스를 허용하면 로그가 사라진다.

- 뷰 인스턴스

  - 뷰 인스턴스는 뷰로 화면을 개발하기 위해 필수적으로 생성해야 하는 기본 단위이다. (ex`new Vue`) 
  - new Vue()로 인스턴스를 생성할 때 Vue를 생성자라고 합니다. Vue 생성자는 뷰 라이브러리를 로딩하고 나면 접근할 수 있다. 생성자를 사용하는 이유는 뷰로 개발할 때 필요한 기능들을 생성자에 미리 정의해 놓고 사용자가 그 기능을 재정의하여 편리하게 사용하도록 하기 위해서다. 
    - 생성자란 객체를 새로 생성할 때 자주 사용하는 옵션과 기능들을 미리 특정 객체에 저장해 놓고, 새로 객체를 생성할 때 기존에 포함된 기능과 더불어 기존 기능을 쉽게 확장하여 사용하는 기법이다. 

- 뷰 인스턴스 유효 범위

  - 뷰 인스턴스를 생성하면 HTML의 특정 범위 안에서만 옵션 속성들이 적용되어 나타난다. 
  - Vue()로 인스턴스 생성 후 옵션 속성을 적용하는 과정
    - 뷰 라이브러리 파일 로딩 -> 인스턴스 객체 생성(옵션 속성 포함) -> 특정 화면 요소에 인스턴스를 붙인다 -> 인스턴스 내용이 화면 요소로 변환 -> 변환된 화면 요소를 사용자가 최종 확인(인스턴스가 화면에 적용되는 과정)

- 뷰 인스턴스 라이프 사이클

  - created는 인스턴스가 생성되었을 때 호출할 동작을 정의하는 속성 이처럼 인스턴스의 상태에 따라 호출할 수 있는 속성을 **라이프 프사이클 속성**이라고 한다. 그리고 라이프 사이클 속성에서 실행되는 커스텀 로직을 **라이프 사이클 훅**이라고 한다.
  - 라이프 사이클 속성에는 created, beforeCreate, beforeMount, mounted 등 인스턴스의 생성, 변경, 소멸과 관련되어 총 8개가 있다
  - beforeCreate
    - 인스턴스가 생성되고 나서 가장 처음으로 실행되는 라이프 사이클 단계
    - data, method 속성이 아직 인스턴스에 정의되어 있지 않고, 돔과 같은 화면 요소에도 접근할 수 없다.
  - created
    - data, method 속성이 정의되어서 this.data or this.fetchData()와 같은 로직들을 이용하여 정의된 값에 접근하여 로직을 실행한다.
    - 아직 template 속성에 정의된 돔 요소로 접근할 수 없다. 
  - beforeMount
    - created단계 이후 template 속성에 지정한 마크업 속성을 render() 함수로 변환한 후 el 속성에 지정한 화면 요소에 인스턴스를 부착하기 전에 호출되는 단계
  - mounted 
    - el 속성에서 지정한 화면 요소에 인스턴스가 부착되고 나면 호출하는 단계, 화면 요소에 접근할 수 있어 화면 요소를 제어하는 로직을 수행하기 좋은 단계
  - beforeUpdate
    - el 속성에서 지정한 화면 요소에 인스턴스가 부착되고 나면 인스턴스에 정의한 속성들이 화면에 치환됩니다. 치환된 값은 뷰의 반응성을 제공하기 위해 $watch속성으로 감시한다. 이를 데이터 관찰이라고 한다.
  - updated
    - 데이터가 변경되고 나서 강상 돔으로 다시 화면을 그리고나면 실행되는 단계
    - 데이터 변경 후 화면 요소 제어와 관련된 로직을 추가하기 좋은 단계이다. 이 단계에서 데이터 값을 변경하면 무한 루프에 빠질 수 있으므로 가급적이면 데이터 값을 갱신하는 로직은 beforeUpdate에 추가하자
  - beforeDestroy
    - 뷰 인스턴스가 파괴되기 직전에 호출하는 단계이다. 뷰 인스턴스의 데이터를 삭제하기 좋은 단계이다. 
  - destroyed
    - 뷰 인스턴스가 파괴되고 나서 호출되는 단계이다. 

  ```html
  <!DOCTYPE html>
  <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta http-equiv="X-UA-Compatible" content="IE=edge" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <title>Vue sample</title>
    </head>
    <body>
      <div id="apps">{{ message }}</div>
      <script src="https://cdn.jsdelivr.net/npm/vue@2.5.2/dist/vue.js"></script>
      <script>
        new Vue({
          el: "#apps",
          data: {
            message: "안녕하세요 저는 킴이에요",
          },
          beforeCreate: function () {
            console.log("beforeCreate");
          },
          created: function () {
            console.log("created");
          },
          mounted: function () {
            console.log("mounted");
            this.message = "Hello Vue!";
          },
          updated: function () {
            console.log("updated");
          },
        });
      </script>
    </body>
  </html>
  ```






#### 뷰 컴포넌트

- 컴포넌트 등록하기

  - 지역 컴포넌트는 특정 인스턴스에서만 유효한 범위를 갖고, 전역 컴포넌트는 여러 인스턴스에서 공통으로 사용할 수 있다.(뷰로 접근 가능한 모든 범위)

  - 전역 컴포넌트를 모든 인스턴스에 등록하려면 Vue 생성자에서 .component()를 호출하여 수행하면 된다.

    ```html
    Vue.component('컴포넌트 이름', {
    	// 컴포넌트 내용
    })
    ```

  - 뷰 라이브러리 파일 로딩 -> 뷰 생성자로 컴포넌트 등록 ->인스턴스 객체 생성 -> 특정 화면 요소에 인스턴스 부착 -> 인스턴스 내용 변환(등록된 컴포넌트 내용도 변환)- `<my-component>`가 `<div>`로 변환됨 -> 변환된 화면 요소를 사용자가 최종 확인

    ```html
    <div id='app'>
      <button>컴포넌트 등록</button>
      <!--등록한 my-componenet가 최종적으로 변환된 모습-->
      <div>전역 컴포넌트가 등록되었습니다.</div>
    </div>
    ```

  - 지역 컴포넌트 등록은 인스턴스에 component 속성을 추가하고 등록할 컴포넌트 이름과 내용을 정의하면 된다.

    ```html
    new Vue({
    	components: {
    		'컴포넌트 이름': 컴포넌트 내용
    }
    })
    ```

  - 지역 컴포넌트는 새 인스턴스를 생성할 때마다 등록해 줘야 한다.

  - 지역 컴포넌트는 유효 범위를 벗어나면 HTML 사용자 정의 태그로 인식한다.

  ```html
  <!DOCTYPE html>
  <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta http-equiv="X-UA-Compatible" content="IE=edge" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <title>Vue Component Registration</title>
    </head>
    <body>
      <div id="app">
        <h3>첫 번째 인스턴스 영역</h3>
        <my-global-component></my-global-component>
        <my-local-component></my-local-component>
      </div>
      <hr />
      <div id="app2">
        <h3>두 번째 인스턴스 영역</h3>
        <my-global-component></my-global-component>
        <my-local-component></my-local-component>
      </div>
      <script src="https://cdn.jsdelivr.net/npm/vue@2.5.2/dist/vue.js"></script>
      <script>
        //전역 컴포넌트 등록
        Vue.component("my-global-component", {
          template: "<div>전역 컴포넌트가 등록되었습니다.</div>",
        });
        //지역 컴포넌트 내용
        var cmp = {
          template: "<div>지역 컴포넌트가 등록되었습니다</div>",
        };
        // 첫 번째 인스턴스
        new Vue({
          el: "#app",
          // 지역 컴포넌트 등록
          components: {
            "my-local-component": cmp,
          },
        });
  
        new Vue({
          el: "#app2",
        });
      </script>
    </body>
  </html>
  ```

  

#### 뷰 컴포넌트 통신

- 뷰 컴포넌트로 화면을 구성하므로 같은 웹 페이지라도 데이터를 공유할 수 없습니다. 컴포넌트마다 자체적으로 고유한 유효 범위를 갖는다. 

- 각 컴포넌트의 유효 범위가 독립적이기 때문에 다른 컴포넌트의 값을 직접적으로 참조할 수가 없다. 

```html
    <script src="https://cdn.jsdelivr.net/npm/vue@2.5.2/dist/vue.js"></script>
    <script>
      //첫 번째 컴포넌트 내용
      var cmp1 = {
        template: "<div>첫 번째 지역 컴포넌트: {{ cmp1Data }}</div>",
        data: function () {
          return {
            cmp1Data: 100,
          };
        },
      };

      //두 번째 컴포넌트 내용
      var cmp2 = {
        template: "<div>두 번째 지역 컴포넌트: {{ cmp2Data }}</div>",
        data: function () {
          return {
            cmp2Data: cmp1.data.cmp1Data,
          };
        },
      };

      new Vue({
        el: "#app",
        //지역 컴포넌트 등록
        components: {
          "my-component1": cmp1,
          "my-component2": cmp2,
        },
      });
    </script>
```

- 위에 컴포넌트2는 아무것도 출력되지 않는다. 직접 참조할 수 없기 때문이다.

- 상-하위 컴포넌트 관계
  - 트리 구조에서 부모 노드, 자식 노드처럼 컴포넌트 간의 관계가 부모, 자식으로 이루어진 컴포넌트를 의미한다. 지역 또는 전역 컴포넌트를 등록하면 등록된 컴포넌트는 자연스럽게 하위 컴포넌트가 된다. 그리고 하위 컴포넌트를 등록한 인스턴스는 상위 컴포넌트가 된다.

- 상위에서 하위 컴포넌트로 데이터 전달하기

  - Props 속성

    - 상위 컴포넌트에서 하위 컴포넌트로 데이터를 전달할 때 사용하는 속성

    - 정의 방식

      ```html
      Vue.component('child-component', {
      	props: ['props 속성 이름'],
      });
      ```

    - HTML 코드에 등록된 child-component 컴포넌트 태그에 v-bind 속성을 추가한다.

      ```html
      <child-component v-bind:props 속성 이름="상위 컴포넌트의 data 속성"></child-component>
      ```

    - v-bind 속성 왼쪽 값으로 하위 컴포넌트에 정의한 props 속성을 넣고 오른쪽 값으로 하위 컴포넌트에 전달할 상위 컴포넌트의 data 속성을 지정한다.

    ```html
    <div id="app">
      <child-component v-bind:propsdata="message"></child-component>
    </div>
    <script>
    	Vue.component('child-component', {
        props: ['propsdata'],
        template: '<p>{{ propsdata }}</p>',
      });
      new Vue({
        el: '#app',
        data: {
          message: "Hello Vue! passed from Parent Component"
        }
      });
    </script>
    ```

    - 순서
      - new Vue()로 인스턴스를 하나 생성합니다
      - Vue.component()를 이용하여 하위 컴포넌트인 child-component를 등록한다
      - child-component의 내용에 props 속성으로 propsdata를 정의한다
      - html에 컴포넌트 태그를 추가한다
      - child-component의 template 속성에 정의된 `<p>{{ propsdata }}</p>` 는 message에 정의된 내용이 들어간다. 
    - 뷰 인스턴스 안에 마치 상위 컴포넌트가 존재하는 것처럼 보이는 이유는 컴포넌트를 등록함과 동시에 뷰 인스턴스 자체가 상위 컴포넌트가 되기 때문이다. 
    - 새로운 컴포넌트를 등록하면 기존에 있는 컴포넌트는 상위 컴포넌트가 되고 새로 등록된 컴포넌트는 하위 컴포넌트가 되고 이렇게 새 컴포넌트를 등록한 인스턴스를 최상위 컴포넌트라고도 부른다.


- 하위에서 상위 컴포넌트로 이벤트 전달

  - 하위에서 상위 컴포넌트로 통신을 하려면 이벤트를 발생시켜 상위 컴포넌트에 신호를 보내면 된다. 

  - 이벤트 발생과 수신 형식

    ```html
    <!--이벤트 발생-->
    this.$emit('이벤트명');
    
    <!--이벤트 수신-->
    <child-component v-on:이벤트명="상위 컴포넌트의 메서드명"></child-component>
    ```

    - emit을 호출하는 위치는 하위 컴포넌트의 특정 메서드 내부이기 떄문에 호출할 때 사용하는 this는 하위 컴포넌트를 가리킨다. 

  ```html
  <div id='app'>
    <!--하위 컴포넌트의 이벤트명 = 상위 컴포넌트의 메서드명 -->
   	<child-component v-on:show-log="printText"></child-component>
  </div>
  <script>
  	Vue.component('child-component', {
      //1. 버튼요소 추가
      template: '<button v-on:click="showLog">show</button>',
      //2. 메서드 추가
      methods: {
        showLOg: function() {
          this.$emit('show-log');
        }
      }
    });
    
    var app = new Vue({
      el: '#app',
      data: {
        message: 'Hello Vue! passed from Parent Component'
      },
      methods: {
        printText: function() {
          console.log("received an event");
        }
      }
    })
  </script>
  ```

  - 순서
    - [show] 버튼을 클릭하면 클릭 이벤트 v-on:click="showLog"에 따라 showLog() 메서드가 실행된다.
    - showLog() 메서드 안에 this.$emit('show-log')가 실행되면서 show-log 이벤트가 발생한다. 
    - Show-log 이벤트는 `<child-component>`에 정의한 v-on:show-log에 전달되고, v-on: show-log의 대상 메서드인 최상위 컴포넌트의 메서드 printText()가 실행된다.
    - printText()는 received an event라는 로그를 출력하는 메서드이므로 마지막으로 콘솔에 로그가 출력된다. 



- 같은 레벨의 컴포넌트 간 통신

  - 뷰는 상위에서 하위로만 전달해야하는 규칙이 있다 따라서 바로 옆 컴포넌트에 값을 전달하기 위해서는 공통 상위 컴포넌트에서 2개의 하위 컴포넌트에 props를 내려 보내야 한다. 
  - 같은 레벨에 통신이 가능하도록 구조를 갖춰야 한다. 그래서 같은 레벨 간에 통신이 가능하도록 구조를 갖춰야 하는데 이를 해결할 수 있는 방법이 바로 **이벤트 버스**이다. 

- 관계 없는 컴포넌트 간 통신 - 이벤트 버스

  - 이벤트 버스를 이용하면 상위 - 하위 관계를 유지하고 있지 않아도 데이터를 한 컴포넌트에서 다른 컴포넌트로 전달할 수 있다.
  - 중간 컴포넌트를 거치지 않고 하위 컴포넌트에서 상위 컴포넌트로 바로 데이터를 전달할 수 있어서 편리하다

- 이벤트 버스 형식

  ```html
  <!-- 이벤트 버스를 위한 추가 인스턴스 1개 생성 -->
  var eventBus = new Vue();
  
  <!-- 이벤트를 보내는 컴포넌트 -->
  methods = {
  	메서드명: function() {
  		eventBus.$emit('이벤트명', 데이터);
  	}
  }
  
  <!-- 이벤트를 받는 컴포넌트 -->
  methods: {
  	created: function()  {
  		eventBus.$on('이벤트명', function(데이터) {
  			...
  		});
  	}
  }
  ```





- 이벤트 버스 구현하기

  ```html
  <div id = "app">
    <child-component></child-component>
  </div>
  
  <script>
    //1
  	var eventBus = new Vue();
    Vue.component('child-component', {
  		//2
      template: '<div>하위 컴포넌트 영역입니다. <button v-on:click="showLog">show</button></div>'
      methods: {
      	showLog: function() {
      		eventBus.$emit('triggerEventBus', 100);
    		}
    	}
    });
    
    var app = new Vue ({
      el: '#app',
      created: function() {
        //3
        eventBus.$on('triggerEventBUs', function(value) {
          console.log("이벤트를 전달받음. 전달받은 값 : ", value);
        });
      }
    });
  
  </script>
  ```

  - 순서
    - 먼저 이벤트 버스로 활용할 새 인스턴스를 1개 생성하고 eventBus라는 변수에 참조한다. 이제 eventBus변수로 새 인스턴스의 속성과 메서드에 접근할 수 있다
    - 하위 컴포넌트에는 template 속성과 methods 속성을 정의한다. Methods 속성에는 showLog() 메서드를 정의하고, 메서드 안에는 eventBus.$emit()을 선언하여 triggerEventBus라는 이벤트를 발생하는 로직을 추가한다. 이 이벤트를 발생할 때 수신하는 쪽에 인자 값으로 100이라는 숫자를 함께 전달한다. 
    - 상위 컴포넌트의 created 라이프 사이클 훅에 eventBus.$on()으로 이벤트를 받는 로직을 선언한다. 발생한 이벤트 triggerEventBus를 수신할 때 앞에서 전달된 인자 값 100이 콘솔에 출력된다. 







#### 4. 상용 웹 앱을 개발하기 위한 필수 기술들 - 라우터 & HTTP 통신

- SPA(싱글 페이지 애플리케이션)
  - 페이지를 이동할 때마다 서버에 웹 페이지를 요청하여 새로 갱신하는 것이 아니라 미리 해당 페이지들을 받아 놓고 페이지 이동 시에 클라이언트의 라우팅을 이용하여 화면을 갱신하는 패턴을 적용한 애플리케이션

- 라우팅이란?

  - 라우팅이란 웹 페이지 간의 이동 방법을 말합니다. 라우팅은 현대 웹 앱 형태 중 하나인 싱글 페이지 애플리케이션에서 주로 사용하고 있습니다. 
  - 라우팅을 이용하면 화면 간의 전환이 매끄러울 뿐만 아니라 애플리케이션의 사용자 경험을 향상 시킬 수 있다.
  - 일반적으로 브라우저에서 웹 페이지를 요청하면 서버에서 응답을 받아 웹 페이지를 다시 ㄷ사용자에게 돌려주는 시간 동안 화면 상에 깜빡거림 현상이 나타난다. 그런데 라우팅을 사용하면 깜빡거림 없이 화면을 매끄럽게 전환하고 더 빠르게 화면을 조작할 수 있어서 사용자 경험이 향상된다.
  - 뷰뿐만 아니라 다른 자바스크립트 프레임워크들도 이용하여 화면을 전환하고 있으며, 일반 HTML 파일들로 라우팅 자바스크립트 라이브러리를 이용하여 라우팅 방식의 페이지 이동을 구현할 수 있다.

  

- 뷰 라우터

  - 뷰 라우터는 뷰에서 라우팅 기능을 구현할 수 있도록 지원하는 공식 라이브러리입니다.  뷰 라우터를 이용하여 뷰로 만든 페이지 간에 자유롭게 이동할 수 있다. 

  - 특수 태그와 기능

    - `<router-link to="URL 값"> ` : 페이지 이동 태그. 화면에서는 `<a>` 로 표시되며 클릭하면 to에 지정한 URL로 이동한다.
    - `<router-view>`: 페이지 표시 태그. 변경되는 URL에 따라 해당 컴포넌트를 뿌려주는 영역입니다. 
      - `<router-view>`에 나타낼 화면은 `<scirpt>`에서  정의한다. 

    ```html
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Vue Router Sample</title>
      </head>
      <body>
        <div id="app">
          <h1>뷰 라우터 예제</h1>
          <p>
            <!--URL 값을 변경하는 태그-->
            <router-link to="/main">Main 컴포넌트로 이동</router-link>
            <router-link to="/login">Login 컴포넌트로 이동</router-link>
          </p>
          <!--URL 값에 따라 갱신되는 화면 영역-->
          <router-view></router-view>
        </div>
        <script src="https://cdn.jsdelivr.net/npm/vue@2.5.2/dist/vue.js"></script>
        <script src="https://unpkg.com/vue-router@3.0.1/dist/vue-router.js"></script>
        <script>
          // Main, Login 컴포넌트 정의
          var Main = { template: "<div>main</div>" };
          var Login = { template: "<div>login</div>" };
    
          // 각 URL에 맞춰 표시할 컴포넌트 지정
          var routes = [
            { path: "/main", component: Main },
            { path: "/login", component: Login },
          ];
    
          //뷰 라우터 정의
          var router = new VueRouter({
            routes,
          });
    
          //뷰 인스턴스에 라우터 추가
          var app = new Vue({
            router,
            //$mount()는 el 속성과 같이 인스턴스를 화면에 붙여주는 역할을 합니다.
          }).$mount("#app");
        </script>
      </body>
    </html>
    
    ```

    - `$mount() API란?` 
      - el 속성과 동일하게 인스턴스를 화면에 붙이는 역할을 합니다. 인스턴스를 생성할 때 el 속성을 넣지 않았더라도 생성하고 나서 `$mount()`를 이용하면 강제로 인스턴스를 화면에 붙일 수가 있습니다. 참고로 뷰 라우터의 공식 문서는 모두 인스턴스 안에 el을 지정하지 않고 라우터만 지정하여 생성한 다음 생성된 인스턴스를 $mount()를 이용해 붙이는 식으로 안내하고 있다. 

    ```html
    <!-- 라우터 URL의 해시 값(#)을 없애는 방법- history mode 사용--> 
    var router = new VueRouter({
    	mode: 'history',
    	routes
    });
    ```
    
  - - 네스티드 라우터
  
      - 네스티드 라우터는 라우터로 페이지를 이동할 때 최소 2개 이상의 컴포넌트를 화면에 나타낼 수 있다. 네스티드 라우터를 이용하면 URL에 따라서 컴포넌트의 하위 컴포넌트가 다르게 표시된다.
      - 네스티드 라우터와 기본 라우터의 차이점은 최상위 컴포넌트에도 `<router-view>`가 있고, 최상위 컴포넌트의 하위 컴포넌트에도 `<rotuer-view>` 가 있다는 것이다. 그렇기 때문에 URL에 따라 하위 컴포넌트의 내용이 바뀌게 됩니다. 
      - **네스티드 라우터는 화면을 구성하는 컴포넌트의 수가 적을 때는 유용하지만 한 번에 더 많은 컴포넌트를 표시하는 데는 한계가 있다.**
  
      ```html
      <!DOCTYPE html>
      <html lang="en">
        <head>
          <meta charset="UTF-8" />
          <meta http-equiv="X-UA-Compatible" content="IE=edge" />
          <meta name="viewport" content="width=device-width, initial-scale=1.0" />
          <title>Vue Nested Router</title>
        </head>
        <body>
          <div id="app">
            <!--User 컴포넌트가 뿌러질 영역-->
            <router-view></router-view>
          </div>
          <script src="https://cdn.jsdelivr.net/npm/vue@2.5.2/dist/vue.js"></script>
          <!--Router CDN-->
          <script src="https://unpkg.com/vue-router@3.0.1/dist/vue-router.js"></script>
          <script>
            // 하위 컴포넌트가 뿌려질 영역
            var User = {
              template: `<div> User Component <router-view></router-view> </div>`,
            };
      
            //컴포넌트 내용 정의
            var UserProfile = { template: "<p>User Profile Component</p>" };
            var UserPost = { template: "<p>User Post Component</p>" };
      
            // 네스티드 라우팅 정의
            var routes = [
              {
                path: "/user",
                component: User,
                children: [
                  {
                    path: "posts",
                    component: UserPost,
                  },
                  {
                    path: "profile",
                    component: UserProfile,
                  },
                ],
              },
            ];
      
            // 뷰 라우터 정의
            var router = new VueRouter({
              routes,
            });
      
            // 뷰 인스턴스에 라우터 추가
            var app = new Vue({
              router,
            }).$mount("#app");
          </script>
        </body>
      </html>
      
      ```
    
      - 코드 순서
        - `<div id = "app">`에 `<router-view>`를 등록하여 User 컴포넌트가 뿌려질 영역을 정의한다
        - User, UserPost, UserProfile 컴포넌트의 내용을 각 객체에 정의한다. 컴포넌트가 전환된 것을 확인할 수 있게 template 속성을 컴포넌트 내용에 추가했다. 여기서 주목할 부분은 User 컴포넌트의 template에 하위 컴포넌트를 표시할 `<router-view>`가  하나 더 있다.
        - routes에 라우터 정보를 정의한다. 제일 먼저 Path 속성에는 네스티드 라우터를 실행하는 기본 URL을 /user로 설정하고, 상위 컴포넌트는 User 컴포넌트로 지정한다. 그런 다음 Childern 속성에는 URL 값 /user 다음에 올 URL에 따라 표시될 하위 컴포넌트를 정의한다. /user/posts인 경우 UserPost를 표시하고, /user/profile인 경우 UserProfile을 표시하도록 설정한다.
        - 이제 뷰 라우터를 새로 하나 생성하고 앞에서 정의한 라우터 정보를 담은 객체 routes를 정의한다
        - 마지막으로 인스턴스를 하나 생성하고 라우터 정보 router를 포함한다. 그리고 app이라는 id를 가진 요소에 인스턴스를 붙여 화면에 나타낸다. 
    
      - 네임드 뷰
    
        - 특정 페이지로 이동했을 때 여러 개의 컴포넌트를 동시에 표시하는 라우팅 방식이다. 앞에서 본 네스티드와 달리 네임드 뷰는 여러 개의 컴포넌트를 한 번에 표시한다. 
    
        ```html
        <!DOCTYPE html>
        <html lang="en">
          <head>
            <meta charset="UTF-8" />
            <meta http-equiv="X-UA-Compatible" content="IE=edge" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <title>Document</title>
          </head>
          <body>
            <div id="app">
              <router-view name="header"></router-view>
              <router-view></router-view>
              <router-view name="footer"></router-view>
            </div>
            <script src="https://cdn.jsdelivr.net/npm/vue@2.5.2/dist/vue.js"></script>
            <script src="https://unpkg.com/vue-router@3.0.1/dist/vue-router.js"></script>
            <script>
              // 컴포넌트 내용 정의
              var Body = { template: "<div>This is Body</div>" };
              var Header = { template: "<div>This is Body</div>" };
              var Footer = { template: "<div>This is Body</div>" };
        
              //라우터 정의
              var router = new VueRouter({
                routes: [
                  {
                    past: "/",
                    default: Body,
                    header: Header,
                    footer: Footer,
                  },
                ],
              });
        
              //라우터 등록
              var app = new Vue({
                router,
              }).$mount("#app");
            </script>
          </body>
        </html>
        
        ```
    
        - 네임드 뷰 실행 순서
          - 먼저 `<div>`  태그 안에 `<router-view>`를 3개 추가하고 name 속성을 추가한다 여기서 name 속성은 아래 components 속성에 정의하는 컴포넌트와 매칭하기 위한 속성이다. Header 컴포넌트는 header, Footer 컴포넌트는 footer를 각각 name 속성에 값으로 지정한다. 그리고 name 속성이 없는 두 번째 `<router-view>`는 default로 표시될 컴포넌트
          - 이제 `<script>`로 넘어가서 Body, Header, Footer 컴포넌트의 내용이 담길 객체를 선언한다. 각 컴포넌트 내용에는 컴포넌트 영역이 구분될 수 있게 간단한 template 속성을 추가한다
          - 그리고 앞의 네스티드와 다르게 이번엔 라우터를 하나 생성하고 라우터 정보를 바로 그 안에 정의한다.
          - URL 기본값인 '/'을 지정한다
          - components는 앞에서 `<router-view>`에 정의한 name 속성에 따라 표시될 컴포넌트를 정의하는 속성이다.
          - 마지막 인스턴스 생성
        - name 속성에 사용한 값은 예약어가 아니라 사용자가 임의로 정의할 수 있는 값이다. 이름 바꿔도 동일하게 동작한다. 예외적으로 name 속성을 지정하지 않았을 때의 기본 컴포넌트는 default로 접근한다.

​								

​					

#### 뷰 HTTP 통신

- HTTP(hypertext transfer protocol)는 **브라우저와 서버 간에 데이터를 주고받는 통신 프로토콜**이다.

- ajax

  - 서버에서 받아온 데이터를 표시할 때 화면 전체를 갱신하지 않고도 화면 전체를 갱신하지 않고도 화면의 일부분만 변경할 수 있게 하는 자바스크립트 기법이다.
  -  뷰 리소스 - 뷰 프레임워크 필수 라이브러리, 엑시오스
  - 뷰 리소스는 2016년 말에 에반이 공식적인 지원을 중단하기로 결정 
  - 엑시오스는 현재 뷰 커뮤니티에서 가장 많이 사용되는 HTTP 통신 라이브러리이다. 
  - 엑시오스는 Promise 기반의 API 형식이 다양하게 제공되어 별도의 로직을 구현할 필요 없이 주어진 API만으로도 간편하게 원하는 로직을 구현할 수 있다. 
    - Promise 기반의 API 형식
      - Promise란 서버에 데이터를 요청하여 받아오는 동작과 같은 비동기 로직 처리에 유용한 자바스크립트 객체이다.
      - 자바스크립트는 단일 스레드로 코드를 처리하기 때문에 특정 로직의 처리가 끝날때까지 기다려주지 않는다. 
      - 따라서 데이터를 요청하고 받아올 때까지 기다렸다가 화면에 나타내는 로직을 실행해야 할 때 주로 Promise를 활용한다.
  
- 엑시오스 API 형식

  - `axios.get('URL 주소').then().catch()`
    - 해당 URL 주소에 대해 HTTP GET 요청을 보낸다. 서버에서 보낸 데이터를 정상적으로 받아오면 then() 안에 정의한 로직이 실행되고 데이터를 받아올 때 오류가 발생하면 catch()에 정의한 로직이 수행된다
  - `axios.post('URL 주소').then().catch()`
    - 해당 URL 주소에 대해 HTTP POST 요청을 보낸다. 
  - Axis({ 옵션 속성 })
    - HTTP 요청에 대한 자세한 속성들을 직접 정의하여 보낼 수 있다.
  
  ```html
  <!DOCTYPE html>
  <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta http-equiv="X-UA-Compatible" content="IE=edge" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <title>Document</title>
    </head>
    <body>
      <div id="app">
        <button v-on:click="getData">프레임워크 목록 가져오기</button>
      </div>
      <script src="https://cdn.jsdelivr.net/npm/vue@2.5.2/dist/vue.js"></script>
      <!--axios cdn-->
      <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
      <script>
        new Vue({
          el: "#app",
          methods: {
            getData: function () {
              axios
                .get(
                  "https://raw.githubusercontent.com/joshua1988/doit-vuejs/master/data/demo.json"
                )
                .then(function (response) {
                  console.log(response);
                });
            },
          },
        });
      </script>
    </body>
  </html>
  ```
  
  