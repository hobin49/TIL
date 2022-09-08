```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <link rel="stylesheet" href="css/bootstrap.min.css">
</head>
<body>
  <div class="container">
    <h1 class="text-center">회원 가입</h1>
  <script src="js/bootstrap.bundle.min.js"></script>
  </div>
</body>
</html>
```

- min파일 형식은 띄어쓰기랑 탭이랑 엔터가 제거된 파일
- rtl 파일은 right to left이다.
- 나중에 input에 name 추가해야 사용자가 입력값을 이름을 붙여서 서버로 전송한다.
- 개별 input에 주어지는 클래스는 form-control이라는 클래스가 정의된다.
- label에 쓰는 클래스는 form-label이다.
- 만약에 내가 일반적인 파일 인풋이나 숫자를 받아본다고 하면 기본적으로 form-control이라는 클래스가 적용된다.
- `image/*` : 모든 이미지 파일을 사용하기 위해서 와일드카드로 쓰인다.
- active는 하얀색으로 색깔이 변한다.



### Bootstrap Grid System

- Grid system(web design)

- 요소들의 디자인과 배치에 도움을 주는 시스템

- 기본요소

  - Column: 실제 컨텐츠를 포함하는 부분
  - Gutter: 칼럼과 칼럼 사이의 공간 (사이 간격)
  - Container: Column들을 담고 있는 공간

- Bootstrap grid system

  - Bootstrap Grid system은 flexbox로 제작된다
  - Container, rows, column으로 컨텐츠를 배치하고 정렬한다.

- 반드시 기억해야 할 2가지

  - 약수가 많아야 배치를 더 다양하게 가능

  - 12개의 column을 활용한다

  - 6개의 grid breakpoints
    - 화면 너비에 따라 내가 배치를 어떻게 하는지 달라질 수 있는지(분기점)

- Grid system

  ```html
  <div class="container">
    <div class="row">
      <div class = "col"></div>
      <div class = "col"></div>
      <div class = "col"></div>
    </div>
  </div>
  ```

- Grid system breakpoints

| Grid tiers | Class prefix | Size      |
| ---------- | ------------ | --------- |
| xs         | col          | < 576px   |
| sm         | col-sm       | >= 576px  |
| md         | col-md       | >= 768px  |
| lg         | col-lg       | >= 992px  |
| xl         | col-xl       | >= 1200px |
| xxl        | col-xxl      | >= 1400px |

- Grid system breakpoints 연습하기

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
  <title>Document</title>
  <style>
    .box{
      background-color: antiquewhite;
      border: 1px solid black;
      text-align: center;
    }
  </style>
</head>
<body>
  <div class="container">
    <!--gutter라고 불리우는 공간이 padding으로 잡혀있다. 박스 안에 쏙 들어간다.-->
    <div class="row my-3">
      <div class="col"><div class="box">col</div></div>
      <div class="col"><div class="box">col</div></div>
      <div class="col"><div class="box">col</div></div>
  </div>
    <div class="row my-3">
      <div class="col"><div class="box">col</div></div>
      <div class="col"><div class="box">col</div></div>
      <div class="col"><div class="box">col</div></div>
      <div class="col"><div class="box">col</div></div>
</div>
</div>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>  
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
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
  <title>Document</title>
  <style>
    .box{
      background-color: antiquewhite;
      border: 1px solid black;
      text-align: center;
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="row my-3">
      <div class="box col-3">1</div>
      <div class="box col-6">2</div>
      <div class="box col-3">3</div>
  </div>
    <div class="row my-3">
      <div class="box col-1">1</div>
      <div class="box col-1">2</div>
      <div class="box col-1">3</div>
      <div class="box col-1">4</div>
      <div class="box col-1">5</div>
      <div class="box col-1">6</div>
      <div class="box col-1">7</div>
      <div class="box col-1">8</div>
      <div class="box col-1">9</div>
      <div class="box col-1">10</div>
      <div class="box col-1">11</div>
      <div class="box col-1">12</div>
      <div class="box col-1">13</div>
      
      

</div>
</div>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>  
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
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
    <title>Document</title>
    <style>
      .box{
        background-color: antiquewhite;
        border: 1px solid black;
        text-align: center;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <div class="row">
        <!--화면의 크기에 따라 줄어드는 정도 처음에는 12칸 그 다음 줄이면 8칸 더 줄이면 6칸.. 4칸..-->
        <div class="box col-12 col-sm-8 col-md-6 col-lg-4 col-xl-3">1</div>
        
  
  </div>
  </div>
  
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>  
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
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
  <title>Document</title>
  <style>
    .box{
      background-color: antiquewhite;
      border: 1px solid black;
      text-align: center;
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="row">
      <div class="box col-sm-8 col-md-4 col-lg-5">1</div>
      <div class="box col-8 col-sm-2 col-md-4 col-lg-5">2</div>
      <div class="box col-2 col-sm-2 col-md-4 col-lg-5">3</div>
    </div>
</div>
<hr>
<h2 class="text-center">nesting</h2>
<div class="row">
    <div class="box col-6">
      <div class="row">
        <div class="box col-3">1</div>
        <div class="box col-3">2</div>
        <div class="box col-3">3</div>
        <div class="box col-3">3</div>
      </div>
    </div>
    <div class="box col-6">1</div>
    <div class="box col-6">2</div>
    <div class="box col-6">3</div>
</div>
<hr>

<h2 class="text-center">offset</h2>
<div class="row">
    <div class="box col-md-4 offset-4">.col-md-4 .offset-4</div>
    <div class="box col-md-4 offset-md-4 offset-lg-2">.col-md-4 .offset-md-4. .offset-lg-2</div>
</div>
<hr>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>  
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
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
  <title>Document</title>
  <style>
    .box{
      background-color: antiquewhite;
      border: 1px solid black;
      text-align: center;
    }
  </style>
</head>
<body>
  <!-- 총 6개를 배치할건데,
  한 줄에...
  가장 작은 화면 : 한개
  모바일 : 2개
  태블릿 : 3개
  PC : 4
  -->
  <div class="row my-3">
    <div class="col-12 col-sm-6 col-md-4 col-lg-3">
      <div class="box">col</div>
    </div>
    <div class="col-12 col-sm-6 col-md-4 col-lg-3">
      <div class="box">col</div>
    </div>
    <div class="col-12 col-sm-6 col-md-4 col-lg-3">
      <div class="box">col</div>
    </div>
    <div class="col-12 col-sm-6 col-md-4 col-lg-3">
      <div class="box">col</div>
    </div>
    <div class="col-12 col-sm-6 col-md-4 col-lg-3">
      <div class="box">col</div>
    </div>
    <div class="col-12 col-sm-6 col-md-4 col-lg-3">
      <div class="box">col</div>
    </div>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>  
</body>
</html>
```





```html
<!-- page content-->
  <div class="container px-3 px-lg-5 m-">
      <div class="row gx-4 gx-lg-5 align-items-center my-5">
        <div class="col-lo-7"></div>
        <img class="img-fluid rounded mb-4 mb-lg-0" src="./images/이미지사진.jpeg" alt="">
      </div>
        <div class="col-lg-5">
          <h1 class="font-weight-light">Business Name or Tagline</h1>
      <p>This is a template that is great for small businesses. It doesn't have too much fancy flare to it, but it makes a great use of the standard Bootstrap core components. Feel free to use this template for any project you want!</p>
      <a class="btn btn-primary" href="#!">Call to Action!</a>
    </div>
  </div>
  <!-- content Row-->
  <div class="card text-white bg-secondary my-5 py-4 text-center">
    <div class="card-body">
      <p class="text-white m-0">
        "This call to action card is a great place to showcase some important information or display a clever tagline!"
      </p>
    </div>
  </div>
```

```python
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
  <title>Document</title>
  <style>
    .box{
      background-color: antiquewhite;
      border: 1px solid black;
      text-align: center;
    }
    .parent{
      background-color: pink;
      height: 500px;
    }
  </style>
</head>
  <div class="row parent">
    <div class="box col-3 align-self-start">1</div>
    <div class="box col-3 align-self-center">2</div>
    <div class="box col-3 align-self-end">3</div>
</div> 
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>  
</body>
</html>

```

