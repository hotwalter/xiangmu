from django.urls import path,re_path

from . import views
from django.urls import converters,register_converter

#app_name = 'liuyang'
urlpatterns = [
    path('index/<id>',views.index,name='index'),
    re_path(r'login/(?P<nams>\d+)/',views.login,),
    path(r'text/',views.text,name='login'),
]