from django.shortcuts import render, redirect, reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.db.models import Q
from products.models import Product, Category


def do_search(request):
    product_list = Product.objects.all()
    query = request.GET.get('q')
    if query:
        product_list = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        ).distinct()
    paginator = Paginator(product_list, 6)
    page = request.GET.get('page')

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {
        'products': products
    }

    amount = len(product_list)
    if amount == 0:
        messages.info(request, 'Unfortunately, your search returned no items.')
        return redirect(reverse('index'))
    elif amount > 0:
        return render(request, "products.html", context)


