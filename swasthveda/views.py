from django.shortcuts import render
from products.models import product


def homeView(request):
    products=product.objects.all().filter(is_available=True)
    
    context={
        
        'products':products,
    }
    
    return render(request,'home.html',context=context)