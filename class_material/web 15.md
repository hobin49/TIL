### JavaScript LIbrary 활용







```js
//form은 input을 받아서 => name과 value를 쌍으로 하여 => action으로 보낸다.싨
form.addEventListener('submit', function(event) {
  // click이벤트를 막아야 consolo.log가 정상적으로 출력된다.
  event.preventDefault()
  // formData 객체는 요소를 form
  const formData = new FormData(form)
  // map이랑 동일하게 formdata가 배열object가 아니기 때문에 볼 수 없다.
  // 별도의 객체여서 조회 x. 반복하면 됨
  console.log(formData)
  console.log(formData.get('password'))
  // input은 사용자가 입력한 깂에 대한 이름 붙이기다.
  console.log(formData.get('password_confirmation'))
}
```



