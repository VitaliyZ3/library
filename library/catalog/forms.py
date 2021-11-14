from django import forms
from django.forms import models, widgets
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.forms.fields import DateTimeField
from .models import Ticket

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Нікнейм"
        self.fields['password'].label = "Пароль"


class UserRegistrationForm(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Нікнейм в системі "
        self.fields['first_name'].label = "Ім'я"
        self.fields['last_name'].label = "Фамілія"
        self.fields['email'].label = "Адреса поштової скриньки"
        self.fields['password'].label = "Введіть пароль"
        self.fields['password2'].label = "Підтвердження паролю"

    
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ('username', 'first_name','last_name', 'email')
        help_texts = {
            'username': None,
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']

class DateInput(forms.DateInput):
    input_type = 'date'

class SelectBookForm(forms.ModelForm):

    date_of_delivery = forms.DateField(widget= DateInput())

    class Meta:
        model = Ticket
        fields = [ 'reader', 'date_of_delivery', 'book']
        exclude = ['reader', 'book']    