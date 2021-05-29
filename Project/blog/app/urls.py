from django.urls import path , include
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views
s
urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:user>/', userView.as_view(), name='user_page'),
]