from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(forms.Form):
    username=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'please user name'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'ایمیل خود را وارد کنید'}))
    firstname=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'please user name'}))
    lastname=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'please user name'}))
    password1=forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'placeholder':'please user name'}))
    password2=forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'placeholder':'repeat password'}))
    #--------------validation
    def clean_username(self):
        user=self.cleaned_data['username']
        if User.objects.filter(username=user).exists():
            raise forms.ValidationError('user exist')
        return user
    #--- email
    def clean_email(self):
        email=self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('این ایمیل وجود دارد')
        return  email
    def clean_password2(self):
        password1=self.cleaned_data['password1']
        password2=self.cleaned_data['password2']
        if password1!=password2:
            raise forms.ValidationError('password not match')
        elif len(password2)<8:
            raise forms.ValidationError('password is short.')
        elif not any(i.isupper() for i in password2):
            raise forms.ValidationError('حداقل باید پسوورد دارای یک حرف بزرگ باشد')
        return password1

#--------
class UserLoginForm(forms.Form):
    user=forms.CharField()
    password=forms.CharField()
