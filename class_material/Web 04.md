- CSS 원칙
  - Normal flow은 inline과 block으로 배치된다.
  - static은 position이다. 여기서 살짝 벗어난게 relative(offeset-좌측으로부터 몇 상단으로부터 몇), absolute(상위부모 static이 아닌것)
  - absolute와 fixed와 sticky는 normal flow를 벗어난다. 기준이 있으므로
- flex
  - 기본적으로 수직정렬이 어려운데 concept자체를 바꿨다.
  - Normal flow기준으로 화면이 배치가 됐었는데 flex를 사용함으로써 더 유연하게 아이템들을 배치할 수가 있다.
  - 공간의 요소들이 flex되면서 자유자재로 배치할 수 있다.
- html은 마크업 구조 잡고 csss html은 선택해서 스타일링
- 개발자도구를 어떻게 써요?
  - 계획을 무너진 레이아웃을 찍는데 자식:너비는 부모
- 포지션과 디스플레이 차이:
  - 디스플레이는 내가 flow상에 위치 포지션은 어떤 기준점 viewpoint 부모를 기준으로 offset.

### 실습예시

- 홈페이지 상단을 네비게이션바라고 부른다.

- 내가 사이트에서 이동했던 경로(breadcrumb-빵 조각)

- 시맨틱 태그

  - HTML 태그가 특정 목적, 역할 및 의미적 가치를 가지는 것
    - h1 태그는 "이 페이지에서 최상위 제목"인 텍스트를 감싸는 역할(또는 의미)를 나탄낸다.
  - Non semantic 요소로는 div, span 등이 있으며 a, form, table 태그들도 시맨틱 태그로 볼 수 있음
  - 대표적인 시맨틱 태그 목록
    - Header: 문서 전체나 섹션의 헤더(머리말 부분)
    - nav: 네비게이션
    - Aside: 사이드에 위치한 공간, 메인 콘텐츠와 관련성이 적은 콘텐츠
    - section: 문서의 일반적인 구분, 컨텐츠의 그룹을 표현
    - Article: 문서, 페이지, 사이트 안에서 독립적으로 구분되는 영역
    - Footer: 문서 전체나 섹션의 푸터(마지막 부분)

  ```html
  <header>
  	<nav></nav>
  </header>
  <section>
    <article</artcle>
    <article></article>
  </section>
  <footer></footer>
  ```

  - 구글은 명확하게 지키고 있다.
  - 온톨로지

- 사용해야하는 이유

  - 의미론적 마크업
    - 개발자 및 사용자 뿐만 아니라 검색엔진 등에 의미 있는 정보의 그룹을 태그로 표현
    - 단순히 

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <nav class="nav">
    <a class="nav-link" href="">SAMSUNG</a>
  	<ul class="nav-list">
    	<li class="nav-item">
      	<a class="nav-link" href="">스토리</a>
    	</li>
    	<li class="nav-item">
    	<a class="nav-link" href="">멤버십</a>
    	</li>
    	<li class="nav-item">
    	<a class="nav-link" href="">디지털 프라자</a>
    	</li>
    </ul>
  </nav>
</body>
</html>
```

```css
import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100&display=swap');
</style>

*{
  box-sizing: border-box;
}

.nav{
  display: flex;
  justify-content:space-between;
  align-items: center;
  position: sticky;
  top:0;
  height: 50px;
  background-color:white;
}

body {
  height: 10000px;
  font-family: 'Noto Sans KR', sans-serif;
  background-color:aqua;
}

.nav-list{
  display:flex;
  margin: 0; <마진 제거>
  padding: 0; (점 없애기)
  list-style:none;
  
  
}
.nav-link{
  text-decoration: none;
}

.nav-link:visited{
  color: black;
}

.nav-link:hover { <내부 링크 자체를 색깔을 입혀준다.
  color: skyblue;
  background-color: black;
  border-radius: 3px;
  padding:2px; 패딩을 주면 튄다
}

.nav-item{
  margin: 0 10px;
}
```

