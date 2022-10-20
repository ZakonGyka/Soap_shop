from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Product, Category
from django.http import JsonResponse
from django import template
from django.db.models import ObjectDoesNotExist


def index(request):
    new_products = Product.objects.all().order_by('-pub_date')
    paginator = Paginator(new_products, 3)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'index.html',
                  {
                      'new_products': page,
                  }
                  )


def shop_products(request):
    cat_set = ''
    list_products = Product.objects.all()
    list_categories = Category.objects.all()
    if request.GET.get('category'):
        cat_set = request.GET['category']
        if request.GET['category'] != 'all':
            list_products = list_products.filter(category__name=request.GET['category'])

    paginator = Paginator(list_products, 9)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'urls': request.GET.urlencode(),
        })
    return render(request, 'shop.html',
                  {
                      'cat_set': cat_set,
                      'products': page,
                      'categories': list_categories,
                      'paginator': paginator,
                  }
                  )


def product_category(request):
    list_of_categories = Category.objects.all()
    paginator = Paginator(list_of_categories, 9)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'categories.html',
                  {
                      'categories': page,
                      'paginator': paginator,
                  }
                  )


def single_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    images = product.images.all()
    list_products = Product.objects.all()
    last_product = list_products.last()
    first_product = list_products.first()
    if product.id <= last_product.id:
        next_id = product.id + 1
        preview_id = product.id - 1
    else:
        next_id = ''
        preview_id = ''
    return render(request, 'single-product.html',
                  {
                      'product': product,
                      'images': images,
                      'next_id': next_id,
                      'preview_id': preview_id,
                      'first_product': first_product,
                      'last_product': last_product,
                  }
                  )


def page_not_found(request, exception):
    # Переменная exception содержит отладочную информацию,
    return render(request, 'misc/404.html', {'path': request.path}, status=404, content_type='text/html')

# register = template.Library()
#
#
# @register.filter
# def product_next(list_products, current_index):
#     try:
#         return list_products[int(current_index) + 1]
#     except:
#         return ''
#
#
# @register.filter
# def product_previous(list_products, current_index):
#     try:
#         return list_products[int(current_index) - 1]
#     except:
#         return ''

# Create your views here.
