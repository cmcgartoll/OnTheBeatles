from django.contrib.auth.base_user import BaseUserManager
from rest_framework.authtoken.models import Token

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password, **extra_fields):
        if not email:
            raise ValueError('The email must be set')
        if not username:
            raise ValueError('The username must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def get_user_from_token(self, key):
        token = Token.objects.get(key=key)
        return token.user
