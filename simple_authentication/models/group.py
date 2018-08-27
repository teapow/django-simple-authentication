from django.contrib.auth.models import Group as _Group


class Group(_Group):
    """ Wrapper around django.contrib.auth's Group model. """
    pass
