from django import forms

from .models import Node, Title


class NodeForm(forms.ModelForm):
    class Meta:
        model = Node
        exclude = ("status","inherit","slug","stage","user","title",)


class TitleForm(forms.ModelForm):
    class Meta:
        model = Title
        exclude = ("user","slug",)
