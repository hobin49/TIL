### 복습

- 클라이언트가 요청을 하면 서버가 응답한다. 서버랑 db랑 다르다. db는 sql문을 통해서 조회를 할 수 있어 
- 모델을 설계하면 쿼리셋 api를 통해 기본적인 sql을 대체해서 장고 orm을 사용하고 있었다. 

- 장고 서버에서 하는 역할 views.py 요청을 받아서 처리하며 응답. 

- 템플릿은 무슨 역할을 해? django template language- filter와 tag가 필요해 view에서 context를 가져다가 사용 가능 - html 생성

-  요청(프로토콜, path-url, method=get,post), 응답(html, status code)

- 서버는 파이썬으로 코드를 보내면 객체로 보내주는 것 쿼리셋은 (단일 객체로 이루어진 덩어리)
- 모델에서 정의한게 객체에서 다 사용 가능 
- 1:N은 User.content_set.all() 쿼리셋 comment.user 유저객체
- M:N은 user.related_name.all() 쿼리셋 -> article 객체로 이루어진
- article.like_user.all() 쿼리셋 -> 유저객체로 이루어진!
- a.B_set.all() a가 1 B(N)
- c.ds.all() C(M), N(N)
- e.f (E(N), F(1))



### M:N(User: User)

```python
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    #A가 B를 팔로잉 이 것은 서로 친구가 아니다 
    followings = models.ManyToManyField("self", symmetrical=False, related_name="followers")

    @property
    def full_name(self):
        return f'{self.last_name}{self.first_name}'
```

- 마이그레이션 진행
- From_user_id 와 to_user_id라는 테이블이 생긴다. 
- 팔로잉 기능 구현
  - 사용자 프로필 페이지에 들어가서, 
  - 팔로우 상태가 아니면, 팔로우를 누르면 추가(add)
  - 이미 팔로우 상태이면, 팔로우 취소 버튼을 누르면 삭제(remove)
  - 좋아요를 누르지 않았으면 좋아요 누르면 추가 
  - 좋아요 누른 상태이면, 좋아요 취소 버튼을 누르면 삭제  
  - 팔로우/취소 요청을 할 때 URL은 어떻게 할까요? 
  - 처리 완료 후에는 프로필 페이지로 redirect
- 추가사항
  - 셀프좋아요 허용이지만 셀프팔로우는 허용할 수 없다. (if)
- 팔로잉
  - A가 다른 B를 친구 요청(팔로잉)
  - B입장에서는 팔로워로 A가 등록된다
  - 맞팔:서로가 서로를 팔로잉 => symmetrical=False 
  - 싸이월드
    - 일촌 맺으면 서로 일촌이 된다 => symmetrical=True (1과 2가 서로 친구인 상황)



### View decorators & functions

- views는 http request를 받아서 http response를 해준다. 모델과 템플릿이 각자의 역할을 해준다.
- views.py 에서 redirect는 status코드에서 3xx render은 2xx+html 
- login required 3xx
- page not found 4xx
- 문법 오류페이지 5xx

- DoesNotExit at / articles/100(Article matching query )
  - get을 땡겨 왔는데 
- get_object_or_404 을 사용하면 사용자에게 500번 에러에서 400번에러로 유저 잘못이라고 바꿔준다. 
- object를 가져와보고 없으면 404에러 반환
- `from django.views.decorators.http import require_POST` 
- redirect는 get요청만 받는다. post로 보낸 데이터는 redirection  해주지않는다. 