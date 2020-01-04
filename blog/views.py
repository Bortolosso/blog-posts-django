from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from .models import Post
from .forms import CommentForm
from .entities import posts
from .services import post_service 

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 4

def post_detail(request, slug):
    template_name = 'post_detail.html'
    paginate_by = 1
    post = get_object_or_404(Post, slug = slug)
    comments = post.comments.filter(active = True)
    new_comment = None
    #Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data = request.POST)
        if comment_form.is_valid():
            #Create Comment object but dont`t save to database yet \ Criar objeto de comentário, mas não salve no banco de dados ainda
            new_comment = comment_form.save(commit = False)
            # Assign the current post to the comment \ Atribua a postagem atual ao comentário
            new_comment.post = post
            # Save comment to the database \ Salva comentario no banco de dados
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
    })

class PostListAll(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'posts/list_post.html'

def signup(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            username = user_form.cleaned_data.get('username')
            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username = username, password = raw_password)
            login(request, user)
            return redirect('home')
    else:
        user_form = UserCreationForm()
    return render(request, 'singup.html', {
        'user_form': user_form
    })
                   
            
