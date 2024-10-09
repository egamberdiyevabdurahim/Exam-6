from django import forms

from post.models import ProblemModel, OfferModel


class ProblemModelForm(forms.ModelForm):
    class Meta:
        model = ProblemModel
        fields = ['title', 'description']


class OfferModelForm(forms.ModelForm):
    class Meta:
        model = OfferModel
        fields = ['title', 'description']
