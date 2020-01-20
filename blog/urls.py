from blog import views
from django.conf.urls import url
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('list', views.PostListAll.as_view(), name='list_post'),
    path('about-user', views.about, name='about_user'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^addedpost/$', views.added_post, name='added_post'),
    path('<slug:slug>/', views.post_detail, name='post_detail')
]
