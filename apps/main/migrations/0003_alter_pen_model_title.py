# Generated by Django 4.1.6 on 2023-02-02 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_stock_number_of_handles_alter_pen_model_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pen',
            name='model_title',
            field=models.CharField(max_length=100, null=True, unique=True, verbose_name='Название модели'),
        ),
    ]