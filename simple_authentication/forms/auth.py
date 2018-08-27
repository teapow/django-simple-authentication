from django.contrib.auth.forms import AuthenticationForm as _AuthenticationForm


class AuthenticationForm(_AuthenticationForm):
    """ Custom authentication form. """

    def __init__(self, request=None, *a, **kw):
        """ Adds a placeholder to each field equal to the label. """
        super(AuthenticationForm, self).__init__(request=request, *a, **kw)

        for field in self.fields:
            _field = self.fields[field]
            _field.widget.attrs.update({'placeholder': _field.label})
