# Generated by Django 5.0.3 on 2024-04-26 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hesabdari', '0007_alter_customer_all_costs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='number_product',
        ),
        migrations.AlterField(
            model_name='customer',
            name='product',
            field=models.ManyToManyField(to='hesabdari.product', verbose_name='اسامی محصولات خرید کرده '),
        ),
    ]
