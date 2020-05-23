from django.shortcuts import render
from products.models import Product

# Create your views here.


def search(request):
    """ Display search results """
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, "search.html", {"products": products})
