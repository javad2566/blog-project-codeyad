# Generated by Django 5.0.3 on 2024-05-18 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coach', '0007_coach_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='like',
            field=models.IntegerField(default=5, verbose_name='تعداد لایک مربی'),
        ),
    ]
