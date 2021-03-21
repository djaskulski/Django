from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    title = forms.CharField(label='TITLE', widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    description = forms.CharField(required=True,
                                  widget=forms.Textarea(
                                      attrs={
                                          "placeholder": "Your article",
                                          "class": "new-class-name",
                                          "rows": 15,
                                          "cols": 20
                                      }
                                  )
                                  )

    author = forms.CharField(required=True,
                             widget=forms.Textarea(
                                 attrs={
                                     "placeholder": "say your name",
                                     "class": "new-class-name",
                                     "rows": 1,
                                     "cols": 15
                                 }
                             )
                             )

    class Meta:
        model = Article
        fields = [
            'title',
            'description',
            'author'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if not "gold" in title:
            raise forms.ValidationError("This is not a gold product")
        if not "silver" in title:
            raise forms.ValidationError("This is not a silver product")
        return title

    def clean_description(self, *args, **kwargs):
        description = self.cleaned_data.get('description')
        if not "Producted in" in description:
            raise forms.ValidationError("This is not 'Producted in")
        if not "Composition" in description:
            raise forms.ValidationError("This is not 'Composition'")
        return description

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        if not email.endswith(".com"):
            raise forms.ValidationError("Do not forgot .com")
        if not "edu" in email:
            raise forms.ValidationError("Please use your student's email")
        return email


# class RawProductForm(forms.Form):
#     title = forms.CharField(label='TITLE', widget=forms.TextInput(attrs={"placeholder": "hi you"}))
#     description = forms.CharField(required=True,
#                                   widget=forms.Textarea(
#                                       attrs={
#                                           "placeholder": "say my name",
#                                           "class": "new-class-name",
#                                           "rows": 15,
#                                           "cols": 20
#                                       }
#                                   )
#                                   )
#     price = forms.DecimalField(initial=199.99)
