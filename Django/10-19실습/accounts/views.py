from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from articles.models import Article
from django.contrib.auth import get_user_model

# Create your views here.
def index(request, user_pk):
    user = get_user_model().objects.get(pk=user_pk)
    articles = Article.objects.filter(user=user)
    context = {
        "articles": articles,
        "user": user,
    }
    return render(request, "accounts/index.html", context)


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # 세션 저장 유저정보를 form(request, user)으로 부터 가져온다.
            auth_login(request, form.get_user())
            return redirect(request.GET.get("next") or "accounts:index")
    else:
        form = AuthenticationForm()
    context = {
        "form": form,
    }

    return render(request, "accounts/login.html", context)


def logout(request):
    auth_logout(request)
    return redirect("accounts:index")
