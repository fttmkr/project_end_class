# Generated by Django 4.2.5 on 2023-10-03 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_productcategory_alter_product_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ostad', models.CharField(max_length=200, verbose_name='نام استاد')),
                ('time', models.CharField(max_length=200, verbose_name='زمان دوره')),
            ],
            options={
                'verbose_name': ' اطلاعات تکمیلی',
                'verbose_name_plural': 'لیست اطلاعات تکمیلی',
            },
        ),
        migrations.CreateModel(
            name='ProductTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=200, verbose_name='عنوان تگ')),
            ],
            options={
                'verbose_name': 'تگ محصول',
                'verbose_name_plural': 'تگ های محصولات',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='product_information',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_info', to='blog.productinformation', verbose_name='اطلاعات تکمیلی'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_tag',
            field=models.ManyToManyField(to='blog.producttag', verbose_name='تگ محصول'),
        ),
    ]
