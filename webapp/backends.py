# backends.py
from django.contrib.auth.backends import ModelBackend
from .models import loginModel,loginmodel2

class CustomAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = loginmodel2.objects.get(username=username, password=password)
            # Check if the provided password matches the stored password
            if user:
                return user
            else:
                return None
        except loginmodel2.DoesNotExist:
            return None
