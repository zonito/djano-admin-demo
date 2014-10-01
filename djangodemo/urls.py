from django.conf.urls import patterns, include, url
from django.contrib import admin
from helloworld import views

urlpatterns = patterns(
    '',
    url(r'^add/', views.addUser),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/(?P<name>[\w\s]*)$', views.HelloWorld),
)
