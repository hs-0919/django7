from django.contrib import admin
from sangpum.models import Maker, Product

# Register your models here. 관리자 화면

class MakerAdmin(admin.ModelAdmin):
    list_display = ('id','mname','tel','addr')
    
admin.site.register(Maker, MakerAdmin)    

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','pname','price','maker_name')
    
admin.site.register(Product, ProductAdmin) 









