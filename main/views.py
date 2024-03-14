from django.shortcuts import render

from main.models import Product


# Create your views here.


def product_list(request):
    items = Product.objects.all()
    context = {'object_list': items}
    return render(request, 'main/product_list.html', context)


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
