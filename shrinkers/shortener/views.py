from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
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


# def redirect_test(request):
#     print("Go Redirect")
#     # 이곳에서 명시하는 index는 urls.py에 있는 이름
#     return redirect("index")


# csrf 체크를 하지 말라는 뜻
@csrf_exempt
def get_user(request, user_id):
    print(user_id)
    if request.method == "GET":
        # Query 파라미터 얻는 법
        abc = request.GET.get("abc")
        xyz = request.GET.get("xyz")
        user = User.objects.filter(pk=user_id).first()
        return render(request, "base.html", {"user": user, "params": [abc, xyz]})
    elif request.method == "POST":
        username = request.GET.get("username")
        if username:
            user = User.objects.filter(pk=user_id).update(username=username)

        return JsonResponse(
            status=201, data=dict(msg="You just reached with Post Method!")
        )
