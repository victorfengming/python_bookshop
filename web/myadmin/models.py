from django.db import models

# Create your models here.

#会员类 包括前台用户所有的信息
class Users(models.Model):
    #主要信息
    phone=models.CharField(max_length=11,unique=True)#s手机号
    password=models.CharField(max_length=80)#密码
    face=models.CharField(max_length=100,default="/static/myadmin/assets/img/user06.png")#头像
    #次要信息
    nickname=models.CharField(max_length=20,null=True)#昵称
    homeaddress=models.CharField(max_length=100,null=True)#居住地
    sex=models.CharField(max_length=6,null=True)#性别
    usertype=models.CharField(max_length=1,null=True)#身份类别
    createtime=models.DateTimeField(auto_now_add=True)#创建时间
    isdel=models.CharField(max_length=10,default='004001')#是否删除
    #自定义用户权限
    class Meta:
        permissions = (
            ("show_Users", "查看用户列表"),
            ("create_Users", "添加用户"),
            ("edit_Users", "修改用户"),
            ("remove_Users", "删除用户"),
        )

#图书分类类
class Booktype(models.Model):
    catename=models.CharField(max_length=20)#分类名
    pid=models.IntegerField()#父级id
    path=models.CharField(max_length=50)#path路径
#自定义商品分类权限
    class Meta:
        permissions = (
            ("show_Booktype", "查看图书分类列表"),
            ("create_Booktype", "添加图书分类"),
            ("edit_Booktype", "修改图书分类"),
            ("remove_Booktype", "删除图书分类"),
        )

#图书类
class Books(models.Model):
    typeid=models.ManyToManyField(to="Booktype")#图书类别id 用作外键联系类别类
    bookname=models.CharField(max_length=70) #图书名称
    recommend=models.CharField(max_length=255,null=True) #推荐语
    author=models.CharField(max_length=50) #作者
    publisher=models.CharField(max_length=150) #出版社
    pdate=models.DateField() #出版时间
    price=models.DecimalField(max_digits=5,decimal_places=2) #价格
    num=models.IntegerField()#库存
    isbn=models.CharField(max_length=13)# 国际书号isbn
    bookdetail=models.TextField(null=True) #商品详情
    cate=models.CharField(max_length=1,default='0') #0上架 1热卖 2促销  3推荐 4下架
    isdel=models.CharField(max_length=6,default="004001") #是否逻辑删除  004001可用  004002不可用
#自定义图书权限
    class Meta:
        permissions = (
            ("show_Books", "查看图书列表"),
            ("create_Books", "添加图书"),
            ("edit_Books", "修改图书"),
            ("remove_Books", "删除图书"),
        )

##图集
class Bookimgs(models.Model):
    img_url=models.ImageField(upload_to="static/myadmin/book_img/")#图书图片地址
    bookid=models.ForeignKey('Books',on_delete=models.CASCADE)#图书id  用来联系图书类


#购物车
class Cart(models.Model):
    #用户ID
    # 商品id
    # 数量
    # 是否选中
    uid=models.ForeignKey('Users',on_delete=models.CASCADE) #会员id  当做外键  用来联系用户类
    bookid=models.ForeignKey('Books',on_delete=models.CASCADE)#图书id 当做外键  用来联系图书类
    num=models.IntegerField()#图书商品的数量
    select=models.IntegerField(default=0)#0未选中  1选中
    # 前端业务的数据是可以被修改的，所以前端价格不能获取，展出的数据不一定真，能用id获取就不要用其他地方获取

class Order(models.Model):
    # 订单号  # uid  # 收货信息
    # 商品信息  # 总价  # 状态 0  1 2 3
    # 创建时间  # 支付时间
    uid=models.ForeignKey('Users',on_delete=models.CASCADE)#用户id  当做外键  用来联系用户类
    username=models.CharField(max_length=10)#收货人姓名
    phone=models.CharField(max_length=11)#收货人电话
    address=models.CharField(max_length=100)#收获人地址
    totalprice=models.DecimalField(max_digits=7,decimal_places=2)#此次购买物品的总价
    # 0未支付  1 已支付  2已发货  3已收货 4已取消
    status=models.IntegerField(default=0)#订单状态
    ordertime=models.DateTimeField(auto_now_add=True)#创建订单的时间
    paytime=models.DateTimeField(null=True)#支付时间
#自定义订单权限
    class Meta:
        permissions = (
            ("show_Order", "查看订单列表"),
            ("create_Order", "添加订单"),
            ("edit_Order", "修改订单"),
            ("remove_Order", "删除订单"),
        )

class OrderItem(models.Model):
    # 订单号  商品id  商品数量 商品价格
    orderid=models.ForeignKey('Order',on_delete=models.CASCADE)#订单id  外键  用作联系订单类
    bookid=models.ForeignKey('Books',on_delete=models.CASCADE)#图书id  外键  用作联系图书id
    num=models.IntegerField()#记录购买同一种商品的数量
    price=models.IntegerField()#价格

class Address(models.Model):
    # 本身id  收货人姓名  电话   收货地址 
    # 会员id   是否默认  是否删除  
    username=models.CharField(max_length=30)#收货人姓名
    phone=models.CharField(max_length=11)#收货人电话
    user_address=models.CharField(max_length=200)#收货人地址
    uid=models.ForeignKey('Users',on_delete=models.CASCADE)#会员ID  外键 用来联系会员ID 
    isdefault=models.CharField(max_length=1,default=0)#0不默认  1默认  是否默认
    isdel=models.CharField(max_length=1,default=0)  #0否  1删除  是否删除







    

    

