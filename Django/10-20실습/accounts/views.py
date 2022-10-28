from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from articles.models import Article, Comment
from django.contrib.auth import get_user_model

# Create your views here.
def index(request, user_pk):
    user1 = get_user_model().objects.get(pk=user_pk)
    # 앞의 유저는 필드명 = 내가 변수에 선언한 유저와 같니?
    articles = Article.objects.filter(user=user1)
    comments = Comment.objects.filter(user=user1)
    context = {
        "articles": articles,
        "comments": comments,
    }
    return render(request, "accounts/index.html", context)


def signout(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("articles:index")
    else:
        form = CustomUserCreationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/signout.html", context)


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get("next") or "articles:index")
    else:
        form = AuthenticationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)


def logout(request):
    auth_logout(request)
    return redirect("articles:index")
