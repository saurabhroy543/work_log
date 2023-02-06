from django import forms
from .models import Author, Book


class AddAuthor(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['author']
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control', 'id': 'authorid'}),
        }


class AddBook(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['book', 'author']
        widgets = {
            'book': forms.TextInput(attrs={'class': 'form-control', 'id': 'bookid'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'id': 'authorid'}),
        }
