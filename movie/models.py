from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import datetime


# Create your models here.
class User(models.Model):
    userName = models.CharField(max_length=50,verbose_name='用户名')
    userPassword = models.CharField(max_length=50,null=True,verbose_name='密码',default="")
    userRegisterTime = models.DateTimeField(verbose_name='注册时间')
    userValidTime = models.CharField(max_length=20,verbose_name='有效时间',default="")
    userGrant = models.IntegerField(default=0,null=True,verbose_name='权限')
    userPreference = models.CharField(max_length=50,verbose_name='喜好',default="")
    class Meta:
        db_table = 'user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name
    def __repr__(self):
        return "<User:%r>" % self.UserName


class Film(models.Model):
    filmName = models.CharField(max_length=50,verbose_name='电影名称')
    filmBrief = models.CharField(max_length=500,verbose_name='电影简介')
    filmType = models.CharField(max_length=50,verbose_name='电影类型')
    filmCover = models.ImageField('封面图片',upload_to='uploads')
    filmPurl = models.CharField(max_length=255, verbose_name="播放地址")
    filmRelease_time = models.DateTimeField(verbose_name='上映时间')
    filmPlay_times = models.IntegerField(verbose_name='观看次数')
    filmLove = models.IntegerField(verbose_name='点赞次数')
    filmPermisson = models.IntegerField(verbose_name='观看权限')
    filmIsTop = models.BooleanField(default=False,verbose_name="置顶封面")
    filmWeight = models.IntegerField(default=0,verbose_name='电影权重')


    class Meta:
        db_table = 'film'
        verbose_name = '电影'
        verbose_name_plural = verbose_name

    def __repr__(self):
        return "<Film:%r>" % self.name











