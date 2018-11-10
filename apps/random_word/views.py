from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string #import random string module

# Create your views here.
def index(request):
    word = get_random_string(length=14)

    if 'attempts' in request.session:
        request.session['attempts'] += 1
    else:
        request.session['attempts'] = 0

    request.session['word'] = word
    return render(request, "random_word/index.html")

def reset(request): 
    request.session.clear()
    return redirect("/")