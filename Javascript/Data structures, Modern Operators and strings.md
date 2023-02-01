#### 1. Destrucuturing Arrays

- destructing 는 ESX(좀 더 디테일하게 내일) 특징이다. 일반적으로 값들을 언팩킹하는 방법 중에 하나다.

- 다른 의미로 복잡한 데이터 구조를 작은 데이터 구조로 변환하는 과정이다.

```js
const arr = [2, 3, 4];
const a = arr[0];
const b = arr[1];
const c = arr[2];

//destructuring
const [x, y, z] = arr;
console.log(x, y, z);

const restaurant = {
  name: 'Classico Italiano',
  location: 'Via Angelo Tavanti 23, Firenze, Italy',
  categories: ['Italian', 'Pizzeria', 'Vegetarian', 'Organic'],
  starterMenu: ['Focaccia', 'Bruschetta', 'Garlic Bread', 'Caprese Salad'],
  mainMenu: ['Pizza', 'Pasta', 'Risotto'],
  
  order: function(starterIndex, mainIndex) {
    return [this.starterMenu[starterIndex], this.mainIndex[mainIndex]];
  }
}  

const [first, second] = restaurant.categories;
// Italian, Pizzeria
console.log(first, second);

const [first, , second] = restaurant.categories;
// Italian, Vegetarian 
// 만약에 아무것도 쓰지 않고 콤마만 하게 되면 그 값을 뛰어 넘게 된다.
console.log(first, second);


// 함수로부터 2개의 값들을 받고 return한다.
const [starter, mainCourse] = restaurant.order(2, 0);
// Garlic bread Pizza
console.log(starter, mainCourse)


//nested destructuring
const nested = [2, 4, [5, 6]];
// 2, [5, 6]
// const [i, , j] = nested;
const [i, , [j, k]] = nested;
// 2, 5, 6
console.log(i, j, k);


//Default values 
const [p, q, r] = [8, 9]
// 8, 9, 1
console.log(p, q, r);

//Default values 
const [p, q= 1, r=1] = [8]
// 8, 1, 1
console.log(p, q, r);
```



- 원래는 우리가 첫 번째와 두 번째 인덱스의 값을 바꿀때 아래의 방식처럼 했다.

  ```js
  const temp = main;
  main = secondary;
  secondary = temp;
  ```

- 하지만 destructuring을 사용하면 위에처럼 임시변수를 만들 필요가 없다

  ```js
  [main, secondary] = [secondary, main];
  ```

  



#### 2.Destructuring Objects

```js
const restaurant = {
  name: 'Classico Italiano',
  location: 'Via Angelo Tavanti 23, Firenze, Italy',
  categories: ['Italian', 'Pizzeria', 'Vegetarian', 'Organic'],
  starterMenu: ['Focaccia', 'Bruschetta', 'Garlic Bread', 'Caprese Salad'],
  mainMenu: ['Pizza', 'Pasta', 'Risotto'],
  
  
  openingHours: {
    thu: {
      open: 12,
      close: 22,
    },
    fri: {
      open: 11,
      close: 23,
    },
    sat: {
      open: 0, // Open 24 hours
      close: 24,
    },
  },
  
  order: function(starterIndex, mainIndex) {
    return [this.starterMenu[starterIndex], this.mainIndex[mainIndex]];
  }
  
  orderDelivery: function({starterIndex, mainIndex, time, address}){
    console.log('Order received! ${this.starterMenu[starterIndex]} and ${this.mainMenu[mainIndex]} will be delivered to ${address} at ${time}');
  }, 

// 오직 하나의 객체가 함수 안으로 들어가다 1개의 argument, 1개의 객체 우리는 4개의 argument가 안으로 들어간게 아니다
restaurant.orderDelivery({
  time: '22:30',
  address: 'Via del Sole, 21',
  mainIndex: 2,
  starterIndex: 2,
});


const { name, openingHours, categories} = restaurant;
//잘 출력 돼
console.log(name, openingHours, categories)

//서드파티로서 활용 가능하다.
const { name: restaurantName, openingHours: hours, categories: tags} = restaurant;
console.log(restaurantName, hours, tags)


// Default values
const { menu = [],  starterMenu: starters = []} = restaurant;
consoloe.log(menu, starters);

// mutating variables
let a = 111;
let b = 999;

const obj = { a: 23, b: 7, c: 14};

// 자바스크립트는 코드 블럭을 기대한다. 우리는 코드 블럭을 할당한 적이 없다
// uncaught syntaxError: Unexpected token '='
{a, b} = obj;

// a = 23, b = 7 정상으로 작동한다. parenthesis를 사용한다.
({a, b} = objl)

// fri: { open:11, close:23}
const { fri } = openingHours;
console.log(open, close);
// 11, 23
const { fri: {open, close} } = openingHours;
console.log(open, close);

// 11, 23
const { fri: {open: o, close: c} } = openingHours;
console.log(open, close);

// 값을 지정할 수도 있다.(default)
 orderDelivery: function({starterIndex =1 , mainIndex = 0, time= '20:00', address}){
    console.log(`Order received! ${this.starterMenu[starterIndex]} and ${this.mainMenu[mainIndex]} will be delivered to ${address} at ${time}`);
  },
};

restaurant.orderDelivery({
  address: 'Via del Sole, 21',
  starterIndex: 1,
});

```



#### 3.The Spread Operator

```js
const arr = [7, 8, 9];
const badNewArr = [1, 2, arr[0], arr[1], arr[2]];
//[1,2,7,8,9]
console.log(badNewArr);

//[1,2,7,8,9]- spread Operator
const newArr = [1, 2, ...arr];
console.log(newArr);

// 1 2 7 8 9 
console.log(...newArr);

//["Pizza", "Pasta", "Risotto", "Gnocci"] , comma를 기준으로 값을 입력하면 자동으로 기본 배열에 새로 추가할 수 있다.
const newMenu = [...restaurant.mainMenu, 'Gnocci'];
console.log(newMenu);


//배열 복사
const MainMenuCopy = [...restaurant.mainMenu];

// 2개 배열 합치기
const menu = [...restaurant.mainMenu, ...restaurant.starterMenu]
console.log(menu);

const str = "Jonas";
const letters = [...str, '','S.'];
//["J", "O", "N", "A", "S", " ", "S."]
console.log(letters);
// Jonas
console.log(...str);

// 문자열이 분해되어서 나오기 떄문에 2개 이상의 값들이 존재하기 때문에 작동하지 않는다.
// Uncaught SyntaxError: Unexpected token '...'
console.log(`${...str} Schmedtmann`);

orderPast: function(ing1, ing2, ing3) {
  console.log(`Here is your delicious pasta with ${ing1}, ${ing2} and ${ing3}`);
}
// Real-world example 
const ingredeients = [prompt('Let\'s make pasta! Ingredient 1?'), prompt('Ingredient 2?'), prompt('Ingredient 3')]
console.log(ingredients);

restaurant.orderPasta(ingredients[0], ingredients[1], ingredients[2]);
restaurant.orderPasta(...ingredients);

//objects
const newRestaurant = {foundedIn: 1998, ...restaurant, founder:'Guiseppe'}

const restaurantCopy = {...restaurant};
restaurantCopy.name = 'Ristorante Roma';
//Ristorante Roma
console.log(restaurantCopy.name);
//Classico Italiano
conosle.log(restaurant.name);
```

- 객체는 iterable하지 않다.

- Iterables: arrays, strings, maps, sets. NOT objects

  



#### 4.Rest Pattern and Parameters

```js
// SPREAD, because on Right side of =  
const arr = [1, 2 ...[3, 4]];

//1) destructuring
// REST, because on LEFT side of (a, b를 제외한 나머지 값들이 호출된다.)
const [a, b, ...others] = [1, 2, 3, 4, 5];
// 1, 2, [3, 4, 5]
console.log(a, b, others)

// pizza, risotto와 그리고 객체에서 나머지 선택되지 않은 값들 
// 만약에 rest pattern 뒤에 이름을 또 쓰게 되면 에러가 뜬다
// Uncaught SyntaxError: Rest Element must be last element
const [pizza, , risotto, ...otherFood, bread] = [
  ...restaurant.mainMenu, ...restaurant.starterMenu
]

//objects
const { sat, ...weekdays } = restaurant.openingHours;
// fri: {open: 11, close:23}
conosle.log(weekdays);

//2.functions // rest parameter
const add = function(...numbers) {
  conosle.log(numbers)
}
// [2, 3], [5, 3, 7, 2] ... 정상적으로 함수 안에 들어간다. 복수의 값들이 하나의 배열 안에 들어가게 된다.

add(2, 3);
add(5, 3, 7, 2);
add(8, 2, 5, 3, 2, 1, 4);

const add = function(...numbers) {
  let sum = 0;
  for(let i = 0; i<numbers.length; i++) sum += numbers[i]
  // 5, 17, 25
  console.log(sum);
};

const x = [23, 5, 7];
// 우리가 array의 값들을 한 꺼번에 함수에 넣고 싶으면 spread operator를 사용한다.
add(...x)


const restaurant = {
  name: 'Classico Italiano',
  location: 'Via Angelo Tavanti 23, Firenze, Italy',
  categories: ['Italian', 'Pizzeria', 'Vegetarian', 'Organic'],
  starterMenu: ['Focaccia', 'Bruschetta', 'Garlic Bread', 'Caprese Salad'],
  mainMenu: ['Pizza', 'Pasta', 'Risotto'],
  
  
  openingHours: {
    thu: {
      open: 12,
      close: 22,
    },
    fri: {
      open: 11,
      close: 23,
    },
    sat: {
      open: 0, // Open 24 hours
      close: 24,
    },
  },
  
  order: function(starterIndex, mainIndex) {
    return [this.starterMenu[starterIndex], this.mainIndex[mainIndex]];
  }

	orderPizza: function(mainIngredient, ... otherIngredients) {
  	console.log(mainIngredient);
  	console.log(otherIngredients);
}

// mushroom and ["onion", "olives", "spinach"] 이렇게 출력- rest parameter에 의해서
restaurant.orderPizza('mushrooms', 'onion', 'olives', 'spinach');
// mushroom and [] 출력
restaurant.orderPizza('mushrooms');
```

- Rest 패턴은 destructuring assignment에서 사용되지 않는 요소들을 수집한다.



#### 5.Short Circulating (&& and ||)

```js
// 어떤 데이터 타입을 쓰던지, 어떤 데이터 타입을 리턴한다 short-cirulating(=short circuit evaluation)이라고 한다
// 우리가 사용한 값들이 불린이 아니어서 그냥 3을 출력한다.
// or operator에서는 short circuiting에서 참인 값이면 첫 번째 값을 리턴한다. 그 뒤에 값은 고려하지 않는다.
console.log('---- or ----')
// 3
console.log(3 || 'Jonas');
// Jonas('' is a falsy value)
console.log('' || "Jonas");
// true
console.log(true || 0);
// null(undefined is a falsy value) 
console.log(undefined || null);

// Hello
console.log(undefined || 0 || '' || 'Hello' || 23 || null);

restaurant.numGeusts = 23;
//23
const guest1 = restaurant ? restaruant.numGuest : 10;
console.log(guest1);

const guest2 = restaurant.numGuest || 10
//23
console.log(guest2);

console.log('---- AND ----')

// 0 
console.log(0 && 'Jonas');
// Jonas (7은 truthy value라서 마지막 값인 Jonas가 return된다)
console.log(7 && 'Jonas');

// null 출력 (and는 truthy value는 건너뛴다.)
console.log("Hello" && 23 && null && 'jonas');

// Practical example
// 
if (restaurant.orderPizza) {
  restaurant.orderPizza('mushrooms', 'spinach');
}

//  mushrooms, ["spinach"]
restaurant.orderPizza && restaurant.orderPizza('mushrooms', 'spinach');
```



#### 6. The Nullish Coalescing Operator (??)

```js
const guest2 = restaurant.numGuests || 10
//10
console.log(guest2);


// 만약에 numGuest가 0이기 떄문에 0이 출력된다(undefined에 속하지 않는다.)
restaurant.numGuests = 0
// nullish values: null and undefined(NOT 0 or '') 두 번째 operand의 값이 실행된다.
// 10 
const guestcorrect = restaurant.numGuests ?? 10;
console.log(guestCorrect);

```



