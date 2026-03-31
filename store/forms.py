from django import forms
from .models import Category, Product

UPLOADCARE_PUBLIC_KEY = '4c3ba9de492e0e0eaddc'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

    class Media:
        js = ['https://ucarecdn.com/libs/widget/3.x/uploadcare.full.min.js']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({
            'role': 'uploadcare-uploader',
            'data-public-key': UPLOADCARE_PUBLIC_KEY,
            'data-images-only': 'true',
        })


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    class Media:
        js = ['https://ucarecdn.com/libs/widget/3.x/uploadcare.full.min.js']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in ('image', 'image2', 'image3'):
            if field_name in self.fields:
                self.fields[field_name].widget.attrs.update({
                    'role': 'uploadcare-uploader',
                    'data-public-key': UPLOADCARE_PUBLIC_KEY,
                    'data-images-only': 'true',
                })