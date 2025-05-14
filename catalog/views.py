from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from catalog.forms import ProductForm, ProductModeratorForm
from django.forms import inlineformset_factory

from catalog.models import Product, Category
from catalog.services import get_cached_products


class MyView(LoginRequiredMixin, View):
    login_url = "users/login/"
    redirect_field_name = "redirect_to"


def home(request):
    return render(request, 'catalog/home.html')

class ProductListView(ListView):
    model = Product
    template_name = "catalog/product_list.html"
    context_object_name = "product_list"


    def get_queryset(self):
        return get_cached_products()



class ProductDetailView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")



    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

    def get_success_url(self):
        return reverse("catalog:product_detail", args=[self.kwargs.get("pk")])


    def get_form_class(self):
        user = self.request.user
        if user.groups.filter().exists():
            return ProductForm
        if user == self.object.owner:
            return ProductForm
        if (
                user.has_perm("catalog.can_change_category")
                and user.has_perm("catalog.can_edit_description")
                and user.has_perm("catalog.can_edit_publication")
                and user.has_perm("catalog.can_unpublish_product")
                and user.has_perm("catalog.can_delete_product")
        ):
            return ProductModeratorForm
        raise PermissionDenied

def form_valid(self, form):
    product = form.save()
    user = self.request.user
    product.owner = user
    product.save()
    return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
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