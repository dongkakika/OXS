#website1 서브앱의 urls
#서브앱의 urls는 같은 위치의 view.py의 함수로 연결을 담당(path)
#같은 이치의 views.py를 식별 못하면 import

from django.contrib import admin
from django.urls import path,include
from.import views #같은 위치의 views를 참조하게 넣어줌

urlpatterns=[
    path('', views.index, name='login'),
]