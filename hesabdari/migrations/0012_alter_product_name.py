# Generated by Django 5.0.3 on 2024-05-05 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hesabdari', '0011_alter_customer_phone_number_alter_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200, unique=True, verbose_name='اسم محصول موجو د '),
        ),
    ]
