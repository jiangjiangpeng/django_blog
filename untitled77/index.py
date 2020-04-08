from django.shortcuts import render
from django.http.request import HttpRequest

def index(request):
    return render(request,'index.html', {'title': 'This is Title', 'message': 'This is message'})

def index(request=HttpRequest()):
    txt = request.GET['txt']
    context = {}
    if txt == '1':
        context['condition1'] = True
    elif txt == '2':
        context['condition2'] = True
    return render('index.html', context)