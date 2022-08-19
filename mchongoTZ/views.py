from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework import generics, mixins
from rest_framework import viewsets


def index(request):
    return render(request, 'index.html')


class CustomerView(
    viewsets.GenericViewSet,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class ProductView(
    viewsets.GenericViewSet,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderView(
    viewsets.GenericViewSet,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailView(
    viewsets.GenericViewSet,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer


class CategoryView(
    viewsets.GenericViewSet,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryView(
    viewsets.GenericViewSet,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class CartView(
    viewsets.GenericViewSet,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class SupplierView(
    viewsets.GenericViewSet,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class InvoiceView(
    viewsets.GenericViewSet,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class InvoiceDataView(
    viewsets.GenericViewSet,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    queryset = InvoiceData.objects.all()
    serializer_class = InvoiceDataSerializer
# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
# def customer(request):
#     if request.method == 'GET':
#         customers = Customer.objects.all()
#         serializer = CustomerSerializer(customers, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = CustomerSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_CREDENTIAL)
#     elif request.method == 'PUT':
#         serializer = CustomerSerializer(Customer, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         Customer.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
# def product(request):
#     if request.method == 'GET':
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ProductSerializer(data=request.data)
#         # if Product.objects.filter(**request.data).exists():
#         #     raise serializers.ValidationError('This data already exists')
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     elif request.method == 'PUT':
#         # produ = Product.objects.get(pk=pk)
#         serializer = ProductSerializer(Product, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         Product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
# def order(request):
#     if request.method == 'GET':
#         orders = Order.objects.all()
#         serializer = OrderSerializer(orders, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = OrderSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_CREDENTIAL)
#     elif request.method == 'PUT':
#         serializer = OrderSerializer(Order, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         Order.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
# def orderdetail(request):
#     if request.method == 'GET':
#         orderdetails = OrderDetail.objects.all()
#         serializer = OrderDetailSerializer(orderdetails, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = OrderDetailSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_CREDENTIAL)
#     elif request.method == 'PUT':
#         serializer = OrderDetailSerializer(OrderDetail, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         OrderDetail.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
# def category(request):
#     if request.method == 'GET':
#         categories = Category.objects.all()
#         serializer = CategorySerializer(categories, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = CategorySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_CREDENTIAL)
#     elif request.method == 'PUT':
#         serializer = CategorySerializer(Category, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         Category.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
# def subcategory(request):
#     if request.method == 'GET':
#         subcategories = SubCategory.objects.all()
#         serializer = SubCategorySerializer(subcategories, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = SubCategorySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_CREDENTIAL)
#     elif request.method == 'PUT':
#         serializer = SubCategorySerializer(SubCategory, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         SubCategory.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
# def cart(request):
#     if request.method == 'GET':
#         carts = Cart.objects.all()
#         serializer = CartSerializer(carts, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = CartSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_CREDENTIAL)
#     elif request.method == 'PUT':
#         serializer = CartSerializer(Cart, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         Cart.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
# def supplier(request):
#     if request.method == 'GET':
#         suppliers = Supplier.objects.all()
#         serializer = SupplierSerializer(suppliers, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = SupplierSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_CREDENTIAL)
#     elif request.method == 'PUT':
#         serializer = SupplierSerializer(Supplier, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         Supplier.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
# def invoice(request):
#     if request.method == 'GET':
#         invoices = Invoice.objects.all()
#         serializer = InvoiceSerializer(invoices, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = InvoiceSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_CREDENTIAL)
#     elif request.method == 'PUT':
#         serializer = InvoiceSerializer(Invoice, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         Invoice.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
# def invoicedata(request):
#     if request.method == 'GET':
#         invoicesdata = InvoiceData.objects.all()
#         serializer = InvoiceDataSerializer(invoicesdata, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = InvoiceDataSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_CREDENTIAL)
#     elif request.method == 'PUT':
#         serializer = InvoiceDataSerializer(InvoiceData, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         InvoiceData.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
