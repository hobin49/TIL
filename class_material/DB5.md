### Join

- 관계형 데이터베이스의 가장 큰 장점이자 핵심적인 기능
- 일반적으로 데이터베이스에는 하나의 테이블에 많은 데이터를 저장하는 것이 아니라 여러 테이블로 나눠 저장하게 되며, 여러 테이블을 결합(Join) 하여 출력하여 활용
- 일반적으로 레코드는 기본키(PK)나 외래키(FK) 값의 관계에 의해 결합함
- FK는 일반적으로 PK다. FK를 사용하면 데이터를 하나 바꾸면 거기에 해당하는 FK의 값들은 자동적으로 변경된다. 

- 대표적인 JOIN
  - INNER JOIN:두 테이블에 모두 일치하는 행만 반환
  - OUTER JOIN:동일한 값이 없는 행도 반환
  - CROSS JOIN:모든 데이터의 조합

```sql
sqlite3 project.sqlite3

CREATE TABLE users(
		id INT PRIMARY KEY,
		name TEXT,
		role_id INT
);


INSERT INTO users VALUES
		(1, '관리자', 1),
		(2, '김철수', 2),
		(3, '이영희', 2);
		
		
.mode column
SELECT * FROM users;
```

- INNER JOIN : 테이블1과 테이블 2에서 조건에 일치하는(동일한 값이 있는) 행만 반환
- JOIN은 테이블 수의 -1만큼 해야한다.

```sql
SELECT *
FROM 테이블1 [INNER](생략가능) JOIN 테이블2
		ON 테이블1.칼럼 = 테이블2.칼럼;
```

```sql
-- 사용자와 각각의 역할을 출력하시오.
SELECT *
FROM users JOIN role
		ON user.role_id = role.id;
		
-- staff(2) 사용자(users)를 역할과 함께 출력하시오.
-- 스테프(2)만 출력하세요.

SELECT *
FROM users JOIN role
		ON user.role_id = role.id;
WHERE role.id = 2;

-- 이름을 출력하세요.
SELECT *
FROM users JOIN role
		ON user.role_id = role.id;
-- 여러 테이블이 있다보니 테이블의 이름을 지정해준다.
ORDER BY users.name DESC; 
```

- OUTER JOIN: 동일한 값이 없는 데이터도 반환할 때 사용

  - 기준이 되는 테이블에 따라 LEFT/RIGHT/FULL 지정

  ```sql
  SELECT *
  FROM 테이블 1 [LEFT|RIGHT|FULL] OUTER JOIN 테이블2
  		ON 테이블1.칼럼 = 테이블2.칼럼;
  		
  		
  -- LEFT OUTER JOIN(A-B) left에 테이블을 만들어주고 오른쪽에 해당하는 데이터들을 붙여주고 
  -- article에 users를 붙인다
  SELECT *
  FROM articles LEFT OUTER JOIN users
  		ON articles.user_id = users.id;
  WHERE articles.user_id IS NOT NULL;
  
  
  -- FULL OUTER JOIN(중복제거)
  
  SELECT *
  FROM articles FULL OUTER JOIN users
  		ON articles.user_id = users.id;
  ```

- CROSS JOIN:모든 가능한 경우의 수를 출력한다.

```sql
SELECT *
FROM users CROSS JOIN role;
```

```sql
sqlite sample.sqlite3
-- albus와 artist의 ID가 같은 것을 출력
SELECT * FROM albums JOIN artists 
		ON albums.ArtistId = artists.ArtistId
LIMIT 5;

```

- https://sql-joins.leopard.in.ua/

