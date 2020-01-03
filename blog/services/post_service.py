from ..models import Post
from django.db import connection

def list_post():
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    return queryset

def list_post_id(id):
    post_id = Post.objects.get(id=id)
    return post_id

def delete_post(Post):
    Post.delete()

def create_post(Post):
    Post.objects.create(
        tittle = Post.tittle, 
        slug = Post.slug,
        author = Post.author,
        content = Post.content,
        status = Post.status
    ).save()

def edit_post(Post, new_post):
    Post.tittle = new_post.tittle
    Post.slug = new_post.slug
    Post.author = new_post.author
    Post.content = new_post.content
    Post.status = new_post.status
    Post.save(force_update = True)