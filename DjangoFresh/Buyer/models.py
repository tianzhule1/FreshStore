from django.db import models
class Buyer(models.Model):
    username=models.CharField(max_length=32,verbose_name="用户名")
    password=models.CharField(max_length=32,verbose_name="密码")
    email=models.EmailField(verbose_name="用户邮箱")
    phone=models.CharField(max_length=32,verbose_name="联系电话",null=True)
    connect_address=models.TextField(max_length=32,verbose_name="联系地址",blank=True)
class Address(models.Model):
    """收货地址"""
    address=models.TextField(verbose_name="收货地址")
    recver=models.CharField(max_length=32,verbose_name="收件人")
    recv_phone=models.CharField(max_length=32,verbose_name="收件人电话")
    post_number=models.CharField(max_length=32,verbose_name="邮编")
    buyer_id=models.ForeignKey(to=Buyer,on_delete=models.CASCADE,verbose_name="用户id")
# Create your models here.
class Order(models.Model):#订单表
    """
    订单表；未支付  1；待发货  2；已发货 3； 已收货 4；已退货  0
    """
    order_id = models.CharField(max_length=32,verbose_name="id订单号")
    goods_count = models.IntegerField(verbose_name="商品订单数量")
    order_user=models.ForeignKey(to=Buyer,on_delete=models.CASCADE,verbose_name="订单用户")
    order_address=models.ForeignKey(to=Address,on_delete=models.CASCADE,verbose_name="订单地址",blank=True,null=True)
    order_price=models.FloatField(verbose_name="订单总价")#浮点型
    order_status=models.IntegerField(default=1,verbose_name="订单状态")
class OrderDetail(models.Model):#订单详情表
    order_id=models.ForeignKey(to=Order,on_delete=models.CASCADE,verbose_name="订单编号（多对一）")
    goods_id=models.IntegerField(verbose_name="商品id")
    goods_name=models.CharField(max_length=32,verbose_name="商品名称")
    goods_price=models.FloatField(verbose_name="商品价格")
    goods_number=models.IntegerField(verbose_name="商品购买数量")
    goods_total = models.FloatField(verbose_name="商品总价")
    goods_store = models.IntegerField(verbose_name="商品id")
    goods_image = models.ImageField(verbose_name="商品图片")


