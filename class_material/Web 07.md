### Bootstrap 활용 실습

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <link rel="stylesheet" href="style.css">
  <!-- CSS only-->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
</head>
<body>
  <nav class= "nav sticky-top align-items-center d-flex justify-content-between p-2 text-bg-dark">
    <div>로고</div>
    <ul class= "list-inline d-flex my-0">
      <li class="list-inline-items mx-2">Home</li>
      <li class="list-inline-items mx-2">Products</li>
    </ul>
  </nav>
  <!-- banner -->
  <section class="banner">
  </section>
  <!--container -->
  <div class="container">
    <h1 class="text-center my-5">Lorem Ipsum</h1>
    <div class="d-flex">
    <img class="mx-1" width="500px"src="images/appaerl.jpeg" alt="">
    <p class="mx-1 text-secondary">Lorem</p>
    </div>  
  </div>
<!-- Javascript Bundle with popper-->  
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>  
</body>
</html>
```

```css
.nav {
  height: 70px;
}

.banner{
  height: 700px;
  background-image: url("../assets/apparel.jpeg");
}
```

- 개발자 도구에서 어떤 css가 적용되는지 확인
- body에 컨테이너를 줄면 줄어든다 방법은? nav안에 다 넣어준다.



### Bootsrap(컴포넌트)

- Components

  - Bootstrap의 다양한 UI 요소를 활용할 수 있다

  - 아래 Components 탭 및 검색으로 원하는 UI 요소를 찾을 수 있다.

  - 기본 제공된 Componenets를 변환해서 활용 

  - id가 있는 경우 무조건 id를 일치시켜서 유지해야한다. 대부분 자바스크립트를 활용하고 있고, 타겟으로 활용되는 경우가 있다.

  - **Data-bs-target이랑 id랑 같아야 한다.**

  - Acadian, alert(실제로 많이 사용되는 색깔)

  - Postion absolute = 네모 위에 네모

    ```html
    class="position-absolute top-0 start-100 translate-middle badge rounded-pill bg"
    ```

  - Notion 상단이 breadcrumb
  - card 사용할때 복붙했을 때 **Inline style이 있는 것을 반드시 확인해주세요** 

  ```html
  <div class="card" style="width: 18rem;">
    <img src="..." class="card-img-top" alt="...">
    <div class="card-body">
      <h5 class="card-title">Card title</h5>
      <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
      <p class="card-text text-primary">200,000원</p>
      <span class="badge text-bg-danger">품절</span>
    </div>
  </div>
  ```

  - Buttons

    - 클릭 했을 때 어떤 동작이 일어나도록 하는 요소

    ```html
    <button type="button" class="btn btn-primary">Primary</button>
    <button type="button" class="btn btn-primary">Secondary</button>
    <button type="button" class="btn btn-primary">Success</button>
    <button type="button" class="btn btn-primary">Danger</button>
    <button type="button" class="btn btn-primary">Warning</button>
    <button type="button" class="btn btn-primary">Info</button>
    <button type="button" class="btn btn-primary">Light</button>
    <button type="button" class="btn btn-primary">Dark</button>
    <button type="button" class="btn btn-primary">Link</button>
    ```

  - Dropdowns

    - dropdown, dropdown-menu, dropdown-item 클래스를 활용해 옵션 메뉴를 만들 수 있다.

    ```html
    <div class="dropdown">
      <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
        Dropdown button
      </button>
      <ul class="dropdown-menu">
        <li><a class="dropdown-item" href="#">Action</a></li>
        <li><a class="dropdown-item" href="#">Another action</a></li>
        <li><a class="dropdown-item" href="#">Something else here</a></li>
      </ul>
    </div>
    ```

  - Forms > Form controls

    - form-control 클래스를 사용해 `<input>` 및 `<form>` 태그를 스타일링 할 수 있다.

    ```html
    <div class="mb-3">
      <label for="exampleFormControlInput1" class="form-label">Email address</label>
      <input type="email" class="form-control" id="exampleFormControlInput1" placeholder="name@example.com">
    </div>
    <div class="mb-3">
      <label for="exampleFormControlTextarea1" class="form-label">Example textarea</label>
      <textarea class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
    </div>
    ```

  - Navbar

    - Navbar 클래스를 활용하면 네비게이션 바를 제작할 수 있다

    ```html
    <nav class="navbar navbar-expand-lg bg-light">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">Navbar</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <a class="nav-link active" aria-current="page" href="#">Home</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Link</a>
            </li>
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                Dropdown
              </a>
              <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="#">Action</a></li>
                <li><a class="dropdown-item" href="#">Another action</a></li>
                <li><hr class="dropdown-divider"></li>
                <li><a class="dropdown-item" href="#">Something else here</a></li>
              </ul>
            </li>
            <li class="nav-item">
              <a class="nav-link disabled">Disabled</a>
            </li>
          </ul>
          <form class="d-flex" role="search">
            <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
            <button class="btn btn-outline-success" type="submit">Search</button>
          </form>
        </div>
      </div>
    </nav>
    ```

    

  - Carousel 

    - 회전목마 

    ```html
    <div id="carouselExampleInterval" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-inner">
        <div class="carousel-item active" data-bs-interval="10000">
          <img src="..." class="d-block w-100" alt="...">
        </div>
        <div class="carousel-item" data-bs-interval="2000">
          <img src="..." class="d-block w-100" alt="...">
        </div>
        <div class="carousel-item">
          <img src="..." class="d-block w-100" alt="...">
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleInterval" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleInterval" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
    ```

    - Modal
      - 사용자가 상호작용 하기 위해서 사용하며, 긴급 상황을 알리는 데 주로 사용
      - 현재 열려 있는 페이지 위에 또 다른 레이어를 띄움
      - 페이지를 이동하면 자연스럽게 사라짐(제거를 하지 않고도 배경 클릭시 사라짐 - 옵션에 따라 다름)
      - Modal은 자바스크립트를 활용하며, 반드시 target과 id가 일치되어야 한다.

    ```html
    <!-- Button trigger modal -->
    <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
      Launch demo modal
    </button>
    
    <!-- Modal -->
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            ...
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button type="button" class="btn btn-primary">Save changes</button>
          </div>
        </div>
      </div>
    </div>
    ```

    - 눌렀을때 동작은 js cdn이 있어야 한다.
    - icons 사용하기
      - cdn link 받아야지 icon 사용가능 
    - nav바의 경우 nav > div > div > ul > li로 구성되어 있는데 3번째 div에 d-flex랑 justify-content-end를 설정해줘야 공간배치가 정상적으로 작동된다

    ```html
    <nav class="navbar navbar-expand-lg bg-primary sticky-top">
        <div class="container-fluid ">
          <a class="navbar-brand text-light" href="#">Navbar</a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse d-flex justify-content-end" id="navbarNav">
            <ul class="navbar-nav ">
              <li class="nav-item">
                <a class="nav-link active text-light" aria-current="page" href="#">Home</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">Features</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">Pricing</a>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    ```

    