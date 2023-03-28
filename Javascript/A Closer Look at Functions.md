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

- 자바스크립트는 레퍼런스에 의해서 통과되지 않는다 오직 value에 의해서만 값이 바뀐다.