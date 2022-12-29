- HTML 정리
  - Hyper Text Markup Language의 약자로 Hypertext(웹 페이지에서 다른 페이지로 이동할 수 있도록 하는 것) 기능을 가진 문서를 만드는 언어이다. 웹페이지를 위한 마크업 언어(문서 처리의 원활한 지원을 위해 문서에 추가되는 약속된 정보) 라고 할 수 있습니다.
  - html 문서는 단순히 텍스트 파일에 불과하고 웹 브라우저가 해석을 해서 구조를 통해 화면에 렌더링 해주고 되고 사용자는 View라고 하는 스크린을 통해 접하게 되는 것이다. 
  - HTML은 구조적 설계라고 할 수 있습니다
  - 역사
    - 1980년, 유럽 입자 물리 연구소의 계약자였던 팀 버너스리가 HTML의 원형인 인콰이어를 제안하였다. 인콰이어는 연구원들이 문서를 이용하기 공유하기 위한 체계였다. 1989년 버너스리는 인터넷 기반 하이퍼텍스 체계를 제안하는 메모를 작성하게 됩니다. 버너스 리는 1990년 말에 HTML을 명시하고, 브라우저와 서버 소프트웨어를 작성했다. 
    - 일반 공개 설명은 1991년 처음으로 HTML 태그로 부르면서 시작되었다. SGML의 영향을 받았는데 SGML은 문서용 마크업 언어를 정의하기 위한 메타 언어이다.
    - 버너스리는 SGML 응용 프로그램이 되는 HTML을 고안해야 했고 공식적으로 국제 인터넷 표준화 기구에 의하여 HTML 규격에 대한 최초의 제안을 간행물로 정의했다. 
  
- css 정리

  - 1994년 하콤 비움 리가 발명했으며 W3C(World Wide Web Consortium)에서 관리했다. 

  ```css
  /* 배경색 음영 배치하기 */
  img {
    /* x축, y축, 흐림정도, 색깔 */
    box-shadow: -15px -15px 0 #ea987e;
  }
  
  ```

  ```css
  /* 줄무늬 음영 배치하기 */
  .pic {
    position: absolute; /*의사 요소 기준 주지 않으면 전체 바탕에 absoulte한 줄무늬가 올라가게 된다.*/ 
  }
  
  .pic img{
    position: relative; /* z-index를 활성화하기 위해 필요 */ 
    z-index: 2; /*사진을 줄무늬 음영 위에 표시 */
  }
  
  .pic::before {
    content: '';
    position: absolute;
    bottom: -15px; /*사진에서 아래로 15px만큼 이동*/
    right: -15px; /*사진에서 오른쪽으로 15px만큼 이동*/
    width: 100%; /*포함하는 부모 요소의 폭 100%;*/
    height: 100%; /*포함하는 부모 요소의 높이 100%*/
    background-image: repeating-linear-gradient (
    	-45deg, /* 선을 -45도 회전 */
      #d34e23 0px, #d34e23 2px, /* 색을 입힌 선 0px 위치에서 2px위치까지 같은 색을 입힌 가로 선을 표현한다.*/
      rgba(0 0 0 / 0 ) 0%, rgba(0 0 0 / 0) 1% /*여백 투명한 부분 0% 위치에서 1%위치까지 투명한 여백을 만든다*/
    	);
    z-index: 1; /*줄무늬 음영을 사진 아래에 표시*/
  }
  ```

  ```css
  /* 점무늬 음영 배치하기 */
  .pic {
     position: absolute; /* 의사 요소 기준*/
  }
  
  .pic img {
     position: relative; /* z-index를 활성화하기 위해 필요 */
     z-index: 2; /* 사진을 점 패턴 위 계층에 표시한다 */
  }
  .pic::before {
     content: '';
     position: absolute;
     bottom: -30px;
     right: -30px;
     width: 100%; /* 감싸고 있는 부모 요소의 폭 크기 100% */
     height: 100%; /* 감싸고 있는 부모 요소의 높이 크기 100% */
     background-image: radial-gradient(
        #ea987e 20%, /* 점의 색과 크기 지정 */
        rgba(0 0 0 / 0) 10%
     );
     background-size: 10px 10px; /* 반복하지 않는 상태에서의 background 크기 지정 */
     background-position: right bottom; /* 점 패턴 시작 위치 지정(점 무늬의 오른쪽 아래 부분이 잘리지 않고 표시된다)*/
     z-index: 1; /* 점 패턴을 사진 아래 계층에 표시 */
  }
  ```
  
  ```css
  /*피사체에 그림자 배치하기 */
  img {
     filter: drop-shadow(15px 20px 0 blue);
  }
  /* offset-x:x축 값, offset-y:y축 값, blur-radius:퍼짐 효과의 반지름, color:그림자 색상*/
  filter: drop-shadow(offset-x offset-y blur-radius color);
  ```
  
  ```css
  /*대각선으로 이미지에 프레임 만들기*/
  .pic {
     position: absolute; /* 의사 요소 기준 */
  }
  
  .pic::after {
     content: '';
     position: absolute;
     top: 50%; /*테두리 외각 차지*/
     left: 50%;
     transform: translate(-50%, -50%); /*상하좌우의 중앙에 배치한다*/
     width: calc(100% + 20px); /* 왼쪽과 오른쪽의 대각선 프레임 절반값 x 2를 더하는 계산식 */
     height: calc(100% + 20px); /* 위와 아래의 대각선 프레임 절반값 x 2를 더하는 계산식 +border-width:20의 절반 값*/
     border-image-source: repeating-linear-gradient(
        45deg, /* 45도 회전 */
        #256388 0px, #256388 2px, /* 색을 입힌 선 */
        rgba(0 0 0 / 0) 2px, rgba(0 0 0 / 0) 7px /* 여백(투명) 부분 */
     );
     border-image-slice: 20; /* border 네 변의 사용 범위를 지정 */
     border-width: 20px; /* 테두리 폭 */
     border-image-repeat: round; /* 타일 형태로 반복해서 표시 */
     border-style: solid; /* 실선으로 표현 */
  }
  ```
  
  ```css
  /*사진 모서리를 액자처럼 꾸미기 */
  .pic {
    position: absolute;
  }
  
  .pic::before,
  .pic::after {
    content: "";
    position: absolute;
    transform: rotate(-35deg);
    /*대각선의 너비 조절*/
    width: 70px;
    /*대각선의 높이 조절*/
    height: 25px;
    background-color: #fff;
  }
  
  .pic::before {
    top: -10px;
    left: -25px;
    border-bottom: 1px solid #aaa;
  }
  
  .pic::after {
    bottom: -10px;
    right: -25px;
    border-top: 1px solid #aaa;
  }
  
  ```
  
  



