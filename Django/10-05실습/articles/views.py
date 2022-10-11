from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.

# 보이는 페이지
def index(request):
    # 입력 데이터를 받아와야 한다.
    articles = Article.objects.order_by("pk")
    context = {"articles": articles}
    return render(request, "articles/index.html", context)


# 생성 함수
def create(request):
    # 만약 요청 방법이 post라면
    if request.method == "request":
        # 유효성 검사
        articleForm = ArticleForm(request.POST)
        if articleForm.is_valid():
            # 저장
            articleForm.save()
            return redirect("articles:index")
    else:
        articleForm = ArticleForm()

    context = {"articleForm": articleForm}

    return render(request, "articles/new.html", context=context)


# 삭제
def delete(request, pk):
    Article.objects.get(id=pk).delete()

    return redirect("articles:index")


# 상세보기
def detail(request, pk):
    article = Article.objects.get(pk=pk)

    context = {"article": article}

    return render(request, "articles/detail.html", context)


# 업데이트하기
def update(request, pk):
    article = Article.objects.get(id=pk)
    # POST이면?
    if request.method == "POST":
        # 유효성 체크
        articleForm = ArticleForm(request.POST, instance=article)
        if articleForm.is_valid():
            articleForm.save()
            # 해당 글로 가야해
            return redirect("article:detail", article.pk)
    # GET이면?
    else:
        articleForm = ArticleForm(instance=article)
    context = {"articleForm": articleForm}
    return render(request, "articles/update.html", context)
