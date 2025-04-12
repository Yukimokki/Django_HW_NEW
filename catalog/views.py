from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.models import Product


def home(request):
    return render(request, 'catalog/home.html')

class ProductListView(ListView):
    model = Product
    template_name = "catalog/product_list.html"
    context_object_name = "product_list"


class ProductDetailView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class ProductCreateView(CreateView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'description', 'preview', 'category', 'price']
    success_url = reverse_lazy("catalog:product_list")

    def get_success_url(self):
        return reverse("catalog:product_detail", args=[self.kwargs.get("pk")])


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")

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


# def products_list(request):
#     products = Product.objects.all()
#     context = {"products": products}
#     return render(request,'catalog/products_list.html', context)
#
# def product_detail(request, pk):
#     product = get_object_or_404(Product,pk=pk)
#     context = {"product": product}
#     return render(request, 'catalog/product_detail.html', context)