#### 1.Activating Strict Mode

- 개발자에게 편의성을 주는 모드입니다. 현재 사용이 금지된 구문들을 찾아서 개발자들에게 알려주도록 경고를 띄워주는 역할을 한다.
- 눈에 띄는 에러를 제공해주고 특정한 것들을 하지 못하게 막는다

```js
//acticvate strict mode
'use strict';


let hasDriversLicense = false;
const passTest = true;

if (passTest) hasDriversLicense = true;
if (hasDriversLicense) console.log("I can drive :D");

// we cannot use these names as variables.
const interface = 'now';
const private = 534;
const if = 23;
```



#### 2.Functions

- Function can hold one or more complete lines of code.
- function은 우리가 원하는 만큼 호출할 수 있다.
- parameter은 약간의 로컬변수와 같다. 함수 안에서만 이용가능하다.

```js
function logger() {
 console.log('My name is Jonas');
}

// calling / running / invoking function
logger();
logger();
logger();

function fruitProcessor(apples, oranges) {
  console.log(apples, oranges);
  const juice = `Juice with ${apples} apples and ${oranges} oranges.`;
  return juice;
} 

const appleJuice = fruitProcessor(5, 0); 
console.log(appleJuice);
//변수에 담지 않고 출력
console.log(fruitProcessor(5, 0));

const appleOrangeJuice = fruitProcessor(2, 4);
console.log(appleOrangeJuice);
```



#### 3.Function Declarations vs Expressions

- functions들은 문자, 숫자, 불린 값들이지 어떠한 형태의 타입이 아니다. 그게 어떠한 값이면 우리는 그것을 변수 안에 저장할 수 있다.

```js
// Function declaration
function calcAge1(birthYear) {
  return 2037 - birthYear;
}

const age1 = calcAge1(1991);


// Function expression
// function is not a type
const calcAge2 = function (birthYear) {
  return 2037 - birthYear;
}

const age2 = calcAge2(1991);

//result is all the same
console.log(age1, age2);
```





#### 4.Arrow Functions

- 쉽고 빠르게 쓸 수 있다
- Curly braces 쓸 필요가 없다
  - return이 내재적으로 발생한다.
  - return keyword가 없어도 쓸 수 있다.
- 복수의 파라미터를 받을때는 소괄호를 사용한다.
- 더 많은 파라미터를 쓸수록 arrow function의 장점이 없어지게 된다.

```js
// Arrow function

const calAge3 = birthYear => 2037 - birthYear;
const age3 = calAge3(1991);
console.log(age3);


const yearsUntilRetirement = (birthYear, firstName) => {
  const age = 2037 - birthYear;
  const retirement = 65 - age;
  //return retirement;
  return `${firstName} retires in ${retirement} years`;
}

console.log(yearsUntilRetirement(1991, "Jonas"));
console.log(yearsUntilRetirement(1980, "Bob"));
```



#### 5. Functions Calling Other Functions 

- function을 쓰지 않으면 값이 변경되어 있을시에 변수에 담아 놓은 부분들을 다 바꿔야 한다. 그래서 함수를 쓰자!

```javascript
function cutFruitPieces(fruit) {
  return fruit * 4;
}

function fruitProcessor(apples, oranges) {
  const applePieces = cutFruitPieces(apples);
  const orangePieces = cutFruitPieces(oranges);

  console.log(apples, oranges);
  const juice = `Juice with ${applePieces} piece of apples and ${orangePieces} pieces of oranges.`;
  return juice;
} 


console.log(fruitProcessor(2, 3)); 
```



#### 6.Reviewing Functions

- console.log를 return 뒤에 놓으면 실행되지 않으니 return 전에 실행해야한다.
- Function declaration
  - Function that can be used before it's declared
- Function expression
  - Essentially a function value stored in a variable 
- Arrow Function
  - Great for a quick one-line functions. Has no this keyword
  - Omit (function, return)

```js
function calcAge(birthYear) {
  return 2037 - birthYear;
}

const calcAge = function (birthYear) {
  return 2037 - birthyear;
}


const calcAge = birthYear => 2037 - birthYear;


// calling, running or invoking the function, using()
console.log(yearsUntilRetirement(1991, 'Jonas')); 
```

- Parameter: placeholder(가목적어) to receive input values. Like local variables of a function
- function body: block of code that we want to reuse. Processes the function's input data.

- Return: statement to output a value from the function and terminate execution.
- Arguments: actual values of function parameters, to iuput data
- Variable: to save returned value(function output)

```js
const calcAge = function(birthYear) {
  return 2037 - birthYear;
}



const yearsUntilRetirement = function (birthYear,
firstName) {
  const age = calcAge(birthYear);
  const retirement = 65 - age;

  if (retirement > 0 ) {
    console.log(`${firstName} retires in ${retirement} years`); 
    return retirement;
  } else {
    console.log(`${firstName} has already retired`);
    return -1;
  }
}

console.log(yearsUntilRetirement(1991, 'Jonas'));
console.log(yearsUntilRetirement(1970, 'Mike'));
```





#### Coding Challenge #1 

```js
function calcAverage(a, b, c) {
  return (a + b + c) / 3
}

const scoreDolphins = calcAverage(44, 23, 71);
const scoreKoalas = calcAverage(62, 54, 49);

console.log(scoreDolphins, scoreKoalas)

// 1. Declaration
function Checkwinner(avgDolphins, avgKoalas) {
  if(avgKoalas >= 2 * avgDolphins) {
    console.log(`Koalas win (${avgKoalas} vs ${avgDolphins})`)
  } else if (avgKoalas <= 2 * avgDolphins) {
    console.log(`dolphins win (${avgDolphins} vs ${avgKoalas})`)
  } else {
    console.log("No team wins")
  }

}

Checkwinner(scoreDolphins, scoreKoalas)

//2. expression 
const checkwinner = function(avgDolphins, avgKoalas) {
  if (avgDolphins >= 2 * avgKoalas) {
    console.log(`Koalas win (${avgDolphins} vs ${avgKoalas})`);
  } else if(avgKoalas >= 2 * avgDolphins){
    console.log(`Dolphins win (${avgKoalas} vs ${avgDolphins})`)
  } else {
    console.log("No team wins")
  }

}

Checkwinner(scoreDolphins, scoreKoalas)

```



#### 7.Introduction to Arrays

- Array is not a primitive value ans so we can actually always change it so we can mutate it.
- **const를 써도 값은 바뀔 수 있다**

```js
const firstName = 'Jonas';
//리스트 안에 변수를 담아도 되고, 숫자를 계산해도 되고, 이미 만들어진 array를 넣어도 된다.
const jonas = [firstName, "Schmedtmann", 2037 - 1991, 'teacher', friends];

console.log(jonas)


//Exercise
const calcAge = function(birthYear) {
  return 2037 - birthYear;
}

//this is not gonna work; 
// this year is an array. it doesn't know what to do with it.
const year = [1991, 1975, 2002, 2009, 2015];
// Nan
// console.log(calcAge(year));

const age1 = calcAge(year[0]);
const age2 = calcAge(year[1]);
const age3 = calcAge(year[2]);
console.log(age1, age2, age3);
//value를 생성하니까 array 안에 들어가도 돼
const ages = [calcAge(year[0]), calcAge(year[1]), calcAge(year[2])]
calcAge(year[year.length - 1]);
console.log(ages)
```



#### 8.Basic array operations

- 기본적으로 값을 추가할때는 `push`, array 앞에 추가하고 싶을때는 `unshift` 를 사용한다.
- 값을 지우고 싶으면 `pop`, 앞의 요소를 삭제하고 싶으면 `shift`를 사용한다.
- array 의 요소의 인덱스를 알고 싶으면 `indexOf`를 사용한다.
- 어떤 값이 array 안에 포함되어 있는지 확인하려면 `includes` 를 사용한다. true/false로 반환해준다.

```js
const friends = ['Michael', 'Steven', 'Peter'];
// print(4) we don't need to calculate separately
// Add elements
const newLength = friends.push("Jay");
console.log(friends);
console.log(newLength);

// unshift method also returned the length of the new array.
friends.unshift('John');
console.log(friends);


//Remove elements
friends.pop(); // Last
const popped = friends.pop();
console.log(popped);
console.log(friends)

friends.shift(); //first
console.log(friends);

//list index
console.log(friends.indexOf('Steven'));
console.log(friends.indexOf('Bob'));


//ES6 method return true/false

friends.push(23);
console.log(friends.includes('Steven'));
console.log(friends.includes('Bob'));
//it does not do type coercion.
console.log(friends.includes(23));

if (friends.includes('Steven')) {
  console.log("You have a friend called Peter");
}
```

#### Coding Chanllenge #2 

```js
// method1.ternary expression
const calcTip = function(bill) {
  return bill >= 50 && bill <= 300 ? bill * 0.15 : bill * 0.2;
}

// method2.arrow function
// const variable = parameter => if (parameter condition) ?(=) a : else b  
const calcTip = bill => bill >= 50 && bill <= 300 ? bill * 0.15 : bill * 0.2


const bills = new Array(125, 555, 44);

const tips = [calcTip(bills[0]), calcTip(bills[1]), calcTip(bills[2])];


const total = [tips[0] + bills[0], tips[1] + bills[1], tips[2] + bills[2]];
console.log(total);
```



#### 9.Introduction to Objects

- Key-value를 통해서 리스트 안에 value가 정확히 무엇을 가리키는지 알려줄 수 있다.
- 파이썬의 딕셔너리와 비슷하다. object literal syntax라고 불린다.
- 기존에 리스트에서 우리가 어떻게 요소들을 접근해야 하는지 모르기 떄문에 문제가 발생한다. 
- 리스트는 더 많은 순서 데이터가 있을때 사용하고 객체들은 더 구조화되어 있지 않은 경우에 사용된다. 그래서 이름을 지어준다. 그래서 우리는 이름으로 접근한다.

```js
const jonasArray = [
  'Jonas',
  'Schmedtmann',
  2037 - 1991,
  'teacher',
  ['Michael', 'Peter', 'Steven']
];

const jonas = {
  firstName: 'Jonas',
  lastName: 'Schmedtmann',
  age: 2037 - 1991,
  job: "teacher",
  friends: ['Michael', 'Peter', 'Steven']
}

```

#### 10. Dot vs Bracket Notation

- objects에서 순서는 중요하지 않다 왜냐하면 이름 자체로 접근하기 때문이다. 

- operator precedence에서 dot과 bracket notation은 똑같다. 

- **변수를 활용해서 key에 해당하는 값을 찾고 싶다면 Bracket Notation을 사용해야 한다**

- bracket notation에서는 키 값을 작은 따옴표로 묶는다는 점을 기억해야한다. 

- 만약 아래처럼 미리 작은 따옴표를 bracket 안에 넣어두면 undefined를 돌려준다.

  ```js
  function findValue(obj, keyValue) {
      return obj['keyValue'];
  }
  findValue(user, name);    // undefined
  ```



```js
//objects
const jonas = {
  firstName: 'Jonas',
  lastName: 'Schmedtmann',
  age: 2037 - 1991,
  job: "teacher",
  friends: ['Michael', 'Peter', 'Steven']
}

// dot notation
console.log(jonas.lastName);
//bracket notation(if you omit single quotation marks! it won't be working);
console.log(jonas['lastName']);


const nameKey = 'Name';
// working(bracket notation + variable)
console.log(jonas['first' + nameKey]);
console.log(jonas['last' + nameKey]);

//not working(dot notation)- not a computed property name. difference between dot and bracket
console.log(jonas.'last' + nameKey);

const interestIn = prompt('What do you want to know about Jonas? Choose between first Name, lastnmae, age, job, and friends;');

// interestIn이 문자열로 들어간다.
if (jonas[interestIn]) {
  console.log(jonas[interestIn]);
} else {
  console.log('Wrong request! Choose between first Name, lastnmae, age, job, and friends')
}


jonas.location = 'Portugal';
jonas['twitter'] = '@jonasschmedtman';
console.log(jonas);


// Challenge 
// "Jonas has 3 friends, and his best friend is called Michael"
console.log(`${jonas.firstName} has ${jonas.friends.length} friends, and his best friend is called ${jonas['friends'][0]}`)
// jonas.friends[0]
```



#### 11. Objects Methods

- this를 사용하면 object 자체를 가리키기 때문에 object명을 썼을때 관련된 부분을 다 바꿔야하는 것들에서 발생하는 불편함을 제거할 수 있다.
- this를 이용해서 새로운 값을 object에 넣게 되면 함수를 계속 실행하지 않고 바로 계산된 값을 받을 수 있다.

```js

const jonas = {
  firstName: 'Jonas',
  lastName: 'Schmedtmann',
  birthYear: 1991,
  job: "teacher",
  friends: ['Michael', 'Peter', 'Steven'],
  hasDriverLicense: true,

  // calcAge : function(birthYear) {
  //   return 2037 - birthYear
  // }
  calcAge : function() {
    this.age = 2037 - this.birthYear;
    return this.age;
  },

  getSummary : function(){
    return `${this.firstName} is a ${this.calcAge()}-year old ${jonas.job}, and he has ${this.hasDriverLicense ? 'a' : 'no' } driver's license.`
  },

}

// if argument values might change,then we have to change it everywhere
console.log(jonas.calcAge());
//jonas['calcAge'] is a function, it needs parenthesis.
// console.log(jonas['calcAge'](1991));

// below it doesn't work
// function calcAge(birthYear){
//    return 2037 - birthYear
//  }


// challenge 
// "Jonas is a 46-year old teacher, and he has a/no driver's license"
console.log(jonas.getSummary())

```





#### Coding Challenge #3

```js
const mark = {
  name : 'Marks',
  mass : 78,
  height: 1.69,

  calcBMI: function() {
    this.bmi = this.mass / this.height ** 2;
    return this.bmi;
  }
}

const john = {
  name : "John",
  mass : 92,
  height : 1.95,
  calcBMI: function() {
    this.bmi = this.mass / this.height ** 2;
    return this.bmi;
  }
}

//이걸 써줘야 밑에서 bmi를 접근했을때 값을 출력해준다. 안하면 undefined
mark.calcBMI();
john.calcBMI();

console.log(mark.bmi);

if (mark.bmi < john.bmi) {
  console.log(`John's BMI (${john.bmi}) is higher than Mark's ${mark.bmi}!`)
} else {
  console.log(`mark's BMI ${mark.bmi} is higher than Mark's ${john.bmi}!`)
}

```



#### 12.Iteration: The for Loop

```js
// for loop keep running while condition is TRUE 
for(let rep = 1; rep <= 10; rep ++) {
  console.log(`Lifting weights repetition ${rep}`);
}
```

- for (1.변수 선언; 2.범위(조건식); 3.증감식)



#### 13.Looping Arrays, Breaking and Continuing

- **하드코딩의 뜻은 값을 고정시켜 놓는다는 것이고, 소프트코딩은 가변적인 값을 의미한다**

```js
const jonas = [
  'Jonas',
  'Schmedtmann',
  2037 - 1991,
  'teacher',
  ['Michael', 'Peter', 'Steven']
];

const types = [];
// console.log(jonas[0])
// console.log(jonas[1])
// console.log(jonas[2])
// ...
// console.log(jonas[4])
// jonas[5] does NOT exist


for (let i = 0; i < jonas.length ;i++) {
  // Reading from jonas array
  console.log(jonas[i], typeof jonas[i]);

  // Filling types array
  //['string', 'string', 'number', 'string', 'object']
  // types[i] = typeof jonas[i];
  types.push(jonas[i])
}

console.log(types);

const years = [1991, 2007, 1969, 2020];
const ages = [];

for (let i = 0; i < years.length; i++) {
  ages.push(2037 - years[i]);
}

console.log(ages)


// continue and break
console.log('--- ONLY STRINGS ---')
for (let i = 0; i < jonas.length; i++) {
  // continue will immediately exit the current iteration. 
  if(typeof jonas[i] !== 'string') continue;

  console.log(jonas[i], typeof jonas[i]);
}

// continue and break
console.log('--- break with number ---')
for (let i = 0; i < jonas.length; i++) {
  // 종료문 설정
  if(typeof jonas[i] === 'number') break;

  console.log(jonas[i], typeof jonas[i]);
}
```



#### 14.Looping Backwards and Loops in Loops

```js
const jonas = [
  'Jonas',
  'Schmedtmann',
  2037 - 1991,
  'teacher',
  ['Michael', 'Peter', 'Steven'],
  true
];


for (let i = jonas.length -1; i >= 0; i--) {
  console.log(jonas[i]);
}


for (let exercise = 1; exercise < 4; exercise++) {
  console.log(`-------- Starting exercise ${exercise}`);

  for (let rep = 1; rep < 6; rep++) {
    console.log(`Exercise ${exercise}: LIfting weight repetition ${rep}`)
  }
}
```

#### 15.The while Loop

- for 문은 구하고자 하는 값의 조건이 무엇인지 정확할 경우
- while문은 내가 구하고자 하는 값의 조건이 무엇인지 정확히 모를 경우, 유동적인 경우

```js
for (let rep = 1; rep <= 10; rep++) {
  console.log(`LIfting weight repetition ${rep}`)
}

let rep = 1;
while (rep <= 10) {
  console.log(`WHITE: LIfting weight repetition ${rep}`);
  rep ++;
}

let dice = Math.trunc(Math.random() * 6) + 1;
// console.log(dice);

//while loop does really not have to depend on any counter variable.
// whenever you do need a loop without a counter you can reach for the while loop

while (dice !== 6) {
  console.log(`You rolled a ${dice}`);
  dice = Math.trunc(Math.random() * 6) + 1;
  if (dice === 6) console.log('Loop is about to end...');
}
```



#### Coding Challenge #4

```js
bills = [22, 295, 176, 440, 37, 105, 10, 1100, 86, 52]

const tips = []
const totals = []



const calcTip = function(bill) {
  return bill >= 50 && bill <= 300 ? bill * 0.15 : bill * 0.2;
}

for (let i = 0; i < bills.length; i++) {
  const tip = calcTip(bills[i]);
  tips.push(tip);
  totals.push(tip + bills[i]);
}
console.log(bills, tips, totals);

const calcAverage = function(arr) {
  let sum = 0;
  for(let i = 0; i < arr.length; i++) {
      sum += arr[i];
  }
  return sum / arr.length;
}
console.log(calcAverage([2, 3, 7]));
console.log(calcAverage(totals));
console.log(calcAverage(tips));
```

