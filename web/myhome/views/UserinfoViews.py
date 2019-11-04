from django.shortcuts import render,HttpResponse,reverse
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password, make_password
from myadmin import models
import random,time,os
from .IndexViews import typecom,usercom
import re
# Create your views here.

def index(request):
    context={'typelist':typecom(),'userinfo':usercom(request)}
    return render(request,'myhome/user/my-account.html',context)

def modiuser(request):
    data=request.POST.dict()
    data.pop("csrfmiddlewaretoken")
    #头像  昵称 手机号  性别  身份  密码
    #获取头像
    userobj=models.Users.objects.get(id=request.session["User"]["id"])
    try:
        filename=imgupload(request)
        if filename:
            url='.'+data["old_face"]
            # os.remove(url)
            data["face"]=filename
        else:
            data["face"]=data["old_face"]
        data.pop("old_face")
        if data["old_password"]:
            if not check_password(data["old_password"],userobj.password):
                return HttpResponse("<script>alert('密码错误');history.back()</script>")
            else:
                if not re.findall('\d{6}',data['password']):
                    return HttpResponse("<script>alert('请输入有效的密码');history.back()</script>")
                if data["password"]!=data["confirm_password"]:
                    return HttpResponse("<script>alert('新密码与确认密码不一致');history.back()</script>")
                else:
                    data['password']= make_password(data['password'], None, 'pbkdf2_sha256')
                    data.pop("old_password")
                    data.pop("confirm_password")
        else:
            data["password"]=userobj.password
        obj=models.Users.objects.filter(id=request.session["User"]["id"]).update(**data)
        info='更新成功'
        url=reverse("myhome_userinfo")
        return HttpResponse(f"<script>alert('{info}');location.href='"+url+"'</script>")
    except:
        info='更新失败，操作异常，请稍后再试'
        url=reverse("myhome_userinfo")
        return HttpResponse(f"<script>alert('{info}');location.href='"+url+"'</script>")



def seeorder(request,id):
    orderobj=models.Order.objects.get(id=id)
    itemlist=orderobj.orderitem_set.all()
    context={'itemlist':itemlist}
    return render(request,'myhome/user/orderitem.html',context)

def delitem(request):
    try:
        id=request.GET.get("id")
        itemobj=models.OrderItem.objects.get(id=id)
        itemobj.delete()
        orderobj=models.Order.objects.get(id=itemobj.orderid.id)
        if not orderobj.orderitem_set.all().count():
            orderobj.delete()
        return JsonResponse({'code':0,'msg':'删除成功'})
    except:
        return JsonResponse({'code':1,'msg':'删除失败'})

   

#获取上传头像路径并存入文件视图
def imgupload(request):
    file=request.FILES.get("face",None)
    if file:
        hz=file.name.split('.').pop()
        name=str(random.randint(10000,99999)+time.time())+'.'+hz
        try:
            with open(f'./static/myadmin/user_img/{name}','wb+') as fp:
                    for chunk in file.chunks():
                        fp.write(chunk)
            filename=f'/static/myadmin/user_img/{name}'
            return filename
        except:
            return False