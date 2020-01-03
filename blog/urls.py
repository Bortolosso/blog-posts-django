from .views import *
from django.urls import include, path

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('<slug:slug>/', post_detail, name='post_detail'),
    path('list', PostListAll.as_view(), name='list_post'),
]