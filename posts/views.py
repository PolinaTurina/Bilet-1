from django.shortcuts import render
from .models import *

def post_list_view(request):
    posts = Post.objects.all()
    context = {'post_list' : posts}
    return render (request, 'posts/post_list.html', context)


