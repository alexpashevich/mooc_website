from django.conf.urls import patterns, include, url
# from django.contrib import admin
from moocs import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^moocs/(?P<mooc_id>\d+)/$', views.mooc, name='mooc'),
    url(r'^lessons/(?P<lesson_id>\d+)/$', views.lesson, name='lesson'),
    url(r'^register/$', views.register, name='register'),
    url(r'^load_description_full/$', views.load_description_full, name='load_description_full')
)