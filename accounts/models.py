from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50, blank=True)
    GENDER_CHOICES = (
        ('Женский', 'Woman'),
        ('Мужской', 'Man'),
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    dateOfBirth = models.DateField(blank=True)
    description = models.CharField(max_length=250, blank=True)
    city = models.CharField(max_length=50)



