'''
相关功能：App测试用例和用例步骤的增删改查
'''
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import JsonResponse
from web.models import Product, AppTest, AppTestStep


# App测试用例列表
def app_test_manage(request):
    app_tests = AppTest.objects.all().order_by('id')

    paginator = Paginator(app_tests, 10)
    # 获取page的值，如果没有，则设置使用默认值1
    page = request.GET.get('page', 1)
    # 获取第几页
    page_object = paginator.page(page)

    data = {
        'app_tests': page_object,
    }
    return render(request, 'app_test/app_test_manage.html', context=data)


# 添加App测试用例
def app_test_add(request):
    pro_names = Product.objects.all()

    if request.method == "GET":
        data = {
            'pro_names': pro_names,
        }
        return render(request, 'app_test/app_test_add.html', context=data)
    elif request.method == "POST":
        app_product = request.POST.get('dropdown')
        app_t_name = request.POST.get('app_t_name')
        app_t_desc = request.POST.get('app_t_desc')
        app_ter = request.POST.get('app_ter')
        app_t_res = request.POST.get('app_t_res')

        if app_t_name == "":
            return JsonResponse({'code': 202})

        AppTest.objects.create(
            app_t_name=app_t_name,
            app_t_desc=app_t_desc,
            app_ter=app_ter,
            app_t_res=app_t_res,
            app_t_pro_id=app_product,
        )
        return JsonResponse({'code': 200})
    return JsonResponse({'code': 201})


# 删除App测试用例
def app_test_delete(request):
    app_t_id = request.GET.get('app_t_id')
    try:
        app_t_obj = AppTest.objects.get(id=app_t_id)
        app_t_obj.delete()
        return JsonResponse({'code': 200})
    except Exception as e:
        print(e)
        return JsonResponse({'code': 201})


# 编辑App测试用例
def app_test_update(request, app_t_id):
    pro_names = Product.objects.all()
    app_test = AppTest.objects.get(id=app_t_id)

    if request.method == "GET":
        data = {
            'pro_names': pro_names,
            'app_test': app_test,
        }
        return render(request, 'app_test/app_test_update.html', context=data)
    elif request.method == "POST":
        app_product = request.POST.get('dropdown')
        app_t_name = request.POST.get('app_t_name')
        app_t_desc = request.POST.get('app_t_desc')
        app_ter = request.POST.get('app_ter')
        app_t_res = request.POST.get('app_t_res')

        if app_t_name == "":
            return JsonResponse({'code': 202})

        AppTest.objects.filter(id=app_t_id).update(
            app_t_name=app_t_name,
            app_t_desc=app_t_desc,
            app_ter=app_ter,
            app_t_res=app_t_res,
            app_t_pro_id=app_product
        )
        return JsonResponse({'code': 200})
    return JsonResponse({'code': 201})


# 搜索App测试用例
def app_test_search(request):
    search_name = request.GET.get('app_t_name')
    app_t_list = AppTest.objects.filter(app_t_name__icontains=search_name)

    paginator = Paginator(app_t_list, 10)
    # 获取page的值，如果没有，则设置使用默认值1
    page = request.GET.get('page', 1)
    # 获取第几页
    app_lists = paginator.page(page)

    data = {
        "app_tests": app_lists,
    }
    return render(request, 'app_test/app_test_manage.html', context=data)


# App测试用例步骤列表
def app_step_manage(request, app_t_id):
    app_steps = AppTestStep.objects.all()
    data = {
        'app_t_id': app_t_id,
        'app_steps': app_steps,
    }

    return render(request, 'app_test/app_step_manage.html', context=data)


# 添加App测试用例步骤
def app_step_add(request, app_t_id):
    app_test = AppTest.objects.all()

    if request.method == "GET":
        data = {
            'app_t_id': app_t_id,
            'app_test': app_test,
        }
        return render(request, 'app_test/app_step_add.html', context=data)
    elif request.method == "POST":
        app_test_id = request.POST.get('dropdown')
        app_step = request.POST.get('app_step')
        app_find_method = request.POST.get('app_find_method')
        app_element = request.POST.get('app_element')
        app_opt_method = request.POST.get('app_opt_method')
        app_test_data = request.POST.get('app_test_data')
        app_assert_data = request.POST.get('app_assert_data')
        app_result = request.POST.get('app_result')

        if app_step == "":
            return JsonResponse({'code': 202})

        AppTestStep.objects.create(
            app_step=app_step,
            app_find_method=app_find_method,
            app_element=app_element,
            app_opt_method=app_opt_method,
            app_test_data=app_test_data,
            app_assert_data=app_assert_data,
            app_result=app_result,
            app_test_id=app_test_id
        )
        return JsonResponse({'code': 200})
    return JsonResponse({'code': 201})


# 删除App测试用例步骤
def app_step_delete(request):
    app_s_id = request.GET.get('app_s_id')
    try:
        app_s_obj = AppTestStep.objects.get(id=app_s_id)
        app_s_obj.delete()
        return JsonResponse({'code': 200})
    except Exception as e:
        print(e)
        return JsonResponse({'code': 201})


# 编辑App测试用例步骤
def app_step_update(request, app_t_id, app_s_id):
    app_tests = AppTest.objects.all()
    app_s_obj = AppTestStep.objects.get(id=app_s_id)

    if request.method == "GET":
        data = {
            'app_t_id': app_t_id,
            'app_s_id': app_s_id,
            'app_tests': app_tests,
            'app_step': app_s_obj
        }
        return render(request, 'app_test/app_step_update.html', context=data)
    elif request.method == "POST":
        app_t_id = request.POST.get('dropdown')
        app_step = request.POST.get('app_step')
        app_find_method = request.POST.get('app_find_method')
        app_element = request.POST.get('app_element')
        app_opt_method = request.POST.get('app_opt_method')
        app_test_data = request.POST.get('app_test_data')
        app_assert_data = request.POST.get('app_assert_data')
        app_result = request.POST.get('app_result')

        if app_step == "":
            return JsonResponse({'code': 202})

        AppTestStep.objects.filter(id=app_s_id).update(
            app_step=app_step,
            app_find_method=app_find_method,
            app_element=app_element,
            app_opt_method=app_opt_method,
            app_test_data=app_test_data,
            app_assert_data=app_assert_data,
            app_result=app_result,
            app_test_id=app_t_id
        )
        return JsonResponse({'code': 200})
    return JsonResponse({'code': 201})
