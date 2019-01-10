from django.conf.urls import url

from myApp import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),

]