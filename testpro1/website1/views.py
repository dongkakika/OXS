from django.shortcuts import render
from .models import UserInfo
from django.views.generic import View
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import *

# Create your views here.

def index(request):
    return render(request,'website1/index.html')


def _CBNU(request):
    cbnu_infos = cbnu_info.objects.all()
    context = {'cbnu_infos': cbnu_infos}
    return render(request, "website1/_CBNU.html", context)

def _COM(request):
    com_infos = com_info.objects.all()
    context = {'com_infos': com_infos}
    return render(request, "website1/_COM.html", context)

def _JJ(request):
    jj_infos = jj_info.objects.all()
    context = {'jj_infos': jj_infos}
    return render(request, "website1/_JJ.html", context)

def _JK(request):
    jk_infos = jk_info.objects.all()
    context = {'jk_infos': jk_infos}
    return render(request, "website1/_JK.html", context)

def _JT(request):
    jt_infos = jt_info.objects.all()
    context = {'jt_infos': jt_infos}
    return render(request, "website1/_JT.html", context)

def _SW(request):
    sw_infos = sw_info.objects.all()
    context = {'sw_infos': sw_infos}
    return render(request, "website1/_SW.html", context)

def _JJD(request):
    jjd_infos = jjd_info.objects.all()
    context = {'jjd_infos': jjd_infos}
    return render(request, "website1/_JJD.html", context)

def log(request):
    return render(request, "website1/log.html")



class Login(View):
    def get(self, request):
        return render(request,'website1/login.html')
    def post(self,request):

        id=request.POST.get('userid')
        pw=request.POST.get('userpw')
        msg=False
        infos = UserInfo.objects.all()
        for info in infos:
            if info.userid == id and info.userpw == pw:
                name = info.username
                msg = True
            msg = name + '님, 로그인에 성공하셨습니다!'

            context = {
                'msg': msg,
            }

            return render(request, 'website1/result.html', context)
