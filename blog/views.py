from django.shortcuts import render
from blog.data import posts
from typing import Any
from django.http import Http404, HttpRequest


# Create your views here.

def blog(request:HttpRequest):

    print("home", id)
    
    context = {
        #'text': '',
        'posts': posts,
    }
    return render(request, 'blog/index.html', context)

def post(request: HttpRequest, post_id:int):

    print("home", id)

    found_post: dict[str, Any] | None = None

    for post in posts:
        
        if post['id'] == post_id:
            found_post = post
            break

    if found_post is None:
        raise Http404("Post não existe!")

    context = {
        #'text': '',
        'post': found_post,
        'title': found_post['title'] + ' - '
    }
    return render(request, 'blog/post.html', context)

def exemplo(request):
    context = {
        'text' : 'Estou em exemplo do blog',
        'title' : 'Exemplo - '
    }
    return render(request, 'blog/exemplo.html', context)