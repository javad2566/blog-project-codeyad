# Generated by Django 5.0.3 on 2024-05-05 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hesabdari', '0010_remove_customer_product_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.IntegerField(null=True, verbose_name='شماره تماس مشتری'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200, unique=True, verbose_name='اسم محصول   '),
        ),
    ]
