from django.shortcuts import render, redirect
from shortener.models import User

# Create your views here.


def index(request):
    user = User.objects.filter(username="admin").first()
    email = user.email if user else "Annoymous User"
    print(email)
    print(request.user.is_authenticated)
    if request.user.is_authenticated is False:
        email = "Annoymous User"
    print(email)
    # render(request, 템플릿, 템플릿 내 변수)
    return render(request, "base.html", {"welcome_msg": "Hello, World!"})


def redirect_test(request):
    print("Go Redirect")
    # 이곳에서 명시하는 index는 urls.py에 있는 이름
    return redirect("index")
