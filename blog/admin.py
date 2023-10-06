from django.contrib import admin

# Register your models here.
from . import models
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','price','is_active','description']
    list_editable=['price','is_active']
    # readonly_fields = ['slug']
    Prepopulated_field={'slug':['title']}
    list_filter = ['is_active','price']
admin.site.register(models.Product,ProductAdmin)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['title','url_title'  ]
    list_editable = ['url_title']
admin.site.register(models.ProductCategory, ProductCategoryAdmin)
class ProductInfotmationAdmin(admin.ModelAdmin):
    list_display = ['name_ostad','time']
    list_editable = ['time']

admin.site.register(models.ProductInformation,ProductInfotmationAdmin)
class ProductTagAdmin(admin.ModelAdmin):
    list_display = ['tag']
admin.site.register(models.ProductTag, ProductTagAdmin)

