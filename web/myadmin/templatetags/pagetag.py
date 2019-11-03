from django import template

#转义HTML标签  转义成实体符  &nbsp;
from django.utils.html import format_html

register = template.Library()

@register.simple_tag
def cheng(a,b):
    res=a*b
    return res






@register.simple_tag
# 定义分页优化的函数
def PageShow(count,request):
    # count 是总页数
    # request 请求对象
    # count = int(count)

    # p接收当前的页码数
    p = int(request.GET.get('page',1))


    # 获取url中的所有参数
    data = request.GET.dict()
    
    print(count,type(count))

    args = ''
    for k,v in data.items():
        if k != 'page':
            args += '&'+k+'='+v
    
    # 开始
    start = p-5
    # 结束
    end = p+4
    # 判断当前页是否小于5
    if p <= 5:
        start = 1
        end = 10
    # 判断当前页大于总页数
    if p > count-5:
        start = count-5
        end = count
    # 判断总页数小于10
    if count < 10:
        start = 1
        end = count

    pageHtml = ''
    # 首页
    pageHtml += '<li><a href="?page=1{args}">首页</a></li>'.format(args=args)
    # 上一页
    if p>1:
        pageHtml += '<li><a href="?page={p}{args}">上一页</a></li>'.format(p=p-1,args=args)
    for x in range(start,end+1):
        if p == x:
            pageHtml += '<li class="am-active"><a href="?page={p}{args}">{p}</a></li>'.format(p=x,args=args)
        else:
            pageHtml += '<li><a href="?page={p}{args}">{p}</a></li>'.format(p=x,args=args)
    # 下一页
    if p<count:
        pageHtml += '<li><a href="?page={p}{args}">下一页</a></li>'.format(p=p+1,args=args)
    # 尾页
    pageHtml += '<li><a href="?page={p}{args}">尾页</a></li>'.format(p=count,args=args)
    return format_html(pageHtml)


