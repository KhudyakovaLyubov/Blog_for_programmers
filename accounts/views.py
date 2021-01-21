from django.shortcuts import render
import accounts.forms
import account.forms
import account.views

class LoginView(account.views.LoginView):
    form_class = account.forms.LoginEmailForm

class SignupView(account.views.SignupView):
    form_class = accounts.forms.SignupForm
    identifier_field = 'email'

    def generate_username(self, form):
        username = form.cleaned_data["email"]
        return username

    def after_signup(self, form):
        super(SignupView, self).after_signup(form)

    def update_profile(self, form):
        profile = self.created_user.profile
        profile.some_attr = "some value"
        profile.save()
