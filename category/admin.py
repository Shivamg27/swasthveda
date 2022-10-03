from unicodedata import category
from django.contrib import admin
from .models import category

# Register your models here.

from .models import category

class CategoryAdmin(admin.ModelAdmin):
    
    prepopulated_fields={'slug':('name',)}
    list_display=('name','slug')
    

admin.site.register(category,CategoryAdmin)
