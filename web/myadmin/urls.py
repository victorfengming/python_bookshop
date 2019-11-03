"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from .views import *
urlpatterns = [

    # path('admin/', admin.site.urls),

    #首页
    path('', IndexViews.index,name='myadmin_index'),
    
    #登录
    path('login', IndexViews.mylogin,name='myadmin_login'),
    #执行登录
    path('dologin', IndexViews.dologin,name='myadmin_dologin'),
    #验证码地址
    path('yzm', IndexViews.verifycode,name='myadmin_yzm'),

    #注销
    path('cancel', IndexViews.cancel,name='myadmin_cancel'),

    #用户管理
    path('user/index', UserViews.index,name='myadmin_user_index'),
    path('user/add', UserViews.adduser,name='myadmin_user_add'),
    path('user/del/<int:id>', UserViews.deluser,name='myadmin_user_del'),
    path('user/mod', UserViews.moduser,name='myadmin_user_mod'),

    #图书类别管理
    path('type/index', TypeViews.index,name='myadmin_type_index'),
    path('type/add', TypeViews.add,name='myadmin_type_add'),
    path('type/insert', TypeViews.insert,name='myadmin_type_insert'),
    path('type/delete', TypeViews.delete,name='myadmin_type_delete'),
    path('type/edit', TypeViews.edit,name='myadmin_type_edit'),

    #图书管理
    path('book/index', BookViews.index,name='myadmin_book_index'),
    path('book/add', BookViews.add,name='myadmin_book_add'),
    path('book/insert', BookViews.insert,name='myadmin_book_insert'),
    path('book/delete', BookViews.delete,name='myadmin_book_delete'),
    path('book/edit', BookViews.edit,name='myadmin_book_edit'),
    path('book/update', BookViews.update,name='myadmin_book_update'),

     #订单管理
    path('order/index', OrderViews.index,name='myadmin_order_index'),
    # path('order/edit', OrderViews.editorder,name='myadmin_order_edit'),
    


    #权限管理
    
    #管理员管理
    path('auth/user/index', IndexViews.authuser_index,name='myadmin_authuser_index'),
    path('auth/user/add', IndexViews.authuser_add,name='myadmin_authuser_add'),
    path('auth/user/insert', IndexViews.authuser_insert,name='myadmin_authuser_insert'),
    path('auth/user/del/<int:id>', IndexViews.authuser_del,name='myadmin_authuser_del'),
    path('auth/user/edit', IndexViews.authuser_edit,name='myadmin_authuser_edit'),



    ##组管理
    path('auth/group/index', IndexViews.authgroup_index,name='myadmin_authgroup_index'),
    path('auth/group/add', IndexViews.authgroup_add,name='myadmin_authgroup_add'),
    path('auth/group/insert', IndexViews.authgroup_insert,name='myadmin_authgroup_insert'),
    path('auth/group/del/<int:id>', IndexViews.authgroup_del,name='myadmin_authgroup_del'),
    path('auth/group/edit', IndexViews.authgroup_edit,name='myadmin_authgroup_edit'),


]
