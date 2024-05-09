from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from . models import Customer,Contact
from django.utils.translation import gettext, gettext_lazy as _



#Registration
#class CustomerRegistration(UserCreationForm):
   #password2 = forms.CharField(label='Confrim Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
   # email = forms.CharField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))
#class CustomerRegistration(UserCreationForm):
 #   model = User
#    fields = '__all__'
 #   labels = {'email':'Email','first name':'First Name','last name':'Last Name'}

class CustomerRegistration(UserCreationForm):
    username = UsernameField(label=('Username'), widget=forms.TextInput(attrs={'class':'form-input'}))
    firstname = forms.CharField(label=('First Name'), widget=forms.TextInput(attrs={'class':'form-input'}))
    lastname = forms.CharField(label=('Last Name'), widget=forms.TextInput(attrs={'class':'form-input'}))
    password1 = forms.CharField(label=('Password'), widget=forms.PasswordInput(attrs={'class':'form-input'}))
    password2 = forms.CharField(label=('Confirm Your Password'), widget=forms.PasswordInput(attrs={'class':'form-input'}))
    email = forms.CharField(label=('Email'), required=True, widget=forms.EmailInput(attrs={'class':'form-input'}))

    class Meta:
            model = User
            fields = ['username','firstname','lastname','email','password1','password2']

#login form

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-input' }))

    password = forms.CharField(label=_('Password'),strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current_password','class':'form-input' }))


class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_('Old Password'), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'autofocus': True, 'class':'form-input'}))

    new_password1 = forms.CharField(label=_('New Password'), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new password', 'class':'form-input'}), help_text=password_validation.password_validators_help_text_html())


    new_password2 = forms.CharField(label=_('Confirm New Password'), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new password', 'class':'form-input'}))

#password reset 
class MyPasswordResetForm(PasswordResetForm):
     email = forms.EmailField(max_length=50,label=_('Email'),widget=forms.EmailInput(attrs={'autocomplete':'email','class':'form-input','placeholder':'Enter Your Valid Email'}))


#set password form
class MySetPasswordForm(SetPasswordForm):
     new_password1 = forms.CharField(label=_('New Password'),strip=False,widget=forms.PasswordInput(attrs={'autocompelete':'new-password','placeholder':'Enter New Password','class':'form-input'}),help_text=password_validation.password_validators_help_text_html)

     new_password2 = forms.CharField(label=_('Confrim New Password'),strip=False,widget=forms.PasswordInput(attrs={'autocompelete':'new-password','placeholder':'Enter Re-Password','class':'form-input'}))

#Customer Profile
class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name','surname','mobile_number','address_line_1','address_line_2','postcode','state','area','email','country','region','image']
        widgets ={'name':forms.TextInput(attrs={'class':'form-input'}),'surname':forms.TextInput(attrs={'class':'form-input'}),'mobile_number':forms.NumberInput(attrs={'class':'form-control'}),'address_line_1':forms.TextInput(attrs={'class':'form-input'}),'address_line_2':forms.TextInput(attrs={'class':'form-input'}),'postcode':forms.NumberInput(attrs={'class':'form-input'}),'state':forms.TextInput(attrs={'class':'form-input'}),'area':forms.Select(attrs={'class':'form-input'}),'email':forms.EmailInput(attrs={'class':'form-input'}),'country':forms.TextInput(attrs={'class':'form-input'}),'region':forms.TextInput(attrs={'class':'form-input'})}


#contact
class ContactForm(forms.ModelForm):
     class Meta:
        model = Contact
        fields = ['name','email','message']
        widgets ={'name':forms.TextInput(attrs={'class':'form-input'}),'email':forms.EmailInput(attrs={'class':'form-input'}),'message':forms.Textarea(attrs={'class':'form-input'})}
