from django.db import models

class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="название категории",
        help_text="Category name",
    )
    description = models.TextField(
        verbose_name="описание категории",
        help_text="describe the category",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="название продукта",
        help_text="Product's name",
    )
    description = models.TextField(
        verbose_name="описание продукта",
        help_text="describe the product",
        blank=True,
        null=True,
    )
    preview = models.ImageField(
        upload_to="products/photo",
        blank=True,
        null=True,
        verbose_name="превью продукта",
        help_text="Upload photo",
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="категория продукта",
        help_text="select product category",
        related_name="products",
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    created_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата создания",
        help_text="date when added",
    )

    updated_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата последнего изменения",
        help_text="date when changed",
    )
