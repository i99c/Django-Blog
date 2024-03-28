from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Yazılımcı Hanım',
        'title': 'Blog Post 1',
        'content': 'Benim ilk blog gönderim',
        'date_posted': '28 Mart 2024'
    },
    {
        'author': 'Oyuncu',
        'title': 'Blog Post 2',
        'content': 'Benim ilk ikinci gönderim',
        'date_posted': '05 Nisan 2024'
    },
]


def home(request):

    context= {
        'posts':posts
    }
    
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': "About Pages"})
