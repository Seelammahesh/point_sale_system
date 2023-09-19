from django.contrib import admin

# Register your models here.
from .models import Category,SubCategory,Product
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['id','category','name']
    list_filter = ['category']
    search_fields = ['name']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','sub_category','name','image', 'price','description','created_at','updated_at']
    list_filter = ['name','price']
    search_fields = ['id']




admin.site.register(Category,CategoryAdmin)
admin.site.register(SubCategory,SubCategoryAdmin)
admin.site.register(Product,ProductAdmin)
