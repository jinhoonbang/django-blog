from django.conf.urls import url
from django.contrib import admin

from . import views

#from posts import views
#use from posts import views as post_view

urlpatterns = [
    url(r'^$', "posts.views.post_list"),
    url(r'^create/$', "posts.views.post_create"),
    url(r'^detail/$', "posts.views.post_detail"),
    url(r'^update/$', "posts.views.posupdatete"),
    url(r'^delete/$', "posts.views.posdeletete"),
]
