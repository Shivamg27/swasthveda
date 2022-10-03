from audioop import reverse
from distutils.command.upload import upload
from pydoc import describe
from tabnanny import verbose
from unicodedata import name
from django.db import models
from django.urls import reverse
# Create your models here.

class category(models.Model):
    name=models.CharField(unique=True,max_length=30)
    slug=models.SlugField(unique=True,max_length=100)
    description=models.TextField(max_length=255,blank=True)
    category_image=models.ImageField(upload_to='photos/category',blank=True)
    
    class Meta:
        verbose_name='category'
        verbose_name_plural='categories'

    
    def get_url(self):
        return reverse('product_by_catagory',args=[self.slug])

    
    
    def __str__(self):
        return self.name
    
    