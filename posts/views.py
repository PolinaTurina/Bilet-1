from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import *
from .forms import *
from django.db.models import Q


def post_detail_view(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.post = post
            comment.save()
            form = CommentForm()
    else:
        form = CommentForm()

    comments = Comment.objects.filter(post=post) 

    context = {'post_detail': post, 'comments': comments, 'comment_form': form}
    return render(request, 'posts/post_detail.html', context)



def post_list_view(request):

    q = request.GET.get('q', '')
    if q:
        posts= Post.objects.filter(Q(title__icontains=q) | Q(create_date__icontains=q))
    else:
        posts = Post.objects.all()
    


    if request.method == 'POST':
        form = PostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts')
    else:
        form = PostForm()
    context = {'post_list' : posts, 'post_form': form}
    return render (request, 'posts/post_list.html', context)


