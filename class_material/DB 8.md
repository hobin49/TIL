### QuerySet API

- gt

  `Entry.ojects.filter(id__gt = 4)`

  대응되는 쿼리(같은 의미)

  `SELECT ... WHERE id > 4;`

- gte

  `Entry.objects.filter(id__gte = 4)`

  대응되는 쿼리(같은 의미)

  `SELECT ... WHERE id >= 4;`

  

  

- It, Ite

  `Entry.objects.filter(id__lt = 4)`

  `Entry.objects.filter(id__ite = 4)`

  대응되는 쿼리

  ```sql
  SELECT ... WHERE id < 4;
  SELECT ... WHERE id <= 4;
  ```

  

- in 

  `Entry.objects.filter(id__in=[1,3,4])`

  `Entry.objects.filter(headline__in = "abc")`

  대응되는 쿼리

  ```sql
  SELECT ... WHERE id IN(1, 3, 4);
  SELECT ... WHERE headline IN ('a', 'b', 'c'); 
  ```

  

  

- startswith

  `Entry.objects.filter(headline__startswith='Lennon')`

  대응되는 쿼리

  `SELECT ... WHERE headline ILIKE 'Lennon%' ; `

  - ILIKE는 대소문자 구별 안 함

  

  

  

- istratswith

  `Entry.objects.filter(headline__istartswith='Lennon')`

​		대응되는 쿼리

​		`SELECT ... WHERE headline ILIKE 'Lennon%';`

- endswith

```django
Entry.objects.filter(headline__endswith = 'Lennon')
Entry.objects.filter(headline__iendswith = 'Lennon')
```

```sql
SELECT ... WHERE headline LIKE '%Lennon';
SELECT ... WHERE headline ILIKE '%Lennon';
```



- contains(시작, 끝 contains)

```python
Entry.objects.get(headline__contains="Lennon")
Entry.objects.get(headline__icontains = "Lennon")
```

```sqlite
SELECT ... WHERE headline LIKE '%Lennon%';
SELECT ... WHERE headline ILIKE '%Lennon%';
```



- range

  ```python
  import datetime
  start_date = datetime.date(2005, 1, 1)
  end_date = datetime.date(2005, 3, 31)
  Entry.objects.filter(pub_date__range(start_date, end_date))
  ```

  ```sqlite
  SELECT ... WHERE pub_date
  BETWEEN '2005-01-01' and '2005-03-31'
  ```

  

- 복합 활용

  `inner_qs = Blog.objects.filter(name__contains = "Cheddar")`

  `entries = Entry.objects.filter(blog__in = inner_qs)`

​		대응되는 쿼리

```sql
SELECT ...
WHERE blog.id IN (SELECT id FROM ... WHERE NAME
LIKE '%Cheddar%')
```

- 활용

  `Entry.objects.all()[0] + [n:m]-슬라이싱`

  대응되는 쿼리

  ` SELECT ... LIMIT 1;`

​		`Entry.objects.order_by('-id')`  - 내림차순

​		대응되는 쿼리

​		` SELECT ORDER BY id DESC`

​		`Genre.objects.order_by('-id').query)`

​		`Genre.objects.all().query`

​		`Genre.objects.get(id=1) `-QuerySet:개별 오브젝트의 모음 그래서 오류 발생 

​		`Genre.objects.order_by('-id')[2:5].query)`



### ORM 확장(1:N)

```python
class Genre(models.Model):
  	name = models.CharField(max_length = 30)
    
class Artist(models.Model):
  	name = models.CharField(max_length = 30)
    debut = models.DateField()
    
class Album(models.Model):
  	name = models.CharField(max_length = 30)
    genre = models.ForeignKey('Genre', on_delete = models.CASCADE)
    artist = models.ForeignKey('Artist', on_delete = models.CASCADE)
```

- models.ForeignKey 필드

  - 2개의 필수 위치 인자

    - Model class:참조하는 모델
    - On_delete: 외래 키가 참조하는 객체가 삭제되었을 때 처리 방식
      - CASCADE: 부모 객체(참조 된 객체)가 삭제 됐을 떄 이를 참조하는 객체도 삭제 (댓글을 지워야 한다)
      - PROTECT : 삭제되지 않음(댓글 있으면 글 지우지 못하게)
      - SET_NULL: NULL 설정
      - SET_DEFAULT:기본 값 설정(남겨놨던 댓글을 지우지 않기 위해서 )

    ```python
    #내가 만약에 id가 1인 장르를 쓰고 싶다
    genre = Genre.objects.get(id = 1)
    album.genre = genre
    
    
    album.artist = Artist.objects.get(id = 1)
    album.artist = artist
    album.save()
    
    #값
    #테이블에 실제 필드는 _id가 붙어있기 때문에 
    album = Album()
    album.genre_id = 1
    album.artist_id = 1
    album.name = "미아"
    album.save()
    
    # N => 1(참조)
    #앨범의 id가 1인 것의 장르의 이름은?
    album.objects.get(id=1).name
    #장르의 이름은..?
    album.genre #장르 객체
    #앨범의 장르의 이름은 장르의 객체이다
    album.genre.name
    
    
    album.artist
    album.artist_id
    
    # 1=> N(역참조)
    # 클래스이름_set
    # id가 1인 장르의 모든 앨범은?
    g1 = Genre.obejects.get(id=1)
    g1.album_set.all()
    
    gl.albun_set.all().query
    ```

    - 참조

      - 앨범 입장에서 장르는 직접 참조하고 있다. 그냥 직접 쓰면 돼
      - album = Album.objects.get(1)
      - album.artist(artist의 객체(인스턴스))
      - album.genre(artist의 객체(인스턴스))

    - 역참조

      - genre = Genre.objects.get(1)
      - 별도의 설정이 없다면 항상 소문자 underbar_set의 형태를 사용한다.
      - Genre.album_set.all() **album의 인스턴스가 담긴 쿼리셋 왜냐면 1:N이기 떄문에 0개 이상의 많은 것들을 담고 있어서 한 개의 인스턴스가 올 수가 없다.**

      - 트로트인 앨범들(쿼리셋)
      - 앨범의 장르(인스턴스)
      - 뽀린키는 관계들을 만들기 위해 사용

    - create

      ```python
      artist = Artist.objects.get(1)
      genre = Genre.obejects.get(1)
      
      album = Album()
      album.name = '앨범1'
      album.artist = artist #1.객체의 저장
      album.genre = genre
      album.save
      ```

      

- 총정리
  - **ORM은 파이썬으로 db를 조작한다**
  - 테이블 생성 => 클래스정의(-makemigrations, -migrate)
  - 쿼리(sql)-CRUD