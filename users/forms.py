from django import forms
from .models import UserModel


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = UserModel
        fields = ['displayName']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['profileImage']

'''
class SessionUpdateForm(forms.ModelForm):
    class Meta:
        model = SessionListModel
        fields = ['object']
        '''
