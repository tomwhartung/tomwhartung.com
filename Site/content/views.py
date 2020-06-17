
from django.shortcuts import render


def home(request):
    title = 'Home - TomWHartung.com';
    template = 'content/home.html'
    context = {
        'title': title,
    }
    return render(request, template, context)
