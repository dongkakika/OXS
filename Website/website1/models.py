from django.db import models

# Create your models here.
# 내가 원하는 자료의 형태를 클래스로 정의하기(단일 자료의 형태)

class UserInfo(models.Model):
    username=models.CharField(max_length=20)
    userid=models.CharField(max_length=20)
    userpw=models.CharField(max_length=20)
