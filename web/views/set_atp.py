'''
相关功能：系统相关设置
'''
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render
from web.models import UserInfo, Set


# 公共设置列表
def set_manage(request):
    sets = Set.objects.all().order_by('id')

    paginator = Paginator(sets, 10)
    # 获取page的值，如果没有，则设置使用默认值1
    page = request.GET.get('page', 1)
    # 获取第几页
    page_object = paginator.page(page)

    data = {
        'sets': page_object,
    }
    return render(request, 'set/set_manage.html', context=data)


# 添加公共设置
def set_add(request):
    if request.method == "GET":
        return render(request, 'set/set_add.html')
    elif request.method == "POST":
        set_name = request.POST.get('set_name')
        set_value = request.POST.get('set_value')

        if set_name == "":
            return JsonResponse({'code': 202})
        else:
            Set.objects.create(
                set_name=set_name,
                set_value=set_value
            )
            return JsonResponse({'code': 200})
    return JsonResponse({'code': 201})


# 删除公共设置
def set_delete(request):
    set_id = request.GET.get('set_id')
    try:
        set_obj = Set.objects.get(id=set_id)
        set_obj.delete()
        return JsonResponse({'code': 200})
    except Exception as e:
        print(e)
        return JsonResponse({'code': 200})


# 编辑公共设置
def set_update(request, set_id):
    set_obj = Set.objects.get(id=set_id)

    if request.method == "GET":
        data = {
            'set_obj': set_obj,
        }
        return render(request, 'set/set_update.html',context=data)
    elif request.method == "POST":
        set_name = request.POST.get('set_name')
        set_value = request.POST.get('set_value')

        if set_name == "":
            return JsonResponse({'code': 202})
        else:
            Set.objects.filter(id=set_id).update(
                set_name=set_name,
                set_value=set_value
            )
            return JsonResponse({'code': 200})
    return JsonResponse({'code': 201})


# 用户列表
def set_user_manage(request):
    atp_user = UserInfo.objects.all()

    paginator = Paginator(atp_user, 10)
    # 获取page的值，如果没有，则设置使用默认值1
    page = request.GET.get('page', 1)
    # 获取第几页
    page_object = paginator.page(page)

    data = {
        'atp_user': page_object,
    }
    return render(request, 'set/set_user_manage.html', context=data)
