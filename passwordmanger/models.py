from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse_lazy


class PasswordsManger(models.Model):
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    site_name = models.CharField(max_length=120)
    site_url = models.CharField(max_length=250)
    site_username = models.CharField(max_length=120)
    site_password = models.CharField(max_length=120)

    def __str__(self):
        return self.site_name

    def get_absolute_url(self):
        return reverse_lazy('home', args=[str(self.id)])