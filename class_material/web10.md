항상 카드에 마진 my-3 주고 width-18rem되어 없애고 그리고 space between해도 된다.

Card-title fw-bold 아니면

style을 .card-title{

Font-weight: bold;

}

카드들에 gx를 주지 않아도 떨어진다.

이미지에 placeholder를 써도 돼

밑줄 치고 싶으면

클래스로 별도 관리

.original-price{

​	text-align:center

​	text-decoration: line-through

}

카드에 Position relative가 되어있어서 absolute를 쓸 필요가 없다.

position element - bootstrap

뱃지를 이미지 기준 좌측 하단에 배치하려면 이미지랑 뱃지를 하나로 묶고 

```html
<div class="position-relative">
  <img src ="">
  <span class="badge text-bg-danger position-absolute start-0 bottom-0 m-1"></span>
</div>
```



<img src = "" alt="logo" style="height:60px">

```
 <a href="#here">위 소제목으로 가지겠죠?</a>
```

