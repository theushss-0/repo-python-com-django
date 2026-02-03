from django.shortcuts import render
from blog.data import posts


# Create your views here.

def blog(request):

    print("home", id)
    
    context = {
        #'text': '',
        'posts': posts,
    }
    return render(request, 'blog/index.html', context)

def post(request, post_id):

    print("home", id)

    found_post = None

    for post in posts:
        
        if post['id'] == post_id:
            found_post = post
            break


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