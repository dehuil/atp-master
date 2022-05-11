'''
相关功能：流程接口，流程接口步骤的增删改查
'''
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import JsonResponse
from web.models import Product, ApiTest, ApiStep


# 流程接口列表
def api_test_manage(request):
    api_t_list = ApiTest.objects.all().order_by('id')

    paginator = Paginator(api_t_list, 10)
    # 获取page的值，如果没有，则设置使用默认值1
    page = request.GET.get('page', 1)
    # 获取第几页
    api_t_lists = paginator.page(page)

    data = {
        'api_test': api_t_lists,
    }
    return render(request, 'api_test/api_test_manage.html', context=data)


# 流程接口添加
def api_test_add(request):
    pro_names = Product.objects.all()

    if request.method == "GET":
        data = {
            'pro_names': pro_names,
        }
        return render(request, 'api_test/api_test_add.html', context=data)
    elif request.method == "POST":
        api_t_product = request.POST.get('dropdown')
        api_t_name = request.POST.get('api_t_name')
        api_t_desc = request.POST.get('api_t_desc')
        api_ter = request.POST.get('api_ter')
        api_t_status = request.POST.get('api_t_status')

        if api_t_name == "":
            return JsonResponse({'code': 202})

        ApiTest.objects.create(
            api_t_name=api_t_name,
            api_t_desc=api_t_desc,
            api_ter=api_ter,
            api_t_status=api_t_status,
            api_t_product_id=api_t_product,
        )
        return JsonResponse({'code': 200})
    return JsonResponse({'code': 201})


# 流程接口删除
def api_test_delete(request):
    api_t_id = request.GET.get('api_t_id')
    try:
        api_t_obj = ApiTest.objects.get(id=api_t_id)
        api_t_obj.delete()
        return JsonResponse({'code': 200})
    except Exception as e:
        print(e)
        return JsonResponse({'code': 201})


# 流程接口编辑
def api_test_update(request, api_t_id):
    pro_names = Product.objects.all()
    api_test = ApiTest.objects.get(id=api_t_id)

    if request.method == "GET":
        data = {
            'pro_names': pro_names,
            'api_test': api_test,
        }
        return render(request, 'api_test/api_test_update.html', context=data)
    elif request.method == "POST":
        api_t_product = request.POST.get('dropdown')
        api_t_name = request.POST.get('api_t_name')
        api_t_desc = request.POST.get('api_t_desc')
        api_ter = request.POST.get('api_ter')
        api_t_status = request.POST.get('api_t_status')

        if api_t_name == "":
            return JsonResponse({'code': 202})

        ApiTest.objects.filter(id=api_t_id).update(
            api_t_name=api_t_name,
            api_t_desc=api_t_desc,
            api_ter=api_ter,
            api_t_status=api_t_status,
            api_t_product_id=api_t_product,
        )
        return JsonResponse({'code': 200})
    return JsonResponse({'code': 201})


# 流程接口搜索
def api_test_search(request):
    search_name = request.GET.get('api_t_name')
    api_t_list = ApiTest.objects.filter(api_t_name__icontains=search_name)

    paginator = Paginator(api_t_list, 10)
    # 获取page的值，如果没有，则设置使用默认值1
    page = request.GET.get('page', 1)
    # 获取第几页
    api_t_lists = paginator.page(page)

    data = {
        "api_test": api_t_lists,
    }
    return render(request, 'api_test/api_test_manage.html', context=data)


# 流程接口步骤列表
def api_step_manage(request, api_t_id):
    api_steps = ApiStep.objects.all()
    data = {
        'api_t_id': api_t_id,
        'api_steps': api_steps,
    }

    return render(request, 'api_test/api_step_manage.html', context=data)


# 流程接口步骤添加
def api_step_add(request, api_t_id):
    api_tests = ApiTest.objects.all()

    if request.method == "GET":
        data = {
            'api_t_id': api_t_id,
            'api_tests': api_tests,
        }
        return render(request, 'api_test/api_step_add.html', context=data)
    elif request.method == "POST":
        api_test_id = request.POST.get('dropdown')
        api_s_step = request.POST.get('api_step')
        api_s_name = request.POST.get('api_name')
        api_s_url = request.POST.get('api_url')
        api_s_param_value = request.POST.get('api_param_value')
        api_s_method = request.POST.get('method_check')
        api_s_result = request.POST.get('api_result')
        api_s_status = request.POST.get('api_s_status')

        if api_s_name == "":
            return JsonResponse({'code': 202})

        ApiStep.objects.create(
            api_s_step=api_s_step,
            api_s_name=api_s_name,
            api_s_url=api_s_url,
            api_s_param_value=api_s_param_value,
            api_s_method=api_s_method,
            api_s_result=api_s_result,
            api_s_status=api_s_status,
            api_test_id=api_test_id,
        )
        return JsonResponse({'code': 200})
    return JsonResponse({'code': 201})


# 流程接口步骤删除
def api_step_delete(request):
    api_s_id = request.GET.get('api_s_id')
    try:
        api_s_obj = ApiStep.objects.get(id=api_s_id)
        api_s_obj.delete()
        return JsonResponse({'code': 200})
    except Exception as e:
        print(e)
        return JsonResponse({'code': 201})


# 流程接口步骤修改
def api_step_update(request, api_t_id, api_s_id):
    api_tests = ApiTest.objects.all()
    api_s_obj = ApiStep.objects.get(id=api_s_id)

    if request.method == "GET":
        data = {
            'api_s_id': api_s_id,
            'api_t_id': api_t_id,
            'api_tests': api_tests,
            'api_step': api_s_obj
        }
        return render(request, 'api_test/api_step_update.html', context=data)
    elif request.method == "POST":
        api_test_id = request.POST.get('dropdown')
        api_s_step = request.POST.get('api_step')
        api_s_name = request.POST.get('api_name')
        api_s_url = request.POST.get('api_url')
        api_s_param_value = request.POST.get('api_param_value')
        api_s_method = request.POST.get('method_check')
        api_s_result = request.POST.get('api_result')
        api_s_status = request.POST.get('api_s_status')

        if api_s_name == "":
            return JsonResponse({'code': 202})

        ApiStep.objects.filter(id=api_s_id).update(
            api_s_step=api_s_step,
            api_s_name=api_s_name,
            api_s_url=api_s_url,
            api_s_param_value=api_s_param_value,
            api_s_method=api_s_method,
            api_s_result=api_s_result,
            api_s_status=api_s_status,
            api_test_id=api_test_id,
        )
        return JsonResponse({'code': 200})
    return JsonResponse({'code': 201})
