from django.urls import path, include

from . import views
from mchongoTZ.router import router

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls))

]
