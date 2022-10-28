### Many to many relationship

- N:1의 한계
  - 동일한 환자지만 다른 의사에게 예약하기 위해서는 객체를 하나 더 만들어서 예약을 진행해야 한다
    - 새로운 환자 객체를 생성할 수 밖에 없다
  - 외래 키 컬럼에 '1, 2' 형태로 참조하는 것은 Integer 타입이 아니기 떄문에 불가능
  - 그렇다면 "예약 테이블을 따로 만들자"

- 병원 예약 시스템 구축을 위한 데이터 베이스 모델링을 진행한다면? 
  - 한 환자가 두 의사한테 예약하는건 N대 1로 불가능하다. 
- 중개 모델
  - 환자 모델의 외래키를 삭제하고 별도의 예약 모델을 새로 작성
  - 예약 모델은 의사와 환자에 각각 N:1 관계를 가진다.
  - 데이터베이스 초기화 후 Migration 진행 및 shell_plus 실행
    - migration 파일 삭제
    - 데이터베이스 파일 삭제

- 의사와 환자 생성 후 예약 만들기

  ```python
  doctor1 = Doctor.objects.create(name="alice")
  patient1 = Patient.objects.create(name="carol")
  
  Reservation.objects.create(doctor=doctor1, patient=patient)
  ```

- 1번 의사에게 새로운 환자 예약이 생성 된다면

  ```python
  patient2 = Patient.objects.create(name="done")
  
  Reservation.objects.create(doctor=doctor1, patient=patient2)
  ```

- 환자 모델에 Django ManyToManyField 작성

  ```python
  #hospitals/models.py
  
  class Patient(models.Model):
    
    doctors = models.ManyToManyField(Doctor), related_name=patients
    name = models.TextField()
    
    def __str__(self):
      	return f"{self.pk}번 환자 {self.name}'
      
  # p1.doctors.all() #환자 1이 만난 의사들 (직접적으로 정보를 볼 수 있다.- 환자의 정보를 볼 수 있다.)
  # related_name을 사용하면 
  # doctor.patient_set.all() = > doctor.patient.all()로 사용 가능
  ```

- 데이터베이스 초기화 후 Migration 진행

- 의사 1명과 환자 2명 생성

  ```python
  doctor1 = Doctor.objects.create(name="alice")
  patient1 = Patient.objects.create(name="carol")
  patient2 = Patient.objects.create(name="dane")
  ```

- 예약 생성

  ```python
  # patient1이 doctor1에게 예약
  patient1.doctors.add(doctor1)
  
  # patient1 - 자신이 예약한 의사목록 확인
  patient1.doctors.all()
  
  # doctor1 - 자신이 예약된 환자목록 확인
  doctor1.patient_set.all()
  ```

- 예약 취소하기 (삭제)

- 기존에는 해당하는 Reservation을 찾아서 지워야 했다면, 이제는 .remove() 사용

  ```python
  # patient2가 doctor1 진료 예약 취소
  patient2.doctors.remove(doctor1)
  
  patient2.doctors.all()
  
  doctor1.patient_set.all()
  ```

- Django는 ManyToManyField를 통해 중개 테이블을 자동으로 생성한다.

- 'related_name' argument

  - Target model이 source model을 참조할 때 사용할 manager name

  - ForeignKey()의 related_name과 동일

    ```python
    class Patient(models.Model):
      	#ManyToManyField - related_name 작성
        doctors = models.ManyToManyField(Doctor, related_name="patients")
        name = models.TextField()
        
        def __str__(self):
          return f"{self.pk}"번 환자 {self.name}'
    ```

    ```python
    #에러 발생 (related_name을 설정하면 기존 _set manager는 사용할 수 없다)
    doctor1.patient_set.all()
    AttributorError: "Doctor" object has no attribute 'patient_set'
     
    #변경 후
    doctor1.patients.all()
    ```

  

  

  - 'through' argument

    - 그렇다면 중개 모델을 직접 작성하는 경우는 없을까?
      - 중개 테이블을 수동으로 지정하려는 경우 through 옵션을 사용하여 사용하려는 중개 테이블을 나타내는 Django 모델을 지정 가능
    - 가장 일반적인 용도는 중개테이블에 추가 데이터를 사용해 다대다 관계와 연결하려는 경우
    - 추가 모델을 작성할때 사용한다.

    ```python
    #외래키 삭제 
    Class Patient(models.Model):
      	#through를 사용하면 환자 입장에서 의사를 찾을때 reservation을 통해서 가져온다.
        # patient.reservation_set.all() #예약들
        # patient.doctors.all() #의사정보들
      	doctors = models.ManyTomanyField(Doctor, through="Reservation")
      	name = models.TextField()
        
        def __str__(self):
          return f "{self.pk}번 환자 {self.name}"
     
    #중개모델 작성
    class Reservation(models.Model):
      	doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE )
        patient = models.ForeignKey(Patient, on_delete=models.CASCADE )
        #새로운 모델을 만들때 중개모델을 만들어서 가고 through를 사용한다.
        symptom = models.TextField()
        reserved_at = models.DateTimeField(auto_now_add=True)
        
        def __str__(self):
          	return f"{self.doctor.pk}번 의사의 {self.patient.pk}번 환자"
    
    
    # patient.reservation_set.all() #예약들
    # patient.doctors.all() #의사들 
    ```

    

  ### ManyToManyField

  - 다대다 관계 설정 시 사용하는 모델 필드

  - 하나의 필수 위치인자(M:N 관계로 설정할 모델 클래스)가 필요

  - 모델 필드의 RelatedManger를 사용하여 관련 개체를 추가, 제거 또는 만들 수 있다

    - add(), remove(), create(), clear() ...

  - 데이터베이스에서의 표현

    - Django는 다대다 관계를 나타내는 중개 테이블을 만든다
    - 테이블 이름은 ManyToManyField 이름과 이를 포함하는 모델의 테이블 이름을 조합하여 생성된다
    - 'db_table' arguments를 사용하여 중개 테이블의 이름을 변경할 수도 있다

  - ManyTomanyField's Arguments

    - related_name

      - target model이 source model을 참조할 떄 사용할 manager name
      - ForeignKey의 related_name 동일

    - through

      - 중개 테이블을 직접 작성하는 경우, through 옵션을 사용하여 중개 테이블을 나타내는 Django 모델을 지정
      - 일반적으로 중개 테이블에 추가 데이터를 사용하는 다대다 관계와 연결하려는 경우에 사용된다.

    - symmetircal 

      - 기본 값 : True
      - ManyToManyField가 동일한 모델(on self)을 가리키는 정의에서만 사용

      ```python
      #예시
      
      class Person(models.Model):
        	friends = models.ManyToManyField('self')
          # friends = models.ManyToManyField('self', symmetrical=False)
      ```

      - True일 경우
        - _set 매니저를 추가 하지 않는다
        - Source 모델의 인스턴스가 target 모델의 인스턴스를 참조하면 자동으로 target 모델 인스턴스도 source 모델 인스턴스를 자동으로 참조하도록 함(대칭)
        - 즉 내가 당신의 친구라면 당신도 내 친구가 된다.
      - 대칭을 원하지 않는 경우 False로 설정
        - Follow 기능 구현에서 다시 확인할 예정

    - Related Manager

      - N:1 혹은 M:N 관계에서 사용 가능한 문맥(context)
      - Django는 모델 간 N:1 혹은 M:N 관계가 설정되면 역참조시에 사용할 수 있는 manager를 생성
        - 우리가 이전에 모델 생성 시 objects라는 매니저를 통해 queryset api를 사용했던 것처럼 related manager를 통해 queryset api를 사용할 수 있게 된다.
      - 같은 이름의 메서드여도 각 관계(N:1, M:N)에 따라 다르게 사용 및 동작됨
        - N:1에서는 target 모델 객체만 사용 가능
        - M:N 관계에서는 관련된 두 객체에서 모두 사용 가능 
      - 메서드 종류
        - add(), remove(), create(), clear(), set() 등 

    - methods 

      - add()
        - "지정된 객체를 관련 객체 집합에 추가"
        - 이미 존재하는 관계에 사용하면 관계가 복제되지 않는다
        - 모델 인스턴스, 필드 값(PK)을 인자로 허용
      - remove()
        - "관련 객체 집합에서 지정된 모델 개체를 제거"
        - 내부적으로 QuerySet.delete()를 사용하여 관계가 삭제된다
        - 모델 인스턴스, 필드 값(PK)을 인자로 허용한다. 

    - 중개 테이블 필드 생성 규칙

      - 소스 및 대상 모델이 다른 경우
        - id
        - <containing_model>_id
        - <other_model>_id
      - ManyToManyField가 동일한 모델을 가리키는 경우
        - id
        - from_`<model>`_ _id
        - to_`<model>` _id

    

    

  ### Like 

  - ManyToManyField 작성

    ```python
    # articles/models.py
    
    class Article(models.Model):
        title = models.CharField(max_length=10)
        content = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
        user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_articles")
    ```

  - 마이그레이션 진행

  - 모델 관계 설정

    - like_users 필드 생성 시 자동으로 역참조에는 .article_set 매니저가 생성된다
    - 그러나 이전 N:1(Article-User)관계에서 이미 해당 매니저를 사용 중
      - user.article_set.all() -> 해당 유저가 작성한 모든 게시글 조회
      - user가 작성한 글들(user.article_set)과 user가 좋아요를 누른 글(user.article_set)을 구분할 수 없게 된다.
    - user와 연계된 ForeignKey 혹은 ManyToManyField 중 하나에 related_name을 작성해야 한다.

    - User - Article간 사용 가능한 related manager 정리
      - article.user
        - 게시글을 작성한 유저 - N:1
      - user.article_set
        - 유저가 작성한 게시글(역참조) - N:1
      - article.like_users
        - 게시글을 좋아요한 유저 - M:N 
      - user.like_articles
        - 유저가 좋아요한 게시글(역참조) - M:N

    ```python
    # articles/urls.py
    urlpattern = [
      ...
      path('<int:article_pk>/likes/', views.likes, name="likes"),
    ]
    
    # articles/views.py
    def likes(request, article_pk):
      	article = Article.objects.get(pk=article_pk)
        
        if article.like_users.filter(pk=request.user.pk).exists():
          # if request.user in article.like_users.all():
          	article.like_users.remove(request.user)
        else:
          	article.like_users.add(request.user)
        return redirect('articles:index')
    ```

    - .exists()
      - QuerySet에 결과가 포함되어 있으면 True를 반환하고 그렇지 않으면 False를 반환
      - 특히 큰 QuerySet에 있는 특정 개체의 존재와 관련된 검색에 유용

  - `AUTH_USER_MODEL` 는 외래키 모델을 전달할 때 문자열로 전달합니다. 외래키가 임포트될 때 모델 클래스 탐색에 실패하면 모든 앱이 로드될 때까지 실제 모델 클래스의 탐색을 미룹니다. 그렇기 때문에 항상 올바른 사용자 모델을 얻을 수 있습니다.

  ```html
  <div>
    {% if request.user.is_authenticated %}
    <form action="{% url 'articles:likes' article.pk %}" method="POST">
      {% csrf_token %}
      {% if request.user in article.like_users.all %}
      	<input type="submit" value="좋아요 취소">
      {% else %}
      	<input type="submit" value="좋아요">
      {% endif %}
      {{articles.like_user.count}}
    </form>
  </div>
  ```

  

  

  좋아요 기능 구현

(1) DB 좋아요 기록할 것인지..?

Article - User(N)

Article은 User에게 0개 이상의 User에게 좋아요를 받는다.

User는 0개 이상의 글에 좋아요를 누를 수 있다.

(2) 로직

상세보기 페이지에서 좋아요 링크를  누르면, (URL : /articles/`<int:pk>`/like) 앗! user정보는 request.user에서 가져다 쓸 예정 (로그인 해야해)

좋아요를 DB에 추가하고 다시 상세보기 페이지로 redirect!!





```python
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = ProcessedImageField(upload_to='images/', blank=True,
                                processors=[ResizeToFill(1200, 960)],
                                format='JPEG',
                                options={'quality': 80})
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL)

#같은 모델을 참조하는 상황에서 related_name을 정해야한다.
```

get vs filter 

get은 하나의 객체를 확인할 때 사용한다. 없으면 오류, 많아도 오류

get은 가지고 오더라도 그 객체



filter은 뭐다?

쿼리셋이다 무조건 0, 1 많이  겟은 직접주고 필터는 박스에 담아서줘요

