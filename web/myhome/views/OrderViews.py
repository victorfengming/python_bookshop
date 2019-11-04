from django.shortcuts import render,HttpResponse,reverse
from django.db import transaction
from django.http import HttpResponseRedirect,JsonResponse
from django.contrib.auth.hashers import check_password, make_password
from myadmin import models
from .IndexViews import typecom
from web import settings
# Create your views here.

from django.views.decorators.cache import never_cache 
#订单结算页
@never_cache
def confirm(request):
    cartids=request.GET.get("cartids",'').split(',')
    cartids=[int(i) for i in cartids]
    data=models.Cart.objects.filter(id__in=cartids)
    userobj=models.Users.objects.get(id=request.session["User"]["id"])
    addresslist=userobj.address_set.all()
    context={'typelist':typecom(),'cartlist':data,'addresslist':addresslist,}
    return render(request,'myhome/order/confirm.html',context)


def create(request):
    # 为什么用post请求，因为post请求跳转到下一页面不做停留
    # 这样就会解决用户不断创建新订单的情况

    # 获取数据
    # 收集订单数据
   
    # 把下订单的购物车商品，在购物车中删除
    # 跳转到订单支付页面
    #获取数据
    data=request.POST.dict()
    data.pop('csrfmiddlewaretoken')
    totalprice=0
    cartids=data["cartids"].split(',')
    cartids=[int(i) for i in cartids]
    addressobj=models.Address.objects.get(id=data["addressid"])
    data["name"]=addressobj.username
    data["phone"]=addressobj.phone
    data["address"]=addressobj.user_address

    # 根据购物车的id获取相对应的购物车的信息
    # try:
    carts=models.Cart.objects.filter(id__in=cartids)
    # 根据购物车里的对象运算出确认订单时提交商品提交的总价
    for i in carts:
        totalprice+=i.num*i.bookid.price
    # 创建订单
    orderdata={
        'uid':models.Users.objects.get(id=request.session["User"]["id"]),
        'username':data["name"],
        'phone':data["phone"],
        'address':data["address"],
        'totalprice':totalprice
    }
    # 实例化订单
    orderobj=models.Order(**orderdata)
    # 存入数据库里
    orderobj.save()
    # 创建订单详情数据，并存入到数据库里，然后删除购物车里所对应的用户提交的商品
    for i in carts:
        itemdata={
            'orderid':orderobj,
            'bookid':i.bookid,
            'price':i.bookid.price,
            'num':i.num
        }
        itemobj=models.OrderItem(**itemdata)
        itemobj.save()
        bookobj=models.Books.objects.get(id=itemobj.bookid.id)
        bookobj.num=bookobj.num-itemobj.num
        bookobj.save()
        i.delete()
    # url=reverse('myhome_order_pay',args=(orderobj.id,))
    return JsonResponse({'code':0,'msg':'添加成功','orderid':orderobj.id})
    # except:
    #     return JsonResponse({'code':0,'msg':'添加失败'})


from web import settings
from utils.pay import AliPay
    
# AliPay 对象实例化
def Get_AliPay_Object():
    alipay = AliPay(
        appid=settings.ALIPAY_APPID,# APPID （沙箱应用）
        app_notify_url=settings.ALIPAY_NOTIFY_URL, # 回调通知地址
        return_url=settings.ALIPAY_RETURN_URL,# 支付完成后的跳转地址
        app_private_key_path=settings.APP_PRIVATE_KEY_PATH, # 应用私钥
        alipay_public_key_path=settings.ALIPAY_PUBLIC_KEY_PATH,  # 支付宝公钥
        debug=True,  # 默认False,
    )
    return alipay

 
    # 发起支付请求    
def buypay(request):
    # try:
    # 获取支付对象
    id=request.GET.get("id")
    print(id)
    orderobj=models.Order.objects.get(id=id)
    alipay = Get_AliPay_Object()
    # 生成支付的url
    query_params = alipay.direct_pay(
        subject='图书商城_书籍购买',  # 商品简单描述
        out_trade_no = orderobj.id,# 用户购买的商品订单号
        total_amount = '%.2f'%orderobj.totalprice,  # 交易金额(单位: 元 保留俩位小数)
    )

    # 支付宝网关地址（沙箱应用）
    pay_url = settings.ALIPAY_URL+"?{0}".format(query_params)  

    print('正在发起支付请求...')

    # 页面重定向到支付页面
    return HttpResponseRedirect(pay_url)
    # except:
    #      return HttpResponse(f"<script>alert('操作异常，请重新选择商品');location.href='/'</script>")

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def pay_result(request):
    # 获取对象
    alipay = Get_AliPay_Object()
    if request.method == "POST":
        # 检测是否支付成功
        # 去请求体中获取所有返回的数据：状态/订单号
        from urllib.parse import parse_qs
        # name&age=123....
        body_str = request.body.decode('utf-8')
        post_data = parse_qs(body_str)

        post_dict = {}
        for k, v in post_data.items():
            post_dict[k] = v[0]

        sign = post_dict.pop('sign', None)
        status = alipay.verify(post_dict, sign)
        print('------------------开始------------------')
        print('POST验证', status)
        print(post_dict)
        out_trade_no = post_dict['out_trade_no']
        

        # 修改订单状态
        ass = {'status':1,'paytime':post_dict['gmt_payment']}
        print(ass)
        models.Order.objects.filter(id=out_trade_no).update(**ass)
        print('------------------结束------------------')
        # 修改订单状态：获取订单号
        return HttpResponse('success')
       


# 回调地址get
def pay_get(request):
    
    alipay = Get_AliPay_Object()
    params = request.GET.dict()
    sign = params.pop('sign', None)
    status = alipay.verify(params, sign)
    print('==================开始==================')
    print('GET验证', status)
    print('==================结束==================')
    return HttpResponse('<script>alert("支付成功");location.href="/userinfo/index"</script>')


