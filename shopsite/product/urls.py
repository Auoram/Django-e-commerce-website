from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('',views.product_list,name='product_list'),
    path('<slug:category_slug>/',views.product_list,name='product_list'),
    path('product/<id:id>/<slug:slug>/',views.product_detail,name='prodect_detail')
]

