'''
相关功能：Web测试用例和用例步骤的增删改查
'''
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import JsonResponse
from web.models import Product, WebTest, WebTestStep


# Web测试用例列表
def web_test_manage(request):
    web_tests = WebTest.objects.all().order_by('id')

    paginator = Paginator(web_tests, 10)
    # 获取page的值，如果没有，则设置使用默认值1
    page = request.GET.get('page', 1)
    # 获取第几页
    page_object = paginator.page(page)

    data = {
        'web_tests': page_object,
    }
    return render(request, 'web_test/web_test_manage.html', context=data)


# 添加Web测试用例
def web_test_add(request):
    pro_names = Product.objects.all()

    if request.method == "GET":
        data = {
            'pro_names': pro_names,
        }
        return render(request, 'web_test/web_test_add.html', context=data)
    elif request.method == "POST":
        web_product = request.POST.get('dropdown')
        web_t_name = request.POST.get('web_t_name')
        web_t_desc = request.POST.get('web_t_desc')
        web_ter = request.POST.get('web_ter')
        web_t_res = request.POST.get('web_t_res')

        if web_t_name == "":
            return JsonResponse({'code': 202})

        WebTest.objects.create(
            web_t_name=web_t_name,
            web_t_desc=web_t_desc,
            web_ter=web_ter,
            web_t_res=web_t_res,
            web_t_pro_id=web_product,
        )
        return JsonResponse({'code': 200})
    return JsonResponse({'code': 201})


# 删除Web测试用例
def web_test_delete(request):
    web_t_id = request.GET.get('web_t_id')
    try:
        web_t_obj = WebTest.objects.get(id=web_t_id)
        web_t_obj.delete()
        return JsonResponse({'code': 200})
    except Exception as e:
        print(e)
        return JsonResponse({'code': 201})


# 编辑Web测试用例
def web_test_update(request, web_t_id):
    pro_names = Product.objects.all()
    web_test = WebTest.objects.get(id=web_t_id)

    if request.method == "GET":
        data = {
            'pro_names': pro_names,
            'web_test': web_test,
        }
        return render(request, 'web_test/web_test_update.html', context=data)
    elif request.method == "POST":
        web_product = request.POST.get('dropdown')
        web_t_name = request.POST.get('web_t_name')
        web_t_desc = request.POST.get('web_t_desc')
        web_ter = request.POST.get('web_ter')
        web_t_res = request.POST.get('web_t_res')

        if web_t_name == "":
            return JsonResponse({'code': 202})

        WebTest.objects.filter(id=web_t_id).update(
            web_t_name=web_t_name,
            web_t_desc=web_t_desc,
            web_ter=web_ter,
            web_t_res=web_t_res,
            web_t_pro_id=web_product
        )
        return JsonResponse({'code': 200})
    return JsonResponse({'code': 201})


# 搜索Web测试用例
def web_test_search(request):
    search_name = request.GET.get('web_t_name')
    web_t_list = WebTest.objects.filter(web_t_name__icontains=search_name)

    paginator = Paginator(web_t_list, 10)
    # 获取page的值，如果没有，则设置使用默认值1
    page = request.GET.get('page', 1)
    # 获取第几页
    web_lists = paginator.page(page)

    data = {
        "web_tests": web_lists,
    }
    return render(request, 'web_test/web_test_manage.html', context=data)


# Web测试用例步骤列表
def web_step_manage(request, web_t_id):
    web_steps = WebTestStep.objects.all()

    data = {
        'web_t_id': web_t_id,
        'web_steps': web_steps,
    }
    return render(request, 'web_test/web_step_manage.html', context=data)


# 添加Web测试用例步骤
def web_step_add(request, web_t_id):
    web_test = WebTest.objects.all()

    if request.method == "GET":
        data = {
            'web_t_id': web_t_id,
            'web_test': web_test,
        }
        return render(request, 'web_test/web_step_add.html', context=data)
    elif request.method == "POST":
        web_test_id = request.POST.get('dropdown')
        web_step = request.POST.get('web_step')
        web_find_method = request.POST.get('web_find_method')
        web_element = request.POST.get('web_element')
        web_opt_method = request.POST.get('web_opt_method')
        web_test_data = request.POST.get('web_test_data')
        web_assert_data = request.POST.get('web_assert_data')
        web_result = request.POST.get('web_result')

        if web_step == "":
            return JsonResponse({'code': 202})

        WebTestStep.objects.create(
            web_step=web_step,
            web_find_method=web_find_method,
            web_element=web_element,
            web_opt_method=web_opt_method,
            web_test_data=web_test_data,
            web_assert_data=web_assert_data,
            web_result=web_result,
            web_test_id=web_test_id,
        )
        return JsonResponse({'code': 200})
    return JsonResponse({'code': 201})


# 删除Web测试用例步骤
def web_step_delete(request):
    web_s_id = request.GET.get('web_s_id')
    try:
        web_s_obj = WebTestStep.objects.get(id=web_s_id)
        web_s_obj.delete()
        return JsonResponse({'code': 200})
    except Exception as e:
        print(e)
        return JsonResponse({'code': 201})


# 编辑Web测试用例步骤
def web_step_update(request, web_t_id, web_s_id):
    web_tests = WebTest.objects.all()
    web_s_obj = WebTestStep.objects.get(id=web_s_id)

    if request.method == "GET":
        data = {
            'web_s_id': web_s_id,
            'web_t_id': web_t_id,
            'web_tests': web_tests,
            'web_step': web_s_obj
        }
        return render(request, 'web_test/web_step_update.html', context=data)
    elif request.method == "POST":
        web_test_id = request.POST.get('dropdown')
        web_step = request.POST.get('web_step')
        web_find_method = request.POST.get('web_find_method')
        web_element = request.POST.get('web_element')
        web_opt_method = request.POST.get('web_opt_method')
        web_test_data = request.POST.get('web_test_data')
        web_assert_data = request.POST.get('web_assert_data')
        web_result = request.POST.get('web_result')

        if web_step == "":
            return JsonResponse({'code': 202})

        WebTestStep.objects.filter(id=web_s_id).update(
            web_step=web_step,
            web_find_method=web_find_method,
            web_element=web_element,
            web_opt_method=web_opt_method,
            web_test_data=web_test_data,
            web_assert_data=web_assert_data,
            web_result=web_result,
            web_test_id=web_test_id
        )
        return JsonResponse({'code': 200})
    return JsonResponse({'code': 201})
