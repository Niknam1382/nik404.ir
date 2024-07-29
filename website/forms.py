from django import forms
from website.models import content, contact

class ContentForm(forms.ModelForm):
    class Meta:
        model = content
        fields = '__all__'

class ContactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = '__all__'