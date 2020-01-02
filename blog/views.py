from django.views import generic
from .models import Post
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 4

# def post_list(request):
#     object_list = Post.objects.filter(status=1).order_by('-created_on')
#     paginator = Paginator(object_list, 6)  # 6 posts in each page
#     page = request.GET.get('page')
#     try:
#         post_list = paginator.page(page)
#     except PageNotAnInteger:
#             # If page is not an integer deliver the first page \ Se a página não for um número inteiro, entregue a primeira página 
#         post_list = paginator.page(1)
#     except EmptyPage:
#         # If page is out of range deliver last page of results \ Se a página estiver fora do intervalo, entregue a última página de resultados
#         post_list = paginator.page(paginator.num_pages)
#     return render(request,
#                   'index.html',
#                   {'page': page,
#                    'post_list': post_list})

# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'post_detail.html'

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