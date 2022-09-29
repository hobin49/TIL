from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.

# 할 일 추가하기
def create(request):
    content = request.GET.get("content")
    priority = request.GET.get("priority")
    deadline = request.GET.get("deadline")

    Todo.objects.create(content=content, priority=priority, deadline=deadline)

    context = {
        "content": content,
        "priority": priority,
        "deadline": deadline,
    }

    return redirect("crud:read")


# 할 일 목록보기
def read(request):
    todos = Todo.objects.order_by("id")
    context = {
        "todos": todos,
    }
    return render(request, "crud/read.html", context)


# 업데이트하기
def update(request, pk_):
    todo = Todo.objects.get(pk=pk_)

    todo.completed = not todo.completed
    # 데이터 수정

    todo.save()

    return redirect("crud:read")


# 할 일 삭제하기
def delete(request, pk):
    Todo.objects.get(id=pk).delete()

    return redirect("crud:read")
