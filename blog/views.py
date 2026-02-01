from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def blog(request):
    
    context = {
        'text': 'Estou no Blog',
        'title': 'Blog - '
    }
    return render(request, 'blog/index.html', context)

def exemplo(request):
    context = {
        'text' : 'Estou em exemplo do blog',
        'title' : 'Exemplo - '
    }
    return render(request, 'blog/exemplo.html', context)