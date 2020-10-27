from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

from .models import Product, Review
from .forms import ReviewForm


def product_list_view(request):
    template = 'app/product_list.html'
    products = Product.objects.all()

    context = {
        'product_list': products,
    }

    return render(request, template, context)


def product_view(request, pk):
    template = 'app/product_detail.html'
    product = get_object_or_404(Product, id=pk)
    reviews = Review.objects.filter(product=product)

    reviewed_items = request.session.get('reviewed_items', [])
    print(reviewed_items)

    context = {
        'product': product,
        'reviews': reviews,
        'is_review_exist': True
    }

    if pk not in reviewed_items:
        form = ReviewForm(request.POST or None, product=product)
        context['is_review_exist'] = False
        context['form'] = form
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                reviewed_items.append(pk)
                request.session['reviewed_items'] = reviewed_items
                return redirect(reverse('product_detail', args=[str(pk)]))

    return render(request, template, context)
