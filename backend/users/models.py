from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.utils.translation import gettext_lazy as _
from .fields import CaseInsensitiveCharField
from phonenumber_field.modelfields import PhoneNumberField

class CustomUser(AbstractUser):
    # first_name, last_name, date_joined already included
    username_validator = ASCIIUsernameValidator()
    username = CaseInsensitiveCharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    email = models.EmailField("email address", unique=True)
    phone = PhoneNumberField(
        _("phone number"), 
        region="US", 
        unique=True,
        blank=True,
        help_text=_(
            "Enter phone number, including country code (e.g. +17071234567)."
        ),
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )

    def __str__(self):
        return self.username