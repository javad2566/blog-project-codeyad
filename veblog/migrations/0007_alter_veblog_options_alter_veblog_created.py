# Generated by Django 5.0.3 on 2024-04-27 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veblog', '0006_alter_veblog_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='veblog',
            options={'ordering': ['created']},
        ),
        migrations.AlterField(
            model_name='veblog',
            name='created',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='تاریخ انتشار وبلاگ'),
        ),
    ]
