"""Model definitions representing users and their key attributes."""

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from ..managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """Model representing a user, their groups and related permissions.

    Used by setting AUTH_USER_MODEL to this class.
    """

    class Meta:
        """Meta class definition."""

        verbose_name = _("user")
        verbose_name_plural = _("users")

    email = models.EmailField(
        verbose_name=_("email"),
        max_length=255,
        unique=True,
        db_index=True,
        help_text=_("The primary identifier for this User.")
    )
    first_name = models.CharField(
        verbose_name=_("first name"),
        max_length=100,
        blank=True,
        db_index=True,
        help_text=_("The first name of the User.")
    )
    last_name = models.CharField(
        verbose_name=_("last name"),
        max_length=100,
        blank=True,
        db_index=True,
        help_text=_("The last name of the User.")
    )
    date_joined = models.DateTimeField(
        verbose_name=_("date joined"),
        default=timezone.now,
        db_index=True,
        help_text=_("The date on which this User joined. Autocompleted.")
    )
    is_active = models.BooleanField(
        verbose_name=_("active"),
        default=True,
        help_text=_("Designates whether this user should be treated as "
                    "active. Un-check this instead of deleting accounts.")
    )
    is_staff = models.BooleanField(
        verbose_name=_("staff"),
        default=False,
        help_text=_("Designates whether the user can log into this admin "
                    "site.")
    )
    force_password_change = models.BooleanField(
        verbose_name=_("force password change"),
        default=False,
        help_text=_("If checked, the user will be forced to change their "
                    "password on their next request. Only effective when "
                    "ForcePasswordChangeMiddleware is installed."),
    )

    USERNAME_FIELD = "email"
    objects = UserManager()

    def __str__(self):
        """Return a representation of the user as a string."""
        name_parts = [_n for _n in (self.first_name, self.last_name) if _n]
        name = " ".join(name_parts)
        return name or self.email

    @property
    def username(self):
        """Return the user's username."""
        return self.get_username()

    @property
    def name(self):
        """Return a displayable name for the user."""
        if not self.is_active:
            return _("Deactivated user")
        else:
            return str(self)

    def get_full_name(self):
        """Return the user's full name."""
        return self.name

    def get_short_name(self):
        """Return a displayable short name for the user."""
        if self.first_name:
            return self.first_name
        return self.email

    def get_long_name(self):
        """Return a displayable long name for the user."""
        if self.first_name and self.last_name:
            return "{first} {last}".format(
                first=self.first_name,
                last=self.last_name
            )
        elif self.first_name:
            return self.first_name
        else:
            return self.email

    def save(self, *args, **kwargs):
        """Ensure the user's email is lower-case before writing to the DB."""
        if self.email:  # pragma: no branch
            self.email = self.email.lower()
        return super(User, self).save(*args, **kwargs)

    def set_password(self, *args, **kwargs):
        """Unset the force password flag."""
        self.force_password_change = False
        return super(User, self).set_password(*args, **kwargs)
