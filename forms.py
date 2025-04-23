from django import forms

class EmailForm(forms.Form):
    recipient = forms.EmailField(label="Recipient Email")
    subject = forms.CharField(label="Subject", max_length=100)
    message = forms.CharField(label="Message", widget=forms.Textarea)
