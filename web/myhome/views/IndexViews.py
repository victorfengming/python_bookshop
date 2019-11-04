from django.shortcuts import render,HttpResponse,reverse
from myadmin import models
from django.core.paginator import Paginator
from django.db.models import Q

import random
#导航中的分类及其对应的子类
def typecom():
    #找出顶级分类
    typelist=models.Booktype.objects.filter(pid=0)
    #循环顶级分类，找出子类，给顶级分类定义一个新的属性，用来寻找对应的子类
    for i in typelist:
        i.sub=models.Booktype.objects.filter(pid=i.id)
    return typelist
def usercom(request):
    userobj=models.Users.objects.get(id=request.session["User"]["id"])
    return userobj

#首页视图
def index(request):
    booklist=models.Books.objects.all()
    context={'typelist':typecom(),'booklist':booklist}
    return render(request,'myhome/index.html',context)

#列表页
def booklist(request,typeid):

    #根据分类id得到分类对象
    typeobj=models.Booktype.objects.get(id=typeid)
    #判断是不是顶级分类，
    if typeobj.pid==0:
        #如果是查询其所对应的所有的子类
        typeobj.sub=models.Booktype.objects.filter(pid=typeobj.id)
        typeobj.parent=typeobj.catename
    else:
        #如果不是，直接把对象赋给定义的属性，然后根据属性在模板直接查询其所对应的图书
        typeobj.sub=models.Booktype.objects.filter(pid=typeobj.pid)
        typeobj.parent=models.Booktype.objects.get(id=typeobj.pid).catename
    bidlist=[]
    for i in range(3):
        res=random.randrange(1,models.Books.objects.all().count())
        bidlist.append(res+50)
    print(bidlist)
    booklist=models.Books.objects.filter(id__in=bidlist)

   
    context={'typelist':typecom(),'list_detail':typeobj,'booklist':booklist}
    return render(request,'myhome/list.html',context)

#详情页
def detail(request,bookid):
    bookobj=models.Books.objects.get(id=bookid)
    booklist=models.Books.objects.all().exclude(id=bookid)
    
    context={'typelist':typecom(),'bookinfo':bookobj,'booklist':booklist}
    return render(request,'myhome/bookdetails.html',context)

#搜索图书
def booksearch(request):
    keywords=request.POST.get("keywords",'')
    bookob=models.Books.objects.all().exclude(isdel="004002")
    bookob=bookob.filter(
        Q(bookname__contains=keywords)|
        Q(author__contains=keywords)|
        Q(publisher__contains=keywords)|
        Q(price__contains=keywords)|
        Q(num__contains=keywords)
    )
    if not bookob:
        return HttpResponse("<script>alert('很抱歉没有您要搜索的内容，请重新输入！！！');location.href='/'</script>")
     # 实例化分页类    参数一数据集  参数二  每一显示的条数
    print(bookob)
    p = Paginator(bookob,5)
	# 获取当前的页码数
    pageindex =request.GET.get('page',1)
    # 获取当前页的数据
    booklist = p.page(pageindex)
    # 获取所有页码
    # pages = p.page_range
    # 获取总页数
    pages = p.num_pages
    context={'typelist':typecom(),'booklist':booklist,'page':pages}
    return render(request,'myhome/search.html',context)

