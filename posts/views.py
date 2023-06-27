from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *
from .forms import *
from django.db.models import Q



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


