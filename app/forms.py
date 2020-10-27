from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.product = kwargs.pop('product')
        super(ReviewForm, self).__init__(*args, **kwargs)

    def save(self, commit=True, product=None):
        review = Review.objects.create(product=self.product, text=self.cleaned_data.get('text'))
        return review

    class Meta(object):
        model = Review
        exclude = ['id', 'product']
