#### Default Parameters

```js
'use strict';
const bookings = [];
const createBooking = function(flightNum, numPassengers = 1, price = 199 * numPassengers) {
  // ES5
  // numPassengers = numPassengers || 1;
  // price = price || 199;

  const booking = {
    flightNum,
    numPassengers,
    price
  }
  console.log(booking);
  booking.push(booking);
}

createBooking('LH123')
//override
createBooking('LH123', 2, 800);
// 398
createBooking('LH123', 2);
// 995
createBooking('LH123', 5);

// 그럼 기존에 default value인 1이 출력된다.
createBooking('LH123', undefined, 1000);
```



#### How Passing Arguments works Value vs reference

- 값에 의한 전달은 함수 호출 시 인자의 값 자체를 복사하여 함수 내부로 전달하며, 참조에 의한 전달은 인자의 메모리 주소를 전달하여 함수 내부에서 해당 메모리 공간의 값을 변경할 수 있습니다.

- **그러나 자바스크립트에서는 오직 값에 의한 전달만이 일어난다**

- 예를 들어 

  ```javascript
  function foo(x) {
    x = x + 1;
  }
  
  let originalX = 1;
  // originalX라는 값을 참조해서 foo()함수를 실행해도 1이 출력된다.
  foo(originalX);
  console.log(originalX); // 1

- 하지만 객체나 배열 같은 참조 타입의 경우에는 객체나 배열의 주소가 값으로 전달되기 때문에, 함수 내부에서 객체나 배열의 값을 변경하면 원래 변수의 값도 변경됩니다. 이것은 참조에 의한 전달과 비슷한 동작을 하기 때문에, 이를 참조에 의한 전달이라고 생각할 수도 있습니다. 하지만 이는 엄밀히 따지면 참조에 의한 전달이 아니라 값에 의한 전달이며, 객체나 배열이 가리키는 값 자체는 변경 가능하다.

  ```js
  function foo(arr) {
    arr.push(4);
  }
  
  let originalArr = [1, 2, 3];
  foo(originalArr);
  console.log(originalArr); // [1, 2, 3, 4]
  ```

  

