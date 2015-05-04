#coding:utf-8
from django.db import models

# Create your models here.
class CoustomersInfo(models.Model):
    """custom info table"""
    uid = models.AutoField(0)
    username = models.CharField(max_length = 50)
    email = models.EmailField()
    telephone = models.CharField(max_length = 11)
    passward = models.CharField(32)
    salt = models.CharField(10)                        #this for md5 salt
    registertime = models.DateTimeField()              #register date time
    latestloginin = models.DateTimeField()             #latest login in time

class ItemsInfo(models.Model):
    """items for sale table"""
    iid = models.AutoField(0)
    item_name = models.CharField(max_length = 50)
    item_description = models.TextField()
    item_onsale = models.BooleanField()
    item_sale_price = models.DecimalField()
    item_old_price = models.DecimalField()
    item_on_date = models.DateField()
    item_off_date = models.DateField()

class OrderInfo(models.Model):
    """order info table"""
    oid = models.AutoField(0)
    uid = models.IntegerField()
    did = models.IntegerField()
    total_cost = models.DecimalField()
    datetime = models.DateTimeField()                   #订单生成详细时间

class OrderDetailInfo(models.Model):
    """order detail info to order id"""
    did = models.AutoField(0)
    detail = models.CharField()                         #订单详细内容
    




    
    

 
    

    

    
    
    
    