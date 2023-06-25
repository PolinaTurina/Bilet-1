from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *
from .forms import *



def post_list_view(request):
    posts = Post.objects.all()

    if request.method == 'POST':
        form = PostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    context = {'post_list' : posts, 'post_form': form}
    return render (request, 'posts/post_list.html', context)


