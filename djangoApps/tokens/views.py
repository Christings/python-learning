from django.shortcuts import render, redirect, HttpResponse
from .models import Administrator
from rest_framework.views import APIView


def login(request):
    message = ""
    if request.method == "POST":
        request.session['is_login'] = True
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        c = Administrator.objects.filter(username=user, password=pwd).count()
        if c:
            request.session['is_login'] = True
            request.session['username'] = user
            rep = redirect('/index.html')
            return rep
        else:
            message = "用户名或密码错误"
    return render(request, 'tokens/login.html', {'msg': message})


def auth(func):
    def inner(request, *args, **kwargs):
        is_login = request.session.get('is_login')
        if is_login:
            return func(request, *args, **kwargs)
        else:
            return redirect('/login.html')

    return inner


@auth
def index(request):
    # 如果用户已经登录，获取当前登录的用户名
    # 否则，返回登录页面
    username = request.session.get('username')
    c = Administrator.objects.filter(username=username).count()
    if c:
        return render(request, 'tokens/index.html', {'username': username})
    else:
        return redirect('/login.html')


def logout(request):
    request.session.clear()
    return redirect('/login.html')


class IndexView(APIView):
    # authentication_classes = []
    # permission_classes = []
    def get(self, request):
        return HttpResponse('首页')
