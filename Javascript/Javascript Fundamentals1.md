### 자바스크립트의 역사

- 1995년 당시 약 90% 시장 점유율로 웹 브라우저 시장을 지배하고 있던 넷스케이프 커뮤니케이션즈는 정적인 HTML을 동적으로 표현하기 위해 경량의  프로그래밍 언어를 도입하기로 결정했다. 그래서 탄생한 것이 브랜던 아이크(파이어폭스 만듬)가 개발한 자바스크립트이다. 
- 자바스크립트는 1996년 넷스케이프 커뮤니티에 탑재되었고 Mocha로 명명되었고 그해 9월에 Livescript라는 이름이 변경되고 12월 최종적으로 Javascript로 최종 명명되었다.
- 1996년 마이크로소프트는 자바스크립트의 파생 버전인 Jscript를 Explorer 3.0에 탑재했다. 그런데 문제는 Jsciprt와 자바스크립트가 표준화되지 못하고 적당히 호환되었다는 것이다. 즉, 자사 브라우저의 시장 점유율을 높이기 위해 자사 브라우저에서만 동작하는 기능을 경쟁적으로 추가하기 시작했다. 웹 페이지가 정상 작동하지 않은 **크로스 브라우징 이슈**가 발생하기 시작했고 모든 브라우저에서 동장하는 웹 페이지를 개발하는 것은 무척 어려워졌다. 
- 그래서 표준화된 자바스크립트의 필요성이 제기되었다. 이를 위해서 1996년 11월에 넷스케이프는 컴퓨터 시스템의 표준을 관리하는 비영리 표준화 기구인 ECMA 인터네셔널에 자바스크립의 표준화를 요청하였다. 
- 1997년 7월 ECMAScript가 탄생되었다. 
- 초창기 자바스크립트는 웹 페이지의 보조적인 기능을 수행하기 위해 한정적인 용도로 사용되었다. 이 시기에 대부분의 로직은 주로 웹 서버에서 실행되었고 브라우저는 서버로부터 전달받은 HTML과 CSS를 단순히 렌더링하는 수준이었다. 
- 1999년 비동기적(Asynchronous-동시에 발생하지 않는)으로 서버와 브라우저가 데이터를 교환할 수 있는 통신 기능인 Ajax(Asnchronous Javascript and XML-인터넷에 연결된 시스템끼리 데이터를 쉽게 주고 받을 수 있게 하는것이다.)
  - **이전의 웹페이지는 완전한 HTML을 전송 받아 웹 페이지 전체를 렌더링하는 방식으로 동작했다**. 따라서 화면이 전환되면 서버로부터 새로운 HTML을 전송 받아 웹 페이지 전체를 처음부터 다시 렌더링했다. **변경이 없는 부분까지 포함된 HTML을 서버로부터 받기 때문에 불필요한 데이터 통신이 발생하고, 변경이 없는 부분까지 처음부터 다시 렌더링해야 하기 때문에 퍼포먼스 측면에서도 불리한 방식**, **화면 전환이 되면 순간적으로 깜빡이는 현상이 발생** 
  -  **즉 Ajax의 등장은 필요없는 부분을 렌더링하지 않고 서버에서 필요한 부분의 데이터를 전송 받아 변경이 필요한 부분만을 한정적으로 렌더링하는 방식이 가능해졌다.** 이로 인해서 웹 브라우저에서도 데스크탑 애플리케이션과 유사한 빠른 퍼포먼스와 부드러운 화면전환이 가능케 됐다.
- 2006년에 Jquery의 등장으로 번거롭고 논란이 있던 DOM을 보다 쉽게 제어할 수 있게 되었고 크로스 브라우징 이슈도 어느정도 해결되었다.
- V8 자바스크립트 엔진이 등장하면서 자바스크립트는 데스크톱 애플리케이션과 유사한 사용자 경험을 제공할 수 있는 웹 애플리케이션 개발 프로그래밍 언어로 정착하게 되었다. 이로써 웹애플리케이션에서 프론트엔드 영역이 주목받는 계기가 되었다. 
- DOM(Document Object Model)은 웹 페이지에 대한 인터페이스이다. 기본적으로 여러 프로그램들이 페이지의 콘텐츠 및 구조, 그리고 스타일을 읽고 조작할 수 있도록 API를 제공한다. HTML 요소들의 구조화된 표현 HTML 문서의 객체 기반 표현 방식이다. 단순 텍스트로 구성된 HTML 문서의 내용의 구조가 객체 모델로 변환되어 다양한 프로그램에서 사용될 수 있다는 점이다.  
- 2009년 ES5 2015에 ES6/ES2015
- ECMAScript는 매년 주기적으로 버전을 발표하고 있다.
- 과거에 쓰던 코드들이 지금도 호환이 가능하다(25년전에 쓰여졌던 코드도 이해할 수 있다)- 버전에 상관 없다.
- 이전 특징들은 하나도 안 없어지고 새로운 것들만 업데이트 되고 있다. 
- 자바스크립트는 절대로 앞으로 호환되지 않는다. 미래에서 온 코드를 이해할 수 없다.
- 트랜스파일은 한언어로 작성된 소스 코드를 비슷한 수준의 추상화를 가진 다른 언어로 변환하는 것을 말한다. 
- ES5
  - fully supported in all browsers
  - ready to be used today

- ES6/ES2015
  - ES6+: Well supported in all modern browsers;
  - No support in older browsers;
  - Can use most features in production with transpiling and polyfilling. 

- polyfile은 기본적으로 지원하지 않는 이전 브라우저에서 최신 기능을 제공하는 데 필요한 코드
- ES2021-now:
  - ESNext: Future versions of the language (new feature proposals that reach Stage 4)
  - Can already use some features in production with transpiling and polyfilling.




### Javascript 특징

- 자바스크립트는 HTML, CSS와 함께 웹을 구성하는 요소 중 하나로 웹 브라우저에서 동작하는 유일한 프로그래밍 언어이다. 
- 개발자가 별도의 컴파일 작업을 수행하지 않은 인터프리터 언어이다. 인터프리터는 소스코드를 즉시 실행하고 컴파일러는 빠르게 동작하는 머신 코드를 생성하고 최적화한다. 
- 자바스크립트는 명령형, 함수형, 프로토타입 기반 객체지향 프로그래밍을 지원하는 멀티 패러다임 프로그래밍 언어다. 
- 자바스크립트는 클래스 기반 객체지향 언어보다 효율적이면서 **강력한 프로토타입(제품의 초기 모델) 기반의 객체지향 언어**이다. 







### 자바스크립트 강의 

- `alert("Hello World")`- 출력 구문
- `let js = 'amazing'`에서 let은 변수를 담을 때 사용
- `if (js === 'amazing') alert('JavaScript is FUN!')`
  - 만약 변수가 일치하면 alert안에 문자열이 출력된다.

```js
let js = "amazing";
      if (js === 'amazing') alert('JavaScript is FUN!');

      console.log(40 + 8 + 23 - 10);
```

- HTML은 Nouns CSS는 Adjectives 그리고 JS는 verbs 
- 고수준 객체지향
- 멀티패러다임 프로그래밍언어
  - 함수형, 명령형, 프로토타입 기반의 객체 지향형이다.

- 고수준 언어
  - 우리는 복잡한 부분에 대해서 생각할 필요가 없다. 예를 들어 프로그램이 실행될 때 컴퓨터의 메모리를 관리하는 부분들
  - 자바스크립트는 추상화라고 불리는 것들이 많이 존재한다.
  - 대부분의 데이터 저장을 위해 객체의 개념의 바탕으로 쓰인다.



### Values and Variables

- `let`을 이용해서 변수를 저장한다. 변수 이름을 우리는 이용한다.
- 변수 컨벤션
  - camel_case 
    - 변수의 첫 글자는 소문자 그리고 그리고 그 다음 단어는 대문자로 사용한다!
      - ex) firstName 
    - 주로 camel_case가 사용된다.
  - Underscore 사용
    - Ex) first_name
  - 맨 앞에 숫자가 오면 안 된다. 에러 발생 
  - 오로지 변수에는 숫자, 글자, underscore, dollar assign만 쓸 수 있다.
    - ex) Jonas&matilda = "Jm" => syntax error 발생
  - new도 변수이름으로 사용할 수 없다.  자바스크립트의 저장된 키워드이기 때문이다.
  - function도 사용할 수 없다!
    - 사용하고 싶으면 `_function` or `$function`만 사용 가능하다.
  - 절대 저장된 키워드 사용하지 말기!!
  - 변수 이름 앞 글자가 대문자이어도 문제는 되지 않지만 소문자로 쓰는게 규칙이니 지키자!
  - 아니면 글자를 다 대문자로 써라
    - Ex) PI = 3.14145;
  - 반드시 변수 이름 지을때는 이해하기 쉽게 지어야한다.





### Data Types

1. Number: Floating point numbers => Used for decimals `let age = 23;`

2. String: Sequence of characters => Used for text `let firstName = "Jonas"`
3. Boolean: Logical type that can only be true or false => used for taking decisions `let fullAge = true`

4. Undefined: Value taken by a variable: it means it's empty value

   Ex)`let year`

5. Null: Also means 'empty value'

6. Symbol(ES2015): Value that is unique and cannot be changed [Not useful for now]

- Javascript has dynamic typing: We do not have to manually define the data type of the value stored in a variable. Instead data types are determined automatically.

  - it's the value that has a type, not the variable.

- comments는 두가지 방법이 있다 `//` 와 `/**/` 

- 코드는 위아래 순서로 읽는다

- Type 출력하는 법

  `console.log(typeof true);`

- 선언하지 않은 부분을 쓰거나  ``안녕하세요""` 이런식으로 쓰면 에러난다. 따옴표 중요하다 

- 변수값을 새로 선언하게 되면 이전에 let을 써서 변수명을 지어줬다면 다시 쓸 필요가 없다.

  ```js
  let year;
  
  year = 1991
  console.log(typeof year); 
  ```

- null은 자바스크립트에서 버그나 에러라고 여겨진다.



#### 13 lecture LET. CONST and VAR

- let은 값을 재할당 할 수 있는데 const는 값을 재할당 할 수 없다.
- let은 값을 초기에 지정하지 않아도 되는데 const는 지정해야한다.
- 기본적으로 const를 쓰는 것을 추천하며 let은 오직 미래에 값이 변할 거 같은 경우에만 사용한다. 변하지 않을 경우에는 const를 사용한다. 
-  var키워드는 완전히 쓰지 말아야한다. var는 구식화된 용어이다. 첫 눈에는  let처럼 작동한다. let처럼 변수 값의 변형이 가능하다.
- let, var, const를 쓰지 않아도 동작은 하지만 전역객체에서 변수들은 사용되기 때문에 항상 사용하자

```js
let age = 30;
age = 31;


const birthYear = 1991;
birthYear = 1990;
```





#### 14 Basic operators 

-  변수에 값을 할당하고 그것을 숫자 대신에 넣어도 연산이 가능하다

```js
//Math operator
const now = 2037;
const ageJonas = 2037 - 1991
const ageSarah = 2037 - 2018;
console.log(ageJonas, ageSarah);

const ages = now - 1991;
const agehobin = now - 1995;
console.log(ages, agehobin)

console.log(ages * 2, ages / 2, 2 ** 3)
// 2 ** 3 means 2 to the power of 3 = 2 * 2 * 2

//concatenate two strings//
const firstName = "Jonas";
const lastName = "Schmedtmann";
console.log(firstName + ' ' + lastName);

// plus operator has prioriy than eqaul operator
// Assignment operator
let x = 10 + 5; // 15
x += 10; // x = x + 10
x *= 4; // x = x * 4 = 100
x++; // x = x + 1
x--; // x = x - 1
x--;
console.log(x);


// Comparison operators
console.log(ageJonas > ageSarah) // >, <, >=, <=
console.log(ageSarah >= 18);

const isFullAge = ageSarah >= 18; //boolean

console.log(now - 1991 > now - 2018)
```



#### 15.Operator Precedence

```js
// Comparison operators
console.log(ageJonas > ageSarah) // >, <, >=, <=
console.log(ageSarah >= 18);

const isFullAge = ageSarah >= 18; //boolean

//According to operator precedence
// 1.math operation 2. comparison operator
console.log(now - 1991 > now - 2018);

let x, y;
x = y = 25 - 10 - 5; // x = y = 10, x = 10 assignment would be from left to right
console.log(x, y);

// grouping is executed first (parenthesis)

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_Precedence
```



#### 16.chanllenge #1

```js
const markMass = 78;
const markHeight = 1.69;
const johnMass = 92;
const johnHeight = 1.95;

const markBmi = markMass / markHeight ** 2;
const johnBmi = johnMass / johnHeight ** 2;

console.log(markBmi, johnBmi); // 78, 92

const markHigherBMI = markBmi > johnBmi;

console.log(markHigherBMI);
```







#### 17.Strings and Template Literals

-  I'm 을 사용하고 싶으면 밖에 "I'm"처럼 큰 따옴표로 처리한다.
- template literal을 사용할 때는 큰 따옴표나 작은 따옴표 대신해서 백틱을 사용한다. template literal은 파이썬의 문자열 포맷팅과 비슷하다.
- 백틱은 아무런 불규칙적인 문자열에도 사용할 수 있다. 모든 문자열에 백틱을 사용한다고 보면 된다.
- ESMi 이전에는 줄바꿈을 하려면 `\n\`을 사용해서 처리를 해줘야했는데 백틱을 사용하면 사용하지 않고 바로 사용이 가능하다

```js
const firstName = "Jonas";
const job = 'teacher';
const birthYear = 1991;
const year = 2037;


const jonas = "I'm " + firstName + ', a' + (year - birthYear) + ' years old ' + job + '!';

const jonasNew = `I'm ${firstName}, a ${year - birthYear} year old ${job}`;
console.log(jonasNew);


console.log('Just a regular string...')

// before ESXi
// console.log('String with \n\ 
// multiple \n\
// lines');


// now
console.log(`String
multiple
lines`);
```





#### 18.Taking Decisions: if/else Statements

- else구문 없어도 초기에는 작동했다
- if else문을 사용할 떄 항상 변수는 밖에서 사용한다.
- else구문은 옵션이다

```js
const age = 15;
const isOldEnough = age >= 18;


if (age >= 18) {
  console.log('Sarah can start driving license ');
} else {
  const yearsLeft = 18 - age;
  console.log(`Sarah is too young. Wait another ${yearsLeft} years :)`);
}

const birthYear = 1998;

let century;
if(birthYear <= 2000) {
  century = 20;
} else {
  century = 21;
}

console.log(century);
```



#### 19.Coding Challenge #2

```js
const markMass = 78;
const markHeight = 1.69;
const johnMass = 92;
const johnHeight = 1.95;

const markBmi = markMass / markHeight ** 2;
const johnBmi = johnMass / johnHeight ** 2;


//template literal // 
if (markBmi > johnBmi) {
  console.log(`Mark's BMI (${markBmi}) is higher than John's (${johnBmi})`)
} else {
  console.log(`john's BMI ${johnBmi} is higher than Mark's (${markBmi})`)
}

//string //

if (markBmi > johnBmi) {
  console.log("Mark's BMI is higher than John's")
} else {
  console.log("john's BMI is higher than Mark's")
}
```



#### 20.Type conversion and coercion

- 형변환은 자동으로 다른 타입으로 변경되는것인데 반면에 Type coercion은 자바스크립트가 자동적으로 미리 강제적으로 바꾼다. 
- 우리는 숫자, 문자, 불린형만 변환할 수 있다. 그러나 불린형은 변환할 수 없다. 불린형은 특별하게 행동하게 된다(truthy/falsy)
- 문자랑 숫자랑 더할때 자동으로 숫자를 문자열로 전환시킨다
- 문자열 + 숫자 = 문자열 + 문자열(숫자) , 문자열 - 숫자 = 숫자(문자열) - 숫자

```js
//type coercion 
// string to number manually
console.log('I am' + 23 + ' years old') 
// 23-13-3 = 10 minus triggers the opposite conversion
//string are converted to numbers 10
console.log('23' - '13' - 3);
//three strings are concatenated. 23103
console.log('23' + '10' + 3);
// 42
console.log('23' * '2');
// 11.5
console.log('23' / '2');

let n = '1' + 1;
n = n - 1;
// 10
console.log(n);

// 95
console.log(2 + 3 + 4  +'5');

// 15
console.log('10' - '4' - '3' -2 +'5')
```



#### 21.Truthy and Falsy Values

- If-else 구문에서 소괄호 안에 들어가는 것은 자바스크립트가 강제로 boolean형태로 바꾼다
- 5 falsy values: 0, '', undefined, null, NaN

```javascript
// 5 falsy values: 0, '', undefined, null, NaN
// falsy
console.log(Boolean(0));
// falsy
console.log(Boolean(undefined));
// truthy
console.log(Boolean("Jonas"));
// truthy
console.log(Boolean({}));

// falsy
console.log(Boolean(''));


const money = 0;
//javascript will try to it to a boolean.
if (money) {
  console.log("Don't spend it all ;)");
  //executed 
} else {
  console.log("You should get a job!");
}

// height === undefined 
let height; 
  if(height) {
    //executed
    console.log('YAY! height is defined');
  } else {
    console.log('Height is Undefined');
  }
```



#### 22.Equality Operators: == vs ===

- `===`  이것은 엄격한 동등연산자이다.(강제 형변환이 이루어지지 않는다. 오직 두개의 값들이 정확히 일치할때 True를 반환한다.)
  - 이것을 쓰는 것을 더 선호한다. 

- 반면에 `==`은 덜 엄격하다. (형변환이 이루어진다.)
  - `'18'` == 18 => true 문자열 18이 숫자형 18로 변한다. 

```js
const age = '18';
  //not executed
if(age === 18) console.log("You just became an adult:D (strict)");
  // esecuted
if(age == 18) console.log("You just became an adult:D (loose)");


const favorite = Number(prompt("What's your favorite number?"));
console.log(favorite);
console.log(typeof favorite);

if (favorite === 23) { // 23 === 23
  console.log("Cool! 23 is an amazing number!")
} else if(favorite === 7) {
  console.log('7 is also a cool number')
} else if (favorite === 9) {
  console.log('9 is also a cool number')
} else {
  console.log("Number is not 23 or 7")
}


if(favorite !== 23) console.log('Why not 23?');
```



#### 23.Boolean Logic 

- A And B(둘다 맞아야)
  - Sarah has a driver's license and good vision
- A or B (둘 중에 하나만 맞으면 돼 )
- NOT A, NOT B
  - inverts true/false value



#### 24.Logical Operators

```js
const hasDriveLicense = true; // A
const hasGoodVision = true; // B

// and operator
console.log(hasDriveLicense && hasGoodVision);
// or operator
console.log(hasDriveLicense || hasGoodVision);
// not operator
console.log(!hasDriveLicense);

const shouldDrive = hasDriveLicense && hasGoodVision;


if(shouldDrive) {
  //will be executed 
  console.log('Sarah is able to drive');
} else {
  console.log("Someone else should drive...");
}

const isTired = true; // C
//True
console.log(hasDriveLicense && hasGoodVision && isTired);


if(hasDriveLicense && hasGoodVision && !isTired) {
  console.log('Sarah is able to drive');
} else {
  // will be executed
  console.log("Someone else should drive...");
}
```





#### 25.Coding Challenge 

```js
// 두 팀의 평균 값들

const dolphins = (96 + 108 + 89) / 3;
const koalas = (88 + 91 + 110) / 3;

if (dolphins > koalas) {
  console.log("Dolphins win the throphy");
} else if (koalas > dolphins) {
  console.log("koalas win the throphy");
} else if (koalas === dolphins) {
  console.log("Both win the trophy");
}



//bonus 1 && bonus 2
const dolphins = (97 + 112 + 101) / 3;
const koalas = (109 + 95 + 123) / 3;

if (dolphins > koalas && dolphins >= 100) {
  console.log("Dolphins win the throphy");
} else if (koalas > dolphins && koalas >= 100) {
  console.log("The winner is koalas");
} else if (koalas === dolphins && dolphins >= 100 && koalas >= 100) {
  console.log("Both win the trophy");
} else {
  console.log('No one wins the tophy');
}

```

#### 26.The switch Statement

- switch문에서 break를 사용하지 않을 경우에 다음 케이스로 계속 이동한다.
- if문에 비하면 덜 쓰인다. if문의 대안으로 나온 것은 아니다.

```js
const day = 'friday'; 

switch(day) {
  case 'monday': // day === 'monday'
    console.log('Plan course structure');
    console.log('Go to coding meetup');
    break;
  case 'tuesday':
    console.log('Prepare theory videos');
    break;
  case 'wednesday':
  case 'thursday':
    console.log('Write code example');
  case 'friday':
    console.log('Record videos');
    break;
  case 'saturday':
  case 'sunday':
    console.log('Enjoy the weekend :D');
    break;
  default:
    console.log('Not a valid day!');  
}


if (day === "monday") {
  console.log('Plan course structure');
  console.log('Go to coding meetup');
} else if(day === 'tuesday') {
  console.log('Prepare theory videos');
} else if (day ===  'wednesday' || day === 'thursday')
{
  console.log('Write code example');
} else if (day === 'friday') {
  console.log('Record videos');
} else if (day === 'saturday' || day === 'sunday') {
  console.log('Enjoy the weekend :D');
} else {
  console.log('Not a valid day!');  
}

```

#### 27.Statements and Expressions

- 구문들은 값을 생성하는 것이 아니고 단순히 호출하는 것인데 표현들은 값을 생성한다. 
- 자바스크립트가 expressions을 기대했는데 statements를 쓴다면 unexpected token 에러 메시지가 뜬다.

```js
// if-else statement doesn't really produce a value just declares
(statement)
if (23 > 10) {
  const str = '23 is bigger'(expression);
}

//template literal 
// insert expressions, but not statements
//this is an expressions

const me = "Jonas";
console.log(`I'm ${2037 - 1991} years old. ${me}`);
```



#### 28.The conditional (Ternary) Operator

- 조건적인 연산자의 경우에는 조건에 따라서 정의된다. 

- expressions에서 하지 못한 template literal에서 조건적인 값들을 가질 수 있다

  - Expressions 뒤에는 statements가 올 수 없었다.

  - 그러나 conditional operator에서는 그게 가능하다

    ```js
    console.log(`l like to drink ${age >= 18 ? 'wine ': 'water'}`);
    ```

```js
const age = 23;
age >= 18 ? console.log('I like to drink wine') :
console.log('I like to drink water');


const drink = age >= 18 ? 'wine ': 'water';
console.log(drink);


let drink2;
if (age >= 18) {
  drink2 = 'wine';
} else {
  drink2 = 'water';
}

console.log(drink2)

console.log(`l like to drink ${age >= 18 ? 'wine ': 'water'}`);
```



#### 29.Coding Challenge #4

```js
const bill = 40; 
const tip = bill >= 50 && bill <= 300 ? bill*0.15 : bill*0.20;

console.log(`The bill was ${bill}, the tip was ${tip}, and the total value ${bill + tip}`);
```

