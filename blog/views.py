from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from .models import Post
from .forms import CommentForm, UserForm, UserProfileInfoForm, UserPostForm


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 10


@login_required
def added_post(request):
    template_name = 'posts/form_post.html'
    if request.method == 'POST':
        new_post = UserPostForm(data=request.POST)
        if new_post.is_valid():
            temp = new_post.save(commit=False)
            temp.author = request.user
            temp.save()
            return redirect('/')
    else:
        new_post = UserPostForm()

    return render(request, template_name, {
        'new_post': new_post
    })


def post_detail(request, slug):
    template_name = 'post_detail.html'
    paginate_by = 1
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but dont`t save to database yet \ Criar objeto de comentário, mas não salve no banco de dados ainda
            new_comment = comment_form.save(commit=False)
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


def index(request):
    return render(request, 'index.html')


@login_required
def special(request):
    template_name = 'index.html'
    return render(request, template_name)


@login_required
def user_logout(request):
    template_name = 'signup/form_login.html'
    logout(request)
    logout_account = HttpResponse(reverse('index'))
    return render(request, template_name)


def register(request):
    template_name = 'signup/form_register.html'
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            # if 'profile_pic' in request.FILES:
            # print('found it')
            # profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, template_name,
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})


def user_login(request):
    template_name = 'signup/form_login.html'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Your account was inactive.')
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, template_name, {})
