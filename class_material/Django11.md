### 회원정보 수정

- UserChangeForm
  - 사용자의 정보 및 권한을 변경하기 위해 admin 인터페이스에서 사용되는 ModelForm 
  - UserChangeForm 또한 ModelForm이기 때문에 instance 인자로 기존 user 데이터 정보를 받는 구조 또한 동일하다
  - 이미 이전에 CustomUserChangeForm으로 확장했기 때문에 CustomUserChangeForm을 사용하기
  - UserchangeForm 역시 ModelForm으로 구성되어 있어, User 모델 정보를 변경하여 활용해야 한다.

```python
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.decorators import login_required

class CustomUserChangeForm(UserChangeForm):
  	
    class Meta:
      	model = get_user_model()
        fields = ("first_name", "last_name", "email")
        
## views.py
@login_required(프로필 수정 페이지로 들어올 필요가 없다.)
def update(request):
  	if request.methos == "POST":
      	form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
          	form.save()
            return redirect("accounts:detail", request.user.pk)
  	#기존값을 로그인한 유저를 인스턴스로 받아와야한다. 
    else:
  		form = CustomUserChangeForm(instance=request.uesr)
    context = {
      'form' : form
    }
    return render(request, "accounts/update.html", context)
```

- 회원정보 수정 페이지 링크 작성

  ```html
  <!--base.html-->
  <div class="container">
    <a href="{% url 'accounts:signup'%}">Signup</a>
    <a href="{% url 'accounts:update'%}">회원정보 수정</a>
    <hr>
    {% block content %}
    {% endblock content %}  
    
  </div>
  ```

### 비밀번호 변경

- PasswordChangeForm
  - 사용자가 비밀번호를 변경할 수 있도록 하는 Form
  - 이전 비밀번호를 입력하여 비밀번호를 변경할 수 있도록 한다
  - 이전 비밀번호를 입력하지 않고 비밀번호를 설정할 수 있는 SetPassowrdForm을 상속받는 서브 클래스

```python
# accounts/urls.py

app_name = 'accounts'
urlpatterns = [
  
  path('password/', views.change_password, name="change_password")
]
# accounts/views.py
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm

def change_password(request):
  	if request.method == "POST":
      	form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
          	form.save()
            return redirect("accounts:index")
    else:
      	form = PasswordChangeForm(request.user)
    context = {
      "form" : form,
    }
    return render(request, 'accounts/change_password.html', context)
```



- Request.user로 유저객체를 쓰는 view함수에서는 무조건 쓰시게.. 로그인이 필요한 경우니까 login_required를 사용하자

- NoReverseMatch at
  - url을 변수화해놓은 것을 path로 변환하는 과정에서 매치되지 않았다



```python
class User(AbstractUser):
  	#호빈이 => 이호빈
    @property
    def full_name(self):
      	return f"{self.last_name}{self.first_name}"
```

- 브랜치를 나눠서 작업
- 항상 푸쉬할때 마스터에서 git add.하면 안 돼!!! 
- 반드시 브랜치로 이동해서 push 
- git checkout master 
- git checkout  -b hotfixt 
- 풀리퀘 하면서 머지 할 떄 까지 내가 하는일 한다.