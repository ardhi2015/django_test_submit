from django.contrib.auth.base_user import BaseUserManager


class AppUserManager(BaseUserManager):
    def create_user(
        self,
        email=None,
        password=None,
        **extra_fields,
    ):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save()
        return user
