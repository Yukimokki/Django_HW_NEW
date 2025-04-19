from django.core.management.base import BaseCommand
from catalog.models import Category, Product

class Command(BaseCommand):
    help = 'Add test products to the database'

    def handle(self, *args, **kwargs):
        # Удаляем существующие записи
        Category.objects.all().delete()
        Product.objects.all().delete()

        category1, _ = Category.objects.get_or_create(name='Курсы', description='Все курсы SkyPro')
        category2, _ = Category.objects.get_or_create(name='Хостинг', description='платформа для ваших курсов')

        products = [
            {'name': 'курс английского', 'price': '200', 'category': category1},
            {'name': 'курс питона', 'price': '300', 'category': category1},
            {'name': 'воркшоп', 'price': '150', 'category': category2},
        ]

        for product_data in products:
            products, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: {products.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exists: {products.name}'))