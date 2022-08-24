- . 객체는 속성과 메소드를 가지고 있다.
- 객체는 모든 것이다. 하나의 타입이기도 하다. 
- 클래스가 사람이면 인스턴스 아이유(틀과 사례)
- 객체가 가지고 있는 값(속성), 메서드: 값이 함수

### ORM

- Object-Relational-Mapping
- 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간의 데이터를 변환하는 프로그래밍 기술
- 파이썬에서는 SQLAlchemy, peewee 등 라이브러리가 있으며 Django 프레임워크에서는 내장 Django ORM을 활용
- "객체로 DB를 조작한다"

```python
Genre.objects.all()
```

- 모델 설계 및 반영

  - (1)클래스를 생성하여 내가 원하는 DB의 구조를 만든다

  ```python
  class Genre(models.Model):
    	name = models.CharField(max_length = 30)
  ```

  

  - (2)클래스의 내용으로 데이터베이스에 반영하기 위한 마이그레이션 파일을 생성한다.

  ```python
  $python manage.py makemigrations
  ```

  ```python
  from django.db import migrations, models
  
  class Migration(migrations.Migration):
    	initial = True
      dependcies = [
        
      ]
      operations = [
        migrations.CreateModel(
        	name = "Genre",
        	fields = [
            	('id', models.AutoField(auto_created = True,
  primary_key = True, serialize = False, verbose_name = "ID")),
            				('name', models.CharField(max_length = 30)),
          ])
      ]
  ```

  

  - (3) DB에 migrate 한다.

    ```python
    $ python manage.py migrate
    ```

    



### 환경설정

```python
from django.db import models


#Genre 클래스를 만드는데.
#Models.Model 내부 클래스를 상속 받는다
#왜 상속 받을까요? 기능들을 활용하고 싶어서. (미리 만들어진)
class Genre(models.Model):
  	name = models.CharField(max_length = 30)
    
$python manage.py makemigrations #파일생성
$python manage.py migrate #db 테이블 만들기
$python manage.py shell_plus # 테스트 조작
IN[1]: genre = Genre()
IN[2]: genre.name = '인디밴드'
IN[3]: genre.name
IN[4]: genre.save() # == INSER INTO
IN[5]: genre.objects.all() # == SELECT * FROM genre

# iu라고 하는 변수의 이름을 가진 Person
# Person 클래스의 인스턴스를 만드는 코드는?
iu = Person()
#iu의 name 속성으로 아이유라고 하는 코드는?
iu.name = '아이유'


```

- 마이그레이션

  - model에 생긴 변화를 DB에 반영하기 위한 방법
  - 마이그레이션 파일을 만들어 DB 스키마를 반영한다

  - 명령어
    - Makemigrations:마이그레이션 파일 생성
    - Migrate:마이그레이션을 DB에 반영

- 클래스 생성 -> 테이블 생성 -> 필드 변경(수정, 삭제, 추가) -> 클래스 수정 -> 마이그레이션 파일 생성 -> db 반영

- Migrate 살펴보기

```python
BEGIN;
--
-- Create model Genre
--
CREATE TABLE "db_genre" (
		"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
		"name" varchar(30) NOT NULL
);
COMMIT;

#트랜잭션(중간에 오류가 발생하면 롤백을 실행시켜 쿼리가 반영되기 이전으로 돌린다.)
```

- 데이터베이스 조작(Datebase API)
  - Genre.objects.all()



### ORM 기본 조작

- create

```python
#1. create 메서드 활용
Genre.objects.create(name = "발라드")

#2. 인스턴스 조작
genre = Genre()
genre.name = '인디밴드'
genre.save()
```

```python
$ python manage.py shell_plus

In [1]: Genre.objects.create(name="트로트")
  
In [2]: genre = Genre()
 
In [3]: genre.name = '락'
 
In [4]: genre.save()
  
IN [5]: Genre.objects.all() #일종의 리스트 queryset 출력
  
IN [6]: Genre.objects.all()[0] #<Genre: Genre object (1)> -1번 아이디 접근 LIMIT 1; 자동으로 접근
  
IN [7]: Genre.objects.all()[0].name

IN [8]: for genre in genres:
    				print(genre.name)
      
IN [9]: Genre.obejects.get(id = 1) # <Genre: Genre object (1)>, 단일객 반드시 하나. 없거나, 많으면 오류
  #PK를 바탕으로 찾을떄는 get을 쓰면 좋다.

IN [10]: Genre.objects.filter(id = 1) # <Genre: Genre object (1)>, 전체 쿼리셋(무조건 결과가 QuerySet)
 # 나머지 모든 where라고 생각했던 것들은 filter를 사용

IN [11]: Genre.objects.filter(name = "락")

IN [12]: genre.name = '인디음악' #변수저장

IN [13]: genre.save()#변수의 값이 바뀌면 저장해줘야한다.

  
IN [14]: genre.delete() #genre 객채 삭제 메서드 호출!! delete는 바로 반영된다.
IN [15]: genre = Genre.objects.get(id = 1)
IN [16]: genre.delete()
```

- Artist 모델 생성

```python
class Artist(models.Model):
  name = models.CharField(max_length. = 30)
  debut = models.DateField()
  
$ python manage.py makemigrations
$ python manage.py migrate

import datetime
#1. Artist 생성
artist = Artist()
artist.name = "아이유"
#2021년 12월 1일
import datetime

artist.debut = datetime.date(2021, 12, 1)
artist.save()

$python manage.py shell_plus
""
import datetime
#1. Artist 생성
artist = Artist()
artist.name = "아이유"
#2021년 12월 1일
#꼭 date객체타입을 쓰지 않아도 돼
artist.debut = datetime.date(2021, 12, 1)
artist.save()
""
In [6] = ive = Artist.objects.get(id = 1)
In [7] = ive.debut



artist = Artist()
artist.name = "아이유"
#2021년 12월 1일
#꼭 date객체타입을 쓰지 않아도 돼
#이렇게 입력해도 date타입 객체로 받아준다.
artist.debut = '2019-12-26'
artist.save()
```

- Read

```python
# 1. 전체 데이터 조회
Genre.objects.all()
# <QuerySet [<Genre: Genre object (1)>, <Genre: Genre object (2)>]>

# 2.일부 데이터 조회(get)
Genre.objects.get(id = 1)
# <Genre: Genre object (1)>

#3.일부 데이터 조회(filter)
Genre.objects.filter(id = 1)
# <Query set [<Genre: Genre object (1)>]>
```

- Update

```python
# 1. genre 객체 활용
genre = Genre.objects.get(id = 1)

# 2. genre 객체 속성 변경
genre.name = '트로트'

# 3. genre 객체 저장
genre.save()
```

- Delete

```python
#1.genre 객체 활용
genre = Genre.objects.get(id=1)

#2.genre 객체 삭제
genre.delete()
```



- 데이터베이스 조작(Database API)

  Genre(Class Name).objects(Manager).all()(QuerySet API)