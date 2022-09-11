from django import forms
from .models import AuthorModel,SessionListModel


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = AuthorModel
        fields = ['displayName']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = AuthorModel
        fields = ['profileImage']

class SessionUpdateForm(forms.ModelForm):
    class Meta:
        model = SessionListModel
        fields = ['object']