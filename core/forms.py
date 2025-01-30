
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15, required=False)
    message = forms.CharField(widget=forms.Textarea, required=True)
