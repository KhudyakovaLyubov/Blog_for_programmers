import account.forms
import accounts.models
from django import forms

class SignupForm(account.forms.SignupForm):

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        del self.fields["username"]