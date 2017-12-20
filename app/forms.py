from django import forms


class PostPhotoForm(forms.Form):
    name = forms.CharField(max_length=15)
    image = forms.ImageField(label='Upload Image')