from django import forms
from .models import User, Messages, MailLists
#A script for Django model form created for Bhulkee
#---code---#
class Maillist(forms.ModelForm):
    """A model form class for collecting and storing new email address"""

    class Meta:
        model = MailLists
        fields = ('emails',)


class UserForm(forms.ModelForm):
    """A model form for 'Enthusiast' users registration"""

    class Meta:
        model = User
        fields = ('username', 'email', 'password','secret_number', 'mobile_no')
   

class Message(forms.ModelForm):
    """A model form for sending messages by users in the platform"""
    
    class Meta:
        model = Messages
        fields = ('heading', 'body')


class UserLogin(forms.Form):
    """A form form signing in and authenticating users"""

    username = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200)