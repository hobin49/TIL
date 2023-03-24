```js
const h1 = document.querySelector("div.hello:first-child h1");


function handleTitleClick() {
  h1.style.color = "blue";
}


function handleMouseEnter() {
  h1.innerText = "mouse is here"
}

function handleMouseLeave() {
  h1.innerText = "mouse is gone"
}

function handleWindowResize() {
  document.body.style.backgroundColor = "tomato";
}

function handleWindowCopy() {
  alert("copier!");
}

function handleWindowOffline() {
  alert("SOS no WIFI");
}

function handleWindowOnline() {
  alert("All good");
}


h1.addEventListener("click", handleTitleClick);
h1.addEventListener("mouseenter", handleMouseEnter);
h1.addEventListener("mouseleave", handleMouseLeave);

// 사이즈 조정시에 칼라 변경
window.addEventListener("resize", handleWindowResize);
// 카피 방지
window.addEventListener("copy", handleWindowCopy);

// wifi 연결 안 되었을때
window.addEventListener("offline", handleWindowOffline);

// wifi 연결 됐을때
window.addEventListener("online", handleWindowOnline);
```



```js
//기존이 className은 이전 클래스를 없애버리는 문제가 있으니 classList.add()나 classList.remove()를 가지고 추가 및 삭제를 하자
function handleTitleClick() {
  const clickedClass = "clicked";
  if (h1.classList.contains(clickedClass)) {
    h1.classList.remove(clickedClass);
  } else {
    h1.classList.add(clickedClass);
  }

}
```

```js
// 위에 보다 간편한 방법은
const h1 = document.querySelector("div.hello:first-child h1");

// 토글을 사용하면 클래스리스트에 클래스가 있으면 삭제하고 없으면 생성하는 역할을 한다.
function handleTitleClick() {
  h1.classList.toggle("clicked");

}

h1.addEventListener("click", handleTitleClick);
```

- **중요한건 addEventListener 안에 있는 함수는 직접 실행하지 않는다는 것이다.**
- setInterval()은 몇 초 간격으로 값을 뽑아낸다.
- setTimeout()은 몇 초 후에 값을 출력한다.

```js
const clock = document.querySelector("h2#clock");


function getClock() {
  const date = new Date();
  const hours = String(date.getHours()).padStart(2, "0");
  // 숫자형 -> 문자형 변환후에 padStart를 사용해서 2숫자가 한 자리여도 앞에 0이 붙을 수 있게
  const minutes = String(date.getMinutes()).padStart(2, "0");
  const seconds = String(date.getSeconds()).padStart(2, "0");
  clock.innerText = `${hours}:${minutes}:${seconds}`
}

getClock();
setInterval(getClock, 1000);
```

