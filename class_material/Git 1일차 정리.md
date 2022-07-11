## 1일차 정리

![git:gihub](https://media.vlpt.us/images/yeeed711/post/d4c38b37-a2aa-4fff-9ac6-63a57a8e0424/git.png)

- **😸git 이란 무엇인가?**
  
  -  Git은 2005년 리눅스를발명한 리눅스 토르발스가 개발했다.
  - Git은 `분산버전관리 시스템`이다. (**버전: 컴퓨터 소프트웨어의 특정 상태** )
  - Terminal을 통해서 Git을 사용하는데 Terminal 같은 환경을 *CLI(Comman line interface)*라고 한다.
  
- **📖 용어 정리**
  - pwd(print working directory): 현재 디렉토리 출력
  
  - cd(change directory): 디렉토리 이동
  
  - ls(list): 목록
  
  - mkdir(make directory): 디렉토리 생성 
  
  - touch: 파일의 날짜와 시간 생성
  
  - cd .. : 상위 폴더로 이동(**주의할점: cd와 마침표 사이의 한 칸 간격이 있어야 한다**)
    - 폴더의 이름이 띄어쓰기가 되어 있다면 두 가지 방법이 있다. 예시) **cd 새 \ 폴더 or 새_폴더**
    - `cd + Tab`을 하면 해당 디렉토리에 있는 파일을 볼 수 있다.
    
  - rm: 파일을 지운다.
    - 파일 말고 폴더를 지우고 싶다면 🤔: *rm -r + 폴더* 
    
  - git init: init을 입력하면 (master)가 생기면서 폴더가 git으로 관리되고 있다는 것을 알 수 있다. (**맥 OS에서는 master를 설정하지 않으면 뜨지 않음**) git을 통해서 저장소를 초기화 하겠다고 한다면   `.git`이라는 생성되고 여기에 모든 정보들이 기록된다. (**`.git`에 들어가면 들어오지 말라고 `GIT_DIR`이라고 뜬다)
  
  - git status: 폴더에서 일어나는 모든 일들을 추척한다. 파일의 상태를 확인하고 커밋 안 된 파일을 체크할 때 사용
  
  - git add < file >: working directory 상의 변경 내용을 staging area에 추가하기 위해 사용
  
  - git commit -m "커밋 메시지": **커밋 메시지를 통해 내가 무슨 작업을 했는지 기록하는 행위 or 나중에 버전을 되돌아가고 싶을 때 그 버전을 명확하게 되돌아 가고 싶을 때 **
  
    - Untrackted 상태의 파일을 staged로 변경 
    - Modified 상태의 파일을 staged로 변경
  
  - git log: 현재 저장소에 기록된 커밋(버전)을 조회
    - git log --1: 직전 커밋을 불러온다.
    - git log --oneline: 한 줄로 나타내준다.
    - git log --2 --oneline: 최근 2개의 커밋을 한 줄로 나타내준다.
    
  - git config --global user.email "이메일": 이메일을 등록한다. (**만약에 다시 등록하면 덮여쓰여진다**)
  
  - git config --global user.name "아이디": 아이디를 등록한다.
  
  - git config --global --list: 등록된 아이디와 이메일을 등록한다. 
  
  - git config -l<**설정확인**>
  
  - git config --global -l<**branch, email, id**>
  
    



- 📋버전을 기록하는 방법:

  - 기록하는 방법은 크게 3단계로 구성되어 있다. 

  ![](data:image/png;base64,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)

  - working directory 에서 작업을 하면 👉 staging area에서 add 하고 👉 repository에서 버전으로 남긴다.
  - 특히 staging area의 경우 중간과정으로 사용하며 개발할 때 임시공간의 역할을 맡는다. 
  - **working directory 에서 staging area로 파일이 이동하는 것이 아니라 상태가 바뀌는 것이다**



- 기타(메시지 해석):

  - modified: 수정됐다

  - Staged: 수정한 파일을 곧 커밋할 것이라 표시한 상태

  - Committed: 커밋이 된 상태

  - 커밋할 것이 없댜.: staging area가 비어있다.

  - working too clean: 지금 새로 작업할 것도 없다.(working directory가 비어있다.)

  - Untracked: 한 번도 커밋하지 않아서 staged로 바로 간다. 
  
  - Unmodified: 실제로 커밋된 적 파일인데 수정하지 않은 파일 👉 수정(add)하면 modified 👉add하면 staged가 된다.
  
    ![](https://t1.daumcdn.net/cfile/tistory/2447383557690E1003)

1.보고서 파일을 새로 만들었다 👉 Untracked

2.보고서 파일 add 👉 staged

3.보고서 파일 commit 👉 unmodified

4.보고서 수정 👉 modified



- 커밋 👉 의미있는 저장(sw 👉 반드시 작동 가능한 상태)



### 링크

[마크다운 문법](https://www.markdownguide.org/cheat-sheet/)

[GItHub Flavored Markdown](https://github.github.com/gfm/)

[mastering markdown](https://guides.github.com/features/mastering-markdown/)

[markdown guide](https://www.markdownguide.org/)

[google Technical writing](https://developers.google.com/tech-writing)

[technical writing conference](https://engineering.linecorp.com/ko/blog/write-the-docs-prague-2018-recap/)
