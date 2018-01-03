from django import forms
from app.models import ImageModel


class PostPhotoForm(forms.ModelForm):
    # name = forms.CharField(max_length=15)
    # image = forms.ImageField(label='Upload Image')
    class Meta:
        model = ImageModel
        fields = ('name', 'image')


class EditPhotoForm(forms.Form):
    over_lay = forms.ChoiceField(choices=[
        ('/home/basecamp/Pictures/Happy_New_Year_FIlter.png', '2017 filter'),
        ('None', 'No Filter'),
    ])
