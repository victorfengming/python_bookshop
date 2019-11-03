import os
import random
import re
import time
#密码加密
from django.contrib.auth.hashers import check_password, make_password
# 导入分页类
from django.core.paginator import Paginator
#模型多条件查询
from django.db.models import Q
from django.shortcuts import HttpResponse, render, reverse

from django.contrib.auth.decorators import permission_required
from web import settings
from .. import models

# Create your views here.

##会员列表页
@permission_required('myadmin.show_Users',raise_exception=True)
def index(request):
    global ob
    ob=None
    keywords=None
    types='all'
    search=''
    if request.method=='GET':
        # 查询所有有效的会员数据 除了没有被逻辑删除的图书
        ob=models.Users.objects.all().exclude(isdel="004002")
    else:
        data=request.POST.dict()
        data.pop("csrfmiddlewaretoken")
        keywords=data["keywords"]
        keywords=keywords.strip()
        types=data["type"]
        # 没有选指定的类别时，按照所有类别进行查询
        if types=='all':
            if keywords:
                ob=models.Users.objects.filter(
                      Q(nickname__contains=keywords) |
                      Q(phone__contains=keywords) |
                      Q(homeaddress__contains=keywords) |
                      Q(sex__contains=keywords) |
                      Q(usertype__contains=keywords) 
                )
        elif types=='sex':
            if keywords=='男':
                search={types+'__contains':'1'}
            elif keywords=='女':
                search={types+'__contains':'0'}
            else:
                url=reverse("myadmin_user_index")
                return HttpResponse(f"<script>alert('没有您要查询的内容！！！');location.href='{url}'</script>")
            ob=models.Users.objects.filter(**search)  
        elif types=='usertype':
            if keywords=='老师'or keywords=='老' or keywords=='师':
                search={types+'__contains':'0'}
            elif keywords=='学生'or keywords=='学' or keywords=='生':
                search={types+'__contains':'1'}
            elif keywords=='白领' or keywords=='白' or keywords=='领':
                search={types+'__contains':'2'}
            else:
                url=reverse("myadmin_user_index")
                return HttpResponse(f"<script>alert('没有您要查询的内容！！！');location.href='{url}'</script>")
            ob=models.Users.objects.filter(**search)  
        else:
            #有指定选项类别时的查询
            search={types+'__contains':keywords}
            ob=models.Users.objects.filter(**search)  
    # 实例化分页类    参数一数据集  参数二 每一页显示的条数
    p = Paginator(ob,5)
	# 获取当前的页码数
    pageindex =request.GET.get('page',1)
    # 获取当前页的数据
    userlist = p.page(pageindex)
    # 获取所有页码
    # pages = p.page_range
    # 获取总页数
    pages = p.num_pages
    context={'userlist':userlist,'keywords':keywords,'type':types,'page':pages}
    return render(request,'myadmin/users/index.html',context)

# 会员添加函数
@permission_required('myadmin.create_Users',raise_exception=True)
def adduser(request):
    if request.method=='GET':
        return render(request,'myadmin/users/adduser.html')
    else:
        data=request.POST.dict()
        data.pop('csrfmiddlewaretoken')
        if re.findall('^1\d{10}$',data['phone']):
            if re.findall('\w{6}$',data['password']):
                #给密码进行加密
                data['password']= make_password(data['password'], None, 'pbkdf2_sha256')
                # 获取图片的路径
                filename=imgupload(request)
                try:
                    if filename:
                        data["face"]=filename
                    else:
                        # 当用户没有添加图片时进行提交时，对应的input的name会传过来
                        # 但是如果用户进行头像上传，对应的input的name属性就不会传过来
                        data.pop('face')
                    obj=models.Users(**data)
                    obj.save()
                    info='添加成功'
                    url=reverse('myadmin_user_index')
                except:
                    info='添加失败'
                    url=reverse('myadmin_user_add')
            else:
                info='请输入有效的密码'
                url=reverse('myadmin_user_add')
        else:
            info='请输入有效的手机号'
            url=reverse('myadmin_user_add')
        return HttpResponse(f"<script>alert('{info}');location.href='"+url+"'</script>")


##删除用户信息视图
@permission_required('myadmin.remove_Users',raise_exception=True)
def deluser(request,id):
    try:
        data=models.Users.objects.get(id=id)
        url='.'+data.face
        os.remove(url)
        data.isdel='004002'
        data.save()
        info='删除成功'
        url=reverse("myadmin_user_index")
        return HttpResponse(f"<script>alert('{info}');location.href='"+url+"'</script>")
    except:
        info='删除失败'
        url=reverse("myadmin_user_index")
        return HttpResponse(f"<script>alert('{info}');location.href='"+url+"'</script>")

##修改用户信息视图
@permission_required('myadmin.edit_Users',raise_exception=True)
def moduser(request):
    if request.method=='GET':
        id=request.GET.get("id")
        data=models.Users.objects.get(id=id)
        return render(request,'myadmin/users/moduser.html',{'userinfo':data})   
    else:
        data=request.POST.dict()
        data.pop('csrfmiddlewaretoken')
        try:
            filename=imgupload(request)
            if filename:
                os.remove('.'+data["old_face"])
                data["face"]=filename
            else:
                data["face"]=data["old_face"]
            data.pop("old_face")
            obj=models.Users.objects.filter(id=data["id"]).update(**data)
            info='更新成功'
            url=reverse("myadmin_user_index")
            return HttpResponse(f"<script>alert('{info}');location.href='"+url+"'</script>")
        except:
            info='更新失败'
            url=reverse("myadmin_user_mod",args=(data["id"],))
            return HttpResponse(f"<script>alert('{info}');location.href='"+url+"'</script>")

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



