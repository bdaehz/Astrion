from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomTextInput (forms.TextInput):
    
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('attrs', {})['class'] = 'input' 
        super (CustomTextInput, self).__init__(*args, **kwargs)        


class RegisterForm (UserCreationForm):
    username = forms.CharField(
        label="Username",
        widget=CustomTextInput(
            attrs={
                'placeholder': "Pecausa27"
            }
        )
    )
    email = forms.EmailField(
        label='Email',
        widget=CustomTextInput(
            attrs={
                'placeholder': "example@gmal.com"
            }
        )
    )
    password1 = forms.CharField(
        label="Password",
        widget=CustomTextInput(
            attrs={
                'type': 'password'
            }
        )
    )
    password2 = forms.CharField(
        label="Confirm Password", 
        widget=CustomTextInput(
            attrs={
                'type': 'password'
            }
        )
    )
    class Meta: 
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
