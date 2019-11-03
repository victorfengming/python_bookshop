from django.shortcuts import render,reverse
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import permission_required
from django.core.paginator import Paginator
from django.db.models import Q
from .. import models
from .import TypeViews
import re,os

# Create your views here.
#查看图书视图
@permission_required('myadmin.show_Books',raise_exception=True)
def index(request):
    ##接收参数
    keywords=request.GET.get("keywords",'')
    keywords=keywords.strip()
    fieldname=request.GET.get("fieldname",None)
    ob=models.Books.objects.all().exclude(isdel="004002")
    if fieldname:
        if fieldname=='all':
            if keywords:
               
                ob=ob.filter(
                    Q(bookname__contains=keywords)|
                    Q(author__contains=keywords)|
                    Q(publisher__contains=keywords)|
                    Q(price__contains=keywords)|
                    Q(num__contains=keywords)
                )
        else:
            search={fieldname+'__contains':keywords}
            ob=ob.filter(**search)
    # 实例化分页类    参数一数据集  参数二  每一显示的条数
    p = Paginator(ob,5)
	# 获取当前的页码数
    pageindex =request.GET.get('page',1)
    # 获取当前页的数据
    booklist = p.page(pageindex)
    # 获取所有页码
    # pages = p.page_range
    # 获取总页数
    pages = p.num_pages
    context={'booklist':booklist,'page':pages,'fieldname':fieldname,'keywords':keywords}
    return render(request,'myadmin/books/index.html',context)

#添加视图
@permission_required('myadmin.create_Books',raise_exception=True)
def add(request):
    data=models.Booktype.objects.extra(select={'paths':'concat(path,id)'}).order_by("paths")
    types=TypeViews.selectAlltype(data)
    return render(request,'myadmin/books/addbook.html',{'typelist':types})

@permission_required('myadmin.create_Books',raise_exception=True)
def insert(request):
   
    # 获取表单的内容
    data=request.POST.dict()
    data.pop("csrfmiddlewaretoken")
    # 弹出typeid，因为分类与图书的关系是多对多，所以他们的关系存在另外一张表里
    data.pop("typeid")
    #获取图书的图片集合
    try:
        imglist=request.FILES.getlist("pics")
        if len(imglist)!=3:
            data.pop("pics")
        #获取对应的所属分类id ，然后存入相应的表里，多对多的关系
        typeid=request.POST.getlist("typeid")
        if not typeid:
            return HttpResponse(f"<script>alert('请为选择分类项');location.href='{url}''</script>")
        if not data["recommend"]:
            data.pop("recommend")
        if not re.findall('^\d+?\.\d{2}$',data["price"]):
            return HttpResponse(f"<script>alert('请输入有效的售价');location.href='{url}'</script>")
        if not re.findall('\d{13}',data["isbn"]):
            return HttpResponse(f"<script>alert('请输入有效的国际书号');location.href='{url}'</script>")
        if not  re.findall('\d',data["num"]):
            return HttpResponse(f"<script>alert('请输入有效的库存数量');location.href='{url}'</script>")

        ##创建书籍对象，完成添加，获取图书的对象
        obj=models.Books(**data)
        obj.save()


        #根据获取的id得到分类模型里的对象，然后存入多对多的关系里
        typeobjs=models.Booktype.objects.filter(id__in=typeid)
        ##给书籍和分类设置关系，必须是在对象保存之后才能在多对多的表里面添加对应的分类的关系
        obj.typeid.set(typeobjs)
    
        # 判断是否上传了图片，如果上传了，就删除文件夹中的就图片，没上传，就不用删除
        if imglist:
            for i in imglist:
                img_obj=models.Bookimgs()
                img_obj.bookid=obj
                img_obj.img_url=i
                img_obj.save()
                url=reverse('myadmin_book_index')
            return HttpResponse(f"<script>alert('添加成功');location.href='{url}'</script>")
        else:
            url=reverse("myadmin_book_add")
            return HttpResponse(f"<script>alert('请为书籍添加一张或多张封面图');location.href='{url}';</script>")
    except:
        url=reverse("myadmin_book_add")
        return HttpResponse(f"<script>alert('操作异常，请稍后再试！！！');location.href='{url}';</script>")
  
@permission_required('myadmin.remove_Books',raise_exception=True)
def delete(request):
    id=request.GET.get("id")
    obj=models.Books.objects.get(id=id)
    #先删除对应文件夹里的图片，然后删除对应关系，最后删除图书商品
    for i in obj.bookimgs_set.all():
        os.remove(i.img_url.path)
    #删除对应的分类关系
    obj.delete()

    # data.isdel="004002"
    # data.save()
    return JsonResponse({"code":0,"msg":"删除成功"})

@permission_required('myadmin.edit_Books',raise_exception=True)
def edit(request):
    id=request.GET.get("id")
    data=models.Books.objects.get(id=id)
    return render(request,'myadmin/books/editbook.html',{'bookinfo':data})

@permission_required('myadmin.edit_Books',raise_exception=True)
def update(request):
    #获取图片数据
    data=request.POST.dict()
    data.pop("csrfmiddlewaretoken")
    # 处理图片
    # 判断是否上传了图片，如果上传了，就删除文件夹中的就图片，没上传，就不用删除
    try:
        img_url=request.FILES.get('img_url',None)
        # 用户上传了图片
        if img_url:
            url='./'+data["old_img_url"]
            if data["old_img_url"]:
                os.remove(url)
            obj=models.Books.objects.get(id=data["id"])
            imgxx={'img_url':data["old_img_url"],'bookid':obj}
            #查询旧图片在表里所对应的删除，然后删除
            img_obj=models.Bookimgs.objects.filter(**imgxx)
            img_obj.delete()
            # 实例化一个图书图集对象，在图集类里添加用户上传的新的图片，然后保存
            img_obj=models.Bookimgs()
            img_obj.bookid=obj
            img_obj.img_url=img_url
            img_obj.save()
        else:
            data.pop("img_url")
        data.pop("old_img_url")
        
        # 处理图书的数据,更新已修改的数据
        if not data["recommend"]:
            data.pop("recommend")
        if re.findall('^\d+?\.\d{2}$',data["price"]):
            if re.findall('\d{13}',data["isbn"]):
                ob=models.Books.objects.filter(id=data["id"]).update(**data)
                info='修改成功'
                url=reverse('myadmin_book_index')     
                return HttpResponse(f"<script>alert('{info}');location.href='"+url+"';</script>")
        else:
            info='修改失败，请输入有效的值'
            url=reverse('myadmin_book_edit')
            id=str(data["id"])
            return HttpResponse(f"<script>alert('{info}');location.href='{url}?id={id}';</script>")
    except:
        url=reverse('myadmin_book_edit')
        id=str(data["id"])
        return HttpResponse(f"<script>alert('程序异常，请稍后再试！！！');location.href='{url}?id={id}';</script>")
  
