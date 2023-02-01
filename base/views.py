from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def new_page(request):
    return render(request, "new.html")
