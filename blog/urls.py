from django.conf.urls import include,url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post_data_input/$', views.post_data_input, name='post_data_input'),
    url(r'^post_result1/$', views.post_data_input, name='post_data_input'),
]