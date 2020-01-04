from .views import *
from django.urls import include, path
from django.conf.urls import url

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('<slug:slug>/', post_detail, name='post_detail'),
    path('list', PostListAll.as_view(), name='list_post'),
    path(r'^sigup/$', signup, name='signup'),
]