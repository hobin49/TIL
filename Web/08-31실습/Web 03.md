- 어제 실습1

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <link rel="stylesheet" href="style.css">
  <style>
    .subtext {
      display:block;
      font-size: 16px;
    }
    .title{
      text-align: center;
    }
    .item-list{
      width: 900px;
    }
    .item{
      width: 300px;
      dlsplay: inline-block; <!--inline block은 4px공백 존재 한 줄에 그림 2개 -->
      margin: -4px;
    }
    .item-img{
      width: 100%;
    }
    .item-subtitle{
      color: rgb(132, 128, 128);
      font-weight: bold;
    }
  </style>
  
</head>
<body> <!-- br쓰면 줄바꿈 된다.파란 공간이 있어야 가운데 정렬 가능 --> 
	<h2 class="title"><span class="subtext">ALL ABOUT</span>BESPOKE 김치플러스 Infinite Line</h2>
  <div class ="item-list">
    
  <div class="item">
    <img class="item-img"src="./images/1.webp" alt"김치플러스">
    <p>INSTALLATION </p>
    <h3>김치 냉장 가이드</h3>
    <p>블라블라</p>
  </div>
    
  <div class="item">
    <img class="item-img"src="./images/1.webp" alt"김치플러스">
    <p>INSTALLATION </p>
    <h3>김치 냉장 가이드</h3>
    <p>블라블라</p>
  </div>
 </div>
</body>
</html>
```

### CSS Position

- 문서 상에서 요소의 위치를 지정
- Static: 모든 태그의 기본 값(기준 위치)
  - 일반적인 요소의 배치 순서에 따름(좌측 상단) - Normal Flow
  - 부모 요소 내에서 배치 될 때는 부모 요소의 위치를 기준으로 배치 됨
- 아래는 좌표 프로퍼티(top, bottom, left, right)를 



- 1.relative: 상대 위치(형이 일이 있어서 자취를 하러 나가다)
  - 자기 자신의 static 위치를 기준으로 이동(normal flow 유지)
  - 실제 위치는 그대로, 사람 눈에만 이동
  - 레이아웃에서 요소가 차지하는 공간은 static일 때와 같다 (nomal position 대비 offset)
- 2.absolute: 절대 위치(형이 집을 나가서 동생이 첫 번째가 되다)
  - 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않는다.(normal flow에서 벗어난다. 즉 다음 블록 요소가 좌측 상단으로 붙는다.)
  - stactic이 아닌 가장 가까이 있는 부모/조상 요소를 기준으로 이동(없는 경우 브라우저 화면 기준으로 이동)
  - **Absolute 적용이 안 돼면 부모요소가 static인 경우다**
  - 특정 영역 위에 존재 -CSS 기본 원칙인 좌측상단에 배치되지 않는다.
  - 부모를 기준으로 가운데에 위치

- 3.fixed: 고정 위치
  - 요소를 일반적으로 문서 흐름에서 제거 후 레이아웃에 공간을 차지 않는다.
  - 부모요소와 관계없이 viewport를 기준으로 이동
    - 스크롤 시에도 항상 같은 곳에 위치한다.
    - 브라우저 기준으로 우측 하단에 위치.
- 4,sticky: 스크롤에 따라 static -> fixed로 변경
  - 속성을 적용한 박스는 평소에 문서 안에서 position: static 상태와 같이 일반적인 흐름에 따르지만 스크롤 위치가 임계점에 이르면 position: fixed와 같이 박스를 화면에 고정할 수 있는 속성

- static vs relative vs absolute

```html
<!-- static-->
div {
	height: 100px;
	width: 100px;
	background-color: #9775fa;
	color:black;
	line-height: 100px;
	text-align: center;
}

<!-- relative-->
.relative {
	position: relative,
	top: 100px;
	left: 100px;
}

<!-- absolute-->
.parent {
	position: relative;
}

.absolute-child{
	position: absolute;
	top: 50px;
	left: 50px;
}

<!-- fixed-->
.fixed {
	position: fixed;
	bottom: 0;
	right: 0;
}
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <link rel="stylesheet" href="05.css">
<style>
  /* 공통 스타일링 */
div {
  box-sizing: border-box;
  width:100px;
  height:100px;
  border: 1px solid black;
}

.parent{
  position: relative;
  width: 300px;
  height: 300px;
}

.absolute{
  position: absolute;
  top:100px;
  left:100px;
  background-color: crimson;
}

.sibling {
  background-color: deepskyblue;
}

.relative{
  position: relative;
  top: 100px;
  left:100px;
  background-color: crimson;
  
}
  
  </style>  
</head>
<body>
  <div class="parent">
    <div class="absolute">형</div>
    <div class="sibling">동생</div>
  </div>
  <div class="parent">
    <div class="relative">형</div>
    <div class="sibling">동생</div>
  </div>
</body>
</html>
```



- Css 원칙 1, 2: Normal flow
  - 모든 요소는 네모, 좌측상단에 배치
  - display에 따라 크기와 배치가 달라짐
- Css 원칙 3:
  - position으로 위치의 기준을 변경
    - relative: 본인의 원래 위치
    - Absolute: 특정 부모의 위치
    - fixed: 화면의 위치
    - Sticky: 기본적으로 static이나 스크롤 이동에 따라 fixedfh qusrud

- Position sticky:

  - Sticky: 스크롤에 따라 static -> fixed로 변경

    - 속성을 적용한 박스는 평소에 문서 안에서 position: static 상태와 같이 일반적인 흐름에 따르지만, 스크롤 위치가 임계점에 이르면 position: fixed와 같이 박스를 화면에 고정할 수 있는 속성

    - 일반적으로 Navigation Bar에서 사용됨.



### CSS Layout

- DIsplay
- Position
- Fioat(1996)
- Flexbox(2012)
- Grid(2017)
- 기타
  - Responsive Web Design(2010), Media Queries(2012)

- Float
  - 박스를 왼쪽 혹은 오른쪽으로 이동시켜 텍스트를 포함 인라인요소들이 주변을 wrapping 하도록 함
  - 요소가 Normal flow를 벗어나도록 한다. 

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <link rel="stylesheet" href="05.css">
</head>
<body>
  <div class="box left">float left</div>
  <p>lorem 자동 완성으로 길~게</p>
</body>
</html>
```





### Flexbox

- 행과 열 형태로 아이템들을 매치하는 1차원 레이아웃 모델
- 축
  - main axis(메인 축)
  - cross axis(교차 축)
- 구성 요소
  - Flex container(부모 요소) **부모 요소를 만들면 자동으로 자식 요소가 생성한다**
  - Flex item(자식 요소)

- Flexbox 축
  - flex-direction: row 
- Flexbos 구성 요소
  - Flex Container(부모 요소)
    - display 속성을 flex 혹은 inline-flex로 지정
    - display flex를 부모한테 줘야한다.
    - Flex Item들이 놓여있는 영역
  - Flex Item(자식 요소)
    - 컨테이너에 속해 있는 컨텐츠(박스)

```html
<!-- 부모 요소에 display:flex 혹은 inline-flex-->
.flex-container{
	display: flex;
}
```

- 왜 Flexbox를 사용해야 할까?

  - 이전까지 제약사항
    - (수동 값 부여 없이) 수직 정렬	
    - 아이템의 너비와 높이 혹은 간격을 동일하게 배치

- 배치 설정

  - `flex-direction` 

    - Main axix 기준 방향 설정
    - 역방향의 경우 HTML 태그 선언 순서와 시각적으로 다르니 유의(웹 접근성에 영향)
      - 1,row(가로 main), 2.row-reverse(가로 main), 3.column(세로 main), 4.column-reverse(세로 main)

    | 속성           | 의미                                    |
    | -------------- | --------------------------------------- |
    | row (default)  | Main axix 방향을 가로 방향으로 정렬     |
    | row-reverse    | Main axis 방향을 가로의 역방향으로 정렬 |
    | column         | Main axis 방향을 세로 방향으로 정렬     |
    | column-reverse | Main axis 방향을 세로의 역방향으로 정렬 |

    

  - `flex-wrap` 

    - 아이템이 건테이너를 벗어나는 경우 해당 영역 내에 배치되도록 설정
    - 즉, 기본적으로 컨테이너 영역을 벗어나지 못하게 설정
    - No wrap(기본 값): 한 줄에 배치 (보조축 기준 한 줄로)
    - Wrap:넘치면 그 다음 줄로 배치

    | 속성          | 의미                                          |
    | ------------- | --------------------------------------------- |
    | wrap(default) | 아이템들을 아래로 내려(다음 줄로) 정렬        |
    | nowrap        | 아이템들의 크기를 조절하여 한 줄에 모두 정렬  |
    | wrap-reverse  | 아이템들을 아래로 내려(다음 줄로) 역방향 정렬 |

    

    ```html
    .container {
    	display: flex;
    	flex-wrap: wrap;
    }
    ```

  - `Flex-flow`

    - Flex-direction이랑 flex-wrap을 같이 쓸때 사용 가능하다.
    - 예시)`flew-flow: row nowrap;`

- 공간 나누기

  - `Justify-content(main axix)` 
    
    - Main axix를 기준으로 공간 배분(열 기준)
    
    - Flex-start(왼쪽 시작 기준으로 정렬), flex-end(끝을 기준으로 정렬), center(가운데 정렬), space-between(가운데 공간 동일하게 가져가 ), space-around, space-evenly(양쪽 너비 간격 같아)
    
  - `Align-cotent(cross axis)`
    
    - Cross axix를 기준으로 공간 배분(아이템이 한 줄로 배치되는 경우 확인할 수 없음)
    

  | 속성                 | 의미                                                         |
  | -------------------- | ------------------------------------------------------------ |
  | flex-start (default) | 요소들을 컨테이너의 왼쪽(시작점)으로 정렬합니다.             |
  | flex-end             | 요소들을 컨테이너의 오른쪽(끝점)으로 정렬합니다.             |
  | center               | 요소들을 컨테이너의 가운데(중앙)로 정렬합니다.               |
  | space-between        | 요소들 사이에 동일한 간격을 둡니다.                          |
  | space-around         | 요소들 주위에 동일한 간격을 둡니다.(가질 수 있는 영역을 반으로 나눠서 양쪽에) |
  | space-evenly         | 전체 영역에서 아이템 간 간격을 균일하게 분배                 |

- 정렬

  - `align-self`

    - 개별 아이템을 Cross axis 기준으로 정렬
      - 해당 속성은 컨테이너에 적용하는 것이 아니라 개별 아이템에 적용

  - `align-items` 

    - (Cross axix) 를 기준으로 정렬 (한 줄)

    ```html
    flex-start: 요소들을 컨테이너의 꼭대기로 정렬합니다.
    flex-end: 요소들을 컨테이너의 바닥으로 정렬합니다.
    center: 요소들을 컨테이너의 세로선 상의 가운데로 정렬합니다.
    baseline: 요소들을 컨테이너의 시작 위치에 정렬합니다.
    stretch: 요소들을 컨테이너에 맞도록 늘립니다.
    ```

    

    

    - Stretch, flex-start, flex-end, center, baseline(font랑 관련)

    ```html
    .container {
    	display: flex;
    	align-items: flex-start;
    }
    ```

- 수직과 수평을 모두 가운데 정렬하고 싶으면 justfy-content(=center), align-items(=center) 적용

- Flex에 적용하는 속성
  - 기타 속성
    - flex-grow: 남은 영역을 아이템에 분배
    - order: 배치 순서

```html
<div class="flex_item grow-1 order-3">1</div>
<div class="flex_item grow-1">2</div>
<div class="flex_item order-1">3</div>
<div class="flex_item order-2">4</div>
```

- 활용 레이아웃- 수직 수평 가운데 정렬

```html
<!--방법 1 컨테이너 설정-->
.cotainer {
	display: flex;
	justify-content: center;
	align-items: center;
}

<!--방법 2 아이템 설정-->
.container {
	display: flex;
}
.item{
	margin: auto;
}
```

```html
<!-- 활용 레이아웃 카드 배치-->
#layout_03 {
	display: flex;
	flex-direction: column;
	flex-wrap: wrap;
	justify-content: space-around;
	align-content: space-around;
}

#layout_03 {
	display:flex;
	flex-dirction: row;
	flex-wrap: wrap;
	justify-content: space-around;
	align-content: space_around
}
```

- 향목 방향 제어

  - 아직 추가하지 않았음에도 불구하고 flex-direction 아직까지는 항목이 행으로 표시된다. 왜냐하면 초기 값이 flex-direction이 row행이 필요한 경우 속성을 추가할 필요가 없다. 방향을 변경하려면 속성과 4가지 값 중 하나를 추가한다.

- Flex-flow 단축번호:

  - Flex-direction로 column 항목 줄바꿈 허용:

    ```html
    .container {
    	display: flex;
    	flex-flow: column wrap;
    }
    ```

    

- 플랙스 아이템 내부 공간 제어:

  - 컨테이너에 아이템 표시에 필요한 공간보다 많은 공간이 있는 경우, 아이템은 선두에 줄서고 빈 공간을 채울 정도로 커지지 않습니다. 최대 콘텐츠 크기에서 성장을 멈춥니다. 이는 의 초기값이 flex-속성은 다음과 같다.
  - `flex-grow:0`: 아이템이 증가하지 않는다.
  - `flex-shrink: 1`  아이템은 아이템보다 작아질 수 있습니다. `flex-basis`
  - `flex-basis: auto`:아이템의 베이스 사이즈는  auto

  - 다양한 속도로 아이템 증가가 가능하다. 각기 항목에 1, 2, 3.. 이런 식으로 개별적으로 값을 줄 수 있다.

  ```html
  <!-- 1.flex-grow, flex-shrink, flex-basis-->
  .item1 {
  	flex:1 1 auto;
  }
  .item2 {
  	flex:2 1 auto;
  }
  ```

  

- Place-content:

  - justify-content와 align-content를 동시에 사용 가능하다. 

  ```html
  .container{
  	place-content: space-between;
  }
  
  .container{
  	place-content: center flex-end;
  }
  ```

  

- flex를 적용하는 방법

  - flex는 최상위 클래스 옆에 작성해서 하위클래스로서의 역할을 담당한다.
  - 좌측상단으로 쌓이는 원구조로 부터 탈출해서 카드들이 많을때 배치하기 좋다.

  ```html
  
  ```

  