from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.text import slugify

# Create your models here.



class ProductCategory(models.Model):
    title=models.CharField(max_length=300,verbose_name='عنوان')
    url_title=models.CharField(max_length=300,verbose_name='عنوان در url')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='دسته بندی'
        verbose_name_plural='دسته بندی ها'
class ProductInformation(models.Model):
    name_ostad=models.CharField(max_length=200,verbose_name='نام استاد')
    time=models.CharField(max_length=200,verbose_name='زمان دوره')
    def __str__(self):
        return f'{self.name_ostad}---{self.time}'
    class Meta:
        verbose_name=' اطلاعات تکمیلی'
        verbose_name_plural='لیست اطلاعات تکمیلی'
class ProductTag(models.Model):
    tag=models.CharField(max_length=200,verbose_name='عنوان تگ')
    def __str__(self):
        return f'{self.tag}'
    class Meta:
        verbose_name='تگ محصول'
        verbose_name_plural='تگ های محصولات'
class Product(models.Model):
    product_tag = models.ManyToManyField(ProductTag, verbose_name='تگ محصول')
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, null=True, verbose_name='دسته بندی')
    product_information = models.OneToOneField(ProductInformation, on_delete=models.CASCADE, null=True, blank=True,
                                               related_name='product_info', verbose_name='اطلاعات تکمیلی')
    title=models.CharField(max_length=100,verbose_name='عنوان محصول')
    price=models.IntegerField(verbose_name='قیمت محصول')
    description=models.CharField(max_length=300,verbose_name='توضیحات محصول')
    is_active=models.BooleanField(verbose_name='فعال/غیرفعال')
    rating=models.IntegerField(default=0,validators=[MinValueValidator(1),MaxValueValidator(10)],
                               verbose_name='امتیاز محصول')
    slug=models.SlugField(default='',null=False,db_index=True,
                          verbose_name='عنوان درurl')
    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super().save()
    def __str__(self):
        return f'{self.title}---{self.description}---{self.price}'
    def get_absolute_url(self):
       return reversed('product-detail',args={self.slug})
    class Meta:
        verbose_name='محصول'
        verbose_name_plural='محصولات'

class karbaran (models.Model):
    name=models.CharField(max_length=20)
    family=models.CharField(max_length=20)
    age=models.IntegerField()
    # emailk=models.CharField()
    is_active=models.BooleanField()

