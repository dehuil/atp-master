from django.db import models

# 用户表
class UserInfo(models.Model):
    username = models.CharField(verbose_name='用户名', max_length=32, unique=True)
    password = models.CharField(verbose_name='密码', max_length=128)


# 产品表
class Product(models.Model):
    pro_user = models.ForeignKey('UserInfo', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=64)
    product_desc = models.CharField(max_length=128)
    product_er = models.CharField(max_length=64)
    create_time = models.DateTimeField(auto_now=True)


# 单一接口用例表
class Apis(models.Model):
    api_product = models.ForeignKey('Product', on_delete=models.CASCADE)
    api_name = models.CharField(max_length=100)
    api_url = models.CharField(max_length=200)
    api_param_value = models.CharField(max_length=8000)
    REQUEST_METHOD = (
        ('0', 'get'),
        ('1', 'post'),
    )
    api_method = models.CharField(choices=REQUEST_METHOD, default='get', max_length=200)
    api_result = models.CharField(max_length=200)
    api_status = models.BooleanField()
    create_time = models.DateTimeField(auto_now=True)


# 流程接口用例表
class ApiTest(models.Model):
    api_t_product = models.ForeignKey('Product', on_delete=models.CASCADE)
    api_t_name = models.CharField(max_length=64)
    api_t_desc = models.CharField(max_length=200)
    api_ter = models.CharField(max_length=200)
    api_t_status = models.BooleanField()
    create_time = models.DateTimeField(auto_now=True)


# 流程接口步骤表
class ApiStep(models.Model):
    api_test = models.ForeignKey('ApiTest', on_delete=models.CASCADE)
    api_s_name = models.CharField(max_length=100)
    api_s_step = models.CharField(max_length=200)
    api_s_url = models.CharField(max_length=800)
    api_s_param_value = models.CharField(max_length=8000)
    REQUEST_METHOD = (
        ('0', 'get'),
        ('1', 'post'),
    )
    api_s_method = models.CharField(choices=REQUEST_METHOD, default='get', max_length=200)
    api_s_result = models.CharField(max_length=200)
    api_s_status = models.BooleanField()
    create_time = models.DateTimeField(auto_now=True)


# Web用例表
class WebTest(models.Model):
    web_t_pro = models.ForeignKey('Product', on_delete=models.CASCADE)
    web_t_name = models.CharField(max_length=64)
    web_t_desc = models.CharField(max_length=200)
    web_ter = models.CharField(max_length=64)
    web_t_res = models.BooleanField()
    create_time = models.DateTimeField(auto_now=True)


# Web用例步骤表
class WebTestStep(models.Model):
    web_test = models.ForeignKey('WebTest', on_delete=models.CASCADE)
    web_step = models.CharField(max_length=200)
    web_find_method = models.CharField(max_length=200)
    web_element = models.CharField(max_length=200)
    web_opt_method = models.CharField(max_length=200)
    web_test_data = models.CharField(max_length=200, null=True)
    web_assert_data = models.CharField(max_length=200)
    web_result = models.BooleanField()
    create_time = models.DateTimeField(auto_now=True)


# App用例表
class AppTest(models.Model):
    app_t_pro = models.ForeignKey('Product', on_delete=models.CASCADE)
    app_t_name = models.CharField(max_length=64)
    app_t_desc = models.CharField(max_length=200)
    app_ter = models.CharField(max_length=64)
    app_t_res = models.BooleanField()
    create_time = models.DateTimeField(auto_now=True)


# App用例步骤表
class AppTestStep(models.Model):
    app_test = models.ForeignKey('AppTest', on_delete=models.CASCADE)
    app_step = models.CharField(max_length=200)
    app_find_method = models.CharField(max_length=200)
    app_element = models.CharField(max_length=200)
    app_opt_method = models.CharField(max_length=200)
    app_test_data = models.CharField(max_length=200, null=True)
    app_assert_data = models.CharField(max_length=200)
    app_result = models.BooleanField()
    create_time = models.DateTimeField(auto_now=True)


# Bug表
class Bug(models.Model):
    bug_pro = models.ForeignKey('Product', on_delete=models.CASCADE)
    bug_name = models.CharField(max_length=100)
    bug_detail = models.CharField(max_length=500)
    BUG_LEVEL = (
        ('low', '轻微'),
        ('mid', '一般'),
        ('high', '严重'),
    )
    bug_level = models.CharField(choices=BUG_LEVEL, default='严重', max_length=200)
    BUG_STATUS = (
        (0, '激活'),
        (1, '已解决'),
        (2, '已关闭'),
    )
    bug_status = models.CharField(choices=BUG_STATUS, default='激活', max_length=200)
    bug_creat_er = models.CharField(max_length=200)
    bug_assign = models.CharField(max_length=200)
    create_time = models.DateTimeField(auto_now=True)


# 系统设置表
class Set(models.Model):
    set_name = models.CharField(max_length=200)
    set_value = models.CharField(max_length=600)