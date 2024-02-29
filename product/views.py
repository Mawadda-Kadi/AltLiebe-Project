from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from .models import Product

# Create your views here.

class ProductList(generic.ListView):
    model = Product
    template_name = "product/product_list.html"
    paginate_by = 4

    def get_queryset(self):
        """Override to customize the query."""
        return Product.objects.filter(available=True).order_by('-created_at')

class ProductDetail(DetailView):
    model = Product
    template_name = 'product/product_detail.html'

    def get_queryset(self):
        """Ensure only available products can be viewed."""
        return super().get_queryset().filter(available=True)

