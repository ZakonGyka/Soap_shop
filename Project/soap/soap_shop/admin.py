from django.contrib import admin
from .models import Product, Category, ProductImage


class ImageGallery(admin.TabularInline):
    fk_name = 'product'
    model = ProductImage
    verbose_name = 'Изображение товара'
    verbose_name_plural = 'Изображения товара'


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'amount',
        'price',
        'category',
        'context',
        'check_product_image_exist',
        'pub_date',
    )
    inlines = [ImageGallery]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_count_product', 'slug', 'check_category_image_exist', 'pub_date')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

# Register your models here.
