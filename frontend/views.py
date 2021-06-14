from django.shortcuts import render
from django.core.paginator import Paginator

# Create your views here.
from .models import Product


def product(request):
    
    products = Product.objects.all()
    
    # search code
    item_name = request.GET.get('item_name')
    if item_name!=''and item_name is not None:
        products = products.filter(productname__icontains = item_name)
    
    # Paginator code
    paginator = Paginator(products, 4)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    return render(request, 'frontend/product.html', {'products':products})

def product_details(request,id):
    product = Product.objects.get(id=id)

    return render(request, 'frontend/product_details.html', {'product': product})