from django.db import models


class LoopImg(models.Model):
    img1 = models.CharField(max_length=50)
    img2 = models.CharField(max_length=50)
    img3 = models.CharField(max_length=50)
    img4 = models.CharField(max_length=50)
    bg = models.CharField(max_length=50)


class User(models.Model):
    email = models.CharField(max_length=30, unique=True, null = True)
    phone = models.CharField(max_length=30, unique=True, null = True)
    password = models.CharField(max_length=256)
    token = models.CharField(max_length=256)
    name = models.CharField(max_length=30, null=True)

class Rwm(models.Model):
    rwmID = models.CharField(max_length=50)
    rwmName = models.CharField(max_length=50)
    rwmPricetype = models.CharField(max_length=50)
    rwmPrice = models.CharField(max_length=50)
    rwmdel = models.CharField(max_length=50)
    rwmImg = models.CharField(max_length=256)
    bigImg = models.CharField(max_length=50)


class Cart(models.Model):
    user = models.ForeignKey(User)
    goods = models.ForeignKey(Rwm)

    # 是否选中
    isselect = models.BooleanField(default=True)
    # 数量
    number = models.IntegerField()
    # 颜色
    color = models.CharField(max_length=20)
    # 尺寸
    size = models.CharField(max_length=20)

