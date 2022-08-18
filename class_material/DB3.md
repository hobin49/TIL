### 기본 함수와 연산

- 문자열 함수
  - SUBSTR(문자열, start, length): 문자열 자르기
    - 시작 인덱스는 1, 마지막 인덱스는 -1
  - TRIM(문자열), LTRIM(문자열), RTRIM(문자열): 문자열 공백 제거
  - LENGTH(문자열): 문자열 길이
  - REPLACE(문자열, 패턴, 변경값): 패턴에 일치하는 부분을 변경
  - UPPER(문자열), LOWER(문자열): 대소문자 변경
  - ||:문자열 합치기(concatenation) -pipe sign



```sql
-- 문자열 합치기 
__ (성+ 이름) 출력, 5명만

SELECT last_name || first_nmae 이름(AS 생략 가능), age, country, phone, balance FROM users LIMIT 5; 

-- 문자열 길이 LENGTH
SELECT LENGTH(first_name), first_name FROM USERS LIMIT 5;

-- 문자열 변경 REPLACE
SELECT first_name, phone, REPLACE(phone, "-", "") FROM users LIMIT 5;

-- 숫자 활용
SELECT MOD(5, 2) FROM users LIMIT 1;

-- 올림, 내림, 반올림
SELECT CEIL(3.14), FLOOR(3.14), ROUND(3.14) FROM users LIMIT 1;

-- 제곱근
SELECT SQRT(9) FROM users LIMIT 1:
  
-- 9^2
SELECT POWER(9, 2) FROM users LIMIT 1;
```

- 숫자 함수
  - ABS(숫자): 절대 값
  - SIGN(숫자): 부호 (양수 1, 음수 -1, 0 0)
  - MOD(숫자1, 숫자2): 숫자1을 숫자2로 나눈 나머지
  - CEIL(숫자), FLOOR(숫자), ROUND(숫자, 자리): 올림, 내림, 반올림
  - POWER(숫자1, 숫자2): 숫자1의 숫자2 제곱
  - SQRT(숫자): 제곱근



### GROUP BY

- Aggregation function(집계 함수) 다시보기
  - 값 집합에 대한 계산을 수행하고 단일 값을 반환(레코드)
    - 여러 행으로부터 하나의 결괏값을 반환하는 함수
  - SELECT 구문에서만 사용됨
  - 예시
    - 테이블 전체 행 수를 구하는 COUNT(*)
    - Age 컬럼 전체 평균 값을 구하는 AVG(age)



- GROUP BY

  - "make a set of summary rows from a set of rows"
  - SELECT 문의 optional 절
  - 행 집합에서 요약 행 집합을 만듦
  - 선택된 행 그룹을 하나 이상의 열 값으로 요약 행으로 만듦
  - **문장에 WHERE 절이 포함된 경우 반드시 WHERE 절 뒤에 작성한다**

  ```sql
  SELECT * FROM 테이블이름 GROUP BY 컬럼1, 컬럼2;
  ```

  

  - 지정된 컬럼의 값이 같은 행들로 묶음
  - 집계함수와 활용하였을 때 의미가 있다
  - 그룹화된 각각의 그룹이 하나의 집합으로 집계함수의 인수로 넘겨진다.

  ```sql
   SELECT * FROM users GROUP BY last_names;
  ```

  |  id  | last name |
  | :--: | :-------: |
  |  1   |    김     |
  |  2   |    김     |
  |  3   |    박     |
  |  4   |    이     |

  |  id  | last_name |
  | :--: | :-------: |
  |  1   |    김     |
  |  3   |    박     |
  |  4   |    이     |

  

  ```sql
  -- 성을 기준으로 각 성의 평균을 출력한다.
  SELECT AVG(age) FROM users GROUP BY 성;
  
  -- 각 성씨가 몇 명씩 있는지 조회한다면?
  SELECT last_name, COUNT(*) FROM users GROUP BY last_name;
  
  -- GROUP BY에서 활용하는 컬럼을 제외하고는 집계함수를 쓰세요
  SELECT last_name, AVG(age), COUNT(*) FROM users GROUP BY last_name;
  
  -- GROUP BY는 결과가 정렬되지 않아요. 기존 순서와 바뀐다. 
  -- 원칙적으로 내가 정렬해서 보고 싶으면 ORDER BY!
  
  -- GROUP BY WHERE를 쓰고 싶다. 
  -- 100번 이상 등장한 성만 출력하고 싶음 밑 구문처럼 하면 오류 발생한다.
  SELECT last_name, COUNT(last_name) FROM users WHERE COUNT(last_name) > 100 GROUP BY last_name;
  
  -- 조건에 따른 GROUP을 하시려면 HAVING을 사용한다.
  SELECT last_name, COUNT(last_name), FROM users GROUP BY last_name HAVING COUNT(last_nmae) > 100;
  ```

- SELECT 문장 실행 순서
  - FROM => WHERE => GROUP BY => HAVING => SELECT => ORDER BY
    - FROM 테이블을 대상으로
    - WHERE 제약조건에 맞춰서 뽑아서
    - GROUP BY 그룹화한다.
    - HAVING 그룹 중에 조건과 맞는 것만을
    - SELECT 조회하여
    - ORDER BY 정렬하고
    - LIMIT/OFFSET 특정 위치의 값을 가져온다.
- ALTER TABLE
  - 1.테이블 이름 변경
  - 2.새로운 column 추가
  - 3.column 이름 수정
  - 4.column 삭제

```sql
-- 1. 테이블 이름 변경
ALTER TABLE table_name
RENAME TO new_name;

-- 2. 새로운 컬럼 추가
ALTER TABLE table_nmae
ADD COLUMN column_definition;

-- 3. 컬럼 이름 수정
ALTER TABLE table_name
RENAME COLUMN current_name To new_name;

-- 4. 컬럼 삭제
ALTER TABLE table_name
DROP COLUMN column_name;
```

- 테이블이 만들어지기 전에 데이터가 있는데 NOT NULL을 하면 오류가 발생한다.

- Q.title과 content라는 컬럼을 가진 articles라는 이름의 table을 새롭게 만들어 보세요 (두 컬럼 모두 비어 있으면 안되며, rowid를 사용한다)

```sql
CREATE TABLE	articles (
title TEXT NOT NULL,
content TEXT NOT NULL
);
```

- Q.ariticles 테이블에 값을 추가해보세요 (title은 1번제목, content는 1번내용)

```sql
INSERT INTO articles VALUES ('1번제목', '1번 내용');
```

- 방금 만든 테이블의 이름을 변경해보기

```sql
ALTER TABLE 기존테이블이름 RENAME TO 새로운테이블이름;
```

- 새로운 컬럼 이름은 Created_at이며, TEXT 타입에 NULL 설정

```sql
sqlite> ALTER TABLE news ADD COLUMN created_at TEXT NOT NULL;
Error: Cannot add a NOT NULL COLUMN with default value NULL-
```

- 테이블에 있던 기존 레코드들에는 새로 추가할 필드에 대한 정보가 없다. 그렇기 때문에 NOT NULL 형태의 컬럼은 추가가 불가능
  해결 방법 2가지

  - 1.NOT NULL 설정 없이 추가하기
  - 2.기본 값(DEFAULT) 설정하기

  ```sql
  ALTER TABLE news ADD COLUMN subtitle TEXT NOT NULL DEFAULT '소제목';

