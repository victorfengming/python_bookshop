from django.shortcuts import render,reverse
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from .. import models
from django.contrib.auth.models import User,Permission,Group
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import permission_required
# Create your views here.

def index(request):
    return render(request,'myadmin/index.html')

def mylogin(request):
    return render(request,'myadmin/login.html')

    
def dologin(request): 
    data=request.POST.dict()
    data.pop('csrfmiddlewaretoken')
    #检测验证码
    if request.session['verifycode'].lower()!=data["code"].lower():
        return HttpResponse("<script>alert('验证码错误');history.back()</script>")
    username=request.POST["username"]
    password=request.POST["password"]
    user=authenticate(request,username=username,password=password)
    if user is not None:
        login(request,user)
        #完成登录
        request.session['AdminUser']={'uid':user.id,'username':user.username}
        url=reverse('myadmin_index')
        return HttpResponse(f"<script>alert('登录成功');location.href='{url}'</script>")
    else:
        return HttpResponse("<script>alert('密码错误');history.back()</script>")
    

def verifycode(request):
    #引入绘图模块
    from PIL import Image, ImageDraw, ImageFont
    #引入随机函数模块
    import random
    #定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(20, 100), 255)
    width = 100
    height = 25
    #创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    #创建画笔对象
    draw = ImageDraw.Draw(im)
    #调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    #定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    #随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    #构造字体对象
    font = ImageFont.truetype('arial.ttf', 23)
    #构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    #绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    #释放画笔
    del draw
    #存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    #内存文件操作  3.0以后的版本不支持cStringIO()  直接导入io即可   然后使用二进制流进行文件的输入与输出
    import io
    buf = io.BytesIO()
    #将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    #将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')


def cancel(request):
    try:
        del request.session["AdminUser"]
        logout(request)
        url=reverse('myadmin_login')
        info='注销成功'
    except:
        url=reverse('myadmin_index')
        info='注销失败'
    return HttpResponse(f"<script>alert('{info}');location.href='{url}'</script>")   



    path('auth/user/index', IndexViews.authuser_index,name='myadmin_authuser_index'),
    path('auth/user/add', IndexViews.authuser_add,name='myadmin_authuser_add'),
    path('auth/user/insert', IndexViews.authuser_insert,name='myadmin_authuser_insert'),
    path('auth/group/index', IndexViews.authgroup_index,name='myadmin_authgroup_index'),
    path('auth/group/add', IndexViews.authgroup_add,name='myadmin_authgroup_add'),
    path('auth/group/insert', IndexViews.authgroup_insert,name='myadmin_authgroup_insert'),


@permission_required('auth.add_group',raise_exception=True)
def authuser_index(request):
    data=User.objects.all().exclude(id=request.session["AdminUser"]["uid"])
    context={'userdata':data}
    return render(request,'myadmin/auth/user/index.html',context)

@permission_required('auth.add_group',raise_exception=True)
def authuser_add(request):
    groupdata=Group.objects.all()
    context={'groupdata':groupdata}
    return render(request,'myadmin/auth/user/add.html',context)
@permission_required('auth.add_group',raise_exception=True)
def authuser_insert(request):
    try:
        data=request.POST.dict()
        data.pop("csrfmiddlewaretoken")
        gs=request.POST.getlist("gs")
        if gs:
            data.pop("gs")
        else:
            if data["is_superuser"]=='1':
                data["is_superuser"]=True
                ob=User.objects.create_superuser(**data)
            else:
                ob=User.objects.create_user(**data) 
            if gs:
                ob.groups.set(gs)
                ob.save()
            return HttpResponse("<script>alert('管理员创建成功');location.href='/myadmin/auth/user/index';</script>")
    except:
        return HttpResponse("<script>alert('管理员创建失败');location.href='/myadmin/auth/user/add';</script>")
@permission_required('auth.add_group',raise_exception=True)
def authuser_del(request,id):
    try:
        userobj=User.objects.get(id=id)
        userobj.groups.clear() 
        userobj.delete()
        return HttpResponse("<script>alert('管理员删除成功');location.href='/myadmin/auth/user/index';</script>")
    except:
        return HttpResponse("<script>alert('管理员删除失败');location.href='/myadmin/auth/user/index';</script>")

@permission_required('auth.add_group',raise_exception=True)
def authuser_edit(request):
    if request.method=='GET':
        id=request.GET.get("id")
        userobj=User.objects.get(id=id)
        groupdata=Group.objects.all()
        context={"userinfo":userobj,"groupdata":groupdata}
        return render(request,'myadmin/auth/user/edit.html',context)
    else:
        data=request.POST.dict()
        data.pop("csrfmiddlewaretoken")
        try:
            data.pop("gs")
            gs=request.POST.getlist("gs")
            userobj=User.objects.get(id=data["id"])
            userobj.username=data["username"]
            userobj.email=data["email"]
            userobj.is_superuser=data["is_superuser"]
            userobj.save()
            userobj.groups.clear()
            userobj.groups.set(gs)
            return HttpResponse("<script>alert('管理员编辑成功');location.href='/myadmin/auth/user/index';</script>")
        except:
            id=data["id"]
            return HttpResponse(f"<script>alert('管理员编辑失败');location.href='/myadmin/auth/user/edit?id={id}';</script>")
@permission_required('auth.add_group',raise_exception=True)
def authgroup_index(request):
    #获取所有的组
    groupdata=Group.objects.all()
    #分配数据
    context={'groupdata':groupdata}
    return render(request,'myadmin/auth/group/index.html',context)

@permission_required('auth.add_group',raise_exception=True)
def authgroup_add(request):
    #读取所有的权限信息
    Permission.objects.all()
    #读取所有权限信息，并排除以Can开头的系统默认生成的权限
    perms=Permission.objects.exclude(name__startswith='Can')
    #分配数据
    context={'perms':perms}
    return render(request,'myadmin/auth/group/add.html',context)

@permission_required('auth.add_group',raise_exception=True)
def authgroup_insert(request):
    #获取组名
    name=request.POST.get("name")
    #创建组
    g=Group(name=name)
    g.save()
    #获取权限
    prms=request.POST.getlist('prms',None)
    if prms:
        g.permissions.set(prms)
    return HttpResponse("<script>alert('组创建成功');location.href='/myadmin/auth/group/index';</script>")

@permission_required('auth.add_group',raise_exception=True)
def authgroup_del(request,id):
    try:
        groupobj=Group.objects.get(id=id)
        groupobj.user_set.clear()
        groupobj.delete()
        return HttpResponse("<script>alert('组删除成功');location.href='/myadmin/auth/group/index';</script>")
    except:
        return HttpResponse("<script>alert('组删除失败');location.href='/myadmin/auth/group/index';</script>")

@permission_required('auth.add_group',raise_exception=True)
def authgroup_edit(request):
    if request.method== 'GET':
        id=request.GET.get("id")
        groupobj=Group.objects.get(id=id)
         #读取所有的权限信息
        Permission.objects.all()
        #读取所有权限信息，并排除以Can开头的系统默认生成的权限
        perms=Permission.objects.exclude(name__startswith='Can')
        context={'perms':perms,'groupinfo':groupobj}
        return render(request,'myadmin/auth/group/edit.html',context)
    else:
        id=request.POST.get("id")
        name=request.POST.get("name")
        prmss=request.POST.getlist("prms")
        try:
            groupobj=Group.objects.get(id=id)
            groupobj.name=name
            groupobj.save()
            groupobj.permissions.clear()
            groupobj.permissions.set(prmss)
            return HttpResponse("<script>alert('组编辑成功');location.href='/myadmin/auth/group/index';</script>")
        except:
            return HttpResponse(f"<script>alert('组编辑失败');location.href='/myadmin/auth/group/edit?id={id}';</script>")

    

        