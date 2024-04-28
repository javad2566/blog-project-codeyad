# Generated by Django 5.0.3 on 2024-04-22 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veblog', '0002_veblog_aouter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veblog',
            name='type',
            field=models.TextField(blank=True, choices=[('A', 'برنامه نویسی'), ('B', 'طراحی سایت با المنتور'), ('C', 'طراحی سایت با جنگو')], default='A', null=True, verbose_name='نوع وبلاگ'),
        ),
    ]
