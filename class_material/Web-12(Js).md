## 자바스크립트

- DOM 조작

```html
<script>
	console.log('hello, js!')
  alert('Js 학습이 시작되었습니다.')
</script>

<script>
	console.log('hello, js!')
  <!-- h1요소를 만들고 -->
  const title = document.createElement('h1') 
  <!--텍스트를 추가-->      
  title.innerText = "JS기초" <이름 변경>
  <!-- 선택자로 body 태그를 가져와서 -->  
  const body = document.querySelector('body')
  <!-- body 태그에 자식 요소로 추가-->
  body.appendChild(title)
</script>

<body>
  <h1 id="title">Js 기초</h1>
  <h2>DOM 조작</h2>
  <p class="text">querySelector</p>
  <p class="text">querySelectorAll</p>
</body>

const title = document.createElement('h1')
<!--a태그 생성-->
const a = document.createElement('a')
alert
a.innerText = "구글로 떠나기"
const body = document.queryselector('body')
body.appendchild(a)

title.innertext ="변경하고 싶은 제목"
<!--보안적 이슈 대문에 innerHTML은 사용하지 않는다-->
title.innerHTML = '<h2>우왕</h2>'
<!-- 노드 아래 있는 child를 삭제-->
body.removechild("삭제할 부분")
<!-- 타이틀 삭제-->
title.remove()
```

- 개발자도구를 눌러서 console에서 조작 가능

- Window.print() -프린트

- Window.confirm('가입하시겠습니까?')

- const

  - JS 변수 선언 키워드

  - 변경 불가능
  - 객체를 바꾼거지 객체의 속성을 바꾼 것이 아니다

- Iet

  - JS 변수 선언 키워드
  - 변경 가능

- document.querySelector와 querySelectorAll의 차이는 querySelector는 **반드시 하나만 반환하고**  querySelectorAll은 **모든 결과를 반환한다.** 

- ID는 하나만 선언하고 class는 많이 선언해도 된다. 
  - getElementByID, getElementsByClassName

```html
<!-- attribute-->
<style>
  .red {
    color: red;
  }
  .blue {
    color: blue;
  }
</style>
<body>
 
  <h1 class="red">
    안녕하세요
  </h1>

<script>
  <!-- a tag조작-->
	const a = document.createElement('a')
  a.innerText = "실라버스"
  const body = document.querySelector('body')
  body.appendChild(a)
  <!--링크를 제작-->
  a.setAttribute('href', 'https://syllaverse.com')
  
 	<!-- h1 tag 조작-->
  const h1 = document.querySelector('h1')
  console.log(h1.classList)
</script>
</body>
<개발자 도구 console에서))
console.log(a.getAttribute('href'))

     
const h1 = document.querySelector('h1')
h1
h1.getaAttribute('class')
h1.setAttribute('class', 'blue')     
h1.classLIst
h1.classList.replace('red', 'blue')
```

- 클래스를 여러개를 주고 싶다면?
  - classList를 사용하면 적용되는 클래스를 클래스 목록을 따로따로 배열 형식으로 담아서 준다



### 자료공유 활용한 정리

- 브라우저(browser)

  - URL로 웹(WWW)을 탐색하며 서버와 통신하고,

  - HTML 문서나 파일을 출력하는 GUI 기반의 소프트웨어

  - 인터넷의 컨텐츠를 검색 및 열람하도록 함

  - "웹 브라우저"라고도 함

  - 주요 브라우저
    - Google Chrome, Mozilla Firefox, Microsft Edge, Opera, Safari

- JavaScript의 필요성
  - 브라우저 화면을 '동적'으로 만들기 위함
  - 브라우저를 조작할 수 있는 유일한 언어
- JavaScript의 탄생
  - 1994년 당시 넷스케이프 커뮤니케이션스사의 Netscape Navigator(NN) 브라우저가 전세 계 점유율을 80% 이상 독점하며 브라우저의 표준 역할을 한다.
  - 당시 넷스케이프에 재직 중이던 브랜던 아이크가 HTML을 동적으로 동작하기 위한 회사 내부 프로젝트를 진행 중 JS를 개발
  - Javascript 이름 변천사
    - Mocha -> LiveScript -> JavaScript (1995)
  - 그러나 1995년 경쟁사 마이크로스프트에서 이를 채택하여 커스터마이징한 JScript를 만듦
  - 이를, IE 1.0 에 탑재 ->1차 브라우저 전쟁의 시작

- 제1차 브라우저 전쟁
  - 넷스케이프 vs 마이크로소프트 (이하 MS)
  - 빌 게이츠 주도하에 MS는 1997년 IE 4를 발표하면서 시장을 장악하기 시작
    - 당시 윈도우 OS의 시장 점유율은 90%
    - 글로벌 기업 MS의 공격적인 마케팅
  - MS의 승리로 끝나며 2001년부터 IE의 점유율은 90%를 상회
  - 1998년 넷스케이프에서 나온 브랜던 아이크 외 후계자들은 모질라 재단을 설립
    - 파이어폭스를 통해 IE에 대항하며 꾸준히 점유율을 올려 나감
- 제2차 브라우저 전쟁
  - MS vs Google
  - 2008년 Google의 Chrome(이하 크롬) 브라우저 발표
  - 2011년 3년 만에 파이어폭스의 점유율을 돌파 후 2012년부터 전 세계 점유율 1위 등록
  - 크롬의 승리 요인
    - 압도적인 속도
    - 강력한 개발자 도구 제공
    - 웹 표준
- 파편화와 표준화
  - 제 1차 브라우저 전쟁 이후 수많은 브라우저에서 자체 자바스크립트 언어를 사용하게 됨
  - 결국 서로 다른 자바스크립트가 만들어지면서 크로스 브라우징 이슈가 발생하여 웹 표준의 필요성이 제기
  - 크로스 브라우징
    - W3C에서 채택된 표준 웹 기술을 채용하여 각각의 브라우저마다 다르게 구현되는 기술을 비슷하게 만들되, 어느 한쪽에 치우치지 않도록 웹 페이지를 제작하는 방법론(동일성이 아닌 동등성)
    - 브라우저마다 렌더링에 사용되는 엔진이 다르기 때문
- 파편화와 표준화
  - 1996년부터 넷스케이프는 표준 제정의 필요성을 주장
    - ECMA 인터내셔널(정보와 통신 시스템을 위한 국제적 표준화 기구)에 표준 제청 요청
  - 1997년부터 ECMAScript 1 (ES1) 탄생
  - 제1차 브라우저 전쟁 이후 제기된 언어의 파편화를 해결하기 위해 각 브라우저 회사와 재단은 표준화에 더욱 적극적으로 힘을 모으기 시작
- 2015년 ES2015 (ES6) 탄생
  - "Next-gen of JS"
  - JavaScript의 고질적인 문제들을 해결
  - JavaScript의 다음 시대라고 불릴 정도로 많은 혁신과 변화를 맞이한 버전
  - 이때부터 버전 순서가 아닌 출시 연도를 붙이는 것이 공식 명칭이나 통상적으로 ES6라 부른다
  - 현재는 표준 대부분이 ES6+로 넘어옴
- Vanilla JavaScript
  - 크로스 브라우징, 간편한 활용 등을 위해 많은 라이브러리 등장(JQuery 등)
  - ES6 이후, 다양한 도구의 등장으로 순수 자바스크립트 활용의 증대

### DOM(Document Object Model)

- DOM 조작
  - 문서(HTML) 조작
- BOM 조작
  - navigator, screen, location, frames, history, XHR
- JavaScript Core

- DOM
  - HTML, XML과 같은 문서를 다루기 위한 문서 프로그래밍 인터페이스
  - 문서를 구조화하고 구조화된 구성 요소를 하나의 객체로 취급하여 다루는 논리적 트리 모델
  - 문서가 구조화되어 있으며 각 요소는 객체로 취급
  - 단순한 속성 접근, 메서드 활용뿐만 아니라 프로그래밍 언어적 특성을 활용한 조작 가능
- 주요 객체
  - Window: DOM을 표현하는 창. 가장 최상위 객체
  - document: 페이지 컨텐츠의 Entry Point역할을 하며, `<body>` 등과 같은 수많은 다른 요소들을 포함
  - navigator, location, history, screen

- DOM-해석
  - 파싱
    - 구문 분석, 해석
    - 브라우저가 문자열을 해석하여 DOM Tree로 만드는 과정
- BOM 이란
  - Browser Object Model
  - 자바스크립트가 브라우저와 소통하기 위한 모델
  - 브라우저의 창이나 프레임을 추상화해서 프로그래밍적으로 제어할 수 있도록 제공하는 수단
    - 버튼, URL 입력창, 타이틀 바 등 브라우저 윈도우 및 웹페이지 일부분을 제어 가능
  - Window 객체는 모든 브라우저로부터 지원받으며 브라우저의 창(window)를 지칭

- BOM 조작

```html
<!--탭 함-->
window.open()
<!--인쇄 창-->
window.print()
<!--메시지 확인, 취소 버튼이 있는 대화상자 창-->
window.confirm()
<!--document도 브라우저 내에 종속되어 있기 때문에 window 전역 객체에 포함-->
window.document
```

- 브라우저와 그 내부의 문서를 조작하기 위해 ECMAScript(JS)를 학습



### DOM 조작

- Document는 문서 한 장(HTML)에 해당하고 이를 조작

- DOM 조작 순서

  - 선택
  - 변경

- 객체의 상속 구조

  - EventTarget
    - Event Listener를 가질 수 있는 객체가 구현하는 DOM 인터페이스

  - Node
    - 여러 가지 DOM 타입들이 상속하는 인터페이스
  - Element 
    - Document 안의 모든 객체가 상속하는 가장 범용적인 인터페이스
    - 부모인 Node와 그 부모인 EventTarget의 속성을 상속
  - Document
    - 브라우저가 불러온 웹 페이지를 나타냄
    - DOM 트리의 진입점(entry point) 역할을 수행
  - HTMLElement
    - 모든 종류의 HTML 요소
    - 부모 element의 속성 상속

- DOM 선택 - 선택 관련 메서드(1/2)

  - document.querySelector(selector)
    - 제공한 선택자와 일치하는 element 하나 선택
    - 제공한 CSS selector를 만족하는 첫 번째 element 객체를 반환 (없다면 null)
  - Document.querySelectorAll(selector)
    - 제공한 선택자와 일치하는 여러 element를 선택
    - 매칭 할 하나 이상의 셀렉터를 포함하는 유효한 CSS selector를 인자(문자열)로 받음
    - 지정된 셀렉터에 일치하는 NodeList를 반환

- DOM 선택 - 선택 관련 메서드 (2/2)

  - getElementById(id)
  - getElementsByTagName(name)
  - getElementsByClassName(names)

- querySelector(), querySelectorAll()을 사용하는 이유

  - id, class 그리고 tag 선택자 등을 모두 사용 가능하므로, 더 구체적이고 유연하게 선택 가능
  - ex) document.querySelector('#id'), document.querySelectAll('.class')

- DOM 선택 - 선택 메서드별 반환 타입

  - 단일 element
    - `getElementById()`
    - **querySelector()**
  - HTMLCollection
    - `getElementByTagName()`
    - `getElementByClassName()`
  - NodeList
    - **querySelectorAll**

- DOM 선택 - HTMLCollection & NodeList
  - 둘 다 배열과 같이 각 항목에 접근하기 위한 index를 제공(유사 배열)
  - HTMLCollection
    - name, id, index 속성으로 각 항목에 접근 가능
  - NodeList
    - index로만 각 항목에 접근 가능
    - 단, HTMLCollection과 달리 배열에서 사용하는 forEach 메서드 및 다양한 메서드 사용 가능
  - 둘 다 Live Collection으로 DOM의 변경사항을 실시간으로 반영하지만, **querySelectorAll()** 에 의해 반환되는 NodeList는 Static Collection으로 실시간으로 반영되지 않음.
- DOM 선택 - Collection
  - Live Collection
    - 문서가 바뀔 때 실시간으로 업데이트 됨
    - DOM의 변경사항을 실시간으로 collection에 반영
    - Ex) HTMLCollection, NodeList
  - Static Collection(non-live)
    - DOM이 변경되어도 collection 내용에는 영향을 주지 않음
    - querySelectorAll()의 반환 NodeList만 stactic collection
- DOM 변경 - 변경 관련 메서드(Creation)
  - document.createElement()
    - 작성한 태그 명의 HTML 요소를 생성하여 반환
  - Element.append()
    - 특정 부모 Node의 자식 NodeList 중 마지막 자식 다음에 Node 객체나 DOMString을 삽입
    - 여러 개의 Node 객체, DOMString을 추가 할 수 있음
    - 반환 값이 없음
  - Node.appendChild()
    - 한 노드를 특정 부모 노드의 자식 노드리스트 중 마지막 자식으로 삽입(node만 추가 가능)
    - 한번에 오직 하나의 노드만 추가할 수 있다
    - 만약 주어진 노드가 이미 문서에 존재하는 다른 노드를 참조한다면 새로운 위치로 이동
- ParentNode.append() vs Node.appendChild()
  - append()를 사용하면 DOMString 객체를 추가할 수도 있지만, .appendChild()는 Node 객체만 허용
  - append()는 반환 값이 없지만, appendChild()는 추가된 Node 객체를 반환
  - Append()는 여러 Node 객체와 문자열을 추가할 수 있지만, .appendChild()는 하나의 Node객체만 추가할 수 있다. 
- DOM 변경 - 변경 관련 속성
  - Node.innerText
    - Node 객체와 그 자손의 텍스트 컨텐츠(DOMString)를 표현(해당 요소 내부의 raw text) (사람이 읽을 수 있는 요소만 남김)
    - 즉, 줄 바꿈을 인식하고 숨겨진 내용을 무시하는 등 최종적으로 스타일링이 적용된 모습으로 표현
  - Element.innerHTML
    - 요소(element) 내에 포함된 HTML 마크업을 반환
    - XSS 공격에 취약하므로 사용 시 주의
- XSS (Cross-site Scripting)
  - 공격자가 입력요소를 사용하여 웹 사이트 클라이언트 측 코드에 악성 스크립트를 삽입해 공격하는 방법
  - 피해자(사용자)의 브라우저가 악성 스크립트를 실행하며 공격자가 엑세스 제어를 우회하고 사용자를 가장 할 수 있도록 함

- DOM 삭제 - 삭제 관련 메서드
  - ChildNode.remove()
    - Node가 속한 트리에서 해당 Node를 제거
  - Node.removeChild()
    - DOM에서 자식 노드를 제거하고 제거된 노드를 반환
    - 노드는 인자로 들어가는 자식 노드의 부모 노드
- DOM 속성 - 속성 관련 메서드
  - Element.setAttribute(name, value)
    - 지정된 요소의 값을 설정
    - 속성이 이미 존재하면 값을 갱신, 존재하지 않으면 지정된 이름과 값으로 새 속성을 추가
  - Element.getAttribute(attributeName)
    - 해당 요소의 지정된 값(문자열)을 반환
    - 인자(attributeName)는 값을 얻고자 하는 속성의 이름
- 정리
  - 선택한다
    - querySelector()
    - querySelectorAll()
  - 변경(조작)한다.
    - innerText
    - innerHTML
    - element.style.color
    - setAttribute()
    - getAttribute()
    - createElement()
    - appendChild()

### 추가 문서 정리

- 자바스크립트는 동적으로 콘텐츠로 바꾸고, 멀티미디어를 제어하고, 애니메이션을 추가하는 등 거의 모든 것을 만들 수 있는 스크립팅 언어이다. 

- 자바스크립트는 예시

```css
<p>Player 1: Chris</p>

p {
  font-family: 'helvetica neue', helvetica, sans-serif;
  letter-spacing: 1px;
  text-transform: uppercase;
  text-align: center;
  border: 2px solid rgba(0, 0, 200, 0.6);
  background: rgba(0, 0, 200, 0.3);
  color: rgba(0, 0, 200, 0.6);
  box-shadow: 1px 1px 2px rgba(0, 0, 200, 0.4);
  border-radius: 10px;
  padding: 3px 10px;
  display: inline-block;
  cursor: pointer;
}

/* javascript 동작 부분 */
const para = document.querySelector('p');

para.addEventListener('click', updateName);

function updateName() {
  const name = prompt('Enter a new name');
  para.textContent = `Player 1: ${name}`;
}
```

- 자바스크립트로 할 수 있는 일들

  - 변수에 값을 저장할 수 있다. 바로 위의 예제를 보면, 요청해서 받은 새로운 이름으 name이라는 변수에 저장한다.

  - 프로그래밍에서 문자열이라고 부르는, 텍스트 조각을 조작한다. 위 예제에서는 문자열 "플레이어: "과 `name` 변수의 값을 합쳐 온전한 텍스트 레이블을 생성합니다.

  - 웹 페이지에서 발생하는 어떤 이벤트에 코드가 응답하도록 합니다. 예제에서는 `click`이벤트를 사용해서 레이블을 클릭하는 순간을 탐지하고, 그 후에 텍스트 레이블을 업데이트하고 있습니다.

  - 애플리케이션 프로그래밍 인터페이스(API)라고 부르는 이 기능들은 여러분의 JavaScript 코드에서 사용할 수 있는 강력한 마법을 추가로 제공한다.

  - 브라우저는 여러부느이 코드(HTML, CSS, JavaScript)를 실행 환경(브라우저 탭)에서 실행합니다.

  - 프로그래밍에서의 **인터프리터**와 **컴파일러**라는 단어를 들어본 적이 있는지 생각해보세요. 인터프리터를 사용하는 언어에서는 코드를 위에서 아래로 실행하고, 코드 구동 결과는 즉시 반환됩니다. 브라우저에서 JavaScript 코드를 실행하기 전에 다른 형태로 변환할 필요가 없다는 점을 기억하세요. 코드는 프로그래머가 읽을 수 있는 형태로 입력되고, 별도의 처리 없이 그대로 실행됩니다.

    반면, 컴파일러를 사용하는 컴파일 언어에서는 컴퓨터가 코드를 실행하기 전에 다른 형태로 변환(컴파일)해야 합니다. 예를 들어, C/C++에서는 코드를 컴파일러로 기계언어로 변환하여, 그 결과를 컴퓨터가 실행합니다. 프로그램은 프로그램의 원본 소스 코드에서 생성한 이진 형식(바이너리)으로부터 실행됩니다.

  -  모던 JavaScript 인터프리터들은 사실 **JIT 컴파일**(just-in-time 컴파일)이라는 기술을 사용해 성능을 향상하기는 합니다. 스크립트의 실행과 동시에 소스 코드를 더 빠르게 실행할 수 있는 이진 형태로 변환하여 최대한 높은 실행 속도를 얻는 방법입니다

- 변수

  - JavaScript 식별자는 문자, 밑줄 (`_`) 혹은 달러 기호 (`$`)로 시작해야 하는 반면 이후는 숫자 (`0`–`9`) 일 수도 있습니다.

    JavaScript가 대소문자를 구분하기에, 문자는 "`A`"부터 "`Z`" (대문자)와 "`a`"부터 "`z`" (소문자)까지 모두 포함합니다.

  - 적절한 이름으로는 `Number_hits`, `temp99`, `$credit` 및 `_name` 등 입니다.

  - `var x = 42`와 같이 [`var`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/var) 키워드로 변수를 선언할 수 있습니다. 이 구문은 실행 맥락에 따라 **지역 및 전역 변수**를 선언하는데 모두 사용될 수 있습니다.

  - `let y = 13`와 같이 [`const`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/const) 혹은 [`let`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/let) 키워드로 변수를 선언할 수 있습니다. 이 구문은 블록 스코프 지역 변수를 선언하는데 사용될 수 있습니다. 아래 [변수 스코프](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Grammar_and_types#변수_스코프)를 참고하세요.

  - 구조 분해 할당 구문을 사용하여 [객체 리터럴](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Grammar_and_types#객체_리터럴)에서 값을 풀기 위해 변수를 선언할 수 있습니다. 예를 들면, `let { bar } = foo`. 이 구문은 `bar`라는 이름의 변수를 생성하고 `foo` 객체에 있는 동일한 이름의 키에 해당하는 값을 변수에 할당합니다.

  - 간단히 변수에 값을 할당 할 수도 있습니다. 예를 들어, `x = 42` 와 같은 구문은 [**선언되지 않은 전역변수**](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/var#설명)를 만듭니다. 뿐만 아니라, 자바스크립트의 엄격한 경고를 만들어냅니다. 선언되지 않은 전역변수는 의도되지 않은 동작을 만들어내고는 합니다. 따라서 선언되지 않은 전역변수를 사용하면 안됩니다.

- 변수 할당

  - 지정된 초기 값 없이 `var` 혹은 `let` 문을 사용해서 선언된 변수는 `undefined` 값을 갖습니다.
  - 선언되지 않은 변수에 접근을 시도하는 경우 `ReferenceError` 예외가 발생한다.

  ```js
  var a;
  console.log('a 값은 ' + a); // a 값은 undefined
  
  console.log('b 값은 ' + b); // b 값은 undefined
  var b;
  // 이것은 아래의 '변수 호이스팅'을 읽기 전에는 혼란스러울 수 있음
  
  console.log('c 값은 ' + c); // Uncaught ReferenceError: c is not defined
  
  let x;
  console.log('x 값은 ' + x); // x 값은 undefined
  
  console.log('y 값은 ' + y); // Uncaught ReferenceError: y is not defined
  let y;
  ```

  - `undefined`를 사용하여 변수 값이 있는지 확인할 수 있습니다. 아래 코드에서, `input` 변수는 값이 할당되지 않았고 [`if`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/if...else)문은 `true`로 평가합니다.

  ```js
  var input;
  if(input === undefined) {
    doThis();
  } else {
    doThat();
  }
  ```

  - `undefined` 값은 불리언 맥락(context)에서 사용될 때 `false`로 동작합니다. 예를 들어, 아래 코드는 `myArray` 요소가 `undefined`이므로 `myFunction` 함수를 실행합니다.

  - `undefined` 값은 수치 맥락에서 사용될 때 `NaN`으로 변환됩니다.

  - [`null`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Operators/null) 값을 평가할 때, 수치 맥락에서는 `0`으로, 불리언 맥락에서는 `false`로 동작합니다. 예를 들면,

  ```js
  var n = null;
  console.log(n * 32); // 콘솔에 0 으로 로그가 남음
  ```

  - 변수 스코프
    - ECMAScript 2015 이전의 JavaScript는 [블록 문](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Control_flow_and_error_handling#block_문) 스코프가 없습니다. 그래서 오히려, 블록 내에 선언된 변수는 그 블록 내에 존재하는 함수(혹은 전역 스코프)에 지역적입니다.

  - 그 이후에는 let을 선언을 사용하면 바뀐다.

  ```js
  if (true) {
    let y = 5;
  }
  console.log(y); // ReferenceError: y is not defined
  ```

  - **호이스팅 - 또 다른 JavaScript 변수의 특이한 점은 예외를 받지 않고도, 나중에 선언된 변수를 참조할 수 있다는 것입니다.**

  - ECMAScript 2015의 `let`과 `const`는 변수를 블록의 상단으로 **끌어올리지만 초기화하지 않습니다.** 변수가 선언되기 전에 블록 안에서 변수를 참조하게 되면 [`ReferenceError`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/ReferenceError)를 발생시키게 되는데, 변수는 블록 시작부터 선언이 처리될 때까지 "temporal dead zone"에 위치하게 되기 때문입니다.

  ```js
  console.log(x); // ReferenceError
  let x = 3;
  ```

  - 함수에서는 함수 선언으로는 호이스팅되지만 함수 표현식으로는 호이스팅 되지 않는다.

  ```js
  /* 함수 선언 */
  
  foo(); // "bar"
  
  function foo() {
    console.log('bar');
  }
  
  /* 함수 표현식 */
  
  baz(); // TypeError: baz is not a function
  
  var baz = function() {
    console.log('bar2');
  };
  ```

  - 상수

    - [`const`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/const) 키워드로 읽기 전용 상수를 만들 수 있습니다.
    - 상수 식별자의 구문은 변수 식별자와 같습니다. 문자, 밑줄이나 달러 기호 (`$`) 로 시작해야 하고 문자, 숫자나 밑줄을 포함할 수 있습니다.

    ```js
    const PI = 3.14;
    ```

    - 상수는 스크립트가 실행 중인 동안 대입을 통해 값을 바꾸거나 재선언될 수 없습니다. 값으로 초기화해야 합니다.
    - 상수에 대한 스코프 규칙은 `let` 블록 스코프 변수와 동일합니다. 만약 `const` 키워드가 생략된 경우에는, 식별자는 변수를 나타내는 것으로 간주됩니다.
    - 상수는 같은 스코프에 있는 함수나 변수와 동일한 이름으로 선언할 수 없다.

    ```js
    // 오류가 발생합니다
    function f() {};
    const f = 5;
    
    // 역시 오류가 발생합니다
    function f() {
      const g = 5;
      var g;
    
      //statements
    }
    ```

    - 그러나, 상수에 할당된 객체의 속성은 보호되지 않아서 다음의 문은 문제없이 실행된다.

      ```javascript
      const MY_OBJECT = {'key': 'value'};
      MY_OBJECT.key = 'otherValue';
      ```

    - 또한, 배열의 내용도 보호되지 않아서 다음의 문도 문제없이 실행됩니다.

      ```javascript
      const MY_ARRAY = ['HTML','CSS'];
      MY_ARRAY.push('JAVASCRIPT');
      console.log(MY_ARRAY); //logs ['HTML','CSS','JAVASCRIPT'];
      ```

    - 자료형 변환

      - JavaScript는 동적 형지정(정형) 언어입니다. 이는 변수를 선언할 때 데이터 형을 지정할 필요가 없음을 의미합니다. 또한 데이터 형이 스크립트 실행 도중 필요에 의해 자동으로 변환됨을 뜻합니다.
      - 자바스크립트는 파이썬과 다르게 문자랑 숫자랑 더할 수 있다. 자동으로 문자열로 변환된다.
      - 다른 연산자를 포함한 식의 경우, JavaScript는 숫자 값을 문자열로 변환하지 않습니다. 예를 들면,

      ```javascript
      '37' - 7 // 30
      '37' + 7 // "377"
      ```

      

      - 문자열을 숫자로 변환하기
        - 숫자를 나타내는 값이 문자열로 메모리에 있는 경우, 변환을 위한 메서드가 있다.
        - `parseInt`는 오직 정수만 반환하므로, 소수에서는 사용성이 떨어집니다.
        - [`parseInt()`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/parseInt)
        - [`parseFloat()`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/parseFloat

    - 배열 리터럴

      - 배열 리터럴은 0개 이상의 식(expression) 목록입니다. 각 식은 배열 요소를 나타내고 대괄호(`[]`)로 묶입니다. 배열 리터럴을 사용하여 배열을 만들 때, 그 요소로 지정된 값으로 초기화되고, 그 `length`는 지정된 인수의 갯수로 설정됩니다.

      - 배열 리터럴에서 모든 요소를 지정할 필요는 없습니다. 만약 잇달아 두 개의 쉼표를 두면, 배열은 지정되지 않은 요소를 `undefined`로 채웁니다. 

        ```js
        let fish = ['Lion', , 'Angel'];
        ```

      - **만약 요소 목록을 후행(trailing) 쉼표로 끝낸다면, 그 쉼표는 무시됩니다.**

    - 조건문

      - If...else문

      ```js
      if (condition) {
        statement_1;
      } else {
        statement_2;
      }
      ```

      - Else... if

      ```js
      if (condition_1) {
        statement_1;
      } else if (condition_2) {
        statement_2;
      } else if (condition_n) {
        statement_n;
      } else {
        statement_last;
      }
      ```

      - 일반적으로는 `if`에 항상, 특히 `if` 문을 중첩할 때는 블록문을 함께 사용하는 것이 좋습니다.

      ```js
      if (condition) {
        statement_1_runs_if_condition_is_true;
        statement_2_runs_if_condition_is_true;
      } else {
        statement_3_runs_if_condition_is_false;
        statement_4_runs_if_condition_is_false;
      }
      ```

      - 또한 `if...else`의 조건에 "`x = y`"와 같은 할당은 지양하세요.
      - **참고:** `true`와 `false` 원시 값을 [`Boolean`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Boolean) 객체의 참과 거짓 값과 혼동하지 마세요!

      ```js
      const b = new Boolean(false);
      if (b)         // 참으로 평가
      if (b == true) // 거짓으로 평가
      ```

      - 다음 예제에서, 함수 `checkData`는 `Text` 객체에 포함된 문자의 수가 3이면 `true`를 반환합니다. 그렇지 않으면 경고를 표시한 후 `false`를 반환합니다.

      ```js
      function checkData() {
        if (document.form1.threeChar.value.length == 3) {
          return true;
        } else {
          alert(
            '정확히 세 글자를 입력하세요. ' +
            `${document.form1.threeChar.value}은(는) 유효하지 않습니다.`);
          return false;
        }
      }
      ```

      - `switch` 문은 프로그램이 표현식을 평가한 후, 그 값과 `case` 레이블의 값을 비교해 일치하는 `case`의 명령문을 실행합니다.

      ```js
      switch (expression) {
        case label_1:
          statements_1;
          break;
        case label_2:
          statements_2;
          break;
          …
        default:
          statements_default;
      }
      ```

      - swich문 평가
        - 우선 표현식(`expression`)의 결과와 일치하는 레이블을 가진 `case` 절을 찾아, 관련된 명령문을 실행합니다.
        - 일치하는 레이블을 찾지 못했으면 `defult`절을 탐색합니다.
          - `default` 절을 찾았으면 관련된 명령문을 실행합니다.
          - `default` 절을 찾지 못했으면 `switch` 문 바깥의 다음 명령문을 실행합니다.
          - (`default`를 마지막에 배치하는 것은 관습적인 것으로, 사실 위치는 상관 없습니다.
          - let, const 키워드로 선언한 변수는 모두 코드 블록(ex. 함수, if, for, while, try/catch 문 등)을 지역 스코프로 인정하는 블록 레벨 스코프를 따른다. var 키워드로 선언한 경우 5가 나왔지만, let 키워드로 선언한 경우 if 문 안에 있는 것은 지역 스코프를 가져 전역에서 console을 찍었을 경우, 전역에 있는 a가 결과 값으로 출력된다. (const 키워드도 let 키워드와 동일하게 동작한다)

​										



​					