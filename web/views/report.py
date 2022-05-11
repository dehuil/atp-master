#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
相关功能：报告列表
'''
import os
from django.core.paginator import Paginator
from django.shortcuts import render


# 单一接口报告列表
def report_apis(request):
    # path = "F:/atp_case/api_case/report/"
    path = r"E:\chromeDown\fukun_apitest-master\ldh_apitest\ldh_apitest\report"
    dirs = os.listdir(path)
    apis_list = []
    for file in dirs:
        apis_list.append(file)

    paginator = Paginator(apis_list, 10)
    # 获取page的值，如果没有，则设置使用默认值1
    page = request.GET.get('page', 1)
    # 获取第几页
    page_object = paginator.page(page)

    data = {
        'apis_list': page_object,
    }
    return render(request, 'report/report_apis.html', context=data)


# Web报告列表
def report_web(request):
    path = r"E:\chromeDown\fukun_apitest-master\ldh_apitest\ldh_apitest\report"
    dirs = os.listdir(path)
    web_list = []
    for file in dirs:
        web_list.append(file)

    paginator = Paginator(web_list, 10)
    page = request.GET.get('page', 1)
    page_object = paginator.page(page)

    data = {
        'web_list': page_object,
    }
    return render(request, 'report/report_web.html', context=data)