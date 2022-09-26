from django.shortcuts import render
import random
from lorem_text import lorem

# Create your views here.


def index(request):

    return render(request, "index.html")


def ping(request):

    return render(request, "ping.html")


def pong(request):
    # print(request)
    # print(dir(request))
    # print(request.GET.get('ball'))
    # ball = request.GET.get('ball')
    # context = {
    #     'name' : ball,
    # }
    # return render(request, 'pong.html', context)
    return render(request, "pong.html", {"name": request.GET.get("ball")})


def print_number(request, _number):

    if _number % 2 == 1:
        result = "홀수"
    else:
        if _number == 0:
            result = "0"
        else:
            result = "짝수"

    context = {
        # "템플릿 변수 이름" : 값
        "number": _number,
        "result": result,
    }

    return render(request, "is-odd-even.html", context)


def calculate(request, number1, number2):
    add = number1 + number2
    minus = number1 - number2
    multiply = number1 * number2
    division = number1 // number2
    context = {
        "number1": number1,
        "number2": number2,
        "add": add,
        "minus": minus,
        "multiply": multiply,
        "division": division,
    }

    return render(request, "calculate.html", context)


def previous(request):

    return render(request, "previous.html")


def check_name(request):
    animal = ["말", "소", "강아지", "토끼", "당나귀", "닭", "얼룩말", "기린", "도룡뇽", "사자", "호랑이"]
    name_ = request.GET.get("your")
    animal = random.choice(animal)
    context = {
        "name": name_,
        "animal": animal,
    }
    return render(request, "check_name.html", context)


def grammar(request):

    return render(request, "grammar.html")


def lorem(request):
    number1 = request.GET.get("number1")
    number2 = request.GET.get("number2")

    food = ["바나나", "짜장면", "사과", "포도", "딸기"]

    foods = random.choice(food)

    lorem_ipsum = []
    for _ in range(5):
        lorem_ipsum.append(foods)

    context = {
        "number1": number1,
        "number2": number2,
        "lorem_ipsum": lorem_ipsum,
    }
    return render(request, "lorem.html", context)
