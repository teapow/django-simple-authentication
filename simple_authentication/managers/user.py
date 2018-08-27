from django.contrib.auth.models import BaseUserManager
from django.utils import timezone


class UserManager(BaseUserManager):
    """
    Model-manager for the custom User-model in the authentication app.

    Note: needs to be overridden in order that the createsuperuser command
    etc. works properly (since we use email as the only reference field,
    there is no username field).
    """
    def _create_user(self, email, password, is_staff, is_superuser,
                     **extra_fields):
        """
        Called to create a user object with the specified attributes.
        Used as a utility method by the two methods defined below.
        """
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set.')

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_active=True,
            is_staff=is_staff,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        """
        Create a normal user with the specified email & password

        :param email: email of the user to create
        :type email: str
        :param password: password to set into the created user
        :type password: str
        :param extra_fields: extra parameters to set into the created user
        :return: authentication.models.User -- the created user
        """
        return self._create_user(
            email=email,
            password=password,
            is_staff=False,
            is_superuser=False,
            **extra_fields
        )

    def create_superuser(self, email, password, **extra_fields):
        """
        Create a super user with the specified email & password

        :param email: email of the user to create
        :type email: str or unicode
        :param password: password to set into the created user
        :type password: str or unicode
        :param extra_fields: extra parameters to set into the created user
        :return: authentication.models.User -- the created super user
        """
        return self._create_user(
            email=email,
            password=password,
            is_staff=True,
            is_superuser=True,
            **extra_fields
        )
