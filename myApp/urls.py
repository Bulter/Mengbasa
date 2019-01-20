from django.conf.urls import url

from myApp import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^detail/(\d+)/$', views.detail, name='detail'),
    url(r'^cart/$', views.cart, name='cart'),

    ## AJAX
    # 获取轮播图
    url(r'^loopimg/$', views.loopimg, name='loopimg'),
    url(r'^checkEP/$', views.checkEP, name='checkEP'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^checkDetail/$', views.checkDetail, name='checkDetail'),
    url(r'^addCart/$', views.addCart, name='addCart'),
]