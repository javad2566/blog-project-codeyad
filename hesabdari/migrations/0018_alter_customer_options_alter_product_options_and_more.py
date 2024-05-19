# Generated by Django 5.0.3 on 2024-05-18 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hesabdari', '0017_product_image_alter_product_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'مشتری', 'verbose_name_plural': 'مشتریان فروشگاه'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'محصول', 'verbose_name_plural': 'محصولات فروشگاه'},
        ),
        migrations.AlterField(
            model_name='customer',
            name='all_costs',
            field=models.BigIntegerField(null=True, verbose_name='کل یدهی مشتری'),
        ),
    ]
