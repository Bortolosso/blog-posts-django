from blog import views
from django.conf.urls import url
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('slug', views.post_detail, name='post_detail'),
    path('list', views.PostListAll.as_view(), name='list_post'),
    # path('register', views.register, name='register'),
    # path('user_login', views.user_login, name='user_login'), 
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
]