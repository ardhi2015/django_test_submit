from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend
from django.db.models import Q


class AuthBackend(BaseBackend):
    def authenticate(self, request, username: str, password: str):
        if username is None or password is None:
            raise ValueError("Invalid credentials")

        user_model = get_user_model()

        try:
            user = user_model.objects.get(
                Q(username__iexact=username) | Q(email__iexact=username)
            )
        except user_model.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None
