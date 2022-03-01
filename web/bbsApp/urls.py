from django.urls import path
from bbsApp import views

urlpatterns = [
    path('index/', views.index, name='bbsIndex'),
    path('joinForm/', views.joinForm, name='joinForm'),
    path('login/', views.bbsLogin, name='bbsLogin'),
    path('bbsList/', views.bbsList, name='bbsList'),
    path('bbsRegisterForm/', views.bbsRegisterForm, name='bbsRegisterForm'),
    path('logOut/',views.bbsLogOut, name='bbsLogOut'),
    path('uploadForm/',views.uploadForm, name='uploadForm'),
    path('bbsRead/',views.bbsRead, name='bbsRead'),
]