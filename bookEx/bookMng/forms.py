from django import forms
from django.forms import ModelForm
from .models import Book

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            'name',
            'web',
            'price',
            'picture',
        ]

class UpdateProfile(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.CharField()