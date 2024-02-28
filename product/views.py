from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponse
from .models import Product

# Create your views here.

class ProductList(generic.ListView):
    queryset = Product.objects
    template_name = "product/product_list.html"
    paginate_by = 4

def product_list(request):
    products = Product.objects.filter(available=True).order_by('-created_at')
    return render(request, 'product/product_list.html', {'products': products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    return render(request, 'product/product_detail.html', {'product': product})