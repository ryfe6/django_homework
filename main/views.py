from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'main/home.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def students_list(request, *args, **kwargs):
    if request.method == 'POST':
        # в переменной request хранится информация о методе, который отправлял пользователь
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')
        # а также передается информация, которую заполнил пользователь
        print(name, phone, message)
    return render(request, 'main/contacts.html')
