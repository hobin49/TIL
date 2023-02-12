#### PJT 생성

- `vue create "프로젝트 이름"`: 뷰 생성

- 폴더 설정 후에(esLint를 package.json에 넣어놨다.)

- `cd "프로젝트 이름" `: 프로젝트 폴더로 이동

- `code .`: vs 코드 실행

- 자 그리고 `eol-last` 오류 발생 대처

  - package.json으로 이동

    - 아래 eslint설정 들어가서 off처리를 해준다.

    ```vue
      "eslintConfig": {
        "rules": {
          "space-before-function-paren": "off",
          "eol-last" :"off"
        }
      },
    ```

    

- 기존의 컴포넌트에 있던 파일 삭제 후에 

- Header Vue를 만들고

  ```vue
  <template>
    <header>
      <h1>{{ title }}</h1>
    </header>
  </template>
  
  <script>
  export default {
    name: 'HeaderV',
    // 상위 Header.vue에서 하위 Header.vue에 title이라는 데이터를 전송한다.
    props: ['title']
    or
    props: {
      title: String
      }
    }
  }
  </script>
  
  <style scoped>
    header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 20px;
    }
  </style>
  
  ```

  

- 메인 App.vue에 Header Vue를 import 한다.

  ```vue
  <template>
  <div class="container">
    <!--import한 HeaderV를 사용한다-->
    <HeaderV title="Hobin" />
  </div>
  </template>
  
  <script>
  // import해주면 Header가 App.vue에 하위 컴포넌트가 된다.
  import HeaderV from './components/Header'
  export default {
    name: 'App',
    //Header 컴포넌트를 사용하기 위해서 등록한다.
    components: {
      HeaderV
    }
  }
  </script>
  
  <style>
  @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400&display=swap');
  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }
  body {
    font-family: 'Poppins', sans-serif;
  }
  .container {
    max-width: 500px;
    margin: 30px auto;
    overflow: auto;
    min-height: 300px;
    border: 1px solid steelblue;
    padding: 30px;
    border-radius: 5px;
  }
  .btn {
    display: inline-block;
    background: #000;
    color: #fff;
    border: none;
    padding: 10px 20px;
    margin: 5px;
    border-radius: 5px;
    cursor: pointer;
    text-decoration: none;
    font-size: 15px;
    font-family: inherit;
  }
  .btn:focus {
    outline: none;
  }
  .btn:active {
    transform: scale(0.98);
  }
  .btn-block {
    display: block;
    width: 100%;
  }
  </style>
  
  ```

  

- 다음 Button.vue를 만들어서 상위인 Header.vue에 연결하는 과정

```vue
<!--Button.vue-->
<template>
	<!--Header.vue에 상위 컴포넌트인 App.vue에서 가져온 클래스-->
	<!--스타일 바인딩 해주고 onclick 이벤트 실행-->
	<button @click="onClick()" :style="{background: color}" class="btn">Add Task</button>
</template>
<script>
	export default{
    name: 'ButtonS',
    props: {
      text: String,
      color: String,
    },
    methods: {
    //이벤트 정의
    onClick() {
      console.log('너 바보')
    }
  }
  }
</script>
```

```vue
<!--Header.vue-->
<template>
	<ButtonS text="Add Task", color="green"/>
</template>

<script>
import ButtonS from './Button'
export default {
	components: {
		ButtonS
	}
}
</script>
```

- 오늘 할일 띄우기(Task.vue -> Tasks.vue -> App.vue)

```vue
<!--Tasks.vue-->
<template>
  <div :key="task.id" v-for="task in tasks">
    <TaskMain :task='task' />
  </div>
</template>

<script>
import TaskMain from './Task'

export default {
  name: 'TaskS',
  props: {
    tasks: Array
  },
  components: {
    TaskMain
  }
}
</script>
```

```vue
<!--App.vue-->
<template>
<div class="container">
  <HeaderV title='Task Tracker'/>
  <!--task 컴포넌트 표시-->
  <TaskS :tasks='tasks' />
</div>
</template>

<script>
import HeaderV from './components/Header'
import TaskS from './components/Tasks'

export default {
  name: 'App',
  components: {
    HeaderV,
    TaskS
  },
  data () {
    return {
      tasks: []
    }
  },
  created() {
    this.tasks = [
      {
        id: 1,
        text: 'Doctors Appointment',
        day: 'March 1st at 2:30pm',
        reminder: true
      },
      {
        id: 2,
        text: 'Meeting at School',
        day: 'March 1st at 2:30pm',
        reminder: true
      },
      {
        id: 3,
        text: 'Food Shopping',
        day: 'March 3rd at 11:00am',
        reminder: true
      }
    ]
  }

}
</script>
```

- Task.vue(Task.vue -> Tasks.vue)

```vue
<!-- 또다른 task등록 Task.vue--> 
<template>
	<!--조건 함수-->
	<div :class="[task.reminder ? 'reminder': '', 'task']">
    <h3>
      {{ task.text }}
      <i class='fas fa-times'></i>
    </h3>
    <p>{{ task.day }}</p>
  </div>
</template>

<script>
export default {
  name: 'TaskMain',
  props: {
    //객체로 받기
    task: Object
  }
}
</script>
```

```vue
<!--Tasks.vue-->
<template>
  <div :key="task.id" v-for="task in tasks">
    <!--Task에 해당하는 컴포넌트-->
    <TaskMain :task='task' />
  </div>
</template>

<script>
import TaskMain from './Task'

export default {
  name: 'TaskS',
  props: {
    tasks: Array
  },
  components: {
    TaskMain
  }
}
</script>
```

- Task.vue -> Tasks.vue -> App.vue 순서로 진행된다



- 삭제기능(x버튼을 누르면)

```vue
<!--Task.vue-->
<!--삭제 기능 버튼-->
<i @click="onDelete(task.id)" class="fas fa-times"></i>

<script>
	methods: {
    onDelete(id) {
      //부모 컴포넌트로 변경값 보내기(메서드 이름, 들어갈 값)
      this.$emit('delete-task', id)
    }
  }
</script>


<!--Tasks.vue -->
<Task @delete-task="$emit('delete-task', task.id)" :task="task"/>

<script>
	export default {
    // App-vue와  Tasks.vue는 부모와 자식 사이이다. 그래서 배열 데이터로 부모 컴포넌트에서 추가한 옵션인 클릭 이벤트를 사용하겠다 명시
    emits: ['delete-task']
  }
</script>

<!--App.vue-->
<Tasks @delete-task="deleteTask" :tasks="tasks" />

<script>
methods: {
	deleteTask(id) {
		if (confirm('Are you sure?')) {
      this.tasks = this.tasks.filter((task) => task.id !== id)
    }
	}
}
</script>
```



- Double click button

```vue
<!-- Task.vue-->
<!-- dblclick을 하면 더블클릭시 이벤트가 발생하는 것이다 emit을 안에 다 만들면 methods에 만들지 않아도 된다 -->
<template>
  <div @dblclick="$emit('toggle-reminder', task.id)" :class="[task.reminder ? 'reminder': '',  'task']">
    <h3>
      {{ task.text }}
      <i @click="$emit('delete-task', task.id)" class='fas fa-times'></i>
    </h3>
    <p>{{ task.day }}</p>
</div>
</template>

<!--Tasks.vue-->
<template>
  <div :key="task.id" v-for="task in tasks">
    <TaskMain @toggle-reminder="$emit('toggle-reminder', task.id)" @delete-task="$emit('delete-task', task.id)" :task='task' />
  </div>
</template>

<script>
import TaskMain from './Task'

export default {
  emits: ['delete-task', 'toggle-reminder']
}
</script>

<!--App.vue-->
<template>
<div class="container">
  <HeaderV title='Task Tracker'/>
  <TaskS @toggle-reminder="toggleReminder" @delete-task="deleteTask" :tasks='tasks' />
</div>
</template>
<script>
 methods: {
    toggleReminder(id) {
      <!-- map은 내가 원하는 방식의 형태로 return 해준다. false == True로 변환-->
      this.tasks = this.tasks.map((task) => task.id === id ? { ...task, reminder: !task.reminder } : task)
    }
  }
</script>
```



- 할 일 추가하기 (AddTask.vue -> App.vue)

```vue
<!--AddTask.vue-->
<template>
	<!-- sumbit 이벤트 발생--> 
  <form @submit="onSubmit" class='add-form'>
    <div class='form-control'>
      <label>업무</label>
      <!--양방향 데이터 바인딩-->
      <input type="text" v-model="text" name="text" placeholder="할 일 추가"/>
    </div>
    <div class='form-control'>
      <label>날짜 & 시간</label>
      <!--양방향 데이터 바인딩-->
      <input type='text' v-model="day" name='day' placeholder="시간/날짜 추가">
    </div>
    <div class='form-control form-control-check'>
      <label>알림설정</label>
      <!--양방향 데이터 바인딩-->
      <input type="checkbox" v-model="reminder" name="remainder"/>
    </div>
    <input type="submit" value="할 일 저장하기" class='btn btn-block'/>
  </form>
</template>

<script>
export default {
  name: 'AddTask',
  data() {
    return {
      // text, day가 사용자가 입력해도 되고 내가 입력해도 되고
      text: '',
      day: '',
      reminder: false
    }
  },
  methods: {
    // submit이벤트 클릭시 발생하는 함수
    onSubmit(e) {
      //submit버튼을 누르면 창이 새로고침 되는 것을 막아준다.
      e.preventDefault()
			
      // 빈 텍스트면 경고창 띄워주고
      if (!this.text) {
        alert('Please add a task')
        // 이게 없으면 빈 텍스트 박스가 등장한다. 그래서 막아주는 효과
        return
      }
			
      
      const newTask = {
        // 배열에 이런식으로 저장이 된다.
        id: Math.floor(Math.random() * 10000),
        text: this.text,
        day: this.day,
        reminder: this.reminder

      }
      //하위 컴포넌트에서 상위 컴포넌트로 정보를 보낼때
      this.$emit('add-task', newTask)
			
      //이건 텍스트에 입력하고 input창을 초기화 하는 단계
      this.text = ''
      this.day = ''
      this.reminder = true
    }
  }
}
</script>


<!--App.vue-->
<template>
<div class="container">
  <AddTask @add-task='addTask'/>
</div>
</template>

<script>
methods: {
    addTask(task) {
      // 기존에 메모함에 새로운 값을 추가 하는거고
      // ...this.tasks가 없으면 새로운 값만 들어오고 기존의 값들은 초기화.
      this.tasks = [...this.tasks, task]
    },
}      
</script>
```



- Add Task 버튼 변경

```vue
<!--Button.vue-->
<template>
  <button @click="$emit('btn-click')" :style="{background: color}" class='btn'>{{text}}</button>
</template>
      
<!--Header.vue-->
<template>
  <header>
    <h1>{{ title }}</h1>
    <!--하위 컴포넌트에서 받아온 btn-click메서드 사용하고-->
    <!-- App.vue에 또 toggle-add-task라는 메서드를 보낸다 -->
    <!-- text바인딩해서 만약에 showAddTask(False)이면 close 아니면 Add로 텍스트를 바꾼다.-->
    <ButtonS @btn-click="$emit('toggle-add-task')" :text="showAddTask ? '닫기' : '추가하기'" :color="showAddTask ? 'red' : 'green'"/>
  </header>
</template>

<script>
import ButtonS from './Button'

export default {
  name: 'HeaderV',
  props: {
    title: String,
    //ShowAddTask를 불린형태로 받아준다.
    showAddTask: Boolean
  },
  components: {
    ButtonS
  }
}
</script>      
    
<!--App.vue-->
<template>
<div class="container">
  <!-- showAddTask바인딩화 해서 data에 들어있는 showaddtask를 사용-->
  <HeaderV @toggle-add-task="toggleAddTask" title='Task Tracker' :showAddTask='showAddTask'/>
  <div v-show='showAddTask'>
    <AddTask @add-task='addTask'/>
  </div>
  <TaskS @toggle-reminder="toggleReminder" @delete-task="deleteTask" :tasks='tasks' />
</div>
</template>    

<script>
export default {
  data () {
    return {
      //showAddTask는 default값으로 false가 들어가 있다.
      showAddTask: false
    }
  },
   methods: {
   //false면 True -> True면 false 만드는것  
    toggleAddTask() {
      this.showAddTask = !this.showAddTask
}
</script>
```



- `npm run serve` : 로컬 서버를 웹팩 데브 서버로 실행

- `npm run build`: 웹팩으로 최종 결과물 변환(빌드)
- `sudo npm i -g serve`
- `serve -s dist`: 빌드된 결과물 보기
- `npm i json server`: json server는 아주 짧은 시간에 REST API를 구축해주는 라이브러리이다. 하지만 REST API 서버의 기본적인 기능을 갖추고 있다. 
  - Json-server에서는 단순히 데이터를 넣고 조회하는 것 외에도 페이징, 필터링, 정렬, 수정, 삭제 등의 기능을 지원한다.

- npm run json-server가 안 될 때
  - `npx json-server --watch db.json --port 3000`

```vue
<!--package.json에 들어가서 scripts 부분에 추가-->
"scripts": {
    "backend": "json-server --watch db.json --port 3000"
  },
<!-- json에 접속 npm run backend 입력하면 담아놨던 배열이 보인다-->
<!--db.json 파일을 만들고 기존에 하드코딩이었던 tasks의 배열들을 넣었줬다..-->
<script>
export default {
  methods: {
    async fetchTasks() {
      const res = await fetch('http://localhost:3000/tasks')

      const data = await res.json()

      return data
    }
  },
  async created() {
    this.tasks = await this.fetchTasks()
  }

}
</script>
```

- 프록시 서버

  - 클라이언트가 자신을 통해 다른 네트워크 서비스에 간접적으로 접속할 수 있게 해주는 응용 프로그램
  - 서버 클라이언트 사이의 중계기로써 빠른 액세스나 안전한 통신등을 확보하기 위한 대리로 통신을 수행하는 것을 프록시라고 한다.
  - 프록시 서버에 캐시를 저장할 수 있다. 다시 동일한 페이지를 리퀘스트 했을 때에는 캐시에 남아 있는 정보를 클라이언트에게 준다. 이것으로 사이트에 접속하는 속도가 빨라진다.

  ```js
  module.exports = {
    devServer: {
      proxy: {
        '^/api': {
          target: 'http://localhost:3000',
          changeOrigin: true,
          logLevel: 'debug',
          pathRewrite: { '^/api': '/' }
        }
  
      }
    }
  }
  ```

  

- 할일 추가 메서드 변경(비동기화)

  ```vue
  <script>
  <!--기존 코드-->
  addTask(task) {
  	this.tasks = [...this.tasks, task]
  }
  
  <!--변경된 코드-->
  async addTask(task) {
        const res = await fetch('api/tasks', {
          method: 'POST',
          headers: {
            // application/json은 Restful API를 사용하게 되며 request를 날릴 때 대부분 json을 많이사용
            //content-type에 따라 데이터를 받는 측에서는 데이터를 어떻게 처리해야 할 지 판단한다.
            'content-type': 'application/json'
          },
          //JSON.stringify(value, replacer, space)
          //value(필수): Json 문자열로 변환할 값이다.
          body: JSON.stringify(task)
        })
  
        const data = await res.json()
  
        this.tasks = [...this.tasks, data]
      },
  </script>      
  ```
  
  - 

- 삭제버튼(비동기화)

```vue
<script>
  <!--새로고침하면 삭제되었던게 다시 돌아오지 않는다-->
			async deleteTask(id) {
      if (confirm('Are you sure?')) {
        const res = await fetch(`api/tasks/${id}`, {
          method: 'DELETE'
        })
				
        res.status === 200 ? this.tasks = this.tasks.filter((task) => task.id !== id) : alert('Error deleting task')
      }
    },
</script>
```

- 상태변화(비동기화)-다시 체크

```vue
<script>
async toggleReminder(id) {
      const taskToToggle = await this.fetchTask(id)
      const updTask = { ...taskToToggle, reminder: !taskToToggle.reminder }

      const res = await fetch(`api/tasks/${id}`, {
        //update
        method: 'PUT',
        headers: {
          'Content-type': 'application/json'
        },
        body: JSON.stringify(updTask)
      })

      const data = await res.json()

      this.tasks = this.tasks.map((task) => task.id === id ? { ...task, reminder: data.reminder } : task)
    }
</script>
```

- API
  - 소프트웨어가 다른 소프트웨어로부터 지정된 형식으로 요청, 명령을 받을 수 있는 수단을 API라고 한다.
  - restful하게 만든 API는 요청을 보내는 주소만으로도 알 수 있다
  - post(create), put(업데이트), patch body가 있어서 get, delete보다 비교적 안전하게 감춰서 실어 보낼 수 있다.
    - put은 정보를 통째로 갈아끼울 때 (변경할 학생의 index가 필요하다.)
    - Patch는 정보 중 일부를 특정 방식으로 변경할 때 
    - Delete를 할때는 그 학생의 인덱스를 표시해야한다.
  - restful ApI란 HTTP 요청을 보낼 때 어떤 URI에 어떤 메소드를 사용할지 개발자들 사이에 널리 지켜지는 약속
