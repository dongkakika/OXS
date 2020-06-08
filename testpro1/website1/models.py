from django.db import models
from django.utils import timezone

# Create your models here.
# 내가 원하는 자료의 형태를 클래스로 정의하기(단일 자료의 형태)

class UserInfo(models.Model):
    username=models.CharField(max_length=20)
    userid=models.CharField(max_length=20)
    userpw=models.CharField(max_length=20)

class Crawlingdata(models.Model):
    Name = models.CharField(max_length=30)
    Period = models.CharField(max_length=50)


