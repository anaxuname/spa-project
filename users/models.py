from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    User - модель пользователя
    """

    username = None
    first_name = None
    last_name = None
    email = models.EmailField(unique=True, verbose_name="Email")
    full_name = models.CharField(max_length=255, verbose_name="Full Name")
    phone_number = models.CharField(max_length=50, verbose_name="Phone_number")
    chat_id = models.CharField(max_length=50, blank=True, null=True, verbose_name="Chat_id")
    avatar = models.ImageField(upload_to="users", blank=True, null=True, verbose_name="Avatar")
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
