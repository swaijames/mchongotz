from rest_framework import routers
from mchongoTZ.views import *

router = routers.DefaultRouter()
router.register('customer', CustomerView)
router.register('product', ProductView)
router.register('Order', OrderView)
router.register('Order_Details', OrderDetailView)
router.register('category', CategoryView)
router.register('SubCategory', SubCategoryView)
router.register('Cart', CartView)
router.register('supplier', SupplierView)
router.register('invoice', InvoiceView)
router.register('InvoiceDetail', InvoiceDataView)
