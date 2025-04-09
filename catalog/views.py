from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from catalog.models import Product


def home(request):
    return render(request, 'catalog/home.html')


def products_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request,'catalog/products_list.html', context)

def product_detail(request, pk):
    product = get_object_or_404(Product,pk=pk)
    context = {"product": product}
    return render(request, 'catalog/product_detail.html', context)

def contacts(request):
    if request.method == 'POST':
        # Получение данных из формы
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        # Обработка данных (например, сохранение в БД, отправка email и т. д.)
        print(name)
        print(phone)
        print(message)
        # Здесь мы просто возвращаем простой ответ
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено. Уже набираем Ваш номер!")
    return render(request, 'catalog/contacts.html')

