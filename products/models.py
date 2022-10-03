from statistics import quantiles
from unicodedata import category
from xml.dom.minidom import CharacterData
from django.db import models
from category.models import category
from django.urls import reverse
# Create your models here.


class product(models.Model):
    
        product_name=models.CharField(max_length=100,unique=True)
        slug=models.SlugField(max_length=100,unique=True)
        description=models.TextField(max_length=500,blank=True)
        price=models.IntegerField()
        stock=models.IntegerField()
        is_available=models.BooleanField(default=True)
        image=models.ImageField(upload_to='photos/products')
        category=models.ForeignKey(category,on_delete=models.CASCADE)
        modified_date=models.DateTimeField(auto_now_add=True)
        created_date=models.DateTimeField(auto_now=True)
        discount=models.FloatField(default=0,blank=True)
        new_price=models.FloatField(default=0,blank=True)
        
        
        
        def __str__(self):
            return self.product_name
        
        
        def setNewPrice(self):
            self.new_price=(self.price-(self.price*(self.discount/100)))
            return self.new_price
        
        def getFloatPrice(self):
            return float(self.price)
        
        
        
        def getFloatNewPrice(self):
            return self.setNewPrice()
        
        def get_url(self):
            return reverse('product_details',args=[self.category.slug,self.slug])
            
            
