### Happy Web

HTML => 구조, CSS => 표현, Javascript => 동작

- 웹 사이트는 브라우저를 통해 동작함
- 브라우저마다 동작이 약간씩 달라서 문제가 생기는 경우가 많음(파편화)
- 해결책으로 웹 표준이 등장
- 크롬을 쓰자
- 웹 표준
  - 웹에서 표준적으로 사용되는 기술이나 규칙
  - 어떤 브라우저든 웹 페이지가 동일하게 보이도록 함(크로싱 브라우징)
  - 구글, 마이크로소프트, 애플, 모질라

### 환경설정

- HTML/CSS 코드 작성을 위한 VS code 추전 확장 프로그램
  - Open in browser
  - Auto rename tag
  - Highlight Matching Tag
  - Public Document - "Web 사전 준비사항 " 확인
    - \[https://abit.ly/ssafy9-document]

### HTML

- 웹 페이지를 작성(구조화)하기 위한 언어
- .html (HTML 파일)

- Hypertext Markup language
  - 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어
  - Hyper Text란?
    - 참조(하이퍼링크)를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트(위키백과)
  - Markup language
    - 구조를 나타내는 언어
    - 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어

- HTML Global Attribute
  - 모든 HTML 요소가 공통으로 사용할 수 있는 대표적인 속성
    - id: 문서 전체에서 유일한 고유 식별자 지정
    - class: 공백으로 구분된 해당 요소의 클래스의 목록(css, js에서 요소를 선택하거나 접근)
    - data-* :페이지에 개인 사용자 정의 데이터를 저장하기 위해 사용
    - style: inline 스타일
    - title: 요소에 대한 추가 정보 지정
    - Tabindex: 요소의 탭 순서

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charest = "UTF-8">
  <title>Document</title>
</head>  
<body>
  <!-- 이것은 주석입니다. -->
  <h1>
    나의 첫번째 HTML
  </h1>
  <p>
    이것은 본문입니다.
  </p>
  <span>
    이것은 인라인요소
  </span>
  <a href="https://www.naver.com"> 네이버로 이동!!</a>
  </body>  
</html>
```



### HTML 기본 구조

- html : 문서의 최상위(root) 요소

- head : 문서 **메타데이터(데이터를 위한 데이터- 사진 데이터(사진 찍으면 그 사진을 설명하는 데이터))** 요소

  - 문서 제목, 인코딩, 스타일, 외부 파일 로딩 등
  - 일반적으로 브라우저에 나타나지 않는 내용
  - title: 브라우저 상단 타이틀

  ```html
  <!DOCTYPE html>
  <html>
    <head>
      <title>HTML 기초</title>
    </head>
    <body>
      HTML 기초
    </body>
  </html>
  ```

  

  - meta: 문서 레벨 메타데이터 요소

    - 메타 데이터를 표현하는 새로운 규약

      - HTML 문서의 메타 데이터를 통해 문서의 정보를 전달
      - 메타정보에 해당하는 제목, 설명 등을 쓸 수 있도록 정의

      ```html
      <meta property= "og:title" content = "Google 뉴스">
      <meta name = "og:description" content = "Google 뉴스가 전세계 매체로부터 종합한 최신 뉴스">
      <meta property= "og:site_name" content = "Google 뉴스">
      <meta property= "og:url" content = "https://news.google.com">
      <meta property= "og:type" content = "website">
      <meta property= "og:image" content = "https://lh3.googleusercontent.com/J6_coFoegx">
      ```

      

- body: 문서 본문 요소

  - 실제 화면 구성과 관련된 내용
  - HTML 요소는 시작 태그와 종료 태그 그리고 태그 사이에 위치한 내용으로 구성
    - 요소는 태그로 컨텐츠를 감싸는 것으로 그 정보의 성격과 의미를 정의
    - 내용이 없는 태그들도 존재(닫는 태그가 없음)
      - br(뛰어쓰기), hr(수평선), img, input, link, meta 

  - 요소는 중첩될 수 있다
    - 요소의 중첩을 통해 하나의 문서를 구조화
    - 여는 태그와 닫는 태그의 쌍을 잘 확인해야함
      - 오류를 반환하는 것이 아닌 그냥 레이아웃이 깨진 상태로 출력되기 때문에, 디버깅이 힘들어 질 수 있음.

- 속성(attribute)
  - `<a href(속성 명)= "https://google.com"-속성 값></a>`
  - 공백은 No! "쌍따옴표 사용"
  - 속성을 통해 태그의 부가적인 정보를 설정할 수 있다
  - 요소는 속성을 가질 수 있으며, 경로나 크기와 같은 추가적인 정보를 제공
  - HTML Global Attribute
    - 모든 HTML 요소가 
- 렌더링(Rendering)
  - 웹사이트 코드를 사용자가 보게 되는 웹 사이트로 바꾸는 과정
  - 어떤 화면을 만드는 것
- DOM(Document Object Model) 트리
  - 텍스트 파일인 HTML 문서를 브라우저에서 렌더링 하기 위한 구조
    - HTML 문서에 대한 모델을 구성함
    - HTML 문서 내의 각 요소에 접근/ 수정에 필요한 프로퍼티와 메서드를 제공함
- 인라인 / 블록 요소
  - HTML 요소는 크게 인라인 / 블록 요소로 나눔
  - 인라인 요소는 글자처럼 취급
  - 블록 요소는 한 줄 모두 사용
- 텍스트 요소

|            태그            |                             설명                             |
| :------------------------: | :----------------------------------------------------------: |
|          <a></a>           |   Href 속성을 활용하여 다른 URL로 연결하는 하이퍼링크 생성   |
| <b></b>, <strong></strong> | 굵은 글씨 요소, 중요한 강조하고자 하는 요소 9보통 굵은 글씨로 표현) |
|     <i></i>, <em></em>     | 기울임 글씨 요소, 중요한 강조하고자 하는 요소 (보통 기울임 글씨로 표현) |
|            <br>            |                   텍스트 내에 줄 바꿈 생성                   |
|           <img>            | src 속성을 활용하여 이미지 표현, alt 속성을 활용하여 대체 텍스트 |
|       <span></span>        |                  의미 없는 인라인 컨테이너                   |

- 그룹 컨텐츠

|           태그            |                             설명                             |
| :-----------------------: | :----------------------------------------------------------: |
|          <p></p>          |                    하나의 문단(paragraph)                    |
|           <hr>            | 문단 레벨 요소에서의 주제의 분리를 의마하며 수평선으로 표현됨 |
|   <ol></ol>, <ul></ul>    |            순서가 있는 리스트, 순서가 없는 리스트            |
|        <pre></pre>        | HTML에 작성한 내용을 그대로 표현, 보통 고정폭 글꼴이 사용되고 공백문자를 유지 |
| <blockquote></blockquote> |     텍스트가 긴 인용문 주로 들여쓰기를 한 것으로 표현됨      |
|        <div></div>        |                 의미 없는 블록 레벨 컨테이너                 |



```html
<!DOCTYPE html>
<html>
 <head>
   <title>HTML 기초</title>
  </head>
  <body>
    <!-- 태그간의 띄어쓰기, 엔터는 동작하지 않아 X -->
    <! -- a태그(ancher) -->
    <a href = "https://google.com">구글</a>
    <!-- b(bold) -->
    <b>굵은 글씨</b>&nbsp;&nbsp;&nbsp;&nbsp;
    <strong>강한 글씨?</strong>
    <!-- i태그(italic) -->
    <i>이탤릭</i><br><br><br><br><br><br><br>
    <em>강한 글씨?</em>
    <img src "보노보노 사진"
         alt = "보노보노" #대체 텍스트 생성
    <!-- heading --> 글씨 키우는 용도로 쓰면 안 돼
    <h1>H1</h1>
    <h2>H2</h2>
    <h6>H6</h6>
    <p>
      문단문단
    </p>
   #!-- ol, ul ==>
		<ol>
      <li>순서가 있음</li>
      <li>순서가 있음</li>
    </ol>
		<ul>
      
      <li>순서가 없음</li>
    </ul>
    <p>
     기본 기본 기본
      우아우아<br>
    </p>
    <blockqutoe>
      인용문?
    </blockqutoe>
    <div>
      
      ???
    </div>
  </body
</html>
```

### CSS

- Cascading Style Sheet

  - 위에서 아래로 흐르면서 스타일을 입혀준다
  - 스타일을 지정하기 위한 언어
  - 선택하고, 스타일을 지정한다
  - css 구문은 선택자를 통해 스타일을 지정할 HTML 요소를 선택한다
  - 중괄호 안에서는 속성과 값, 하나의 쌍으로 이루어진 선언을 진행
  - 각 쌍은 선택한 요소의 속성, 속성에 부여할 값을 의미한다
    - 속성:어떤 스타일 기능을 변경할지 결정한다
    - 값: 어떻게 스타일 기능을 변경할지 결정한다.

  ```css
  h1 {
    color: blue;
    font-size: 15px;
  }
  ```

  ```html
  #css 정의 방법 -2 
  <!DOCTYPE html>
  <html>
    <head>
      <title>제목</title>
      <style>
        h1{
          color:blue;
          font_size:15px;
        }   
      </style>
    </head>
     
    <body>
      <h1>
     	H1!
      </h1>
    </body>
  </html>
  ```

  ```html
  #css 정의 방법 - 3 (외부 참조)
  외부 css 파일을 <head> 내 <link>를 통해 불러온다.
  <!DOCTYPE html>
  <html lang="en">
    <head>
      <title>mySite</title>
      <link rel="Stylesheet" href="mystyle.css"
    </head>
      <h1>
        This is my site
      </h1>
    </html>
  ```

  - **css에서는 작성 순서가 의미 없고 선언된 순서가 중요해**
  - css는 선택해서 스타일을 적용한다
  - 적용에는 우선순위가 있다, 같은 레벨이라면 나중에 '선언' 된 것이 적용된다
  - id, class, 태그는 서로 다른 레벨이다.
  - id > class > 태그 순으로 우선순위를 가진다. 
  - 다만 일반적으로 CSS 스타일링은 클래스로만 한다.
  - id는 잘 활용하지 않고, JS로 개발할 때 보통 활용된다. id는 문서에서 반드시 한번만 등장해야 한다.

  - CSS with 개발자 도구

    - Styles: 해당 요소에 선언된 모든 CSS
    - Computed:해당 요소에 최종 계산된 CSS
    - 웹페이지 오른쪽 버튼 검사 버튼 누르면 볼 수 있다.

  - CSS 기초 선택자

    - 요소 선택자

      - HTML 태그를 직접 선택

    - 클래스 선택자

      - 마침표(.)로 시작하며, 해당 클래스가 적용된 항목을 선택

      ```html
      .title-brown { # 같은 클래스라면 나중에 선언된 것이 적용된다
      	color: brown;
      }
      
      .title-blue {
      	color: blue;
      }
      
      <h1 class = "title-brown title-brown"> #여기에 작성된 순서는 의미 없다.
        H1! 갈색
      </h1>
      ```

      

    - 아이디 선택자

      - #문자로 시작하며, 해당 아이디가 적용된 항목을 선택
      - 일반적으로 하나의 문서에 1번만 사용
      - 여러 번 사용해도 동작하지만, 단일 id를 사용하는 것을 권장