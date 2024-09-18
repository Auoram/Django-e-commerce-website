from django.shortcuts import render,get_object_or_404
from product.models import product
from .models import Cart,Item
from django.views.decorators.http import require_POST
from django.http import JsonResponse
# Create your views here.

@require_POST
def cart_add(request,product_id):
    cart_id = request.session.get('cart_id')

    if(cart_id):
        try:
            cart= Cart.objects.get(id=cart_id)
        except Cart.DoesNotExist:
            cart = Cart.objects.create()
            request.session['cart_id'] = cart.id
    else:
        cart = Cart.objects.create()
        request.session['cart_id'] = cart_id
    
    Product = get_object_or_404(product,id=product_id)

    cart_item, created = Item.objects.get_or_create(cart=cart, Product=Product)

    if not created:
        cart_item.quantity += 1

    cart_item.save()

    response_data = {
        "success":True,
        "message":f'Added {Product.name} to cart'
    }
    
    return JsonResponse(response_data)

def cart_detail(request):
    cart_id = request.session.get('cart_id')
    cart=None

    if(cart_id):
        cart = get_object_or_404(Cart,id=cart_id)

    return render(request, 'cart/detail.html', {'cart':cart})