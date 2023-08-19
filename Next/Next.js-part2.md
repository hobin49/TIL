#### 새로운 프로젝트 생성 / MongoDB 셋팅

- 관계형 데이터베이스 
  - 데이터를 표로 저장함
  - PostgreSQL, MySQL
- 비관계형 데이터베이스
  - 저장방식 제각각
  - Mongo DB의 경우에는 JS object 자료형처럼 데이터 저장가
  - 초보자들한테 좋다.
  - 분산처리 잘해준다. 
    - db 입출력이 1초에 수십만건이다. 많은 데이터를 빠르게 입출력해야하면 비관계 방식이 좋다.
    - 대용량 트래픽 분산처리를 염두해 두고 디자인 
- 홈페이지에서 설치
  - 회원가입 후 
  - DataBase access
  - Network Access 
  - 위의 다 설정하면 끝



#### Next.js에서 MongoDB 사용하기

- DataBase는 그냥 하나의 프로젝트이다. 

- 하나의 database와 post라는 이름의 collection도 하나 만들어보자

- document는 하나의 프로젝트, collection은 폴더, document는 하나의 메모장 파일이다. 

- collection => document => 데이터 

- insert document 버튼을 누르면 document 하나 발행하고

- 내가 입력하고 싶은 key와 value를 입력한다. 

- 설치

  `npm install mongodb`

- page.js에

```react
import { MongoClient } from "mongodb"

export default function Home() {
  //추가할 코드
  const client = await MongoClient.connect('DB접속URL~~', { useNewUrlParser: true })
  // forum 데이터베이스 접속
  const db = client.db("forum")
  // 실행하면 mongodb 데이터 출력해줌
  db.collection("post").find() 
  
  return (
    <div>안녕</div>
  )
}
```



- 아래 코드의 문제점 이렇게 하면 여러번 실행되기 때문에 .connect()는 자주 실행하면 큰일남
  - 서버 띄울 때 1번만 실행하면 좋다. 

```react
import { MongoClient } from "mongodb"

export default async function Home() {
  const client = await MongoClient.connect('mongodb+srv://admin:qwer1234@cluster0.5bwcklp.mongodb.net/', { useNewUrlParser: true })
  const db = client.db("forum")
  db.collection()

  return (
    <div>안녕</div>
  )
}
```



- 해결방법

  - 아무데나 js 파일을 만들어서 
  - mongodb 만든 사람들이 next.js에서 이렇게 짜라고 한거임 

  ```react
  import { MongoClient } from 'mongodb'
  const url = 'DB접속URL~~'
  const options = { useNewUrlParser: true }
  let connectDB
  
  if (process.env.NODE_ENV === 'development') {
    if (!global._mongo) {
      global._mongo = new MongoClient(url, options).connect()
    }
    connectDB = global._mongo
  } else {
    // 변수해 저장해놓고 쓰면 매번 실행안되고 좋다. 
    connectDB = new MongoClient(url, options).connect()
  }
  export { connectDB }
  ```

  - 하지만 개발시 파일저장하면 모든 JS파일 코드 전부 다시 읽고 지나간다.
  - 위의 코드는 개발단계에서 글로변 변수 만들고 재사용해주세요라는 뜻임 

  ```react
  import { connectDB } from "@/util/database"
  
  export default async function Home() {
    const client = await connectDB;
    const db = client.db("forum")
    // 컬렉션의 모든 document 꺼내오려면
    let result = await db.collection("post").find().toArray()
    console.log(result);
    return (
      <div>안녕</div>
    )
  }
  ```

  - DB 입출력 코드는 server component 안에서만 쓰자.





#### 글목록 조회기능 만들기 (DB 데이터 출력)

- 첨보는 프로그램 만들기
  - 프로그램에 필요한 기능 전부 정리
  - 쉬운 기능부터 하나씩 개발
- 게시판에 필요한 기능
  - 글목록 조회기능
  - 상세페이지
  - 글발행기능
  - 수정삭제기능

- 첨보는 세부기능 만들기

  - 어떤 식으로 동작하는 상세하게 한글로 설명
  - 그거 코드로 번역

- 글목록페이지/기능

  - HTML 페이지 필요

    ```react
    export default async function List() {
      return (
        <div className="list-bg">
          <div className="list-item">
            <h4>글제목</h4>
            <p>1월 1일</p>
          </div>
          <div className="list-item">
            <h4>글제목</h4>
            <p>1월 1일</p>
          </div>
          <div className="list-item">
            <h4>글제목</h4>
            <p>1월 1일</p>
          </div>
        </div>
      )
    }
    ```

    

  - 그 페이지 방문하면 DB에서 글 꺼내온다

    ```react
    import { connectDB } from "@/util/database";
    
    export default async function List() {
    
      const db = (await connectDB).db("forum");
      // 컬렉션의 모든 document 꺼내오려면
      let result = await db.collection("post").find().toArray();
      console.log(result);
      return (
        <div className="list-bg">
          <div className="list-item">
            <h4>글제목</h4>
            <p>1월 1일</p>
          </div>
          <div className="list-item">
            <h4>글제목</h4>
            <p>1월 1일</p>
          </div>
          <div className="list-item">
            <h4>글제목</h4>
            <p>1월 1일</p>
          </div>
        </div>
      )
    }
    ```

    

  - 가져온 글들을 HTML에 꽂아넣기

    - 데이터형식
      - [{글내용1}, {글내용2}]

    ```react
    import { connectDB } from "@/util/database";
    
    
    export default async function List() {
    
      const db = (await connectDB).db("forum");
      // 컬렉션의 모든 document 꺼내오려면
      let result = await db.collection("post").find().toArray();
      console.log(result[0].title);
      // return () + 중괄호 동시에 생략 가능
      return (
        <div className="list-bg">
          { result.map((e, i) =>
            <div className="list-item">
              <h4>{result[i].title}</h4>
              <p>1월 1일</p>
              <h4>{result[i].content}</h4>
            </div>
          )}
        </div>
      )
    }
    ```

    

- await

  - 자바스크립트는 처리가 늦게되는 코드를 발견하면 제껴두고 다음줄 실행함
  - await 붙이면 잠깐 기다려준다.
  - Promise 뱉는 코드만 await 붙이기 가능





#### 상세페이지 만들기 1 (Dynamic route)

- 상세페이지

  - 1.글제목 누르면 상세페이지 이동
  - 2.상세페이지 방문시 DB에서 글 꺼내서 HTML에 보여주기
  - 상세페이지 URL
    - /detail/1 접속시 1번 글내용
    - /detail/2 접속시 2번 글내용 
  - 글이 1000개이면 어떻게 상세페이지를 다 만들지?
    - dynamic route 쓰면 비슷한 페이지 여러개 만들 필요 없다.
    - 구조 = detail => [어쩌구] => page.js

  ```react
  import { connectDB } from "@/util/database";
  import { ObjectId } from "mongodb";
  
  export default async function Detail() {
    const db = (await connectDB).db("forum");
    // 컬렉션의 하나의 document를 가져올 때 Id를 식별자로 해야 중복된 것을 가져오지 않는다. 
    // 근데 넘 하드코딩
    let result = await db.collection("post").findOne({ _id: new ObjectId("64b63c7ce455c5118de0fc75")});
    console.log(result);
    return (
      <div>
        <h4>상세페이지임</h4>
          <h4>{result.title}</h4>
          <p>{result.content}</p>
      </div>
    )
  }
  ```

  - 근데 위의 코드는 너무 하드코딩이니 유저가 URL에 입력한 값을 넣어준다. 
    - 이렇게 해서 props를 통해서 props.params.id로 값을 id로 넘겨준다.

  ```react
  import { connectDB } from "@/util/database";
  import { ObjectId } from "mongodb";
  
  export default async function Detail(props) {
    const db = (await connectDB).db("forum");
    // 컬렉션의 모든 document 꺼내오려면
    let result = await db.collection("post").findOne({ _id: new ObjectId(props.params.id)});
  
    return (
      <div>
        <h4>상세페이지임</h4>
        <h4>{result.title}</h4>
        <p>{result.content}</p>
      </div>
    )
  }
  ```

  - 근데 위에 코드도 문제가 있는게 유저가 게시물의 Id를 어떻게 입력해? 
  - Link태그를 활용

  ```react
  // 1. 글목록 보여줄 HTML 페이지 필요
  import { connectDB } from "@/util/database";
  import Link from "next/link"
  
  
  export default async function List() {
  
    const db = (await connectDB).db("forum");
    // 컬렉션의 모든 document 꺼내오려면
    let result = await db.collection("post").find().toArray();
    console.log(result[0]._id);
    // return () + 중괄호 동시에 생략 가능
    return (
      <div className="list-bg">
        { result.map((e, i) =>
          <div className="list-item">
            <Link href={`/detail/${result[i]._id.toString()}/`}>2</Link>
            <h4>{result[i].title}</h4>
            <p>1월 1일</p>
            <h4>{result[i].content}</h4>
          </div>
        )}
      </div>
    )
  }
  ```





#### 상세페이지 만들기 2(useRouter)

- 페이지 이동밥법 useRouter
  - 클라이언트 컴포넌트에서만 사용가능
  - `router.push("이동할 곳")`를 사용하면 이동 가능
    - 뒤로가기는 `router.back()`
    - 앞으로가기는 `router.forward()`
    - 바뀐내용만 새로고침 `router.refresh()`
      - 변동사항이 있는 일부분만 바꿔준다. soft refresh기능
  - server component에서 필요하다면?
    - client component에 작성한 것을 넣어주자.

```react
"use client"
import { useRouter } from "next/navigation"

export default function DetailLink() {
  let router = useRouter()
  return (
    <button onClick={() => { router.push("/")}}>버튼</button>
  )
}
```

- 핵심  prefetch

  - router.prefetch('/detail/dsds') 이렇게 하면 페이지를 미리 로드하기 때문에 빨리 방문할 수 있다.

  - Link 태그만 써도 prefetch기능이 이미 내장되어있음.

  - prefetch기능을 끄고 싶으면? 
    - prefetch = {false}를 입력하면 된다. 
    - 개발중일 prefetch 여부 확인불가

```react
export default async function List() {

  const db = (await connectDB).db("forum");
  // 컬렉션의 모든 document 꺼내오려면
  let result = await db.collection("post").find().toArray();
  return (
    <div className="list-bg">
      { result.map((e, i) =>
        <div className="list-item">
          <Link prefetch={false} href={`/detail/${result[i]._id}/`}>
            <h4>{result[i].title}</h4>
          </Link>
          <DetailLink />
            <p>1월 1일</p>
            <h4>{result[i].content}</h4>
        </div>
      )}
    </div>
  )
}
```

- 현재  URL 출력하고 싶으면?
  - usePathname()
- search parameter 출력하고 싶으면?
  - useSearchParams();
- 유저가  [dynamic route] 입력한 거 출력은
  - useParams();





#### 글 작성기능 만들기 1 (서버기능 개발은)

- 글작성기능 만들기
  - 1.글작성페이지 필요
  - 바로 DB에 저장하면 위험
    - 글 안적고 공백 보내거나 이상한 글 작성하면 안 되니깐
  - 2.버튼 누르면 서버에 글저장해달라고 부탁
    - 서버: 이거 해달라고 요청하면 진짜 해주는 프로그램
    - 서버개발자가 짜는 코드 
      - /url, method를 가지고 이런 요청하면 이런 코드 실행해주세요.
      - 데이터 받기(get), 데이터 등록(post), 데이터 수정시(put, patch), 데이터 삭제(delete) 
  - 3.서버는 부탁 받으면 검사해보고 DB에 저장
  - 글 작성 -> 서버에서 글 검사  -> DB에 저장 (3-tier-architecture)
  
  
  
- Next.js에서 서버기능 만드는 법
  
  - GET 요청 방식
  
    - Pages 폴더 => api 폴더 => test.js 파일 생성
      - 누가 api/test로 GET/POST/PUT/DELETE/PATCH 요청하면 파일안의 코드 실행해준다.
  
  
    ```react
    export default function handler(요청, 응답) {
      console.log(123)
    }
    ```
  
    - 실제로 주소창에 api/test하면 123이 터미널에 출력된다.
    - 근데 계속 저렇게 하면 무한대기 상태이니까 서버 요청을 받았으면 응답을 해줘야한다. 
  
  
  ```react
  // 요청: 요청과 관련된 정보
  // 응답: 응답 도와줌
  export default function handler(요청, 응답) {
    응답.status(200).json('처리완료함')
  }
  ```
  
  - status code
  
    - 서버기능 처리성공시엔 status(200)
  
    - 서버기능 처리실패시엔 status(500)
  
    - 서버기능 처리실패시 (유저잘못) status(400)
  
  - POST 요청 방식
  
    - write 폴더에 page.js 만들자.
    - 서버에 POST method 요청하려면 `<form>` 사용
  
    ```react
    export default function Write() {
      return (
        <div>
          <form action="/api/test" method="POST">
            <button type="submit">버튼</button>
          </form>
        </div>
      )
    }
    ```
  
    - 서버에 GET/POST 요청 오면 각각 다른 코드 실행하고 싶어요
  
      - if로 구분해서 쓰자
  
      ```react
      export default function handler(요청, 응답) {
        if (요청.method == 'GET'){
          응답.status(200).json({ name: '안녕' })
        }
        if (요청.method == 'POST'){
          응답.status(200).json({ name: '바보' })
        }
      }
      ```
  
      - 문제풀이
  
        - DB 글 모두 GET 요청하면 가져오기
  
        ```react
        import { connectDB } from "@/util/database"
        
        export default async function handler(요청, 응답){
          const db = (await connectDB).db("forum")
          let result = await db.collection('post').find().toArray()
          응답.status(200).json(result)
        }
        ```
  
        
  
        - 현재 시간, 날짜 post로 보내주기
  
      ```react
      import { connectDB } from "@/util/database";
      
      export default async function handler(요청, 응답) {
        const date = new Date();
        const today = `${date.getFullYear()}년${date.getMonth()}월${date.getDay()}일${date.getHours()}시${date.getMinutes()}분${date.getSeconds()}초`
        if (요청.method == 'GET'){
          응답.status(200).json(result)
        }
        if (요청.method == 'POST'){
          응답.status(200).json(today)
        }
      }
      ```
  
      - 글발행 기능
  
      ```react
      // write/page.js
      export default function Write() {
        return (
          <div>
            <form action="/api/test" method="POST">
              <input name="title"/>
              <button type="submit">버튼</button>
            </form>
          </div>
        )
      }
      
      // api/test.js
      import { connectDB } from "@/util/database";
      
      export default async function handler(요청, 응답) {
        if (요청.method == 'GET'){
          응답.status(200).json(result)
        }
        if (요청.method == 'POST'){
          // post할 때 요청.body하면 input 값 출력
          응답.status(200).json(요청.body)
        }
      }
      ```
  
      

#### 글 작성기능 만들기 2

- Post/new.js라는 폴더랑 파일을 생성

```react
export default function handler(){
  if (요청.method == 'POST') {
    console.log(요청.body)
  }
}
```



- post하고 그것을 MongoDB 데이터베이스에 넣기 

```react
//write/page.js
export default function Write() {
  return (
    <div className="p-20">
      <h4>글작성</h4>
      <form action="/api/post/new" method="POST">
        <input name="title" placeholder="글제목"/>
        <input name="content" placeholder="글내용"/>
        <button type="submit">버튼</button>
      </form>
    </div>
  )
}

// api/post/new.js
import { connectDB } from "@/util/database";

export default async function handler(요청, 응답){
  if (요청.method == 'POST') {
    const db = (await connectDB).db("forum");
    // db에 저장(컬렉션에 하나의 Document 생성)
    let result = await db.collection("post").insertOne(요청.body);
    return 응답.status(200).json("완료")
  }
}
```

- 응답과 동시에 페이지 이동시키려면?
  - redirect 사용

```react
import { connectDB } from "@/util/database";

export default async function handler(요청, 응답){
  if (요청.method == 'POST') {
    const db = (await connectDB).db("forum");
    // db에 저장(컬렉션에 하나의 Document 생성)
    let result = await db.collection("post").insertOne(요청.body);
    return 응답.status(200).redirect("/경로")
  }
}
```

- 만약 사용자가 input에 아무것도 입력 안하고 post하면? 

```react
import { connectDB } from "@/util/database";

export default async function handler(요청, 응답){
  if (요청.method == 'POST') {
    if (요청.body.title == "") {
      return 응답.status(500).json("너 제목 왜 안씀")
    } 
  }
}
```

- DB 에러 예외처리는?

```react
try {
   const db = (await connectDB).db("forum");
   let result = await db.collection("post").insertOne(요청.body);
   return 응답.status(200).redirect("/list")
} catch(error) {
   console.log(error);
}
```





#### 글 수정기능 만들기1

- 기능 정리
  - 글마다 수정버튼, 누르면 수정페이지 이동
    - 각각의 수정페이지가 존재해야
    - edit/첫글의_id
    - dynamic routes 적용
  - 수정페이지 만들기 (글 가져와서 채워놔야함)
  - 발행 누르면 DB에 있던 글 수정

- 글마다 수정버튼

```react
// 1. 글목록 보여줄 HTML 페이지 필요
export default async function List() {

  const db = (await connectDB).db("forum");
  let result = await db.collection("post").find().toArray();
  console.log(result[0]._id);
  return (
    <div className="list-bg">
      { result.map((e, i) =>
        <div className="list-item">
          <Link href={`/detail/${result[i]._id}/`}>
            <h4>{result[i].title}</h4>
          </Link>
          <Link href={`/edit/${result[i]._id}`}>✏️</Link>
            <p>1월 1일</p>
            <h4>{result[i].content}</h4>
        </div>
      )}
    </div>
  )
}
```

- 수정 페이지

```react
// edit/id/page.js
export default function Write() {
  return (
    <div className="p-20">
      <h4>글작성</h4>
      <form action="/api/post/new" method="POST">
        <input name="title" placeholder="글제목"/>
        <input name="content" placeholder="글내용"/>
        <button type="submit">버튼</button>
      </form>
    </div>
  )
}
```



- 글 가져오기

  - 클릭하면 거기에 해당 id를 props를 활용해서 가져온다. 

  ```react
  import { connectDB } from "@/util/database";
  import { ObjectId } from "mongodb";
  
  export default async function Edit(props) {
    const db = (await connectDB).db("forum");
    let result = await db.collection("post").findOne({ _id: new ObjectId(props.params.id)});
  
    return (
      <div className="p-20">
        <h4>수정페이지</h4>
        <form action="어쩌구" method="POST">
          <input name="title" value={result.title} />
          <input name="content" value={result.content}/>
          <button type="submit">전송</button>
        </form>
      </div>
    )
  }
  ```



- 버튼누르면  DB에 있던 글 수정

```react
import { connectDB } from "@/util/database";
import { ObjectId } from "mongodb";

export default async function Edit(props) {
  const db = (await connectDB).db("forum");
  let result = await db.collection("post").findOne({ _id: new ObjectId(props.params.id)});

  await db.collection("post").updateOne({_id: new ObjectId(props.params.id)}, 
    {$set : { title : "바보", content : "바보2" }}
  );

  return (
    <div className="p-20">
      <h4>수정페이지</h4>
      <form action="어쩌구" method="POST">
        <input name="title" value={result.title} />
        <input name="content" value={result.content}/>
        <button type="submit">전송</button>
      </form>
    </div>
  )
}
```

- 글 수정 api

```react
import { connectDB } from "@/util/database"
import { ObjectId } from "mongodb";

export default async function handler(요청, 응답) {
  if (요청.method == 'POST'){
    console.log(요청.body)
    let db = (await connectDB).db('forum')
    let result = await db.collection('post').updateOne({게시물정보}, { $set : {바꿀데이터}} );
    응답.redirect(302, '/list')
  }
}
```

- 서버에 없는 정보는

  - 유저에게 id를 보내라고 하거나
    - id를 보낼 때 objectID 형태라 toString()해서 문자열로 전달하는게 좋음 혹은 숫자형이나

  ```react
  import { connectDB } from "@/util/database";
  import { ObjectId } from "mongodb";
  
  export default async function Edit(props) {
    const db = (await connectDB).db("forum");
    let result = await db.collection("post").findOne({ _id: new ObjectId(props.params.id)});
    return (
      <div className="p-20">
        <h4>수정페이지</h4>
        <form action="/api/post/edit" method="POST">
          <input name="title" defaultValue={result.title} />
          <input name="content" defaultValue={result.content}/>
          <input style={{display : "none"}} name="_id" defaultValue={result._id.toString()}/>
          <button type="submit">전송</button>
        </form>
      </div>
    )
  }
  ```

  

  - 수정페이지 (updateOne)

  ```react
  import { connectDB } from "@/util/database"
  import { ObjectId } from "mongodb";
  
  export default async function handler(요청, 응답) {
    if (요청.method == 'POST'){
      // id까지 추가로 들어갔으니 제목과 내용만 넣어준다.
      let 바꿀거 = { title : 요청.body.title, content: 요청.body.content}
      let db = (await connectDB).db('forum')
      // id랑, 바꿀 부분 넣어서 update한다.
      let result = await db.collection('post').updateOne({_id : new ObjectId(요청.body._id)}, { $set : 바꿀거});
      console.log(result);
      // 응답 성공하면 list페이지로 이동한다. 
      응답.status(200).redirect("/list")
    }
  }
  ```

  - updateOne시 덮어쓰기 말고 증가처리도 가능하다. 
    - $set 자리에 $inc 자리를 넣는다.

  ```react
  import { connectDB } from "@/util/database"
  import { ObjectId } from "mongodb";
  
  export default async function handler(요청, 응답) {
    if (요청.method == 'POST'){
      let 바꿀거 = { title : 요청.body.title, content: 요청.body.content}
      let db = (await connectDB).db('forum')
      let result = await db.collection('post').updateOne({_id : new ObjectId(요청.body._id)}, { $inc : 1});
      console.log(result);
      응답.status(200).redirect("/list")
    }
  }
  ```

  



#### 삭제기능 만들기 1(AJAX)

- client component는 검색 노출에 이점이 없기 때문에 큰페이지들은 서버컴포넌트로 냅두는게 낫다.
- JS 기능 넣을 부분만 클라이언트 컴포넌트 
- client 컴포넌트에서 DB 데이터를 가져오려면 useEffect는 사용 불가능 유저 브라우저로 전달되기 때문이다.
  - 그래서 서버에 부탁해서 DB게시물 가져온다. 
  - 근데 그러면 비동기적으로 받아오기 때문에 검색 노출이 어렵다.. 
    - HTML을 렌더링 되고나서 useEffect가 실행되기 때문이다. 
    - 구글 엔진 봇들이 페이지 방문시에 텅 빈 HTML 먼저 보이기 때문에 수집하지 않고 실망하고 돌아간다.

- 가장 좋은 방법은 서버 컴포넌트에서 가져온 DB 게시물을 클라이언트에 props를 통해서 데이터를 보내준다. 

```react
// 서버 컴포넌트
export default async function List() {

  const db = (await connectDB).db("forum");
  // 컬렉션의 모든 document 꺼내오려면
  let result = await db.collection("post").find().toArray();
  console.log(result[0]._id);
  // return () + 중괄호 동시에 생략 가능
  return (
    <div className="list-bg">
      <ListItem result = {result}/>
    </div>
  )
}
```

```react
// 클라이언트 컴포넌트
export default function ListItem({result}) {

  return (
    <div>
       {result.map((e, i) =>
        <div className="list-item">
          <Link href={`/detail/${result[i]._id}/`}>
            <h4>{result[i].title}</h4>
          </Link>
          <Link href={`/edit/${result[i]._id}`}>✏️</Link>
            <span>🗑️</span>
            <p>1월 1일</p>
            <h4>{result[i].content}</h4>
        </div>
      )}
    </div>
  )
}
```



- 삭제기능 

  - 버튼 누르면 서버로 삭제요청
  - 서버는 요청받으면 DB에서 삭제
  - Ajax 사용해서 서버로 요청
    - 장점
      - `<form>` 요청시 항상 새로고침이 되는데 (next.js에선 간혹 아닐 수도)
      - Ajax는 새로고침이 되지 않는다. 

  ```react
  <span onClick={() => {
       fetch('/api/test', {
            method : "POST",
            body : JSON.stringify([1, 2, 3])
       })
       .then(() => {
           console.log(123)
           })
       }}>🗑️</span>
  ```

  - 주의할 점
    - array, object 자료형은 항상 JSON.stringfy() 사용해서 데이터를 전송해야한다. 
    - 왜냐하면 서버와 데이터를 주고받을 땐 원래 문자나 숫자밖에 주고받을 수 없다.
    - 그래서 stringfy 메서드를 활용하면 array, object 자료형에 따옴표를 붙어서 서버로 전송할 수 있다.
    - JSON에 붙은 따옴표를 제거해서 array, object 만들고 싶으면 JSON.parse() 안에 넣어보자



#### 삭제기능 만들기 2(Ajax 추가내용과 에러처리)

- 서버에 정보가 없으면 
  - DB 뒤져보거나
  - 유저에게 보내라고하거나
- 삭제 요청

```react
// Listitem.js
'use client'
import Link from "next/link";

export default function ListItem({result}) {

  console.log(result);
  return (
    <div>
       {result.map((e, i) =>
        <div className="list-item" key={i}>
          <Link href={`/detail/${result[i]._id}/`}>
            <h4>{result[i].title}</h4>
          </Link>
          <Link href={`/edit/${result[i]._id}`}>✏️</Link>
            <span onClick={() => {
              // post/delete라는 주소 안에 있는 곳에 method, body를 보낸다. 
              fetch('/api/post/delete', {
                method : "DELETE",
                body : result[i]._id,
              })
              // ajax 요청 완료시 코드실행은
              .then(() => {
                console.log(123)
              })
            }}>🗑️</span>
            <p>1월 1일</p>
            <h4>{result[i].content}</h4>
        </div>
      )}
    </div>
  )
}
```

- 요청 들어오면 DB에서 게시물 삭제

```react
import { connectDB } from "@/util/database";
import { ObjectId } from "mongodb";

export default async function handler(요청, 응답) {
  // 요청 형태가 delete라면
  if (요청.method == "DELETE") {
    const db = (await connectDB).db("forum");
    // db에 요청 body(=== id)값을 new Object 형태로 담아서 삭제 요청
    let result = await db.collection("post").deleteOne({ _id : new ObjectId(요청.body) });
    console.log(result);
    응답.status(200).json("삭제완료")
  }
}
```

- 삭제가 잘 되면 콘솔 찍었을때 { acknowledged: true, deletedCount: 1 }형태가 나온다. 

- `.then()`을 이용해서 요청 완료시 메시지나 데이터를 받는다.

  - Ajax 에러처리는

    - 아래처럼 성공시, 실패시 코드를 구분해서 처리한다.

    ```react
    fetch('/URL')
    .then((r)=>{
      if(r.status == 200) {
        return r.json()
      } else {
        //서버가 에러코드전송시 실행할코드 서버가 status(500) 같은거 보낼때
      }
    })
    .then((result)=>{ 
      //성공시 실행할코드 
    }).catch((error)=>{
      //인터넷문제 등으로 실패시 실행할코드 네트워크 문제
      console.log(error)
    })
    ```

    



#### 삭제기능 만들기 3 (query string / URL parameter)

- 에니메이션 넣기

  - 애니메이션 동작전/동작후 스타일 결정
    - 동작 전 opacity 1
      - transition는 css 스타일이 바뀔때 서서히 바뀌게 해주세요
    - 동작 후 opacity 0
      - 원할 때 에니메이션 동작 후 스타일 넣기

  - 완성품

  ```react
  'use client'
  import Link from "next/link";
  import axios from "axios";
  
  export default function ListItem({result}) {
  
  
    return (
      <div>
         {result.map((e, i) =>
          <div className="list-item" key={i}>
            <Link href={`/detail/${result[i]._id}/`}>
              <h4>{result[i].title}</h4>
            </Link>
            <Link href={`/edit/${result[i]._id}`}>✏️</Link>
              <span onClick={(e) => {
                // post/delete라는 주소 안에 있는 곳에 method, body를 보낸다.
                fetch('/api/post/delete', {
                  method : "DELETE",
                  body : result[i]._id,
                })
                // ajax 요청 완료시 코드실행은
                .then((r) => r.json())
                // e.target 유저가 방금 클릭한 html 요소, 부모노드 요소에 style에 opacity를 주면 된다. 
                .then(() => {
                  e.target.parentElement.style.opacity = 0;
                  // setTimeout함수 사용해서 1초 후에 박스가 사라지게 처리
                  setTimeout(() => {
                    e.target.parentElement.style.display = "none";
                  }, 1000)
                })
              }}>🗑️</span>
              <p>1월 1일</p>
              <h4>{result[i].content}</h4>
          </div>
        )}
      </div>
    )
  }
  ```

  

- GET 요청시에도 2개 방법 쓰면 서버로 데이터 전송가능

  - 서버로 데이터 보내는 법

    - fetch는 body에 넣기

    - 서버로 데이터 전송시 귀찮으면 query string /URL parameter 활용 

    - 1. query string

      - url 뒤에 ?데이터이름 =값 입력가능

      ```react
      // query string 작성하면 서버로 데이터 전송
      fetch('/api/test2?name=kim&age=20') 
      ```

      ```react
      // 요청.query를 입력하면 { name: "kim"}이 잘 출력된다. 
      export default function handler(요청, 응답) {
        console.log(요청.query)
        return 응답.status(200).json()
      }
      ```

      - 장점
        - 간단하다.
        - GET 요청도 데이터 전송 가능
      - 단점
        - 데이터 많으면 더러움
        - URL에 데이터 노출됨

    - URL 파라미터

      - Api 폴더에 abc 폴더 생성 후에 [어쩌구].js 파일 만들고
      - 누가 /api/abc/아무문자로 요청하면 파일의 코드가 실행된다. 
      - 1.URL parameter를 하나 만들고
      - 2.URL parameter 자리에 데이터입력

      ```react
      // abc/[어쩌구].js
      fetch('/api/abc/kim')
      ```

      ```react
      // 요청.query를 입력하면 { name: "kim"}이 잘 출력된다. 
      export default function handler(요청, 응답) {
        console.log(요청.query)
        return 응답.status(200).json()
      }
      ```

      
