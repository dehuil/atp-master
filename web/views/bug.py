'''
相关功能：Bug管理页面的增删改查功能
'''
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render
from web.models import Product, Bug


# Bug管理页面
def bug_manage(request):
    bugs = Bug.objects.all().order_by('id')

    paginator = Paginator(bugs, 10)
    # 获取page的值，如果没有，则设置使用默认值1
    page = request.GET.get('page', 1)
    # 获取第几页
    page_object = paginator.page(page)

    data = {
        'bugs': page_object,
    }
    return render(request, 'bug/bug_manage.html', context=data)


# 添加Bug
def bug_add(request):
    pro_names = Product.objects.all()

    if request.method == "GET":
        data = {
            'pro_names': pro_names,
        }
        return render(request, 'bug/bug_add.html', context=data)
    elif request.method == "POST":
        bug_product = request.POST.get('dropdown')
        bug_name = request.POST.get('bug_name')
        bug_detail = request.POST.get('bug_detail')
        bug_level = request.POST.get('bug_level')
        bug_status = request.POST.get('bug_status')
        bug_creat_er = request.POST.get('bug_creat_er')
        bug_assign = request.POST.get('bug_assign')

        if bug_name == "":
            return JsonResponse({'code': 202})

        Bug.objects.create(
            bug_name=bug_name,
            bug_detail=bug_detail,
            bug_level=bug_level,
            bug_status=bug_status,
            bug_creat_er=bug_creat_er,
            bug_assign=bug_assign,
            bug_pro_id=bug_product
        )
        return JsonResponse({'code': 200})
    return JsonResponse({'code': 201})


# 删除Bug
def bug_delete(request):
    bug_id = request.GET.get('bug_id')
    try:
        bug_obj = Bug.objects.get(id=bug_id)
        bug_obj.delete()
        return JsonResponse({'code': 200})
    except Exception as e:
        print(e)
        return JsonResponse({'code': 201})


# 编辑Bug
def bug_update(request, bug_id):
    pro_names = Product.objects.all()
    bug = Bug.objects.get(id=bug_id)

    if request.method == "GET":
        data = {
            'pro_names': pro_names,
            'bug': bug,
        }
        return render(request, 'bug/bug_update.html', context=data)
    elif request.method == "POST":
        bug_product = request.POST.get('dropdown')
        bug_name = request.POST.get('bug_name')
        bug_detail = request.POST.get('bug_detail')
        bug_level = request.POST.get('bug_level')
        bug_status = request.POST.get('bug_status')
        bug_creat_er = request.POST.get('bug_creat_er')
        bug_assign = request.POST.get('bug_assign')

        if bug_name == "":
            return JsonResponse({'code': 202})

        Bug.objects.filter(id=bug_id).update(
            bug_name=bug_name,
            bug_detail=bug_detail,
            bug_level=bug_level,
            bug_status=bug_status,
            bug_creat_er=bug_creat_er,
            bug_assign=bug_assign,
            bug_pro_id=bug_product,
        )
        return JsonResponse({'code': 200})
    return JsonResponse({'code': 201})


# 搜索Bug
def bug_search(request):
    search_name = request.GET.get('bug_name')
    bug_list = Bug.objects.filter(bug_name__icontains=search_name)

    paginator = Paginator(bug_list, 10)
    # 获取page的值，如果没有，则设置使用默认值1
    page = request.GET.get('page', 1)
    # 获取第几页
    bug_lists = paginator.page(page)

    data = {
        "bugs": bug_lists,
    }
    return render(request, 'bug/bug_manage.html', context=data)
