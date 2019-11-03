from django.shortcuts import render,HttpResponse,reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from myadmin import models
from .IndexViews import typecom

# 添加收货地址
@csrf_exempt 
def addaddress(request):
    #获取数据
    data=request.GET.dict()
    # 收货地址表里有 收货人姓名  电话  地址  会员id   
    userobj=models.Users.objects.get(id=request.session["AdminUser"]["id"])
    num=userobj.address_set.filter(user_address=data["address"],username=data["name"]).count()
    if not num:
        addressdata={
            'username':data["name"],
            'phone':data["phone"],
            'user_address':data["address"],
            'uid':userobj
        }
        print('11231223')
        addressobj=models.Address(**addressdata)
        addressobj.save()
        return JsonResponse({'code':0,'msg':'添加成功'})
    else:
        return JsonResponse({'code':1,'msg':'添加失败,您已经有一个相同的地址了'})

# 删除收货地址
def deladdress(request):
    try:
        id=request.GET.get("id")
        addressobj=models.Address.objects.get(id=id)
        addressobj.delete()
        return JsonResponse({'code':0,'msg':'删除成功'})
    except:
         return JsonResponse({'code':1,'msg':'删除失败'})


def modiaddress(request):
    pass
