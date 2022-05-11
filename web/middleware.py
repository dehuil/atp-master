from django.shortcuts import redirect
from django.conf import settings
from web import models
from django.utils.deprecation import MiddlewareMixin


class Atp(object):

    def __init__(self):
        self.user = None


class MD1(MiddlewareMixin):
    def process_request(self, request):

        request.atp = Atp()

        user_id = request.session.get('user_id')
        user_obj = models.UserInfo.objects.filter(id=user_id).first()

        request.atp.user = user_obj

        if request.path_info in settings.WHITE_REGEX_URL_LIST:
            return
        if not request.atp.user:
            return redirect('atp:login')
