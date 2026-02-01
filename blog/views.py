from django.shortcuts import render
from blog.data import posts


# Create your views here.

def blog(request):
    
    context = {
        'text': '',
        'posts': posts,
    }
    return render(request, 'blog/index.html', context)

def exemplo(request):
    context = {
        'text' : 'Estou em exemplo do blog',
        'title' : 'Exemplo - '
    }
    return render(request, 'blog/exemplo.html', context)