### CASE

- CASE문은 특정 상황에서 데이터를 변환하여 활용할 수 있다
- ELSE를 생략하는 경우 NULL값이 지정됨(웬만하면 작성하는 게 좋다.)

```sql
CASE
		WHEN 조건식 THEN 식
		WHEN 조건식 THEN 식
		ELSE 식
END
```

```sql
SELECT id, CASE WHEN gender = 1 THEN 남자 WHEN gender = 2 THEN 여자 END AS 성별 FROM table LIMIT 5;

SELECT id, smoking CASE 
WHEN smokinng = 1 THEN "비흡연자" WHEN smoking = 2 THEN "흡연자" WHEN smoking = 3 THEN "헤비스모커" ELSE '무응답' END FROM healthcare LIMIT 50;

-- 나이에 따라서 구분
-- 청소년(~18), 청년(~40), 중장년(~90)
SELECT first_name, last_name, age CASE WHEN age <= 18 THEN "청소년" WHEN age <= 40 THEN "청년" WHEN age <= 90 THEN "중장년" ELSE "노년" END FROM users LIMIT 10;
```

### 서브쿼리

- 서브 쿼리는 특정한 값을 메인 쿼리에 반환하여 활용하는 것
- 실데 테이블에 없는 기준을 이용한 검색이 가능함
- 서브 쿼리는 소괄호로 감싸서 사용하며, 메인 쿼리의 컬럼을 모두 사용할 수 있음
- 메인 쿼리는 서브 쿼리의 컬럼을 이용할 수 없음

```sql
SELECT *(원하는 데이터)
FROM 테이블
WHERE 컬럼1 = (
		SELECT 컬럼1
		FROM 테이블
);
```

- 단일행 서브쿼리

  - 서브쿼리의 결과가 0 또는 1개인 경우

  - 단일행 비교 연산자와 함께 사용(=, <, <=, >=, >, <>)

    - users에서 가장 나이가 작은 사람의 수는?

    ```sql
    SELECT age, COUNT(*) FROM users GROUP BY age ORDER BY AGE LIMIT 1;
    
    -- 서브쿼리
    SELECT COUNT(*) FROM users WHERE age = 15;
    
    -- 서브쿼리--
    SELECT MIN(age) FROM users;
    -- 매인쿼리: 서브쿼리를 괄호로 묶는다(결과를 통해서 내가 값을 받아서 그 값으로 사용하는 거)
    SELECT COUNT(*) FROM users WHERE age = (SELECT MIN(age) FROM users);
    ```

    

    - users에서 평균 계좌 잔고가 높은 사람의 수는?

    ```sql
    -- 서브쿼리
    SELECT AVG(balance) FROM users;
    
    -- 메인쿼리
    SELECT COUNT(*) FROM users WHERE balance > (SELECT AVG(balance) FROM users);
    ```

    

- 다중행 서브쿼리

  - 서브쿼리 결과가 2개 이상인 경우
  - 다중행 비교 연산자와 함께 사용(IN, EXISTS, All, ANY, SOME 등)

- 다중컬럼 서브쿼리

  

  - 단일행 서브쿼리

  - Q.users에서 유은정과 같은 지역에 사는 사람의 수는?

  ```sql
  -- 이은정과 같은 지역에 사는 사람의 수?
  SELECT country, FROM users WHERE last_name = "이" AND first_name = "은정";
  
  -- 전라도와 경상도에 사는 이은정은 몇 명?  
  SELECT COUNT(*) FROM users WHERE country IN (SELECT country, FROM users WHERE last_name = "이" AND first_name = "은정");
  ```

  - Q.전체 인원과 평균 연봉, 평균 나이를 출력하세요 

  ```sql
  SELECT COUNT(*), AVG(연봉), AVG(나이) FROM users;
  -- 인위적으로 서브쿼리 만들기
  SELECT 
  	(SELECT COUNT(*) FROM users) AS 총인원, 
  	(SELECT AVG(balance) FROM users) AS 평균연봉;
  ```

  - 단일행 서브쿼리 - UPDATE에서의 활용

  ```sql
  UPDATE users
  SET balance = (SELECT AVG(balance) FROM users);
  ```

  - 다중행 서브쿼리

  ```sql
  SELECT country FROM users WHERE last_name = "이" AND first_name = '은정';
  
  -- 두 지역에 사는 이은정을 count
  SELECT COUNT(*) FROM users WHERE country = (SELECT country FROM users WHERE last_name = "이" AND first_name = '은정');
  
  -- IN을 사용한다. 경상도 + 전라도를 포함한다. users에서 이은정과 같은 지역에 사는 사람의 수는?
  SELECT COUNT(*) FROM users WHERE country IN (SELECT country FROM users WHERE last_name = "이" AND first_name = '은정');
  ```

  - Q. 특정 성씨에서 가장 어린 사람들의 이름과 나이
  - 다중컬럼 서브쿼리

  ```sql
  -- 특정 성씨별로 가장 적은 나이
  SELECT last_name, MIN(age) FROM users GROUP BY last_name;
  
  -- 특정 성씨에서 가장 적은 나이
  SELECT last_name, age FROM users WHERE age = (SELECT min(age) from users) GROUP BY first_name
  
  -- 특정 성씨에서 가장 어린 사람들의 이름과 나이 
  SELECT last_name, first_name, age FROM users WHERE (last_name, age) IN (SELECT last_name, MIN(age) FROM users GROUP BY last_name ORDER BY last_name);
  
  SELECT * FROM 댓글 WHERE 게시판id = 1;
  ```

  - Q. AC/DC의 모든 앨범

  ```sql
  -- ID 조회
  SELECT ArtistId FROM artists WHERE Name = "AC/DC";
  
  -- 서브쿼리
  SELECT * FROM albums WHERE ARtisID = (SELECT ArtistID FROM artists WHERE Name = "AC/DC");
  ```

  