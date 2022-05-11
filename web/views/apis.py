"""
相关功能：单一接口的增删改查
"""
from io import BytesIO

import xlwt
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from web.models import Apis, Product


#excle执行接口
def apis_excle(request):
    print(request)
    return render(request,'dddddd')

# 单一接口列表
def apis_manage(request):
    apis_list = Apis.objects.all().order_by('id')

    paginator = Paginator(apis_list, 10)
    # 获取page的值，如果没有，则设置使用默认值1
    page = request.GET.get('page', 1)
    # 获取第几页
    page_object = paginator.page(page)

    data = {
        'apis_list': page_object,
    }
    return render(request, 'apis/apis_manage.html', context=data)


# 单一接口添加
def apis_add(request):
    pro_names = Product.objects.all()

    if request.method == "GET":
        data = {
            'pro_names': pro_names,
        }
        return render(request, 'apis/apis_add.html', context=data)
    elif request.method == "POST":
        api_product = request.POST.get('dropdown')
        api_name = request.POST.get('api_name')
        api_url = request.POST.get('api_url')
        api_param_value = request.POST.get('api_param_value')
        api_method = request.POST.get('method_check')
        api_result = request.POST.get('api_result')
        api_status = request.POST.get('api_status')

        if api_name == "":
            return JsonResponse({'code': 202})

        Apis.objects.create(
            api_name=api_name,
            api_url=api_url,
            api_param_value=api_param_value,
            api_method=api_method,
            api_result=api_result,
            api_status=api_status,
            api_product_id=api_product,
        )
        return JsonResponse({'code': 200})
    return JsonResponse({'code': 201})


# 单一接口删除
def apis_delete(request):
    apis_id = request.GET.get('apis_id')

    try:
        apis_obj = Apis.objects.get(id=apis_id)
        apis_obj.delete()
        return JsonResponse({'code': 200})
    except Exception as e:
        print(e)
        return JsonResponse({'code': 201})


# 单一接口编辑
def apis_update(request, apis_id):
    pro_names = Product.objects.all()
    apis = Apis.objects.get(id=apis_id)

    if request.method == "GET":
        data = {
            'pro_names': pro_names,
            'apis': apis,
        }
        return render(request, 'apis/apis_update.html', context=data)
    elif request.method == "POST":
        api_product = request.POST.get('dropdown')
        api_name = request.POST.get('api_name')
        api_url = request.POST.get('api_url')
        api_param_value = request.POST.get('api_param_value')
        api_method = request.POST.get('method_check')
        api_result = request.POST.get('api_result')
        api_status = request.POST.get('api_status')

        if api_name == "":
            return JsonResponse({'code': 202})

        Apis.objects.filter(id=apis_id).update(
            api_name=api_name,
            api_url=api_url,
            api_param_value=api_param_value,
            api_method=api_method,
            api_result=api_result,
            api_status=api_status,
            api_product_id=api_product
        )
        return JsonResponse({'code': 200})
    return JsonResponse({'code': 201})


# 单一接口项目筛选
def apis_pro_search(request):
    search_name = request.GET.get('pro_name')
    pro_list = Apis.objects.filter(api_product__product_name__icontains=search_name)

    paginator = Paginator(pro_list, 10)
    # 获取page的值，如果没有，则设置使用默认值1
    page = request.GET.get('page', 1)
    # 获取第几页
    apis_lists = paginator.page(page)

    data = {
        "apis_list": apis_lists,
    }

    return render(request, 'apis/apis_manage.html', context=data)


# 单一接口接口用例名称搜索
def apis_api_case_name_search(request):
    search_name = request.GET.get('api_case_name')
    api_list = Apis.objects.filter(api_name__icontains=search_name)

    paginator = Paginator(api_list, 10)
    # 获取page的值，如果没有，则设置使用默认值1
    page = request.GET.get('page', 1)
    # 获取第几页
    apis_lists = paginator.page(page)

    data = {
        "apis_list": apis_lists,
    }
    return render(request, 'apis/apis_manage.html', context=data)


def test(request):
    if request.method == "GET":
        pro_names = request.GET.get('pro_name', "123")
        print(pro_names)
        return HttpResponse("name={}".format(pro_names))


# 导出Excel
def apis_excel_export(request, pro_id):
    list_obj = Apis.objects.all().filter(api_product_id=pro_id)

    if list_obj:
        # 创建工作簿
        ws = xlwt.Workbook(encoding="utf-8")
        # 添加第一页数据表
        # 新建sheet表名称
        w = ws.add_sheet("单一接口测试用例表")
        # 写入表头
        w.write(0, 0, u'ID')
        w.write(0, 1, u'产品名称')
        w.write(0, 2, u'接口用例名称	')
        w.write(0, 3, u'Url地址	')
        w.write(0, 4, u'请求参数和值	')
        w.write(0, 5, u'请求方法	')
        w.write(0, 6, u'预期结果	')
        w.write(0, 7, u'测试结果')
        # 写入数据
        excel_row = 1
        for obj in list_obj:
            api_id = obj.id
            api_pro = obj.api_product.product_name
            api_name = obj.api_name
            api_url = obj.api_url
            api_param_value = obj.api_param_value
            api_method = obj.api_method
            api_result = obj.api_result
            api_status = obj.api_status
            # 写入每一行对应数据
            w.write(excel_row, 0, api_id)
            w.write(excel_row, 1, api_pro)
            w.write(excel_row, 2, api_name)
            w.write(excel_row, 3, api_url)
            w.write(excel_row, 4, api_param_value)
            w.write(excel_row, 5, api_method)
            w.write(excel_row, 6, api_result)
            w.write(excel_row, 7, api_status)
            excel_row += 1
        # 写出到IO
        output = BytesIO()
        ws.save(output)
        # 重新定位到开始
        output.seek(0)
        # 设置HTTPResponse的类型
        response = HttpResponse(content_type="application/vnd.ms-excel")
        response['Content-Disposition'] = 'attachment;filename=apis_test_case.xls'
        response.write(output.getvalue())
        return response
