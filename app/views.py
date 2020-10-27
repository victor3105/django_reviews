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

    form = ReviewForm(request.POST, product=product)
    if request.method == 'POST':
        print('Got POST method')
        if form.is_valid():
            print(form)
            form.save()
            print('Review is saved')
        else:
            print('Form is not valid')
            print(form.data)
            error_msg = 'Неверно заполнен отзыв'

    context = {
        'form': form,
        'product': product
    }

    return render(request, template, context)
