from django.urls import path
from .views import (
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView
)
from .views import ProductList, ProductDetail

urlpatterns = [
    path('', ProductList.as_view(), name='product-list'),
    path('<slug:slug>/', ProductDetail.as_view(), name='product-detail'),
    #path('new/', ProductCreateView.as_view(), name='product-create'),
    #path('<slug:slug>/update/', ProductUpdateView.as_view(), name='product-update'),
    #path('<slug:slug>/delete/', ProductDeleteView.as_view(), name='product-delete'),
]
