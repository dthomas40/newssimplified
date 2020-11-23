from django import forms

class ArticlesForm(forms.Form):
    article1 = forms.CharField(widget=forms.Textarea)
    article2 = forms.CharField(widget=forms.Textarea)