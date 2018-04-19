from django.db import models
from django.contrib.auth.models import User


class UserProfile(User):
    phone = models.CharField(max_length=20, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
