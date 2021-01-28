from django.shortcuts import render

def profile(request):
    return render(request, 'accounts/profile_settings/profile.html')
