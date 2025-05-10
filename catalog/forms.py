from django.forms import ModelForm, BooleanField, ValidationError
from .models import Product, Category
from django.core.validators import MaxLengthValidator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View


class MyView(LoginRequiredMixin, View):
    login_url = "/login/"
    redirect_field_name = "redirect_to"


class StyleFormMixin:
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = "form-check-input"
            else:
                field.widget.attrs['class'] = "form-control"


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        exclude = ("views_counter","owner")

    def clean_name(self):
        list_forbidden_words = [
            "казино",
            "криптовалюта",
            "крипта",
            "биржа",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        ]
        product_name = self.cleaned_data["name"]
        for item in list_forbidden_words:
            if item in product_name:
                raise ValidationError("Вы внесли недопустимое слово в название продукта")
        return product_name

    def clean_description(self):
        list_forbidden_words = [
            "казино",
            "криптовалюта",
            "крипта",
            "биржа",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        ]
        product_description = self.cleaned_data["description"]
        for item in list_forbidden_words:
            if item in product_description:
                raise ValidationError("Invalid description. Are you a scammer? Ст. УК РФ 159")
        return product_description


    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise ValidationError ("Price cannot be negative!")
        else:
            return price


class ProductModeratorForm(LoginRequiredMixin, StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = ("description","category","is_published")

    def clean_name(self):
        list_forbidden_words = [
            "казино",
            "криптовалюта",
            "крипта",
            "биржа",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        ]
        product_name = self.cleaned_data["name"]
        for item in list_forbidden_words:
            if item in product_name:
                raise ValidationError("Invalid name")
        return product_name


    def clean_description(self):
        list_forbidden_words = [
            "казино",
            "криптовалюта",
            "крипта",
            "биржа",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        ]
        product_description = self.cleaned_data["description"]
        for item in list_forbidden_words:
            if item in product_description:
                raise ValidationError("Invalid description. Are you a scammer?")
        return product_description