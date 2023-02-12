버셀 배포 도전



#### 콜백함수

```js
//기존 함수
function findUser(id) {
  const user = {
    id: id,
    name: "User" + id,
    email: id + '@test.com',
  };
  return user;
}

const user = findUser(1);
// user:{id:1, name="User1", email:"1@test.com"}
console.log("user": user)

//콜백 함수
function findUserAndCallBack(id, cd) {
  const user = {
    id: id,
    name: "User"+ id,
    email: id + "@test.com",
  };
  cd(user);
}

//두 번째 인자로 콜백 함수를 선언하여 넘겼다.
// 7번째 줄 findUserAndCallBack() 함수가 실행될 떄 cb 매개변수는 콜백 함수는 할당 받으며, 
// cb(user);가 실행될 때, 이 콜백 함수가 실행된다. 
// return이 필요없다.
findUserAndCallBack(1, function(user) {
  console.log("user", user);
});
//결과
user: {id: 1, name: "User1", email: "1@test.com"}
```

- 두 개의 차이는 기존 함수에서는 `findUser()` 함수는 결과값을 리턴하고 함수 외부에서 결과값을 이용하여 작업을 수행하는 반면에, `findUserAndCallBack()` 함수는 결과값을 이용해 해야할 작업까지 함수 내부에서 수행해주기 떄문에 결과값을 굳이 리턴할 필요가 없다.

- 콜백함수는 함수에 파라미터로 들어가는 함수.

  ```js
  function checkMood(mood, goodCallback, badCallback) {
    if (mood == "good") {
      goodCallback();
    } else {
       badCallback();
    }
  }
  
  function cry() {
    console.log(sad);
  }
  
  function happy() {
    console.log(smile);
  }
  
  checkMood("mood", happy, cry)
  ```

  

- 순차적으로 실행하고 싶을 때 사용한다.

```js
function first(파라미터) {
  console.log(1)
  second() == 파라미터
}

function second() {
  console.log(2)
}
// 1출력하고 2도 출력해주세요
first(second)
```

- 비동기 함수란 호출부에서 실행결과를 기다리지 않아도 된다.

- 비동기 함수를 사용하면 로직을 순차적으로 처리할 필요가 없기 때문에 동시 처리에서도 동기 함수대비 유리하다

- 자바스크립트에는 `setTimeout()`이라는 대표적인 내장 비동기 함수가 있다.

  - 두 개의 매개변수를 받는데, 첫번째는 실행할 작업 내용을 담은 콜백 함수이고, 두 번째는 이 콜백 함수를 실행하기 전에 기다리는 밀리초 시간입니다. 즉 `setTimeout`함수는 두 번째 인자로 들어온 시간 만큼 기다린 후에 첫 번째 인자로 들어온 콜백 함수를 실행한다.

  ```js
  function findUser(id) {
    let user;
    setTimeout(function() {
      console.log("waited 0.1sec");
    	user = {
        id: id,
      	name: "User" + id,
      	email: id + '@test.com',
      };
    }, 100);
    return user;
  }
  
  const user = findUser(1);
  console.log("user:", user);
  
  // 출력 순서
  // user: undefined
  // waited: 0.1sec
  // setTimeout은 비동기 함수니까 바로 const user로 넘어가게 된다
  // 그러면서 user 변수에는 undefined이 담겨져서 출력된다. 
  ```

  - 콜백 함수를 사용해서 이전 문제 해결

  ```js
  function findUserAndCallBack (id, cb) {
    setTimeout(function() {
      console.log("waited 0.1sec");
    	user = {
        id: id,
      	name: "User" + id,
      	email: id + '@test.com',
      };
      cb(user);
    }, 100);
  }
  
  findUserAndCallBack (id, function(user)) {
  	console.log("user:", user);                     
  }
  
  //출력
  //waited 0.1 sec.
  //user: {id: 1, name: "User1", email: "1@test.com"}
  ```

  - 결과값을 통해 처리할 로직을 콜백 함수로 넘기는 스타일로 코딩을 해줘야 예상된 결과를 얻을 수 있습니다.
  - 콜백 함수를 중첩해서 연쇄적으로 호출해야하는 복잡한 코드의 경우, 계속되는 들여쓰기 때문에 코드 가독성이 현저하게 떨어지게 된다. **콜백지옥**이라고 불리는 문제를 해결하기 위해 promise 방법이 등장했다.

  #### Promise

  - 현재에는 당장 얻을 수 없지만 가까운 미래에는 얻을 수 있는 어떤 데이터에 접근하기 위한 방법을 제공한다.
  - 당장 원하는 데이터를 얻을 수 없다는 것은 데이터를 얻는데까지 지연시간(delay, latency)이 발생하는 경우를 말합니다.
  - I/O나 Network를 통해서 데이터를 얻는 경우가 대표적이다
  - CPU에 의해서 실행되는 코드 입장에서는 엄청나게 긴 지연시간으로 여겨지기 때문에 Non-blocking 코드를 지향하는 자바스크립트에서는 비동기 처리가 필수적이다.
  - 위의 코드 재작성

  ```js
  findUser(1).then(function(user) {
  	console.log("user:", user);                     
  });
  
  function findUser(id) {
    return new Promise(function (resolve) {
      setTimeout(function() {
        console.log("waited 0.1sec");
    		const user = {
        id: id,
      	name: "User" + id,
      	email: id + '@test.com',
      };
      resolve(user);
    }, 100);
      });
  }
  
  // 결과
  //waited 0.1 sec.
  //user: {id: 1, name: "User1", email: "1@test.com"}
  ```

  - **콜백 함수를 통해 비동기 처리를 하던 기존 코드와 가장 큰 차이점은 함수를 호출하면 Promise 타입의 결과값이 리턴되고, 이 결과값을 가지고 다음에 수행할 작업을 진행한다는 것입니다.**

  - `const promise = new Promise(function(resolve, reject) { ... });`
  - 실제로는 변수에 할당하기 보다는 어떤 함수의 리턴값으로 바로 사용된다.

  ```js
  function returnPromise() {
    return new Promise((resolve, reject) => { ... } );
  }
  ```

  - `resolve()` 함수의 인자로는 미래 시점에 얻게될 결과를 넘겨주고, `reject()`함수의 인자로는 미래 시점에 발생할 예외를 넘겨준다.

  - 예시

    ```js
    function devide(numA, numB) {
      return new Promise((resolve, reject) => {
        if (numB === 0) reject(new Error("Unable to devide by 0."));
        else resolve(numA / numB);
      });
    }
    
    // 결과 성공: 4
    devide(8, 2)
    	.then((result) => console.log('성공', result))
    	.catch((error) => console.log("실패", error));
    
    //실패 후에 catch()메서드가 실행된다.
    devide(8, 0)
    	.then((result) => console.log('성공', result))
    	.catch((error) => console.log("실패", error));
    ```

  - `fetch()`함수는 **API의 URL을 인자로 받고**, 미래 시점에 얻게될 **API 호출 결과를 Promise 객체**로 리턴한다.

    ```js
    fetch("https://jsonplaceholder.typicode.com/posts/1")
    	.then((response) => console.log("response", response))
    	.catch((error) => console.log("error", error));
    
    // 결과
    // response: Response {type: "cors", url: "https://jsonplaceholder.typicode.com/posts/1", redirected: false, status: 200, ok: true, …}
    ```

    - 인터넷 상에서 유효한 URL을 넘기면 예외가 발생하지 않고 상태 코드 200의 응답이 출력됐다.

    - 에러 발생(url을 입력하지 않을 시에)

    ```js
    fetch()
      .then((response) => console.log("response:", response))
      .catch((error) => console.log("error:", error));
    ```

    > ```text
    > error: TypeError: Failed to execute 'fetch' on 'Window': 1 argument required, but only 0 present.
    >     at main-sha512-G7qgGx8Wefk5JskAfRw2DfBPNPQTxDC23DcZ+KQTmNoSr2S6pZ3IJgYs1ThvLvvH7uI_KhycDx_FIDNlu5KhOw==.bundle.js:9070
    >     at <anonymous>:1:
    > ```

    -  Promise는 `then()`과 `catch()` 메서드를 통해서 동기 처리 코드에서 사용하던 `try-catch` 블록과 유사한 방법으로 비동기 처리 코드를 작성할 수 있도록 해줍니다.

    - Promise의 메서드 체이닝

      ```js 
      fetch("https://jsonplaceholder.typicode.com/posts/1")
      	.then((response) => response.json())
      	.then((post) => console.log("post:", post))
      	.catch((error) => console.log("error", error)),
        
      // 결과
      //post: {userId: 1, id: 1, title: "sunt aut facere repellat provident occaecati //excepturi optio reprehenderit", body: "quia et suscipit↵suscipit recusandae //consequuntur …strum rerum est autem sunt rem eveniet architecto"}  
      ```

      - 단순히 응답 결과가 아닌 응답 전문을 json형태로 출력하고 싶은 경우에는 `then()` 메서드를 추가로 연결해준다

      - `then()`과 `catch()` 메서드는 또 다른 Promise 객체를 리턴한다. 그리고 이 Promise 객체는 인자로 넘긴 콜백 함수의 리턴값을 다시 `then()` 과 `catch() 메서드를 통해 접근할 수 있도록 해준다.

      - `then()`과 `catch()`메서드는 마치 사슬처럼 계속 연결하여 연쇄적으로 호출 할 수 있다.

      - `userId`1이 필요한 경우

        ```js
        fetch("https://jsonplaceholder.typicode.com/posts/1")
          .then((response) => response.json())
          .then((post) => post.userId)
          .then((userId) => "https://jsonplaceholder.typicode.com/users/" + userId)
          .then((url) => fetch(url))
          .then((response) => response.json())
          .then((user) => console.log("user:", user))
          .catch((error) => console.log("error:", error));
        
        // user: {id: 1, name: "Leanne Graham", username: "Bret", email: "Sincere@april.biz", address: {…}, …}
        ```

      - 그러나 `then()` 을 연쇄적으로 호출하면 화살표 함수로 한 줄짜리 콜백 함수를 넘긴 경우에는 코드 실행이 break point에서 멈추지 않기 떄문에 디버깅이 상당히 불편하다 그래서 `catch()` 메서드를 사용하여 예외 처리를 해야한다.

      - 다단계 들여쓰기는 코드의 가독성을 떨어지게 만든다. 따라서 다음과  같이 Async/await 대안이 있다.

        

        

#### Async/await

```js
async function fetchAuthorName(postId) {
  const postResponse = await fetch(
  	`https://jsonplaceholder.typicode.com/posts.${postId}`
  );
  const post = await postResponse.json();
  const userId = post.userId;
  const userResponse = await fetch(
  	`https://jsonplaceholder.typicode.com/users/${userId}`
  );
  const user = await userResponse.json();
  return user.name;
}

fetchAuthorName(1).then((name) => console.log("name:", name));
```

- `async`키워드가 붙어있는 함수 내부에서만 사용할 수 있으며 비동기 함수가 리턴하는 Promise로 부터 결과값을 추출해준다.  **`await` 키워드를 사용하면 일반 비동기처럼 바로 실행이 다음 라인으로 넘어가는게 아니라 결과값을 얻을 수 있을 때까지 기다려 준다**. 따라서 일반적인 동기 코드 처리와 동일한 흐름으로 코드를 작성할 수 있으며, 따라서 코드를 읽기도 한결 수월해진다.
- `async` 키워드가 붙어있는 함수를 호출하면 명시적으로 Promise 객체를 생성하여 리턴하지 않아도 Promise 객체가 리턴된다. 따라서 Promise 객체를 사용했던 것 동일한 방식으로 `then()` 메서드를 통해서 결과값을 출력하고 있다.



```js
  methods: {
    async getUser() {
      const res = await fetch('https://randomuser.me/api')
      const { results } = await res.json()

      console.log(results);


      this.firstName = results[0].name.first
      this.lastName = results[0].name.last
      this.email = results[0].email
      this.gender = results[0].gender
      this.pitcure = results[0].pitcure.large
    }
  }
})
```



- 만약 호출부가 또 다른 `async`키워드가 붙어있는 함수의 내부에 있다면 동일한 방식으로 `await`키워드를 사용하여 Promise가 제공할 값에 바로 접근할 수 있다.

  ```js
  async funciton printAuthorName(PostId) {
    const name = await fetchAuthorName(postId);
    console.log("name:", name);
  }
  
  printAuthorName(1);
  ```

  

- 예외처리

  ```javascript
  async function fetchAuthorName(postId) {
    const postResponse = await fetch(`https://jsonplaceholder.typicode.com/posts/${postId}`)
  };
  const post = await postResponse.json();
  const userId = post.userId;
  
  try {
    const userResponse = await fetch (
    	`https://jsonplaceholder.typicode.com/users/${userId}`
    );
    const user = await userResponse.json();
    return user.name;
  }	catch(err) {
    console.log("Faile to fatch user:", err);
    return "Unknown";
  }
  
  fetchAuthorName(1).then((name) => console.log("name:", name));
  ```

  