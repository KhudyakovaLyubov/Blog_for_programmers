from django.shortcuts import render

def profile(request):
    return render(request, 'accounts/profile_settings/profile.html')

def signup(request):
    return render(request, 'accounts/registration/signup.html')

def activate(request):
    return render(request, 'accounts/registration/acc_activate_email.html')
