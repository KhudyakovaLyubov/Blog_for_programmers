from django.urls import path, include
import BlogApp.views

urlpatterns = [
    path('', BlogApp.views.main, name="main"), 
]