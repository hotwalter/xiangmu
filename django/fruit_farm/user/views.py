from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect,reverse
from django.conf import urls
# Create your views here.




def index(request,id):
    s=reverse('liuyang:login')
    print(request.resolver_match.namespace)
    print(s)
    return render(request,'index.html')



def login(request,nams):
    return HttpResponse("登录页面%s"%nams)




def  text(request):
    return HttpResponse("text sucess!")