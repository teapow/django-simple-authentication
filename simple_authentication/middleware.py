import re

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, resolve


class ForcePasswordChangeMiddleware:
    """ Force the user to change their password on the next request. """

    def __init__(self, get_response):
        """ 1.11-style constructor. """
        self.get_response = get_response

    def __call__(self, request):
        """ 1.11-style implementation. """
        user = request.user
        if user.is_authenticated and user.force_password_change:
            path = request.path
            change_url = reverse_lazy(viewname='admin:password_change')

            is_admin_url = getattr(resolve(path), 'app_name') == 'admin'
            is_change_url = re.match(r'^{}?'.format(change_url), path)

            if is_admin_url and not is_change_url:
                return HttpResponseRedirect(redirect_to=change_url)

        response = self.get_response(request)
        return response
