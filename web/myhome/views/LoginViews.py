from django.shortcuts import render,HttpResponse,reverse
from django.contrib.auth.hashers import check_password, make_password
from myadmin import models
from .IndexViews import typecom,usercom

# Create your views here.

def login(request):
    context={'typelist':typecom()}
    return render(request,'myhome/login/login.html',context)

def dologin(request):
    data=request.POST.dict()
    data.pop("csrfmiddlewaretoken")

    nextpath=request.GET.get('nextpath','/')
    if not  nextpath:
        nextpath='/' 
    obj=models.Users.objects.filter(phone=data["phone"])
    if not obj.count():
        return HttpResponse("<script>alert('手机号错误');history.back()</script>")
    if not check_password(data["password"],obj[0].password):
        return HttpResponse("<script>alert('密码错误');history.back()</script>")
    else:
        request.session['AdminUser']={'id':obj[0].id,'phone':obj[0].phone}
        url=reverse('myhome_index')
        return HttpResponse(f"<script>alert('登录成功');location.href='{nextpath}'</script>")

def logout(request):
#   del  request.session["AdminUser"]
    # request.session.AdminUser=''
    try:
        request.session.flush()
        url=reverse('myhome_login')
        info="注销成功，请登录"
    except:
        info="注销不成功，请重新注销"
        url=reverse('myhome_index')
    return HttpResponse(f"<script>alert('{info}');location.href='"+url+"'</script>")