# Generated by Django 4.0.1 on 2022-03-29 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('soap_shop', '0001_squashed_0032_category_pub_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='pub_date',
        ),
    ]
