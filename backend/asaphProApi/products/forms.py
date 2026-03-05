from django import forms
from backend.asaphProApi.products import Product

class ProductForms(forms.ModelForm):
    class Meta:
        model = Product
        fields =('name','content', 'price')
