## HTML

- table의 각 영역을 명시하기 위해 <thread> <tbody> <tfoot> 요소를 활용



| ID   | Name   | Major            |
| ---- | ------ | ---------------- |
| 1    | 홍길동 | Computer Science |
| 2    | 김철수 | Business         |
| 총계 | 2명    |                  |

- <tr>으로 가로 줄을 구성하고 내부에는 <th>혹은 <td>로 셀을 구성
- colspan, rowspan 속성을 활용하여 셀 병합
- <caption>을 통해 표 설명 또는 제목을 나타냄
- table 태그 기본 구성
  - thread
    - tr > th
  - tbody
    - tr > td
  - tfoot
    - tr > td
  - caption

```html
<body>
  <table>
    <thread>
    <tr>
    <th>Id</th>
    <th>Name</th>
   	<th>Major</th>
    </tr>
    </thread>
  </table>
	<tbody>
    <tr>
    	<td>1</td>
      <td>홍길동</td>
      <td>Computer Science</td>
    </tr>
    <tr>
    	<td>2</td>
    	<td>김철수</td>
    	<td>Business</td>
  	</tr>
  </tbody>
  <tfoot>
    <tr>
    	<td>총계</td>
      <td colspan="2">2명</td>
    </tr>
  </tfoot>
  <caption>1반 학생 명단</caption>
</body>
```



- form

  - !!<form>은 정보(데이터)를 서버에 제출하기 위해 사용하는 태그
  - 기본 속성
    - **action** : form을 처리할 서버의 URL(데이터를 보낼 곳)
    - Method: form을 제출할 때 사용할 HTTP 메서드 (GET 혹은 POST)
    - enctype: method가 post인 경우 데이터의 유형
      - Application/x-www-form-unlencoded : 기본값
      - Multipart/form-data: 파일 전송시 (input type이 file인 경우)
      - text/plain: HTML5 디버깅 용 (잘 사용되지 않음)

  - Input:

    - 다양한 타입을 가지는 입력 데이터 유형과 위젯이 제공됨

    - https://www.google.com/search?q=HTML

      ```html
      <!-- action은 서버에 제출이 되는 주소-->
      <!-- q는 사용자가 입력한 값에 변수 이름을 붙여놓고 나중에 서버에서도 q를 뽑아서 사용할 수 있다-->
      <form action="/search" method="GET">
        	<input type="text" name="q">
      </form>
      ```

      ```html
      <!DOCTYPE html>
      <html lang="en">
      <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
      </head>
      <body>
        <form action="">
          username: <input type="text" name="username">
          password: <input type="email" name="username">
          name: <input type="password" name="name" autofocus>
          <input type="submit" value = "얍">
        </form>
      </body>
      </html>
      ```

      - required를 하면 작성하고 넘어가게끔
      - autofocus를 하면 자동으로 그곳에 집중되게
      - name: form control에 적용되는 이름 (이름/값 페어로 전송됨)
      - value: form control에 적용되는 값 (이름/값 페어로 전송됨)
      - required, readonly, autofocus, autocomplete, disabled 등

    - input label

      - label을 클릭하여 input자체의 초점을 맞추거나 활성화 시킬 수 있다.

        - 사용자는 선택할 수 있는 영역이 늘어나 웹/모바일(터치) 환경에서 편하게 사용할 수 있다

        - label과 input의 입력의 관계가 시각적 뿐만 아니라 화면리더기에도 label을 읽어 쉽게 내용을 확인할 수 있다.
        - <input>에 id 속성을, <label>에는 for 속성을 활용하여 상호 연관을 시킴

        ```html
        <!DOCTYPE html>
        <html lang="en">
        <head>
          <meta charset="UTF-8">
          <meta http-equiv="X-UA-Compatible" content="IE=edge">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <title>Document</title>
        </head>
        <body>
          <form action="">
            <label for="username">username</label>
            <input type="email" name="username" id="username">
            <label for="password">password</label>
            <input type="password" name="password" id="password">
            <input type="submit" value="얍">
          </form>
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
      </head>
      <body>
        <h1>Form 활용 실습</h1>
        <form action="">
          autofocus 및 label 확인-->
          <div class="input-group">
            <label for="username">아이디</label>
          </div>
          <input type="text" name="username" id="username" autofocus>
      
          <!-- disabled 및 value 확인-->
          <div class="input-group">
            <label for="name">이름</label>
          </div>
          <input type="text" name="name" value="이호빈" id="name" disabled>
      
          <div class="input-group">
            <label for="password">비밀번호</label>
          </div>
          <input type="password" name="password" id="password" required>
      
          <!-- label 확인-->
          <div class = "input-group">
            <label for="agreement">개인정보 수집에 동의합니다.</label>
          </div>
          <input type="checkbox" name="agreement" id="agreement">
          <div class="input-group">
            <label>최종 제출을 확인합니다.</label>
          </div>
          <input type="submit" value="제출">
        </form>
      
      </body>
      </html>
      ```

      

    - input 유형 - 일반

      - 일반적으로 입력을 받기 위하여 제공되며 타입별로 HTML기본 검증 혹은 추가 속성을 활용할 수 있음
        - text:일반 텍스트 입력
        - password: 입력 시 값이 보지이 않고 문자를 특수기호(*로) 표현
        - email:이메일 형식이 아닌 경우 form 제출 불가
        - number: min, nax, step 속성을 활용하여 숫자 범위 설정 가능
        - file: accept 속성을 활용하여 파일 타입 지정 가능

    - Input 유형 - 항목 중 선택

      - 일반적으로 label 태그와 함께 사용하여 선택 항목을 작성함
      - 동일 항목에 대하여는 name을 지정하고 선택된 항목에 대한 **value**를 지정해야 한다.
        - checkbox: 다중선택
        - radio:단일 선택

      ```html
      <div>
        <p>checkbox</p>
        <input id="html" type="checkbox" name="language" value="html">
        <label for="html">HTML</label>
        <input id="python" type="checkbox" name="language" value="python">
        <label for="python">파이썬</label>
        <input id="java" type="checkbox" name="language" value="jave">
        <label for = "java">자바</label>
        <hr>
        <p>radio button</p>
        <input id="행복" type="radio" name="emotion" value="행복">
        <label for="행복">행복</label>
        <input id="슬픔" type="radio" name="emotion" value="슬픔">
        <label for="슬픔">슬픔</label>
        <input id="중립" type="radio" name="emotion" value="중립">
        <label for="중립">중립</label>
      </div>
      ```

      ```html
      <!-- 수업시간 배운거 활용-->
      <!DOCTYPE html>
      <html lang="en">
      <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
      </head>
      <body>
        <div>
          <p>checkbox</p>
          <input id="html" type="checkbox" name="language" value="html">
          <label for="html">HTML</label>
          <input id="python" type="checkbox" name="language" value="python">
          <label for="python">파이썬</label>
          <input id="java" type="checkbox" name="language" value="jave">
          <label for = "java">자바</label>
          <p>date</p>
          <input for="날짜" type="date" name="day">
          <label for = "날짜"></label>
          <hr>
          <p>radio button</p>
          <input id="행복" type="radio" name="emotion" value="행복">
          <label for="행복">행복</label>
          <input id="슬픔" type="radio" name="emotion" value="슬픔">
          <label for="슬픔">슬픔</label>
          <input id="중립" type="radio" name="emotion" value="중립">
          <label for="중립">중립</label>
          <p>color</p>
          <input id="색깔" type="color" name="색깔">
          <label for="색깔"></label>
        </div>
      </body>
      </html>
      ```

      

    - Form 서버에 전송하고 input으로 입력을 받아서 사용자 입력 값을 변수에 담아주고 **value는 사용자가 입력한 어떠한 패스워드가 있을때 뭐를 입력했는지 알려면 input 태그에 value에 mapping돼서 넘어간다.**

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Document</title>
    </head>
    <body>
      <form action="">
        <label for="username">username</label>
        <input type="email" name="username" id="username">
        <label for="password">password</label>
        <input type="password" name="password" id="password">
        <input type="submit" value="얍">
        <br>
        <label for="mincho">민초</label>
        <input type="radio" name="is_mincho" id="username" value="hobin49@naver.com">
        <label for="passowrd">민초</label>
        
      </form>
    </body>
    </html>
    ```

    - 사용자가 입력 or 선택 개발자가 입력
    - Value(값) name(이름)으로 매핑되서 서버에 전송
    - Input 유형 - 기타
      - 다양한 종류의 input을 위한 picker를 제공
        - Color: color picker
        - date: date picker
      - hidden input을 활용하여 사용자 입력을 받지 않고 서버에 전송되어야 하는 값을 설정
        - hidden: 사용자에게 보이지 않는 input

    

## Bootstrap

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  
</body>
</html>
```



- CDN(Content Delivery(Distribution) Network)
  - 컨텐츠(CSS, JS, Image, Text등)을 효율적으로 전달하기 위해 여러 노드에 가진 네트워크에 데이터를 제공하는 시스템
  - 개별 end-user의 가까운 서버를 통해 빠르게 전달 가능(지리적 이점) 외부 서버를 활용함으로써 본인 서버의 부하가 적어짐

- spacing

  - 클래스를 지우면 안 돼

  - Spacing(Margin and padding)

    - {propperty}{sides}-{size}
      - Where **property** is one of:
        - m - for classes that set **margin**
        - p - for classes that set **padding**
      - m{property}t{sides}-3{size}

    ```html
    <div class="mt-3 ms-5">bootsrap-spacing</div>
    ```

    - sides:
      - Where sides is one of:
        - t - for classes that set `margin-top`or `padding-top`
        - b - for classes that set `margin-bottom`or `padding-bottom`
        - s - (start) for classes that set `margin-left` or `padding-left`  in LTR, `margin-right` or `padding-right`  in RTL 
        - e - (end) for classes that set `margin-right` or `padding-right`in LTR, `margin-left`  or `padding-left` in RTL
        - x - for classes that set both `*-left`  and `*-right` 
        - y - for classes that set both `*-top`  and `*-bottom` 
        - blank - for classes that set a `margin`  or `padding`  on all 4 sides of the element
    - size:
      - where size is on of:
        - 0 - for classes that eliminate the `margin`  or `padding`  by setting it to 0 
        - 1 - (by default) for classes that set the `margin`  or `padding`  to `$spacer * .25`
        - 2 - (by default) for classes that set the `margin`  or `padding`  to `$spacer * .5`
        - 3 - (by default) for classes that set the `margin`  or `padding`  to `$spacer 1rem`
        - 4 - (by default) for classes that set the `margin`  or `padding`  to `$spacer * .1.5`
        - 5 -  (by default) for classes that set the `margin`  or `padding`  to `$spacer * .3`
        - auto - for classes that set the `margin`  to auto

    ```html
    .mt-1 {
    	margin-top: 0.25rem !important;
    }
    <!-- 16 * 0.25 = 4px -->
    <!-- 브라우저 <html>의 root 글꼴 크기는 16px -->
    ```

    | class name | rem  |  Px  |
    | :--------: | :--: | :--: |
    |    m-1     | 0.25 |  4   |
    |    m-2     | 0.5  |  8   |
    |    m-3     |  1   |  16  |
    |    m-4     | 1.5  |  24  |
    |    m-5     |  3   |  48  |

    ```html
    .mx-0 {
    	margin-right: 0 !important;
    	margin-left: 0 !important;
    }
    <!-- 가로(왼쪽, 오른쪽) margin이 0 -->
    ```

    ```html
    .mx-auto {
    	margin-right: auto !important;
    	margin-left: auto !important;
    }
    
    <!-- 블록 요소(인라인 요소 아님) 수평 중앙 정렬 가로 가운데 정령 -->
    ```

    ```html
    .py-0{
    	padding-top: 0 !important;
    	padding-top: 0 !important;
    }
    <!-- 위 아래 padding이 0-->
    ```

- spacing 종합

|  m   | margin  |
| :--: | :-----: |
|  p   | padding |

|  t   |     top     |
| :--: | :---------: |
|  b   |   bottom    |
|  s   |    left     |
|  e   |    right    |
|  x   | left, right |
|  y   | top, botoom |

|  0   |   0rem   | 0px  |
| :--: | :------: | :--: |
|  1   | 0.25 rem | 4px  |
|  2   | 0.5 rem  | 8px  |
|  3   |  1 rem   | 16px |
|  4   | 1.5 rem  | 24px |
|  5   |  3 rem   | 48px |

- Color

```html
<h2>Color</h2>
<div class="bg-primary">이건 파랑</div>
<div class="bg-secondary">이건 회색</div>
<div class="bg-dagner">이건 빨강</div>
<div class="text-success">이건 초록색 글씨</div>
<div class="text-danger">이건 빨간색 글씨</div>
```

- Text

```html
<h2>Text</h2>
<p class="text-start">margin-top 3</p>
<p class="text-center">margin-top 4</p>
<p class="text-end">mx-auto, 가운데 정렬</p>
<a href = "#" class="text-decoration-none">Non-underlined link</a>
<p class="fw-hold">Bold text.</p>
<p class="fw-normal">Normal weight text.</p>
<p class="fw-light">Light weight text.</p>
<p class="fst-italic">Italic text</p>
```





### Display

- 백그라운드 이미지나 높이랑 너비는 css에서 작성해야한다. 

```html
<h2>Display</h2>
<div class="d-inline p-2 bg-primary text-white">d-inline</div>
<div class="d-inline p-2 bg-dark text-white">d-inline</div>
<div class="d-block p-2 bg-primary text-white">d-inline</div>
<div class="d-block p-2 bg-dark text-white">d-inline</div>
<div class="box bg-warning d-sm-none d-md-block">보이냐?? 안보이나??</div>
<div class="box bg-success d-md-none d-xl-block">d-inline</div>
```



```html
<h2>Position</h2>
<div class="box fixed-top">fixed-top</div>
<div class="box fixed-bottom">fixed-bottom</div>
```





### Bootstrap 자세히

- 다운로드를 피하려면 아래의 태그들을 html 파일에 붙여넣는다.

```html
<head>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
</head>
<div>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-	A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.5/dist/umd/popper.min.js" integrity="sha384-		Xe+8cL9oJa6tN/veChSP7q+mnSPaj5Bcu9mPX5F5xIGE0DVittaqT5lorf0EI7Vk" crossorigin="anonymous"></script>
	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.min.js" integrity="sha384-ODmDIVzN+pFdexxHEHFBQH3/9/vQ9uori45z4JjnFsRydbmQbmL5t1tQ0culUzyK" crossorigin="anonymous"></script>
</div>
```

- Layout

  - Breakpoints

    - Core concepts
      - Breakpoints are the building blocks of responsive design. 
      - Use media queries to architect your CSS by breakpoint.
      - Mobile first, responsive design is the goal. 

    | Breakpoint                    | Class infix | Dimensions |
    | ----------------------------- | ----------- | ---------- |
    | Extra small<핸드폰>           | None        | <576px     |
    | Small<핸드폰>                 | sm          | >=576px    |
    | Medium<테블릿 Pc, 구형모니터> | md          | >=768px    |
    | Large<테블릿 Pc>              | lg          | >=992px    |
    | Extra large<모니터화면>       | xl          | >=1200px   |
    | Extra extra large             | xxl         | >= 1400px  |

    - Min-width

      - Bootstrap primaily uses the following media query ranges - or breakpoints - in our source Sass files for our layout, grid system, and components 

      ```html
      // X-Small devices (portrait phones, less than 576px)
      // No media query for `xs` since this is the default in Bootstrap
      
      // Small devices (landscape phones, 576px and up)
      @media (min-width: 576px) { ... }
      
      // Medium devices (tablets, 768px and up)
      @media (min-width: 768px) { ... }
      
      // Large devices (desktops, 992px and up)
      @media (min-width: 992px) { ... }
      
      // X-Large devices (large desktops, 1200px and up)
      @media (min-width: 1200px) { ... }
      
      // XX-Large devices (larger desktops, 1400px and up)
      @media (min-width: 1400px) { ... }
      ```

    - single breakpoint

      - There are also media queries and mixins for targeting a single segment of screen sizes using the minimum and maximum breakpoint widths.

      ```html
      @media (min-width: 768px) and (max-width: 991.98px) { ... }
      ```

    - Between breakpoints

      ```html
      @include media-breakpoint-between(md, xl) { ... }
      ```

    

- Content

  - reboot

    - For example, consider these : root CSS variables for common <body>styles

    ```css
      @if $font-size-root != null {
        --#{$prefix}root-font-size: #{$font-size-root};
      }
      --#{$prefix}body-font-family: #{$font-family-base};
      @include rfs($font-size-base, --#{$prefix}body-font-size);
      --#{$prefix}body-font-weight: #{$font-weight-base};
      --#{$prefix}body-line-height: #{$line-height-base};
      --#{$prefix}body-color: #{$body-color};
      @if $body-text-align != null {
        --#{$prefix}body-text-align: #{$body-text-align};
      }
      --#{$prefix}body-bg: #{$body-bg};
          
          
      body {
      margin: 0; // 1
      font-family: var(--#{$prefix}body-font-family);
      @include font-size(var(--#{$prefix}body-font-size));
      font-weight: var(--#{$prefix}body-font-weight);
      line-height: var(--#{$prefix}body-line-height);
      color: var(--#{$prefix}body-color);
      text-align: var(--#{$prefix}body-text-align);
      background-color: var(--#{$prefix}body-bg); // 2
      -webkit-text-size-adjust: 100%; // 3
      -webkit-tap-highlight-color: rgba($black, 0); // 4
    }
    ```

    - horizon rules
      - `<hr>`s are styled via `border-top` have a default  `opacity: .25` and automatically inherit their `border-color`via color, including when color is set via the parent

    ```html
    <hr>
    
    <div class="text-success">
      <hr>
    </div>
    
    <hr class="border border-danger border-2 opacity-50">
    <hr class="border border-primary border-3 opacity-75">
    ```

    - Lists
      - All lists - `<ul>`, `<ol>`, and  `<dl>` -have their `margin-top` removed and a `margin-bottom: 1rem` Nested lists have no `margin-bottom.` We've also reset the `padding-left` on `<ul>` and `<ol>` elements
      - description lists have updated margins. `<dd>`s reset `margin-left` to 0 and add `margin-bottom: .5rem`<dt>s are bolded.

    - Inline code

      - Wrap inline snippets of code with `<code>` Be sure to escape HTML angle brackets. 

      ```html
      For example, <code>&lt;section&gt;</code> should be wrapped as inline.
      
      => For example, <code>&lt;section&gt;</code> should be wrapped as inline.
      ```

    - Code blocks

      - Use `<pre>`s for multiple lines of code. Once again, be sure to escape any angle brackets in the code for proper rendering. The `<pre>` element is reset to remove its `margin-top`and use `rem` units for its `margin-bottom`

        ```html
        <pre><code>&lt;p&gt;Sample text here...&lt;/p&gt;
        &lt;p&gt;And another line of sample text here...&lt;/p&gt;
        </code></pre>
        
        => <pre><code>&lt;p&gt;Sample text here...&lt;/p&gt; &lt;p&gt;And another line of sample text here...&lt;/p&gt;</code></pre>
        ```

    -  Variables

      - For indicating variables use the `<var>` tag

      ```html
      <var>y</var> = <var>m</var><var>x</var> + <var>b</var>
      
      => y = mx + b
      ```

    - User input

      - Use the `<kbd>` to indicate input that is typically entered via keyboard.

      ```html
      To switch directories, type <kbd>cd</kbd> followed by the name of the directory.<br>
      To edit settings, press <kbd><kbd>ctrl</kbd> + <kbd>,</kbd></kbd>
      
      => kdb is to make like a hover on the cursor
      ```

    - Pointers on buttons

      - Reboot includes an enhancement for `role="button"`to change the default cursor to `pointer` Add this attribute to elements to help indicate elements are interactive. This role isn't necessary for `<button>`  elements, which get their own `cursor`change. 

      ```html
      <span role="button" tabindex="0">Non-button element button</span>
      
      =>Non-button element button
      ```

      

- Typography
- Headings
  - All HTML headings, `<h1>` through `<h6>`, are available.

```html
<h1>h1. Bootstrap heading</h1>
<h2>h2. Bootstrap heading</h2>
<h3>h3. Bootstrap heading</h3>
<h4>h4. Bootstrap heading</h4>
<h5>h5. Bootstrap heading</h5>
<h6>h6. Bootstrap heading</h6>
```

- customizing headings.

  - Use the included utility classes to recreate the small secondary heading text from Bootstrap 3.

  ```html
  <h3>
    Fancy display heading
    <small class="text-muted">With faded secondary text</small>
  </h3>
  ```

  