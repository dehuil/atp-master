'''
相关功能：注册，登陆
'''
from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
from django.shortcuts import render, redirect
from web.models import UserInfo


# 登录
def login(request):
    if request.method == "GET":
        return render(request, 'account/login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = UserInfo.objects.filter(username=username).first()

        if user_obj:
            if check_password(password, user_obj.password):
                request.session['user_id'] = user_obj.id

                return JsonResponse({'code': 200})
            else:
                return JsonResponse({'code': 201})
        return JsonResponse({'code': 201})


# 注册
def register(request):
    if request.method == "GET":
        return render(request, 'account/register.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = UserInfo.objects.filter(username=username)

        if user.exists():
            return JsonResponse({'code': 201})
        elif username == "" or password == "":
            return JsonResponse({'code': 202})
        else:
            password = make_password(password)

            UserInfo.objects.create(
                username=username,
                password=password,
            )
            return JsonResponse({'code': 200})