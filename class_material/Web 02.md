### CSS 기본 스타일

- px(픽셀)
  - 모니터 해상도의 한 화소인 '픽셀' 기준
  - 픽셀의 크기는 변하지 않기 때문에 고정적인 단위
- %
  - 백분율 단위
  - 가변적인 레이아웃에서 자주 사용
- em
  - (바로 위, 부모 요소에 대한) 상속의 영향을 받음
  - 배수 단위, 요소에 지정된 사이즈에 상대적인 사이즈를 가짐
- rem
  - (바로 위, 부모 요소에 대한) 상속의 영향을 받지 않음
  - 최상위 요소(html)의 사이즈를 기준으로 배수 단위를 가짐
  - 루트 기반

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    .font-big {
      font-size: 36px;

    }
    .em {
      font-size: 2em; 
    }
    .rem {
      font-size: 2rem;<!-36px>
    }
  </style>
  <title>Document</title>
</head>
<body>
  <ul class="font-big">
    <li class="em">2em</li> <!--72px>
    <li class="rem">2rem</li> <!--36px>
    <li>no class</li> <!--36px>
  </ul>
  
</body>
</html>
```



- 크기 기반(viewport)
  - 웹 페이지를 방문한 유저에게 바로 보이게 하는 웹 컨텐츠의 영역 (디바이스 화면)
  - 디바이스의 viewport를 기준으로 상대적인 사이즈가 결정된다.
  - 예)vw, vh, vmin, vamx
- 색상 단위(background-color: red;)
  - 대소문자를 구분하지 않음
  - red, blue, black과 같은 특정 색을 직접 글자로 나타낸다.
- RGB 색상(background-color: rgb(0, 255, 0);)
  - 16진수 표기법 혹은 함수형 표기법을 사용해서 특정 색을 표현하는 방식
- HSL 색상(background-color: hsl(0, 100%, 50%);)
  - 색상, 채도, 명도를 통해 특정 색을 표현하는 방식

- 색상 단위

```html
p { color: black;}
p { color: #000;}
p { color: #000000;}
p { color: rgb(0, 0, 0)}
p { color: hsl(120, 100%, 0);}
p { color: rgba(0, 0, 0, 0.5);}
p { color: hsla(120, 100% 0.5);}



<!--모두 블랙 RGB 색상 - '#' + 16진수 표기법, rgb()함수형 표기법
HSL 색상(색상, 채도, 명도), a는 alpha(투명도)
-->
```



- CSS 문서 표현

  - 필요할때 MDN문서를 잘 찾아보자
  - 텍스트
    - 서체(font-family), 서체 스타일(font-style, font-weight 등)
    - 자간(letter-spacing), 단어 간격(word-spacing), 행간(line-height) 등

  - 컬러(color), 배경(background-image, background-color)
  - 기타 HTML 태그별 스타일링
    - 목록(li), 표(table)

### CSS Selectors

- 선택자 유형
  - 기본 선택자
    - 전체 선택자, 요소 선택자
    - 클래스 선택자, 아이디 선택자, 속성 선택자 
    - **클래스를 주자**
  - 결합자
    - 자손 결합자, 자식 결합자
    - 일반 형제 결합자, 인접 형제 결합자
  - 의사 클래스/요소(Pseudo Class)
    - 링크, 동적 의사 클래스
    - 구조적 의사 클래스, 기타 의사 클래스, 의사 엘리먼트, 속성 선택자
- 선택자 정리
  - 요소 선택자
    - HTML 태그를 직접 선택
  - 클래스 선택자
    - 마침표(.)문자로 시작하며, 해당 클래스가 적용된 항목을 선택
  - 아이디 선택자
    - ''#'' 문자로 시작하며, 해당 아이디가 적용된 항목을 선택
    - 일반적으로 하나의 문서에 1번만 사용
    - 여러 번 사용해도 동작하지만, 단일 id를 사용하는 것을 권장

- CSS 적용 우선순위
  - 1.중요도: 사용시 주의 (생태계 망가뜨려)
    - !important
  - 우선 순위 (Speicifify)
    - 인라인 > id > class, 속성, pseudo-class > 요소, pseudo-element
  - CSS 파일 로딩 순서

- CSS 상속

  - CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속한다.
    - 속성(프로퍼티) 중에는 상속이 되는 것과 되지 않는 것들이 있다.
    - 상속 되는 것 예시
      - 예) Text 관련 요소(font, color, text-align), opacity, visibility 등
    - 상속 되지 않는 것 예시
      - 예) Box model 관련 요소(width, height, margin, padding, border, box-sizing, display),
      - Position 관련 요소(position, top/right/bottom/left, z-index) 등
  - 개발자 도구를 보면 상속 몰라도 된다. - MDN에서 확인한다.
  - MDN에서 확인하기

  ```html
  <body>
    <p>
      안녕하세요! <span>테스트</span> 입니다.
    </p>
  </body>
  ```

  ```html
  <style>
    P {
      /* 상속됨 */
      color: red;
      /* 상속 안됨 */
      border: 3px solid black;
    }
    span {
    }
  </style>
  ```

  



### CSS BOX Model

- 원칙 1
  - 모든 요소는 **네모(박스모델)**이고, 위에서부터 아래로, 왼쪽에서 오른쪽으로 쌓인다**(좌측 상단에 배치)**
  - 모든 HTML 요소는 box 형태로 되어있다.
  - Inline Direction(한 줄 배치)
  - Block dircection(블럭)
  - Margin:
    - 테두리 바깥의 외부 여백 배경색을 지정할 수 없다.
  - Content:
    - 글이나 이미지 등 요소의 실제 내용
  - padding:
    - 테두리 안쪽의 내부 여백 요소에 적용된 배경색, 이미지는 padding까지 적용
  - Border:
    - 테두리 영역

- Box model 구성(margin/padding)

  ```html
  <!-- 상하좌우-->
  .margin-padding{
   margin: 10px;
   padding: 30px;
  }
  
  <!-- 공백을 10씩-->
  .margin-1{
   magrin: 10px;
  }
  
  <!-- 상하공백을 10 그리고 좌우 20씩-->
  .margin-2{
   margin:10px 20px;
  }
  
  <!-- 상 공백을 10 하 공백을 30 좌우 20-->
  .margin-3 {
   margin: 10px 20px 30px;
  }
  
  <!-- 상 공백을 10 우 공백을 20 하 공백을 30 좌 공백을 40 -->
  .margin-4 {
   margin: 10px 20px 30px 40px;
  }
  ```

- Box model 구성 (border)

```html
<!-- border너비 2px, border-style 지정, border 색깔 지정 -->
.border{
  border-width: 2px;
	border-style: dashed;
	border-color: black;
}
<!-- 한줄로 정리 가능-->
.border{
 border:2px, dashed, black;
}
```



- Box-sizing:

```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
      .box1 {
        width: 500px;
        border-width: 2px;
        border-color: green;
        border-style: dashed;
      padding-left: 50px;
      margin-bottom: 30px;
      }

      .box2 {
        width: 500px;
        border: 2px solid black;
      padding: 20px 30px;
      }
    </style>
  </head>
  <body>
    <div class="box1">div1</div>
    <div class="box2">div2</div>
  </body>
  </html>
```



```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .box{
      width: 100px;
      margin: 10px auto;
      padding: 20px;
      border: 1px solid black;
      color: white;
      text-align: center;
      background-color: blueviolet;
    }

    .box-sizing{
      box-sizing: border-box;
      margin-top: 50px;
    }
  </style>
</head>
<body>
  <div class="box">center-box</div>
  <div class="box box-sizing">border-box</div>
</body>
</html>
```

- 기본적으로 모든 요소의 box-sizing은 content-box
  - Padding을 제외한 순수 contents 영역만을 box로 지정
- 다만, 우리가 일반적으로 영역을 볼 때는 border까지의 너비를 100px 보는 것을 원한다
  - 그 경우 box-sizing을 border-box로 설정 

### CSS Display

- 모든 요소는 네모(박스모델)이고, 좌측상단에 배치.
- **display에 따라 크기와 배치가 달라진다.**

- Display: block

  - 줄 바꿈이 일어나는 요소(blocking을 하니까 내 영역으로 못 오니까 다음 줄)
  - 화면 크기 전체의 가로 폭을 차지한다.
  - 블록 레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있다
  - **무조건 margin이 붙어있다**
  - 너비를 가질 수 없다면 자동으로 부여되는 margin

- display: inline

  - 줄 바꿈이 일어나지 않은 행의 일부 요소(한 줄에)

  - Content 너비만큼 가로 폭을 차지한다.

  - width, height, margin-top, margin-bottom 지정할 수 없다.

  - margin top, margin bottom을 줄 수 없다 한 줄로 가야하니까 너비랑 높이도 가질 수 없다.

  - 상하 여백은 line-height로 지정한다.

    

- margin으로 오른쪽을 채우면 올라오고 싶어도 올라오지 못한다.
- display를 바꾸지 않으면 한 줄로 묶을 수 없다
- 블록 레벨 요소와 인라인 레벨 요소
  - 블록 레벨 요소와 인라인 레벨 요소 구분(HTML 4.1까지)
- 대표적인 블록 레벨 요소
  - div / ul, ol, li / p / hr / form 등
- 대표적인 인라인 레벨 요소
  - Span / a / img / input, label / b, em, i, strong 등

- display
  - Block:
    - block의 기본 너비는 가질 수 있는 너비의 100%
    - 너비를 가질 수 없다면 자동으로 부여되는 margin
  - Inline:
    - inline의 기본 너비는 컨텐츠 영역만큼
  - display: inline-block
    - block과 inline 레벨 요소의 특징을 모두 가짐 
    - inline처럼 한 줄에 표시할 수 있고, block처럼 width, height, margin 속성을 모두 지정할 수 있음
  - display: none
    - 해당 요소를 화면에 표시하지 않고, 공간조차 부여되지 않음
    - 이와 비슷한 visibility: hidden은 해당 요소가 공간은 차지하나 화면에 표시만 하지 않는다.
  - 이외 다양한 display 속성은 [링크참조][https://developer.mozilla.org/ko/docs/Web/CSS/diplay]