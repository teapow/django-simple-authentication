from django.core.exceptions import PermissionDenied


def superuser_only(func):
    """ Decorator to limit view access to superusers only. """

    def wrapper(request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied
        return func(request, *args, **kwargs)

    return wrapper
