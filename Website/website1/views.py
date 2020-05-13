from django.shortcuts import render
from .models import UserInfo
from django.views.generic import View
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.

class Login(View):
    def get(self, request):
        return render(request,'main/login.html')
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

            return render(request, 'main/result.html', context)
