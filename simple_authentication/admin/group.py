"""Admin classes for the simple_authentication.Group model."""

from django.contrib.auth.admin import GroupAdmin as _GroupAdmin


class GroupAdmin(_GroupAdmin):
    """Admin class for the Group model of the auth app."""

    filter_horizontal = (
        "permissions",
    )
