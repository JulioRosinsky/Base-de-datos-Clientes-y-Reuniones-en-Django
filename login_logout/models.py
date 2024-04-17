from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].validators = []
        
        self.fields['username'].help_text = ''
        self.fields['username'].widget.attrs['placeholder'] = 'Ingresa tu usuario'
        self.fields['password1'].widget.attrs['placeholder'] = 'Ingresa tu contraseña'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirma tu contraseña'

        self.fields['username'].label = ''
        self.fields['password1'].label = ''
        self.fields['password2'].label = ''

        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'password1', 'password2')