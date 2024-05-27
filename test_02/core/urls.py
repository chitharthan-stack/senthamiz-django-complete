from django.urls import path

from core.views import index, product, product_details, login

#from core.views import index,prd,cat,cat_view

app_name = "core"

urlpatterns = [
    path("", index, name="index"),
    path('category/<cid>/', index, name='category_products'),
    
    path("product/<int:cid>/", product, name="product_by_category"),
    path("product", product, name="product"),
   
    path("product-details/<pid>", product_details, name="product_details"),
   
    path("login", login, name="login"), 
]