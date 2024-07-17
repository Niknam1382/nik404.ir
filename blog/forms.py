from django import forms
from blog.models import Comment

class CommentForm(forms.ModelForm):
    model = Comment
    fields = '__all__'