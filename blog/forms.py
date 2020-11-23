from django import forms

class ArticlesForm(forms.Form):
    article1 = forms.CharField(widget=forms.Textarea placeholder='Article One')
    article2 = forms.CharField(widget=forms.Textarea placeholder='Article Two')