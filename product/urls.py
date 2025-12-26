from django.urls import path
from . import views


app_name='product'
urlpatterns=[
    path('products_detail/<int:id>', views.product, name='products_detail'),
    path('category/<int:id>', views.category_detail, name='category_detail'),
    path('pricelists', views.pricelists, name='pricelists'),
    path('none', views.productnone, name='none'),
]