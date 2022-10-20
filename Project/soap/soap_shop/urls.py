from django.urls import path
from . import views

urlpatterns = [
    path('product/<int:product_id>/', views.single_product, name='single_product'),
    path('categories/', views.product_category, name='categories'),
    path('shop/', views.shop_products, name='shop'),
    path('', views.index, name='index'),

]
