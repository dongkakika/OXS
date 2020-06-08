#website1 서브앱의 urls
#서브앱의 urls는 같은 위치의 view.py의 함수로 연결을 담당(path)
#같은 이치의 views.py를 식별 못하면 import

from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from.import views #같은 위치의 views를 참조하게 넣어줌

urlpatterns=[
    path('', views.index, name='login'),
    url(r'^$', views.index),
    url(r'index.html/$', views.index),
    url(r'_CBNU.html/$', views._CBNU),
    url(r'_COM.html/$', views._COM),
    url(r'_JJ.html/$', views._JJ),
    url(r'_JJD.html/$', views._JJD),
    url(r'_SW.html/$', views._SW),
    url(r'_JK.html/$', views._JK),
    url(r'_JT.html/$', views._JT),
    url(r'log.html/$', views.log)

]