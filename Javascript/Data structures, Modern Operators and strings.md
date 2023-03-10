#### 1. Destrucuturing Arrays

- destructing 는 ESX 특징이다. 일반적으로 값들을 언팩킹하는 방법 중에 하나다.

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
// 잘 출력 돼
console.log(name, openingHours, categories)

// 서드파티로서 활용 가능하다.
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



#### 5.Short Circulating (&& and ||)- 단축평가값

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



#### coding-challenge 1

```js
const game = {
  team1: 'Boyern Munich',
  team2: 'Borrussia Dortmund',
  players: [
    [
      'Neuer',
      'Pavard',
      'Martinez',
      'Alaba',
      'Davies',
      'Kimmich',
      'Goretzka',
      'Coman',
      'Muller',
      'Gnarby',
      'Lewandowski',
    ],
    [
      'Burki',
      'Schulz',
      'Hummels',
      'Akanji',
      'Hakimi',
      'Weigl',
      'Witsel',
      'Hazard',
      'Brandt',
      'Sancho',
      'Gotze',
    ],
 ],
 score: '4:0',
 scored: ['Lewandowski', 'Gnarby', 'Lewandowski', 'Hummels'],
 data: 'Nov 9th, 2037',
 odds: {
  team1: 1.33,
  x: 3.25,
  team2: 6.5,
 },
};


// 1. 배열 2개로 나뉘어진다.
const [players1, players2] = game.players;

// 2. 리스트의 한 명을 뽑고 나머지 배열에 담는다
const[gk, ...fieldPlayers] = players1;


// 3. 모든 플레이어를 담아라(배열 합치기)
const allPlayers = [...players1, ...players2];

// 4. 배열에 추가하기
const players1Final = [...players1, 'Thiago', 'Coutinho', 'Perisic'];

// 5. 객체에 값들 순차적으로 뽑아내기
const {odds: {tema1, x: draw, team2}} = game;

// 6.
const printGoals = function (...players) {
  console.log(`${players.length} goals were scored`);
}

//4 goals were scored
printGoals('Davies', 'Muller', 'Lewandowski', "Kimmich");
//2 goals were scored
printGoals('Davies', 'Muller');
//4
printGoals(...game.scored);

// 7 and 연산자 true이면 앤드 다음이 실행된다.
team1 < team2 && console.log('Team 1 is more likely to win');
team1 > team2 && console.log('Team 2 is more likely to win');
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



#### 7.Logical Assignment Operators

```js
const res1 = {
  name: 'Capri',
  numGuests: 20,
  
};
const res2 = {
  name: 'La Piazza',
  owner: 'Giovanni Rossi',
};

rest1.numGuests = rest1.numGuests || 10;
rest2.numGuests = rest2.numGuests || 10;

// {name:'Capri', numGuests:20}
console.log(rest1);
// {name:'La Piazza', owner:'Giovanni Rossi', numGuests:10}
console.log(rest2);

// OR assignment operator
rest1.numGuests ||= 10;
rest1.numGuests ||= 10;

// nullish assignment operator (null or undefined)
rest1.numGuests ??= 10;
rest1.numGuests ??= 10;

// owner: 0
rest1.owner = rest1.owner && '<ANONYMOUS>';
// owner: '<ANONYMOUS>'
rest2.owner = rest2.owner && '<ANONYMOUS>';

// owner set to undefined, 그래서 owner은 출력되지 않는다.
rest1.owner && '<ANONYMOUS>';
// owner: '<ANONYMOUS>'
rest2.owner && '<ANONYMOUS>';
```





#### 8.Looping Arrays: The for-of Loop

```js
const menu = [...restaurant.starterMenu, ...restaurant.mainMenu];

//continue와 break를 사용할 수 없다
for (const item of menu) console.log(item);



for (const item of menu.entries()) {
  //[1, item], [2, item]...
  console.log(item);
}

for (const [i, el] of menu.entries()){
  // 1: item, 2: bruschetta, 3: Garlic bread, 4: Pizza
  console.log(`${item[0] + 1}: ${item[1]}`)
  // 위에랑 똑같은 결과 값이 나온다.
  console.log(`${i + 1}: ${el}`)
}
```



#### 9. Enhanced object Literals

```js
const weekdays = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun'];
const hours = {
    [weekdays[3]]: {
      open: 12,
      close: 22,
    },
    [weekdays[4]]: {
      open: 11,
      close: 23,
    },
    [weekdays[5]]: {
      open: 0,
      close: 24,
    },
  };


// 밖에서 선언한 객체를 안에다 쓸 수 있다.
const restaurant = {
  // ES6 enhanced object literals
  hours
}

// 바뀐 점( function expression)
// 변경 전
order: function(startIndex, mainIndex) {
  return [this.starterMenu[starterIndex], this.mainMenu[mainIndex]]
}

// 변경 후 (function이 빠졌다.)
order(startIndex, mainIndex) {
  return [this.starterMenu[starterIndex], this.mainMenu[mainIndex]];
}


```



### 10.Optional Chaining

```js
//11
if (restaurant.openingHours.fri) cosole.log (restaurant.openingHOurs.fri.open)

// OPtional chaning 쓰기 전
if (restaurant.openingHours && restaurant.openingHours.fri) 
	cosole.log (restaurant.openingHOurs.fri.open)
	
// WITH optional chaning // 앞에 값이 undefined || null 이면 각각 undefined이나 null이 출력된다.
// 만약 mon(월요일)이 존재하면 open property가 읽을 수 있다.
console.log(restaurant.openingHours.mon?.open);
// ? 없으면 Uncaught TypeError가 뜬다.
console.log(restaurant.openingHours?.mon?.open);

// Example
const days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun'];

for (const day of days) {
  // thu, we open at 12, fri, we open at 11, On sat, we open at 0 
  // 처음에 or 연산자 쓰면 토요일 오픈시간이 0이면 falsy value라서 undefined가 출력된다 
  // 그래서 nuliish coalescing operator를 사용해서 nullish(null, undefined) 아니면 값이 출력될 수 있게 조치를 취한다.
  const open = restaurant.openingHours[day]?.open ?? 'closed';
  console.log(`On ${day}, we open at ${open}`);
}


// Methods
// ["Focaccia", "Pasta"]
console.log(restaurant.order?.(0, 1) ?? 'Method does not exist');
// Method does not exist(nullish coalescing operator('??')) - 앞에 옵셔널 체이닝 파트가 값이 존재하지 않는다. 
console.log(restaurant.orderRisoto?.(0, 1) ?? 'Method does not exist');

// Arrays
const users = [
  {name: 'Jonas', email: 'hello@jonas.io'}
];

// Jonas
console.log(users[0]?.name ?? 'User array empty')

const users = []
// User array empty
console.log(users[0]?.name ?? 'User array empty')

if(users.length > 0) console.log(users[0].name);
else console.log('user array empty')
```

- 특정값이 존재하지 않으면 `undfined` 를 바로 리턴한다.
- 옵셔널체이닝을 사용하지 않으면 바로 `uncaught TypeError`을 만든다.





#### 11.Looping Objects: Object Keys, Values, and Entries

```js
// Property NAMES
const properties = Object.keys(openingHours);
// ["thu", "fri", "sat"]
console.log(properties);

// we are open on 3days
let openStr = `We are open on ${properties.length} days: `


for (const day of properties) {
  //Thu, fri, sat
  console.log(day);
  
  openStr += `${day},`
}
// we are open on 3 days: thu, fri, sat
console.log(openStr)


// Property values
// 0: {open:12, close:22}
const values = Object.values(openingHours);
console.log(values)

// Entire obejct
// 키와 값을 배열로 return 
const entries = Object.entries(openingHours);

// each key, value
for (const x of entries) {
  console.log(entries);
  
}
// [key, value ]
for (const [key, {open, close}] of entries) {
	console.log(`On ${key} we open at ${open} and close at ${close}`)  
}
```



#### coding chanllenge 2

```js
//1.

for (const [i, player] of game.scored.entries()) {
  console.log(`Goal ${i + 1}: ${player}`)
}


//2.
const odds = Object.values(game.odds);
let a = 0
for (const odd of Object.values(odds)) {
  a += odd
}
a /= odds.length;
console.log(a)

//3.
for (const [team, odd] of Object.entries(game.odds)) {
  const teamStr = team === 'x' ? 'draw' : `victory $ {game[team]}`
  console.log(`Odd of victory ${teamStr} ${odd}`)
}

//4.
const scorers = {};
for (const player of game.scored) {
  scorers[player] ? scorers[player]++ : (scorers[player] = 1);
}
console.log(scorers)
```





#### 12.Sets

```javascript
const ordersSet = new Set(['Pasta', 'Pizza', 'Pizaa', 'Risotto', 'Pasta', 'Pizza'])

// pasta, pizza, risotto
console.log(ordersSet);

// 3 (array에 있는 length랑 다른 것이다! 몇 개의 구성으로 되어 있는지 세어준다.
console.log(ordersSet.size);

// true
console.log(ordersSet.has('Pizza'));
// false
console.log(ordersSet.has('Bread'));

ordersSet.add("Garlic Bread");
ordersSet.add("Garlic Bread");
//정상 삭제됨
ordersSet.delete("Risotto");
//set에 모든 데이터들 비운다.
ordersSet.clear();
//Garlic bread 1개만 들어간다.
console.log(ordersSet)
//undefined
console.log(ordersSet[0])


// pasta, pizza, garlic Bread 차례대로 출력
for (const order of ordersSet) console.log(order);

// Example 
const staff = ["Waiter", "Chef", "waiter", "manager", "chef", "waiter"];
// set -> array 변환(spread operator) 사용
const staffUnique = [...new Set(staff)];
// Waiter, chef, manager
console.log(staffUnique);
// 11
console.log(new Set('Jonasschmedtmann').size);

// "J", "o", "N", "A", "S"
console.log(new Set("Jonas"));

```



#### 13.maps

- maps()는 key가 어떤 타입이든지 가질 수 있고 큰 값이어도 된다.
- 그러나 objects에서는 키는 항상 문자열이다.

```js
const rest = new Map();
rest.set('name', 'Classico Italiano');
rest.set(1, "Firenze, Italy")
// {"name" => "Classico Italiano", 1 => "Firenze, Italy", 2 => "Lisbon, Portugal"}
console.log(rest.set(2, "Lisbon, Portugal"))

rest
	.set('categories': ['Italian', 'Pizzeria', 'Vegetarian', 'Organic'])
	.set('open', 11)
	.set('close', 23)
	.set(true, "We are open :D")
	.set(false, "we are closed :(");

console.log(rest.get("name"));
console.log(rest.get(true));
console.log(rest.get(1));

const time = 21;
// true, "We are open :D"
console.log(rest.get(time > rest.get('open') && time < rest.get('close')));

console.log(rest.has('categories'));
rest.delete(2);
console.log(rest);
//7
console.log(rest.size);
// 배열 삽입 가능
rest.set([1,2], "Test")

//undefined ([1, 2])는 힙에서 같은 객체가 아니다. 
console.log(rest.get([1, 2]));

// 그러나 배열을 먼저 선언하게 되면 value가 정상적으로 출력된다
const arr = [1, 2];
rest.set(arr, "Test");
// Test
console.log(rest.get(arr));

rest.set(document.querySelector('h1'), 'Heading');
// key: h1, value: heading
console.log(rest)
```

#### 14.Maps: Iteration

```js
const question = new Map([
  ['question', 'What is the best programming language in the world?'],
  [1, "C"],
  [2, "Java"],
  [3, 'JavaScript'],
  ['correct', 3],
  [true, 'Correct'],
  [false, 'Try again!'],
]);

console.log(question);

// covert object to map
console.log(Obejct.entries(openingHours));
const hoursMap = new Map(Object.entries(openingHours))

for (const [key, value] of question) {
  if (typeof key === 'number') console.log(`Answer ${key}: ${value}`);
}

const answer = Number(prompt('Your answer'));
console.log(answwer);

//having Boolean values as keys
console.log(question.get(question.get('correct') === answer))

// convert map to array 
console.log([...question]);
```



#### 15.Summary: Which Data Structure to Use?

- From the program itself: Data written directly in source code (e.g status messages)
- From the UI: Data input from the user or data written in DOM (e.g tasks in todo app)
- From external sources: Data fetched for example from web API (e.g. recipe objects)
- Array vs Sets
  - Arrays
    - when you ordered list of values 
    - when you need to manipulate data
  - Sets
    - Use when you need to work with unique values
    - Use when high-performance is really important
      - 찾거나 삭제하는데 일반 배열보다 10배 빠르다.
    - Uset to remove duplicates from arrays.
- Objects vs Maps
  - Objects 
    - More "traditional" key/value store ("abused" objects )
    - Easier to write and access values with . and []
    - Use When you need to function(methods)
    - Use when working with JSON (can convert to map)
  - Maps (Es6 전에는 없었다.)
    - Better performance
    - Keys can have any data type
    - Easy to iterate
    - Easy to compute size
    - Use when you simply need to map key to values
    - Use when you need keys that are not strings.

#### 16.code challenge

```js
const events = [...new Set(gameEvents.values())];
events.delete(64);
console.log(
`An event happened, on average, every ${90 / gameEvents.size} minutes`);
for (const [min, event] of gameEvents) {
   const half = min <= 45 ? 'FIRST' : 'SECOND';
   console.log(`[${half} HALF] ${min}: ${event}`);
}
```



#### 17.Working with Strings

 ```js
 const airline = "TAP Air Portugal";
 const plane = "A320";
 
 console.log(plane[0])
 console.log(plane[1])
 console.log(plane[2])
 // 'B'
 console.log('B737'[0])
 // 4
 console.log('B737'.length)
 
 // 6
 console.log(airline.indexOf('r'));
 // 10
 console.log(airline.lastIndexOf('r'))
 //-1
 console.log(airline.indexOf('Portugal'))
 
 //Air Portugal
 console.log(airline.slice(4));
 
 // 7전에 슬라이스를 멈춘다.
 console.log(airline.slice(4, 7));
 
 // TAP
 console.log(airline.slice(0, airline.indexOf(' ')));
 
 // Portugal
 console.log(airline.slice(airline.lastIndexOf(' ') + 1));
 
 // al
 console.log(airline.slice(-2))
 //AP Air Portuga
 console.log(airline.slice(1, -1))
 
 const checkMiddleSeat = function(seat) {
   const s = seat.slice(-1);
   if (s === 'B' || s === "E") console.log('You got the middle seat');
   else console.log('You got luchky')
 } 
 
 checkMiddleSeat('11B');
 checkMiddleSeat('23C');
 checkMiddleSeat('3E')
 
 //object
 console.log(new String('jonas'))
 // string
 console.log(new String('jonas').slice(1));
 ```



