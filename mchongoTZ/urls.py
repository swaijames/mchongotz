from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('customer/', views.customer, name='customer'),
    path('product/', views.product, name='product'),
    path('order/', views.order, name='order'),
    path('orderdetail/', views.orderdetail, name='orderdetail'),
    path('category/', views.category, name='category'),
    path('subcategory/', views.subcategory, name='subcategory'),
    path('cart/', views.cart, name='cart'),
    path('supplier/', views.supplier, name='supplier'),
    path('invoice/', views.invoice, name='invoice'),
    path('invoicedata/', views.invoicedata, name='invoicedata'),

]
