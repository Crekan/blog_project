from django import forms

from .models import Contact, Comment


class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'full-width',
        'placeholder': 'Your Name',
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'full-width',
        'placeholder': 'Your Email',
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'full-width',
        'placeholder': 'Your Message',
        'cols': '30',
    }))

    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')


class CommentForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'full-width',
        'placeholder': 'Your Name',
    }))
    mail = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'full-width',
        'placeholder': 'Your Email',
    }))
    text = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'full-width',
        'placeholder': 'Your Message',
        'cols': '30',
    }))

    class Meta:
        model = Comment
        fields = ('name', 'mail', 'text')
