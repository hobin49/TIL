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

  

#### First-Class and Higher-Order Functions

- 자바스크립트에서 함수는 일급 객체이다. 이것은 함수를 변수에 할당하고 다른 함수의 매개변수로 전달하거나 함수에서 반환할 수 있다는 것을 의미한다. 즉, 함수는 객체처럼 취급되며 객체의 특징을 모두 갖추고 있다.

- 예를 들어, 다음과 같이 함수를 변수에 할당할 수 있다.

  ```js
  const add = (a, b) => a + b;
  
  const add = function(a, b) {
    return a + b;
  }
  ```

  - 함수를 변수에 할당하면 그 변수는 함수의 참조를 가지게 되어 함수의 이름을 바꾸거나 다른 변수에 할당할 수 있다
  - 매개변수로 다른 함수에 들어갈 수 있다.

- 함수는 다른 함수의 매개변수로 전달하는 예시

  ```js
  function sayHello(name) {
    console.log(`Hello, ${name}!`);
  }
  
  function greet(greeting, name) {
    greeting(name);
  }
  
  greet(sayHello, "John");
  ```

  - 이처럼 greet의 매개변수에 sayHello()함수를 넣어주면 그 안에 들어가서 함수가 실행되고 이렇게 하면 함수의 재사용성을 높일 수 있다.



- 함수에서 다른 함수를 반환할 수 있다

  ```js
  function createMultiplier(multiplier) {
    return function(number) {
      return number * multiplier;
    }
  }
  
  const double = createMultiplier(2);
  const triple = createMultiplier(3);
  
  console.log(double(5));//10
  console.log(triple(5))//15
  ```

- 클로저

  - 클로저란 함수 내부에서 정의된 함수외 변수들이 외부에서 접근할 수 없도록 보호되면서도, 함수 내부에서만 사용할 수 있도록 유지되는 현상이다.

  ```js
  function createCounter() {
    let count = 0;
  
    return function() {
      count++;
      console.log(count);
    }
  }
  
  const counter1 = createCounter();
  const counter2 = createCounter();
  
  counter1(); // 1
  counter1(); // 2
  counter2(); // 1
  ```

- 고차함수

  - 함수를 인자로 전달받거나, 함수를 반환하는 함수를 말한다. 즉 함수를 다루는 함수라고 할 수 있다
  - 예를 들어 'Array.prototype.map' 함수는 고차 함수이다. map 함수는 배열의 각 요소를 변형하고, 그 변형된 요소들을 새로운 배열로 반환한다. 이때 map 함수의 인자로 함수를 전달하여 각 요소를 변형하는 로직을 구현할 수 있다. 이러한 인자로 전달되는 함수를 콜백함수라고 한다.

  ```js
  const greet = () => console.log("Hev Jonas");
  // addEventListener()이 Higher-order-function이다. greet은 콜백함수이다.
  btnClose.addEventListener('click', greet)
  ```

  

  ```js
  const numbers = [1, 2, 3, 4, 5];
  
  const doubleNumbers = numbers.map(function(number) {
    return number * 2;
  });
  
  console.log(doubledNumbers);
  ```

  - 위 코드에서 map 함수는 배열 numbers의 각 요소를 2배씩 곱한 새로운 배열을 반환한다. 이때 인자로 전달된 함수는 각 요소를 2배씩 곱하는 로직을 구현한 콜백함수이다.
  - 함수는 함수를 반환하는 경우

  ```js
  function multiplyBy(num) {
    return function(x) {
      return x * num;
    };
  }
  
  const multiplyByTwo = multiplyBy(2);
  
  console.log(multiplyByTwo(4)); // 8
  console.log(multiplyByTwo(6)); // 12
  ```

  - First-class functions는 모든 함수는 값이다. 
  - First-class와 higher-order 함수는 서로 다른 개념입니다. First-class 함수는 함수가 값으로 취급될 수 있는 성질을 나타내는 개념이고, Higher-order 함수는 함수를 다루는 함수를 나타내는 개념이다..? (더 공부가 필요)
