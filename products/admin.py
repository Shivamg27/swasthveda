from django.contrib import admin
from . import models

# Register your models here.
class productAdmin(admin.ModelAdmin):
    list_display=('product_name','slug','price','stock','modified_date','is_available')
    prepopulated_fields={'slug':('product_name',)}
    
admin.site.register(models.product,productAdmin)