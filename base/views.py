from django.http import JsonResponse
from django.shortcuts import render
from .forms import UserRegister
from .models import User


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


#
def register(request):
    form = UserRegister()
    stud = User.objects.all()
    return render(request, 'register.html', {'form': form, 'stu': stud})


def save_register(request):
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            sid = request.POST.get('stuid')
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            if (sid == ''):
                usr = User(name=name, email=email, password=password)
            else:
                usr = User(id=sid, name=name, email=email, password=password)

            usr.save()
            stud = User.objects.values()
            student_data = list(stud)
            return JsonResponse({'status': 'save', 'student_data': student_data})
        else:
            return JsonResponse({'status': 'not saved'})

# delete data


def delete_data(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        pi = User.objects.get(pk=id)
        pi.delete()
        return JsonResponse({'status': 1})
    else:
        return JsonResponse({'status': 0})


def edit_data(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        pi = User.objects.get(pk=id)
        student_data = {'id': pi.id, 'name': pi.name,
                        'email': pi.email, 'password': pi.password}

        return JsonResponse(student_data)
    else:
        return JsonResponse({'status': 0})
