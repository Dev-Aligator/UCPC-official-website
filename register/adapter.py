from django.contrib.auth import get_user_model
from allauth.exceptions import ImmediateHttpResponse
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.socialaccount.signals import pre_social_login
from django.utils.translation import gettext_lazy as _
from allauth.account.adapter import DefaultAccountAdapter
from django.shortcuts import redirect
from django.dispatch import receiver
from django.contrib import messages
from allauth.socialaccount.models import SocialAccount
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import numpy as np

import os

DIRNAME = os.path.dirname(__file__)
scope =[
        'https://www.googleapis.com/auth/spreadsheets',
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name(os.path.join(DIRNAME, 'ucpc-team-list-9acf2432120a.json'), scope)

_name = "UCPC Team List"
client = gspread.authorize(creds)
spreadsheet = client.open(_name)
wks = spreadsheet.worksheet("List_teams")




class UcpcAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=False):
        user = super(UcpcAccountAdapter, self).save_user(request, user, form, commit)
        data = form.cleaned_data
        user.first_name = data.get('first_name')
        user.last_name = data.get('last_name')
        user.save()
        return user

    def new_user(self, request):
        """
        Overrides the default new_user() method to set the user as active by default.
        """
        user = super(UcpcAccountAdapter, self).new_user(request)
        user.is_active = True
        return user

class UcpcSocialAccountAdapter(DefaultSocialAccountAdapter):
    def save_user(self, request, sociallogin, form=None):
        """
        Overrides the default save_user() method to save the user's details from the social account to the User model.
        """
        user = super(UcpcSocialAccountAdapter, self).save_user(request, sociallogin, form)
        if not user.pk:
            user.save()
        data = np.array([[user.email, 'OAuth 2.0 - Provider: Google']])
        idx = f'B{str(len(wks.get_all_values()) + 1)}' 
        wks.update(idx, data.tolist())

        return user

    
    def pre_social_login(self, request, sociallogin):
        """
        Overrides the default pre_social_login() method to implement custom logic before a social login.
        """
        pass
            
@receiver(pre_social_login)
def link_to_local_user(sender, request, sociallogin, **kwargs):
    """
    Receiver function for the pre_social_login signal to link a social account to a local user account.

    If a user already exists with the email address associated with the social account, it redirects to the login page.
    """
    email_address = sociallogin.account.extra_data['email']
    User = get_user_model()
    users = User.objects.filter(email=email_address)
    if users:
        try:
            social_account = SocialAccount.objects.filter(user=sociallogin.account.user, provider=sociallogin.account.provider)
            # If social_account exists, raise an ImmediateHttpResponse with a redirect to the login page.
            if not social_account:
                email_already_taken(request)
        except:
            email_already_taken(request)

def email_already_taken(request):
    """
    Helper function to raise an ImmediateHttpResponse with a redirect to the login page if the email address is already taken.
    """
    messages.error(request, 'An account with this email address already exists. Please log in using your email and password.')
    raise ImmediateHttpResponse(redirect("/login/"))
