from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def new_page(request):
    return render(request, "new.html")


def servey(request):
    print(request.GET(''))
    return render(request, "servey.html")


# HTML with js Date: 31/01/2023
def calculate(request):
    return render(request, 'calculate.html')
