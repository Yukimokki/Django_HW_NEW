from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path,include
from catalog.apps import CatalogConfig
from users.views import UserLoginView
from catalog.views import home, contacts, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('catalog/', ProductListView.as_view(), name='product_list'),
    path('catalog/product/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('catalog/product/create', ProductCreateView.as_view(), name='product_create'),
    path('catalog/product/<int:pk>/update', ProductUpdateView.as_view(), name='product_update'),
    path('catalog/product/<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),
    path('users/login/', UserLoginView.as_view(template_name="users/login.html"), name="login"),
]

# urlpatterns = [
#     path('', home, name='home'),
#     path('contacts/', contacts, name='contacts'),
#     path('catalog/', ProductListView.as_view(), name='product_list'),
#     path('catalog/product/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
#     path('catalog/product/create', ProductCreateView.as_view(), name='product_create'),
#     path('catalog/product/<int:pk>/update', ProductUpdateView.as_view(), name='product_update'),
#     path('catalog/product/<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),
# ]