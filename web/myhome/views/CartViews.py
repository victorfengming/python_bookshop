from django.shortcuts import render,HttpResponse,reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from myadmin import models
from .IndexViews import typecom,usercom


#购物车列表页视图
def index(request):
    context={'typelist':typecom(),'userinfo':usercom(request)}
    return render(request,'myhome/cart/index.html',context)

@csrf_exempt 
def addcart(request):
    data=request.POST.dict()
    #判断在购物车里这个用户下有没有这个商品
    uid=request.session["AdminUser"]["id"]
    # 如果有，就数量加1
    try:
        userobj=models.Users.objects.get(id=uid)
        bookobj=models.Books.objects.get(id=data["bookid"])
        cartobj=userobj.cart_set.filter(bookid=bookobj)
        if cartobj:
            cartobj[0].num+=int(data["num"])
            cartobj[0].save()          
        else:
        # 如果没有，就在购物车里增加这个用户下的这个商品
            cartdata={
                'uid':userobj,
                'bookid':bookobj,
                'num':data["num"]
            }
            cartobj=models.Cart(**cartdata)
            cartobj.save()
        return JsonResponse({'code':0,'msg':'添加成功'})
    except:
        return JsonResponse({'code':1,'msg':'添加失败'})


def delcart(request):
    try:
        bookid=request.GET.get("bookid")
        bookobj=models.Books.objects.get(id=bookid)
        userobj=models.Users.objects.get(id=request.session["AdminUser"]["id"])
        cartobj=userobj.cart_set.get(bookid=bookobj)
        cartobj.delete()
        return JsonResponse({'code':0,'msg':'删除成功'})
    except:
        return JsonResponse({'code':1,'msg':'删除失败'})

def modicart(request):
    try:
        data=request.GET.dict()
        userobj=models.Users.objects.get(id=request.session["AdminUser"]["id"])
        cartobj=userobj.cart_set.get(bookid=data["bookid"])
        cartobj.num=data["num"]
        cartobj.save()
        return JsonResponse({'code':0,'msg':'更新成功'})
    except:
         return JsonResponse({'code':1,'msg':'更新失败'})

