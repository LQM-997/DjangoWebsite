from django import forms

from .models import *


class CommentsForm(forms.Form):
    comment = forms.CharField(required=True)

