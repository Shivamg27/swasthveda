from ast import If
from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from .models import product
from category.models import category
# Create your views here.

def storeView(request,category_slug=None):
    
    
    products=None
    categories=None
    
    
    if category_slug!=None:
    
        categories= get_object_or_404(category,slug=category_slug)
        products=product.objects.filter(category=categories,is_available=True)
        
    else:
    
    
        products=product.objects.all().filter(is_available=True)
        
    
     
    product_count=products.count()
    
    context={
        
        'products':products,
        'product_count':product_count,
        
    }
    
    
    return render(request,'products/store.html',context=context)



def product_details(request,category_slug,product_slug):
    
    
    try:
        single_product=product.objects.get(category__slug=category_slug,slug=product_slug)
    except Exception as e:
        raise e
    
    context={
        'single_product':single_product
    }
    
    return render(request,'products/product_details.html',context=context)