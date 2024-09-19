from django.shortcuts import render,get_object_or_404,redirect
from product.models import product
from .models import Cart,Item
from django.views.decorators.http import require_POST
from django.http import JsonResponse
# Create your views here.

@require_POST
def cart_add(request, product_id):
    cart_id = request.session.get('cart_id')

    if cart_id:
        cart = Cart.objects.get(id=cart_id)
    else:
        cart = Cart.objects.create()
        print("Cart created:", cart.id)
        request.session['cart_id'] = cart.id
        print("Cart ID set in session:", request.session['cart_id'])
    
    Product = get_object_or_404(product,id=product_id)

    cart_item, created = Item.objects.get_or_create(cart=cart, product=Product)

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
    print("Cart ID:", cart_id)

    if cart_id is None:
        print("Cart ID is not set in the session")

    cart = None

    if cart_id:
        try:
            cart = Cart.objects.get(id=cart_id)
            print("Cart:", cart)
        except Cart.DoesNotExist:
            cart = None
            print("Cart does not exist")

    return render(request, 'cart/detail.html', {"cart": cart})

def cart_remove(request,product_id):
    cart_id = request.session.get('cart_id')
    cart = get_object_or_404(Cart,id=cart_id)
    item = get_object_or_404(Item,id=product_id,cart=cart)
    item.delete()

    return redirect("cart:cart_detail")