from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body',)
        widget = {'email': forms.EmailInput(attrs={'required': 'False'})}

