
from django.shortcuts import render,HttpResponse
from .. import models

# Create your views here.

def index(request):
    orderdata=models.Order.objects.all()
    context={'orderdata':orderdata}
    return render(request,'myadmin/order/index.html',context)


