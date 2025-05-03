from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {"blank": True, "null": True}

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, **NULLABLE)
    country = models.CharField(max_length=100, **NULLABLE)
    avatar = models.ImageField(upload_to='users/avatars/', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    token = models.CharField(max_length=100, verbose_name="Token", **NULLABLE)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.email
