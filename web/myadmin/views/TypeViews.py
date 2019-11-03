from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, reverse

from .. import models

# Create your views here.

#处理列表数据，然后显示父级的类别名和path对应的名称
def selectAlltype(data):
    #显示父级的类别名称和path路径对应的名称
    for i in data:
        num=i.path.count(',')-1
        i.sj='|--'*num
        #把path路径显示为分类名称，使具有可读性
        li=i.path.strip().split(',')[0:-1]
        li=[int(j)for j in li]
        if len(li)==1:
            i.pn='顶级分类'
        else:
            n=models.Booktype.objects.filter(id__in=li)
            for j in n:
                i.pn='顶级分类'+','+j.catename
                # print(i.pn)
        #把pid显示为分类名，使具有可读性
        if i.pid!=0:
            i.pname=models.Booktype.objects.get(id=i.pid).catename
    return data

#分类查询操作
@permission_required('myadmin.show_Booktype',raise_exception=True)
def index(request):
    #把数据显示成按照数据的一个类别进行排序
    #显示所有数据
    data=models.Booktype.objects.extra(select={'paths':'concat(path,id)'}).order_by("paths")

    #获取对应的请求数据
    btype=request.GET.get("btype",None)
    keywords=request.GET.get("keywords",None)

     # 根据搜索框显示符合条件的数据 
    if btype=='all' or btype=='catename':
        if keywords:
            #根据分类名和父类名查询
            data=models.Booktype.objects.filter(
                    Q(catename__contains=keywords) 
            )
    elif btype=='pname':
        search={'catename__contains':keywords}
        #根据父类名查找父类id
        if keywords.isdigit():
            return HttpResponse("<script>alert('请输入有效的类别名进行查询');location.href='/myadmin/type/index';</script>")
        ob=models.Booktype.objects.filter(**search)
        for i in ob:
            data=models.Booktype.objects.filter(pid=i.id)

    # 实例化分页类
    p = Paginator(data,5)
    # 获取当前的页码数
    pageindex = request.GET.get('page',1)
    # 获取当前页的数据
    typelist = p.page(pageindex)
    # 获取所有页码
    # pages = p.page_range
    # 获取总页数
    pages = p.num_pages
    # 最终显示的结果数据
    ob=selectAlltype(typelist)      
    context={'typelist':ob,'page':pages}
    return render(request,'myadmin/types/index.html',context)

#分类添加操作
@permission_required('myadmin.create_Booktype',raise_exception=True)
def add(request):
    ##传当前所有的分类
    data=models.Booktype.objects.extra(select={'paths':'concat(path,id)'}).order_by("paths")
    data=selectAlltype(data)
    return render(request,'myadmin/types/addtype.html',{'typelist':data})

#分类添加到数据库操作
@permission_required('myadmin.create_Booktype',raise_exception=True)
def insert(request):
    #获取请求数据
    data=request.POST.dict()   
    data.pop('csrfmiddlewaretoken')
    # 查看添加的类别名在类别表中是否存在
    num=models.Booktype.objects.filter(catename=data["catename"]).count()
    # 如果存在，提醒并返回添加别的类别名
    if num:
        url=reverse("myadmin_type_add")
        return HttpResponse(f"<script>alert('该类别已经存在，请重新选择！！！');location.href='"+url+"'</script>")
    #如果不存在，执行添加操作
    #查看它是子类还是父类
    # 如果是子类，求解相关的path路径
    if int(data["pid"])!=0:
        path=models.Booktype.objects.get(id=data["pid"]).path
        data["path"]=path+data["pid"]+','
    # 如果是父类，执行求解相关的path路径
    else:
        ##查询当前选择path
        data['path']='0,'
    try:
        obj=models.Booktype(**data)
        obj.save()
        info='添加成功'
        url=reverse("myadmin_type_index")
        return HttpResponse(f"<script>alert('{info}');location.href='"+url+"'</script>")
    except:
        info='添加失败'
        url=reverse("myadmin_type_add")
        return HttpResponse(f"<script>alert('{info}');location.href='"+url+"'</script>")

@permission_required('myadmin.remove_Booktype',raise_exception=True)       
def delete(request):
    id=request.GET.get("id")
    ##判断当前类下是否有子类
    num=models.Booktype.objects.filter(pid=id).count()
    try:
        if not num:
            ## 判断当前类型是否还有商品
            typeobj=models.Booktype.objects.get(id=id)
            goodsnum=typeobj.books_set.all().count()
            if not goodsnum:
                obj=models.Booktype.objects.get(id=id)
                obj.delete()
                return JsonResponse({'code':0,'msg':'删除成功'})
            else:
                return JsonResponse({'code':2,'msg':'该类别下有商品不能删除'})
        else:
            return JsonResponse({'code':1,'msg':'删除失败，有子分类'})
    except:
        return JsonResponse({'code':1,'msg':'删除失败，操作异常'})

@permission_required('myadmin.edit_Booktype',raise_exception=True)
def edit(request):
    try:
        id=request.GET.get("id")
        catename=request.GET.get("catename")
        obj=models.Booktype.objects.get(id=id)
        obj.catename=catename
        obj.save()
        return JsonResponse({'code':0,'msg':'更新成功'})
    except:
        return JsonResponse({'code':1,'msg':'更新失败'})

