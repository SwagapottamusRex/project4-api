import email
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
# Create your models here.

class CustomUser(AbstractUser):

  image = models.CharField(max_length=200, blank=True)
  # email = models.EmailField(_('email address'), unique=False)
  