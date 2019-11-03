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
# from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    #首页
    path('', IndexViews.index,name='myhome_index'),
    path('booklist/<int:typeid>', IndexViews.booklist,name='myhome_booklist'),
    path('detail/<int:bookid>', IndexViews.detail,name='myhome_bookdetail'),
    path('search', IndexViews.booksearch,name='myhome_booksearch'),

    # 购物车列表页
    path('cart/index', CartViews.index,name='myhome_cartindex'),
    path('cart/addcart', CartViews.addcart,name='myhome_addcart'),
    path('cart/delcart', CartViews.delcart,name='myhome_delcart'),
    path('cart/modicart', CartViews.modicart,name='myhome_modicart'),

    # 收货地址
    path('address/add', AddressViews.addaddress,name='myhome_address_add'),
    path('address/modi', AddressViews.modiaddress,name='myhome_address_modi'),
    path('address/del', AddressViews.deladdress,name='myhome_address_del'),

    #用户个人信息管理  #支付成功后的跳转地址
    path('userinfo/index', UserinfoViews.index,name='myhome_userinfo'),
    path('userinfo/modiuser', UserinfoViews.modiuser,name='myhome_modiuser'),


    path('userinfo/seeorder/<int:id>', UserinfoViews.seeorder,name='myhome_seeorder'),
    path('userinfo/delitem', UserinfoViews.delitem,name='myhome_delitem'),




    #订单
    path('order/confirm', OrderViews.confirm,name='myhome_confirm'),
    path('order/create', OrderViews.create,name='myhome_order_create'),

    #发起支付请求
    path('order/buy', OrderViews.buypay,name='myhome_order_pay'),
    #回调函数
    path('order/pay_result', OrderViews.pay_result,name='myhome_pay_result'),
     path('order/pay_get', OrderViews.pay_get,name='myhome_pay_get'),


    # path('order/list', OrderViews.mylist,name='myhome_order_list'),







    #登录
    path('login', LoginViews.login,name='myhome_login'),
    path('dologin',LoginViews.dologin,name='myhome_dologin'),
    #注销
    path('logout', LoginViews.logout,name='myhome_logout'),

    #注册
    path('register', RegisterViews.register,name='myhome_register'),
    path('doregister',RegisterViews.doregister,name='myhome_doregister'),

    #检测手机号
    path('checkphone',RegisterViews.checkphone,name='myhome_checkphone'),

    #给手机发送验证码，并返回信息给用户
    path('sendphone', RegisterViews.sendphone,name='myhome_sendphone'),
    path('sendcode', RegisterViews.SendCode,name='myhome_sendcode'),
   
]
