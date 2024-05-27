from django.shortcuts import render
from django.http import HttpResponse
from core.models import Category,Product,ProductImages
from django.shortcuts import render, get_object_or_404

 
def index(request, cid=None):
    categories = Category.objects.all()  # Fetch all categories
    if cid:
        category = get_object_or_404(Category, id=cid)
        # Updated field name from `category` to `Category`
        products = Product.objects.filter(product_status="published", featured=True, Category=category).order_by("-id")
    else:
        products = Product.objects.filter(product_status="published", featured=True).order_by("-id")
        category = None

    context = {
        "products": products,
        "categories": categories, 
        "category": category,
    }

    return render(request, 'core/index.html', context)

def product(request, cid=None):
    if cid:
        category = get_object_or_404(Category, id=cid)
        # Updated field name from `category` to `Category`
        products = Product.objects.filter(product_status="published", Category=category).order_by("-id")
    else:
        products = Product.objects.filter(product_status="published").order_by("-id")
        category = None

    context = {
        "products": products,
        "category": category,
    }

    return render(request, 'core/product.html', context)

def product_details(request,pid):
    product=Product.objects.get(pid=pid)
    #product = get_object_or_404 (Product ,pid=pid)
    p_image = product.p_images.all()
    # Split the special features into a list
    special_features = product.special_features.split(',') if product.special_features else []

    context = {
        "p":product,"p_images":p_image,"special_features": special_features, 
    }
    return render (request,'core/Products_Details.html',context)

def login(request):
    return render (request,'core/login.html')

def cat_lsit(request,cid):
    category_list=Category.objects.get(cid=cid) 
    products = Product.objects.filter(product_status="published", featured=True, category=Category)

    context = {
        "category":category_list,"products":products, 
    }


     