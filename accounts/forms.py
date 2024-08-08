from django import forms
from .models import profile

# class ProfilePictureForm(forms.ModelForm):
#     class Meta:
#         model = profile
#         fields = ['image', 'phone',]

class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['image', 'phone',]