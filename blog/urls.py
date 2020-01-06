from blog import views
from django.conf.urls import url
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('list', views.PostListAll.as_view(), name='list_post'),
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]