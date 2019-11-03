from django.shortcuts import render,reverse
from django.http import HttpResponse
import re

#中间件
class AdminLoginMiddleware:
    def __init__(self, get_response):
        #获取相应
        self.get_response = get_response
        # One-time configuration and initialization.
    ##自动初始化的方法
    def __call__(self, request):
        
        # 检测当前的请求是否已经登录,如果已经登录,.则放行,如果未登录,则跳转到登录页   进入后台说先要卡登录没，如果没登录就不让进
        # 获取当前用户的请求路径  /admin/开头  但不是 /admin/login/  /admin/dologin/   /admin/verifycode
        urllist = [reverse('myadmin_login'),reverse('myadmin_dologin'),reverse('myadmin_yzm')]
        # 判断是否进入了后台,并且不是进入登录页面  后台的路径中肯定有myadmin字样，根据这个进行判断是否进入后台
        if re.match('/myadmin/',request.path) and request.path not in urllist:
            # 检测session中是否存在 adminlogin的数据记录
            if request.session.get('AdminUser','') == '':# 如果在session没有记录,则证明没有登录,跳转到登录页面
                return HttpResponse(f'<script>alert("请先登录");location.href="{urllist[0]}";</script>')
                



        response = self.get_response(request)
        return response