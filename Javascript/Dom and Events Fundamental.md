#### 1.What's the DOM and DOM manipulation

- 우리가 document.querySelector를 통해서('지정하고 싶은 css 클래스')를 통해서 원하는 html 요소를 찾을 수 있다
- Dom은 Document object model의 약자로 html 문서들의 구조적 표현으로써 자바스크립이 html의 요소나 스타일을 조작할 수 있게 접근할 수 있도록 허용해준다.
  - 여기서 조작이란 텍스트, html 속성, 그리고 심지어 CSS 스타일을 바꿀 수 있게 하는 것이다
  - **더 간단히 dom의 정의를 말하면 html문서들과 자바스크립트의 코드를 연결하는 지점이라고 생각하면 된다.**
- 트리 구조에서 각각의 html 요소들은 하나의 객체이다.
- 특별한 객체가 dom을 가르키는 항목이 된다. (Ex) document.querySelector()
- **Dom은 자바스크립트의 부분이 아니다**
- **Dom과 Dom methods들은 WEB APIs에 속한다.**
  - WEB APIs는 브라우저에서 실행하는 라이브러리와 같다. 우리의 자바스크립트 코드로부터 접근할 수 있게 한다. api는 자바스크립트로 쓰여진다. 그리고 자동적으로 우리가 그것을 이용할 수 있게 처리해준다.



#### 2.Selecting and Manipulating Elements

```js
console.log(document.querySelector('.message').textContent);
document.querySelector('.message').textContent = 'Correct Number';

document.querySelector('.number').textContent = 13;
document.querySelector('.score').textContent = 10;

document.querySelector('.guess').value = 23;
console.log(document.querySelector('.guess').value);
```





#### 3.Handling Click Events

```js
//function 부분은 바로 실행되지 않고 이벤트가 실행되고 나서 발생한다.
document.querySelector('.check').addEventListener('click', function () {
  const guess = Number(document.querySelector('.guess').value);
  console.log(guess, typeof guess);

  if (!guess) {
    document.querySelector('.message').textContent = 'No number!';
  }
});
```



#### 4.Implementing the Game Logic

```js
const secretNumber = Math.trunc(Math.random() * 20) + 1;
//this score is part of the so-called application state which is
//basically all the data that is relevant to the application
let score = 20;
document.querySelector('.number').textContent = secretNumber;

document.querySelector('.check').addEventListener('click', function () {
  const guess = Number(document.querySelector('.guess').value);
  console.log(guess, typeof guess);

 	if (!guess) {
    document.querySelector('.message').textContent = '⛔️No number!';

    // when player wins
  } else if (guess === secretNumber) {
    document.querySelector('.message').textContent = '🎉 Correct Number!';
    // when guess is too high
  } else if (guess > secretNumber) {
    if (score > 1) {
      document.querySelector('.message').textContent = 'Too high!';
      score--;
      document.querySelector('.score').textContent = score;
    } else {
      document.querySelector('.message').textContent = '💥 You lost the game!';
      document.querySelector('.score').textContent = 0;
    }
    // when guess is too low
  } else if (guess < secretNumber) {
    if (score > 1) {
      document.querySelector('.message').textContent = 'Too low!';
      score--;
      document.querySelector('.score').textContent = score;
    } else {
      document.querySelector('.message').textContent = '💥 You lost the game!';
      document.querySelector('.score').textContent = 0;
    }
  }
});

```





#### 5.Manipulating CSS styles

- css style을 dom을 활용해서 바꾸고 싶다면  `document.queryselctor('.바꾸고 싶은 class').style.바꾸고 싶은 css= '바꾸고 싶은 내용'` 이런 형식으로 사용해야 한다.

```js
const secretNumber = Math.trunc(Math.random() * 20) + 1;
//this score is part of the so-called application state which is
//basically all the data that is relevant to the application
let score = 20;
document.querySelector('.number').textContent = secretNumber;

document.querySelector('.check').addEventListener('click', function () {
  const guess = Number(document.querySelector('.guess').value);
  console.log(guess, typeof guess);

  if (!guess) {
    document.querySelector('.message').textContent = '⛔️No number!';

    // when player wins
  } else if (guess === secretNumber) {
    document.querySelector('.message').textContent = '🎉 Correct Number!';
    //change background color (inline style)
    document.querySelector('body').style.backgroundColor = '#60b347';
    // change width (inline style)
    document.querySelector('.number').style.width = '30rem';
    // when guess is too high
  } else if (guess > secretNumber) {
    if (score > 1) {
      document.querySelector('.message').textContent = 'Too high!';
      score--;
      document.querySelector('.score').textContent = score;
    } else {
      document.querySelector('.message').textContent = '💥 You lost the game!';
      document.querySelector('.score').textContent = 0;
    }
    // when guess is too low
  } else if (guess < secretNumber) {
    if (score > 1) {
      document.querySelector('.message').textContent = 'Too low!';
      score--;
      document.querySelector('.score').textContent = score;
    } else {
      document.querySelector('.message').textContent = '💥 You lost the game!';
      document.querySelector('.score').textContent = 0;
    }
  }
});
```





#### 6.Coding Chanllenge-the process of reset 

```js
document.querySelector('.again').addEventListener('click', function () {
  score = 20;
  //위에 const에 변수를 할당했는데 아래처럼 또 사용하고 싶으면 위에 변수를 const가 아닌 let을 써야한다. 
  secretNumber = Math.trunc(Math.random() * 20) + 1;

  document.querySelector('.message').textContent = 'Start guessing...';
  document.querySelector('.score').textContent = score;
  document.querySelector('.number').textContent = '?';
  //이 부분은 내가 실수한 부분 값을 empty로 하려면 value에 접근해야한다. 
  document.querySelector('.guess').value = '';
  document.querySelector('body').style.backgroundColor = '#222';
  document.querySelector('.number').style.width = '15rem';
});
```



#### 7.Implementing Highscore

```js
// highscore이라는 변수 설정
let highscore = 0;

if (score > highscore) {
  highscore = score;
  document.queryselector('.highScore').textContent = highScore;
}
```



#### 8.Refactoring Our Code: The DRY Principle

- 리팩토링은 코드를 재구조화하는 작업이다. 그러나 작동하는 것이 변하지 않고 재구조화하는 작업이다. 리팩토링을 통해서 코드를 더 좋게 만들고 중복코드를 제거한다.
- 리팩토링 순서
  - 첫 번째로는 중복코드들을 확인하거나 우리가 가지고 있는 코드들에서 거의 중복되는 것들을 찾는다.
  - 그리고 중복되는 메시지는 함수화처리를 통해서 간단하게 만든다.

- 최종 코드

```js
'use strict';

let secretNumber = Math.trunc(Math.random() * 20) + 1;
//this score is part of the so-called application state which is
//basically all the data that is relevant to the application
let score = 20;
let highScore = 0;

//display message
const displayMessage = function (message) {
  document.querySelector('.message').textContent = message;
};

//display number
const displayNumber = function (number) {
  document.querySelector('.number').textContent = number;
};

//display score
const displayScore = function (score) {
  document.querySelector('.score').textContent = score;
};

//change css style by Dom
const changeBackground = function (color) {
  document.querySelector('body').style.backgroundColor = color;
};

//change css style by Dom
const changeWidth = function (width) {
  document.querySelector('.number').style.width = width;
};

document.querySelector('.check').addEventListener('click', function () {
  const guess = Number(document.querySelector('.guess').value);

  if (!guess) {
    displayMessage('⛔️No number!');

    // when player wins
  } else if (guess === secretNumber) {
    displayMessage('🎉 Correct Number!');
    displayNumber(secretNumber);
    //change background color (inline style)
    changeBackground('#60b347');
    // change width (inline style)
    changeWidth('30rem');

    if (score > highScore) {
      highScore = score;
      document.querySelector('.highscore').textContent = highScore;
    }
    // when guess is wrong.
  } else if (guess !== secretNumber) {
    if (score > 1) {
      displayMessage(guess > secretNumber ? 'Too high!' : 'Too low!');
      score--;
      displayScore(score);
    } else {
      displayMessage('💥 You lost the game!');
      displayScore(0);
    }
  }
});

document.querySelector('.again').addEventListener('click', function () {
  score = 20;
  secretNumber = Math.trunc(Math.random() * 20) + 1;
  displayMessage('Start guessing...');
  displayScore(score);
  displayNumber('?');
  document.querySelector('.guess').value = '';
  changeBackground('#222');
  changeWidth('15rem');
});

```



#### 9.Working with Classes

```js
'use strict';

const modal = document.querySelector('.modal');
const overlay = document.querySelector('.overlay');
const btnCloseModal = document.querySelector('.close-modal');
const btnsOpenModal = document.querySelectorAll('.show-modal');

const openModal = function () {
  console.log('Button clicked');
  modal.classList.remove('hidden');
  overlay.classList.remove('hidden');
};

const closeModal = function () {
  modal.classList.add('hidden');
  overlay.classList.add('hidden');
};

for (let i = 0; i < btnsOpenModal.length; i++)
  btnsOpenModal[i].addEventListener('click', openModal);

btnCloseModal.addEventListener('click', closeModal);
overlay.addEventListener('click', closeModal);

```

- classList
  - element의 class 목록에 하나 이상의 css class를 추가하려면 classList의 add() 또는 삭제하려면 remove() 메소드를 사용해야 한다. 
  - css file에 이미 정의되어 있는 css class가 있어야 한다.



#### 10.Handling an "ESC" Keypress Event

```js
'use strict';

const modal = document.querySelector('.modal');
const overlay = document.querySelector('.overlay');
const btnCloseModal = document.querySelector('.close-modal');
const btnsOpenModal = document.querySelectorAll('.show-modal');

const openModal = function () {
  modal.classList.remove('hidden');
  overlay.classList.remove('hidden');
};

const closeModal = function () {
  modal.classList.add('hidden');
  overlay.classList.add('hidden');
};

for (let i = 0; i < btnsOpenModal.length; i++)
  btnsOpenModal[i].addEventListener('click', openModal);

btnCloseModal.addEventListener('click', closeModal);
overlay.addEventListener('click', closeModal);

document.addEventListener('keydown', function (e) {
  //model does not contain the hidden class.
  if (e.key === 'Escape' && !modal.classList.contains('hidden')) {
    {
      closeModal();
    }
  }
});
```

