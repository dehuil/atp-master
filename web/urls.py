from django.urls import path
from web.views import account, manage, project, apis, api_test, web_test, app_test, bug, set_atp, report

urlpatterns = [
    # 登录注册
    path('login/', account.login, name='login'),
    path('register/', account.register, name='register'),

    # 首页
    path('home/', manage.home, name='home'),
    path('logout/', manage.logout, name='logout'),
    path('jenkins_manage/', manage.jenkins_manage, name='jenkins_manage'),
    path('locust_manage/', manage.locust_manage, name='locust_manage'),

    # 产品管理
    path('product_manage/', project.product_manage, name='product_manage'),
    path('product_add/', project.product_add, name='product_add'),
    path('product_delete/', project.product_delete, name='product_delete'),
    path('product_update/<int:pro_id>/', project.product_update, name='product_update'),
    path('product_search/', project.product_search, name='product_search'),

    # 单一接口用例
    path('apis_excle/', apis.apis_excle, name='apis_excle'),
    path('apis_manage/', apis.apis_manage, name='apis_manage'),
    path('apis_add/', apis.apis_add, name='apis_add'),
    path('apis_delete/', apis.apis_delete, name='apis_delete'),
    path('apis_update/<int:apis_id>/', apis.apis_update, name='apis_update'),
    path('apis_pro_search/', apis.apis_pro_search, name='apis_pro_search'),
    path('apis_api_case_name_search/', apis.apis_api_case_name_search, name='apis_api_case_name_search'),
    path('apis_excel_export/<int:pro_id>/', apis.apis_excel_export, name='apis_excel_export'),

    # 流程接口用例
    path('api_test_manage/', api_test.api_test_manage, name='api_test_manage'),
    path('api_test_add/', api_test.api_test_add, name='api_test_add'),
    path('api_test_delete/', api_test.api_test_delete, name='api_test_delete'),
    path('api_test_update/<int:api_t_id>/', api_test.api_test_update, name='api_test_update'),
    path('api_test_search/', api_test.api_test_search, name='api_test_search'),
    # 流程接口步骤用例
    path('api_step_manage/<int:api_t_id>/', api_test.api_step_manage, name='api_step_manage'),
    path('api_step_add/<int:api_t_id>/', api_test.api_step_add, name='api_step_add'),
    path('api_step_delete/', api_test.api_step_delete, name='api_step_delete'),
    path('api_step_update/<int:api_t_id>/<int:api_s_id>/', api_test.api_step_update, name='api_step_update'),

    # Web测试用例
    path('web_test_manage/', web_test.web_test_manage, name='web_test_manage'),
    path('web_test_add/', web_test.web_test_add, name='web_test_add'),
    path('web_test_delete/', web_test.web_test_delete, name='web_test_delete'),
    path('web_test_update/<int:web_t_id>/', web_test.web_test_update, name='web_test_update'),
    path('web_test_search/', web_test.web_test_search, name='web_test_search'),
    # Web测试用例步骤
    path('web_step_manage/<int:web_t_id>/', web_test.web_step_manage, name='web_step_manage'),
    path('web_step_add/<int:web_t_id>/', web_test.web_step_add, name='web_step_add'),
    path('web_step_delete/', web_test.web_step_delete, name='web_step_delete'),
    path('web_step_update/<int:web_t_id>/<int:web_s_id>/', web_test.web_step_update, name='web_step_update'),

    # App测试用例
    path('app_test_manage/', app_test.app_test_manage, name='app_test_manage'),
    path('app_test_add/', app_test.app_test_add, name='app_test_add'),
    path('app_test_delete/', app_test.app_test_delete, name='app_test_delete'),
    path('app_test_update/<int:app_t_id>/', app_test.app_test_update, name='app_test_update'),
    path('app_test_search/', app_test.app_test_search, name='app_test_search'),
    # App测试用例步骤
    path('app_step_manage/<int:app_t_id>/', app_test.app_step_manage, name='app_step_manage'),
    path('app_step_add/<int:app_t_id>/', app_test.app_step_add, name='app_step_add'),
    path('app_step_delete/', app_test.app_step_delete, name='app_step_delete'),
    path('app_step_update/<int:app_t_id>/<int:app_s_id>/', app_test.app_step_update, name='app_step_update'),

    # Bug管理
    path('bug_manage/', bug.bug_manage, name='bug_manage'),
    path('bug_add/', bug.bug_add, name='bug_add'),
    path('bug_delete/', bug.bug_delete, name='bug_delete'),
    path('bug_update/<int:bug_id>/', bug.bug_update, name='bug_update'),
    path('bug_search/', bug.bug_search, name='bug_search'),

    # 报告列表
    path('report_apis/', report.report_apis, name='report_apis'),
    path('report_web/', report.report_web, name='report_web'),

    # 系统设置
    path('set_manage/', set_atp.set_manage, name='set_manage'),
    path('set_add/', set_atp.set_add, name='set_add'),
    path('set_delete/', set_atp.set_delete, name='set_delete'),
    path('set_update/<int:set_id>/', set_atp.set_update, name='set_update'),
    path('set_user_manage/', set_atp.set_user_manage, name='set_user_manage'),

]