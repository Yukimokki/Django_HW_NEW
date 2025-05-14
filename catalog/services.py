from catalog.models import Product, Category
from config.settings import CACHE_ENABLED
from django.core.cache import cache


def get_cached_products():
    """ gets products' data from cache, if cache is empty, gets data from DB"""
    if not CACHE_ENABLED:
        Product.objects.all()
    key = 'products_list'
    products = cache.get(key)

    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products

def get_cached_categories():
    """ gets categories' data from cache, if cache is empty, gets data from DB"""
    if not CACHE_ENABLED:
        Category.objects.all()
    key = 'products_list'
    categories = cache.get(key)

    if categories is not None:
        return categories
    categories = Category.objects.all()
    cache.set(key, categories)
    return categories