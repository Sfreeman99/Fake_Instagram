from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(
        max_length=254, help_text='Required. Inform a valid email address.')
    birth_date = forms.DateField(help_text="Required: YYYY-MM-DD")

    class Meta:
        model = User
        fields = (
            'username',
            'birth_date',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )
