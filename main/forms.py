from django import forms
from .models import UserName

class NameForm(forms.ModelForm):
    class Meta:
        model = UserName
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'name-input',
                'placeholder': 'Введите ваше имя',
                'autocomplete': 'off'
            })
        }
        labels = {
            'name': ''
        }