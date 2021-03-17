from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]


class RawProductForm(forms.Form):
    title = forms.CharField(label=' ', widget=forms.TextInput(attrs={"placeholder": "hi you"}))
    description = forms.CharField(required=True,
                                  widget=forms.Textarea(
                                      attrs={
                                      "placeholder": "say my name",
                                      "class": "new-class-name",
                                      "rows": 15,
                                      "cols": 20
                                      }
                                    )
                                  )
    price = forms.DecimalField(initial=199.99)
