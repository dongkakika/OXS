from django.shortcuts import render
from .models import UserInfo
from django.views.generic import View
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    return render(request,'website1/index.html')

def _CBNU(request):
    return render(request, "website1/_CBNU.html")

def _COM(request):
    return render(request, "website1/_COM.html")

def _JJ(request):
    return render(request, "website1/_JJ.html")

def _JK(request):
    return render(request, "website1/_JK.html")

def _JT(request):
    return render(request, "website1/_JT.html")

def _SW(request):
    return render(request, "website1/_SW.html")

def _JJD(request):
    return render(request, "website1/_JJD.html")




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
