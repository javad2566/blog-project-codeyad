# Generated by Django 5.0.3 on 2024-04-26 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hesabdari', '0008_remove_customer_number_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='product_number',
            field=models.IntegerField(blank=True, null=True, verbose_name='تعداد محصول'),
        ),
    ]
