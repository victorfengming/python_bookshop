from django.shortcuts import render,reverse
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.hashers import check_password, make_password
from myadmin import models
import requests,random
from .IndexViews import typecom,usercom
# Create your views here.

def register(request):
    context={'typelist':typecom()}
    return render(request,'myhome/login/register.html',context)


def doregister(request):
    data={}
    # 验证验证码
    vcode=request.POST.get("vcode")
    data["phone"]=request.POST.get("phone")
    if (data["phone"]==request.session["msgcode"]["phone"]) and (vcode==request.session["msgcode"]["vcode"]):
        data["password"]=request.POST.get("password")
        data['password']= make_password(data['password'], None, 'pbkdf2_sha256')
        try:
            obj=models.Users(**data)
            obj.save()
            url=reverse('myhome_login')
            return HttpResponse(f"<script>alert('恭喜你，注册成功');location.href='{url}'</script>")
        except:
            url=reverse('myhome_register')
            return HttpResponse(f"<script>alert('注册失败请重新注册');location.href='{url}'</script>")
    else:
        url=reverse("myhome_register")
        return HttpResponse(f"<script>alert('手机号或验证码出错');location.href='"+url+"'</script>")

def checkphone(request):
    phone=request.GET.get('phone')
    num=models.Users.objects.filter(phone=phone).count()
    if num:
       return JsonResponse({'code':1,'msg':'手机号已存在'})
    else:
        return JsonResponse({'code':0,'msg':'手机号可注册'})

def sendphone(request):
    phone=request.GET.get('phone')
    vcode=str(random.randint(10000,99999))
    request.session['msgcode']={'vcode':vcode,'phone':phone}
    if SendCode(phone,vcode):
        return JsonResponse({'code':0,'msg':'短信已发送，请注意查收','vcode':vcode})
    else:
        return JsonResponse({'code':1,'msg':'短信验证码发送失败','vcode':vcode})

# #发送请求给发送验证码的网站，然后获取
# def sendcode(phone,vcode):
#     url='http://106.ihuyi.com/webservice/sms.php?method=Submit'
#     text='您的验证码是：'+vcode+'。请不要把验证码泄露给其他人。'
#     data= {
#         'account':'C57099558',
#         'password':'4953e63f47bc4cdcd6ddf02aeca62482',
#         'mobile':phone,
#         'content':text,
#         'format':'json'
#         }
#     res=requests.post(url=url,data=data)
#     res=res.json()
#     print(res)
#     # {'code': 2, 'msg': '提交成功', 'smsid': '15718313248346759898'}
#     if res["code"]==2 and res["msg"]=='提交成功':
#         return True
#     else:
#         return False


def SendCode(phone,vcode):
	url = 'https://open.ucpaas.com/ol/sms/sendsms'
	data = {
			'sid':'4c0064b5f77af9da37fb74145594092e',
			'token':'1db32087f3b4111610f753a4ded823c1',
			'appid':'328129a7423b4bf595bc4435e80f8e1c',
			'templateid':'510851',
			'param':vcode,
			'mobile':phone
		}
	headers = {
			'Content-Type':'application/json'
	}

	response = requests.post(url,json=data,headers=headers)

	res = response.json()

	if res['code'] == '00000' and res['msg'] == 'OK':
		return True
	else:
		return False
