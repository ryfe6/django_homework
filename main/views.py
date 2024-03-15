from django.shortcuts import render, get_object_or_404

from main.models import Product


# Create your views here.


def product_list(request):
    """Вывод шаблона с информацией о продукте"""
    items = Product.objects.all()
    context = {'object_list': items}
    return render(request, 'main/product_list.html', context)


def contacts(request):
    """Вывод шаблона с контактной информацией"""
    return render(request, 'main/contacts.html')


def product_view(request, pk):
    item = get_object_or_404(Product, pk=pk)
    context = {'item': item}
    return render(request, 'main/product_view.html', context)


def students_list(request, *args, **kwargs):
    if request.method == 'POST':
        # в переменной request хранится информация о методе, который отправлял пользователь
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')
        # а также передается информация, которую заполнил пользователь
        print(name, phone, message)
    return render(request, 'main/contacts.html')
