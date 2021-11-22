from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display=['id','service_name','logo']

@admin.register(ServiceSubCategory)
class ServiceSubCategoryAdmin(admin.ModelAdmin):
    list_display=['services','id','sub_service_name','logo']