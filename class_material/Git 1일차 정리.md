## 1์ผ์ฐจ ์ ๋ฆฌ

![git:gihub](https://media.vlpt.us/images/yeeed711/post/d4c38b37-a2aa-4fff-9ac6-63a57a8e0424/git.png)

- **๐ธgit ์ด๋ ๋ฌด์์ธ๊ฐ?**
  
  -  Git์ 2005๋ ๋ฆฌ๋์ค๋ฅผ๋ฐ๋ชํ ๋ฆฌ๋์ค ํ ๋ฅด๋ฐ์ค๊ฐ ๊ฐ๋ฐํ๋ค.
  - Git์ `๋ถ์ฐ๋ฒ์ ๊ด๋ฆฌ ์์คํ`์ด๋ค. (**๋ฒ์ : ์ปดํจํฐ ์ํํธ์จ์ด์ ํน์  ์ํ** )
  - Terminal์ ํตํด์ Git์ ์ฌ์ฉํ๋๋ฐ Terminal ๊ฐ์ ํ๊ฒฝ์ *CLI(Comman line interface)*๋ผ๊ณ  ํ๋ค.
  
- **๐ ์ฉ์ด ์ ๋ฆฌ**
  - pwd(print working directory): ํ์ฌ ๋๋ ํ ๋ฆฌ ์ถ๋ ฅ
  
  - cd(change directory): ๋๋ ํ ๋ฆฌ ์ด๋
  
  - ls(list): ๋ชฉ๋ก
  
  - mkdir(make directory): ๋๋ ํ ๋ฆฌ ์์ฑ 
  
  - touch: ํ์ผ์ ๋ ์ง์ ์๊ฐ ์์ฑ
  
  - cd .. : ์์ ํด๋๋ก ์ด๋(**์ฃผ์ํ ์ : cd์ ๋ง์นจํ ์ฌ์ด์ ํ ์นธ ๊ฐ๊ฒฉ์ด ์์ด์ผ ํ๋ค**)
    - ํด๋์ ์ด๋ฆ์ด ๋์ด์ฐ๊ธฐ๊ฐ ๋์ด ์๋ค๋ฉด ๋ ๊ฐ์ง ๋ฐฉ๋ฒ์ด ์๋ค. ์์) **cd ์ \ ํด๋ or ์_ํด๋**
    - `cd + Tab`์ ํ๋ฉด ํด๋น ๋๋ ํ ๋ฆฌ์ ์๋ ํ์ผ์ ๋ณผ ์ ์๋ค.
    
  - rm: ํ์ผ์ ์ง์ด๋ค.
    - ํ์ผ ๋ง๊ณ  ํด๋๋ฅผ ์ง์ฐ๊ณ  ์ถ๋ค๋ฉด ๐ค: *rm -r + ํด๋* 
    
  - git init: init์ ์๋ ฅํ๋ฉด (master)๊ฐ ์๊ธฐ๋ฉด์ ํด๋๊ฐ git์ผ๋ก ๊ด๋ฆฌ๋๊ณ  ์๋ค๋ ๊ฒ์ ์ ์ ์๋ค. (**๋งฅ OS์์๋ master๋ฅผ ์ค์ ํ์ง ์์ผ๋ฉด ๋จ์ง ์์**) git์ ํตํด์ ์ ์ฅ์๋ฅผ ์ด๊ธฐํ ํ๊ฒ ๋ค๊ณ  ํ๋ค๋ฉด   `.git`์ด๋ผ๋ ์์ฑ๋๊ณ  ์ฌ๊ธฐ์ ๋ชจ๋  ์ ๋ณด๋ค์ด ๊ธฐ๋ก๋๋ค. (**`.git`์ ๋ค์ด๊ฐ๋ฉด ๋ค์ด์ค์ง ๋ง๋ผ๊ณ  `GIT_DIR`์ด๋ผ๊ณ  ๋ฌ๋ค)
  
  - git status: ํด๋์์ ์ผ์ด๋๋ ๋ชจ๋  ์ผ๋ค์ ์ถ์ฒํ๋ค. ํ์ผ์ ์ํ๋ฅผ ํ์ธํ๊ณ  ์ปค๋ฐ ์ ๋ ํ์ผ์ ์ฒดํฌํ  ๋ ์ฌ์ฉ
  
  - git add < file >: working directory ์์ ๋ณ๊ฒฝ ๋ด์ฉ์ staging area์ ์ถ๊ฐํ๊ธฐ ์ํด ์ฌ์ฉ
  
  - git commit -m "์ปค๋ฐ ๋ฉ์์ง": **์ปค๋ฐ ๋ฉ์์ง๋ฅผ ํตํด ๋ด๊ฐ ๋ฌด์จ ์์์ ํ๋์ง ๊ธฐ๋กํ๋ ํ์ or ๋์ค์ ๋ฒ์ ์ ๋๋์๊ฐ๊ณ  ์ถ์ ๋ ๊ทธ ๋ฒ์ ์ ๋ชํํ๊ฒ ๋๋์ ๊ฐ๊ณ  ์ถ์ ๋ **
  
    - Untrackted ์ํ์ ํ์ผ์ staged๋ก ๋ณ๊ฒฝ 
    - Modified ์ํ์ ํ์ผ์ staged๋ก ๋ณ๊ฒฝ
  
  - git log: ํ์ฌ ์ ์ฅ์์ ๊ธฐ๋ก๋ ์ปค๋ฐ(๋ฒ์ )์ ์กฐํ
    - git log --1: ์ง์  ์ปค๋ฐ์ ๋ถ๋ฌ์จ๋ค.
    - git log --oneline: ํ ์ค๋ก ๋ํ๋ด์ค๋ค.
    - git log --2 --oneline: ์ต๊ทผ 2๊ฐ์ ์ปค๋ฐ์ ํ ์ค๋ก ๋ํ๋ด์ค๋ค.
    
  - git config --global user.email "์ด๋ฉ์ผ": ์ด๋ฉ์ผ์ ๋ฑ๋กํ๋ค. (**๋ง์ฝ์ ๋ค์ ๋ฑ๋กํ๋ฉด ๋ฎ์ฌ์ฐ์ฌ์ง๋ค**)
  
  - git config --global user.name "์์ด๋": ์์ด๋๋ฅผ ๋ฑ๋กํ๋ค.
  
  - git config --global --list: ๋ฑ๋ก๋ ์์ด๋์ ์ด๋ฉ์ผ์ ๋ฑ๋กํ๋ค. 
  
  - git config -l<**์ค์ ํ์ธ**>
  
  - git config --global -l<**branch, email, id**>
  
    



- ๐๋ฒ์ ์ ๊ธฐ๋กํ๋ ๋ฐฉ๋ฒ:

  - ๊ธฐ๋กํ๋ ๋ฐฉ๋ฒ์ ํฌ๊ฒ 3๋จ๊ณ๋ก ๊ตฌ์ฑ๋์ด ์๋ค. 

  ![](data:image/png;base64,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)

  - working directory ์์ ์์์ ํ๋ฉด ๐ staging area์์ add ํ๊ณ  ๐ repository์์ ๋ฒ์ ์ผ๋ก ๋จ๊ธด๋ค.
  - ํนํ staging area์ ๊ฒฝ์ฐ ์ค๊ฐ๊ณผ์ ์ผ๋ก ์ฌ์ฉํ๋ฉฐ ๊ฐ๋ฐํ  ๋ ์์๊ณต๊ฐ์ ์ญํ ์ ๋งก๋๋ค. 
  - **working directory ์์ staging area๋ก ํ์ผ์ด ์ด๋ํ๋ ๊ฒ์ด ์๋๋ผ ์ํ๊ฐ ๋ฐ๋๋ ๊ฒ์ด๋ค**



- ๊ธฐํ(๋ฉ์์ง ํด์):

  - modified: ์์ ๋๋ค

  - Staged: ์์ ํ ํ์ผ์ ๊ณง ์ปค๋ฐํ  ๊ฒ์ด๋ผ ํ์ํ ์ํ

  - Committed: ์ปค๋ฐ์ด ๋ ์ํ

  - ์ปค๋ฐํ  ๊ฒ์ด ์๋.: staging area๊ฐ ๋น์ด์๋ค.

  - working too clean: ์ง๊ธ ์๋ก ์์ํ  ๊ฒ๋ ์๋ค.(working directory๊ฐ ๋น์ด์๋ค.)

  - Untracked: ํ ๋ฒ๋ ์ปค๋ฐํ์ง ์์์ staged๋ก ๋ฐ๋ก ๊ฐ๋ค. 
  
  - Unmodified: ์ค์ ๋ก ์ปค๋ฐ๋ ์  ํ์ผ์ธ๋ฐ ์์ ํ์ง ์์ ํ์ผ ๐ ์์ (add)ํ๋ฉด modified ๐addํ๋ฉด staged๊ฐ ๋๋ค.
  
    ![](https://t1.daumcdn.net/cfile/tistory/2447383557690E1003)

1.๋ณด๊ณ ์ ํ์ผ์ ์๋ก ๋ง๋ค์๋ค ๐ Untracked

2.๋ณด๊ณ ์ ํ์ผ add ๐ staged

3.๋ณด๊ณ ์ ํ์ผ commit ๐ unmodified

4.๋ณด๊ณ ์ ์์  ๐ modified



- ์ปค๋ฐ ๐ ์๋ฏธ์๋ ์ ์ฅ(sw ๐ ๋ฐ๋์ ์๋ ๊ฐ๋ฅํ ์ํ)



### ๋งํฌ

[๋งํฌ๋ค์ด ๋ฌธ๋ฒ](https://www.markdownguide.org/cheat-sheet/)

[GItHub Flavored Markdown](https://github.github.com/gfm/)

[mastering markdown](https://guides.github.com/features/mastering-markdown/)

[markdown guide](https://www.markdownguide.org/)

[google Technical writing](https://developers.google.com/tech-writing)

[technical writing conference](https://engineering.linecorp.com/ko/blog/write-the-docs-prague-2018-recap/)
