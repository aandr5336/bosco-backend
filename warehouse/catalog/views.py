from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'catalog/products.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        brand = request.POST.get('brand')
        size = request.POST.get('size')
        color = request.POST.get('color')
        price = request.POST.get('price')

        if name and brand and size and color and price:
            Product.objects.create(
                name=name,
                brand=brand,
                size=size,
                color=color,
                price=price
            )
            messages.success(request, f'Товар "{name}" успішно додано!')
            return redirect('product_list')

    return render(request, 'catalog/add_product.html')