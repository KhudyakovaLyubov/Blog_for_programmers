from django.urls import path, include
import accounts.views
import account.views
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/registration/login.html'), name='account_login'),
    path('logout/', LogoutView.as_view(next_page='profile'), name='account_logout'),
    path('signup/', account.views.SignupView.as_view(), name='account_signup'),
    path('', accounts.views.profile, name='profile'), 
]