from django.shortcuts import render,get_object_or_404
from .models import Category,product

# Create your views here.

def product_list(request, category_slug=None):
    category = None
    products = product.objects.filter(available=True)
    categories = Category.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request, 'product/products/list.html', {
        'category':category,
        'product':products,
        'categories':categories,
    })

def product_detail(request,id ,slug):
    product = get_object_or_404(product , id=id , slug=slug , available=True)
    return render(request,'product/products/detail.html',{'product':product})