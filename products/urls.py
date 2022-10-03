from django.urls import path,include
from .views import storeView, product_details








urlpatterns = [
    
    path('',storeView,name='store'),
    path('<slug:category_slug>/',storeView,name='product_by_catagory'),
    path('<slug:category_slug>/<slug:product_slug>/',product_details,name='product_details'),
]
