from django.shortcuts import render, redirect
from .forms import ProductForm
from Healthy.models import Product


def index(request):
    return render(request, 'index.html')


def out_of_stock(request):
    if request.method == 'POST':
        form_data = ProductForm(data=request.POST, files=request.FILES)
        if form_data.is_valid():
            product = form_data.save(commit=False)
            product.user = request.user
            product.image = form_data.cleaned_data['image']
            product.save()
            return redirect('/out-of-stock')
    out_of_stock_products = Product.objects.filter(quantity__lte=0, category__is_active=True)
    return render(request, 'outofstock.html', context={'products': out_of_stock_products, 'form': ProductForm})
