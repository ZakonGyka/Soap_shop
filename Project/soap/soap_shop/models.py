from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.safestring import mark_safe


class Product(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название товара',
    )
    context = models.TextField(
        null=True,
        blank=True,
        verbose_name='Описание',

    )
    price = models.FloatField(
        null=True,
        blank=True,
        verbose_name='Цена',
        validators=[MinValueValidator(0), MaxValueValidator(1000000.0)]

    )
    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name='Категория',
        related_name='product',
    )
    amount = models.IntegerField(
        null=True,
        verbose_name='Кол-во товаров',
    )

    pub_date = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
    )

    def check_product_image_exist(self):
        if self.images.exists():
            return mark_safe('<img src="/static/admin/img/icon-yes.svg" alt="True">')
        else:
            return mark_safe('<img src="/static/admin/img/icon-no.svg" alt="True">')

    check_product_image_exist.short_description = 'Наличие фото'

    def __str__(self):
        return f'{self.title}: {self.price}, {self.amount}, {self.category}'

    class Meta:
        constraints = (
            models.CheckConstraint(
                check=models.Q(price__gte=0) & models.Q(price__lte=1000000),
                name='soap_shop_price_constraint',
            ),

        )
        # ordering = ('-pub_date',)


class ProductImage(models.Model):
    product = models.ForeignKey(
        'Product',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='images',
    )

    product_image = models.ImageField(
        upload_to='soap_shop/Product_Img',
        null=True,
        blank=True,
    )


class Category(models.Model):
    name = models.CharField(
        max_length=200,
        db_index=True,
        verbose_name='Категория'
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
        null=True,  # убрать при создании новой БД
        blank=True,  # убрать при создании новой БД
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        null=True,  # убрать при создании новой БД
        blank=True,  # убрать при создании новой БД
    )
    category_image = models.ImageField(
        upload_to='soap_shop/Category_Img',
        null=True,
        blank=True,
    )

    def check_category_image_exist(self):
        if self.category_image:
            return mark_safe('<img src="/static/admin/img/icon-yes.svg" alt="True">')
        else:
            return mark_safe('<img src="/static/admin/img/icon-no.svg" alt="True">')

    check_category_image_exist.short_description = 'Наличие фото'

    # quantity_product
    def get_count_product(self):
        quantity_product = Product.objects.filter(category=self).count()
        return quantity_product

    get_count_product.short_description = 'Кол-во товаров данной категории'

    def __str__(self):
        return f'{self.name}'
