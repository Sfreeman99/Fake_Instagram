from django import forms
from app.models import ImageModel


class PostPhotoForm(forms.ModelForm):
    # name = forms.CharField(max_length=15)
    # image = forms.ImageField(label='Upload Image')
    class Meta:
        model = ImageModel
        fields = ('name', 'image')


class CommentForm(forms.Form):
    comment = forms.CharField(max_length=250)


class EditPhotoForm(forms.Form):
    over_lay = forms.ChoiceField(choices=[
        ('Base Camp Filter', '2018 Base Camp Filter'),
        ('None', 'No Filter'),
    ])
