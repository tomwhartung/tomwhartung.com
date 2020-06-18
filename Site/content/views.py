
from django.shortcuts import render


def home(request):

    """ View for the Home page """

    title = 'Home - TomWHartung.com';
    template = 'content/home.html'
    context = {
        'title': title,
    }
    return render(request, template, context)


def not_found(request, unknown_page='unknown_page'):

    """ Render the 404 not found template """

    template = 'content/404.html'
    context = {
        'unknown_page': unknown_page,
    }
    return render(request, template, context)
