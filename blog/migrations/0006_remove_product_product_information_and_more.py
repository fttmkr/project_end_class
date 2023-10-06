# Generated by Django 4.2.5 on 2023-10-03 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_productinformation_producttag_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_information',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_tag',
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='', verbose_name='عنوان درurl'),
        ),
        migrations.DeleteModel(
            name='ProductInformation',
        ),
        migrations.DeleteModel(
            name='ProductTag',
        ),
    ]
