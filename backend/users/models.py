from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import ASCIIUsernameValidator
from .fields import CaseInsensitiveCharField
from .managers import CustomUserManager
from phonenumber_field.modelfields import PhoneNumberField
from rest_framework.authtoken.models import Token

class CustomUser(AbstractUser):
    # first_name, last_name, date_joined already included
    username_validator = ASCIIUsernameValidator()
    username = CaseInsensitiveCharField(
        "username",
        max_length=150,
        unique=True,
        help_text= "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
        validators=[username_validator],
        error_messages={
            "unique": "A user with that username already exists.",
        },
    )
    email = models.EmailField("email address", unique=True)
    phone = PhoneNumberField(
        "phone number", 
        region="US", 
        unique=True,
        blank=True,
        help_text= "Enter phone number, including country code (e.g. +17071234567).",
        error_messages={
            "unique": "A user with that username already exists.",
        },
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    objects = CustomUserManager()

    def get_album_rating(self, album_id):
        return self.album_ratings.filter(album__id=album_id)

    @property
    def token_key(self):
        return Token.objects.get(user=self).first().key

    def __str__(self):
        return self.username
