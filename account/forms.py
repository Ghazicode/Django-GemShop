from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from .models import User





def start_with_0(value):
    if value[0]!='0':
        raise forms.ValidationError(F"شماره باید با {0} شروع بشود")

class LoginForm(forms.Form):
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'شماره تلفن خود را وارد نمایید',
         'pattern':"[0-9]*"
        }), max_length=11, validators=[start_with_0])
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder':'رمز عبور خود را وارد نمایید'
                                                                 }),validators=[validators.MinLengthValidator(8)]) 
    

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if len(phone) < 11:
            raise ValidationError('تلفن وارد شده معتبر نمیباشد', code='invalid')
            
        
        return phone
    




class RegisterForm(forms.Form):
    fullname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'نام و نام خانوادگی خود را وارد نمایید' }),max_length=50,validators=[validators.MinLengthValidator(4)])
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'شماره تلفن خود را وارد نمایید ', 'pattern':"[0-9]*"}),max_length=11, validators=[start_with_0, validators.MinLengthValidator(11)])
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'رمز خود را وارد نمایید'}),validators=[validators.MinLengthValidator(8)])
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'تکرار رمز خود را وارد نمایید'}), validators=[validators.MinLengthValidator(8)])



    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if len(phone) < 11:
            raise ValidationError('تلفن وارد شده معتبر نمیباشد', code='invalid')

            
        
        return phone
    



    




