from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm
from users.views import profile_view
import logging


logger = logging.getLogger(__name__)

def my_function():
    logger.debug('This is a debug message')

# Create your views here.

class ProductList(generic.ListView):
    model = Product
    template_name = "product/product_list.html"
    context_object_name = 'products'
    paginate_by = 4

    def product_list(request):
        products = Product.objects.filter(Q(availability=0) | Q(availability=1))
        return render(request, 'product/product_list.html', {'products': products})

    def get_queryset(self):
        """Override to customize the query."""
        return Product.objects.all().order_by('-created_at')


class ProductDetail(DetailView):
    model = Product
    template_name = 'product/product_detail.html'

    def get_queryset(self):
        """Ensure only available products can be viewed."""
        return super().get_queryset().all()

class ProductCreate(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/product_create.html'
    # Redirect to product list view after creation
    success_url = reverse_lazy('product-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = None
        return context

    def form_valid(self, form):
        form.instance.seller = self.request.user
        user_profile = self.request.user.profile
        form.instance.location = user_profile.location
        return super(ProductCreate, self).form_valid(form)

class ProductUpdate(UpdateView):
    model = Product
    fields = ['title', 'description', 'price', 'status', 'availability']
    template_name = 'product/product_form.html'
    # Redirect to product list view after updte
    success_url = reverse_lazy('product-list')

class ProductDelete(DeleteView):
    model = Product
    template_name = 'product/product_confirm_delete.html'
    # Redirect to product list view after deletion
    success_url = reverse_lazy('product-list')
