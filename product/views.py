from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm

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

class ProductCreate(CreateView):
    model = Product
    fields = ['title', 'description', 'price', 'slug', 'available', 'created_at']
    template_name = 'product/product_form.html'
    # Redirect to product list view after creation
    success_url = reverse_lazy('product-list')

class ProductUpdate(UpdateView):
    model = Product
    fields = ['title', 'description', 'price', 'slug', 'available']
    template_name = 'product/product_form.html'
    # Redirect to product list view after updte
    success_url = reverse_lazy('product-list')

class ProductDelete(DeleteView):
    model = Product
    template_name = 'product/product_confirm_delete.html'
    # Redirect to product list view after deletion
    success_url = reverse_lazy('product-list')
