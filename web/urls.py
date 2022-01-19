from django.urls import path
from . import views
from django.conf.urls import url
app_name = 'web'
urlpatterns = [
    path('', views.index, name='index'),
    path('articles/', views.articles, name='articles'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    url(r'^(?P<article_id>[0-9]+)/$', views.detail, name='detail')
]