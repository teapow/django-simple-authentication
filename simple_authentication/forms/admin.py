from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import ugettext_lazy as _

from ..models import User


class UserChangeForm(forms.ModelForm):
    """ Change form for the User model in the admin. """

    error_messages = {
        'duplicate_email': _('A user with that email already exists.'),
    }

    password = ReadOnlyPasswordHashField(
        label=_("Password"),
        help_text=_("Raw passwords are not stored, so there is no way to see "
                    "this user's password, but you can change the password "
                    "using <a href=\"../password/\">this form</a>."))

    class Meta:
        """ Metadata for the model-form. """
        model = User
        exclude = ()

    def clean_password(self):
        """ Clean the password value passed in form submission. """
        return self.initial['password']

    def clean_email(self):
        """ Ensure the email address for the user is unique. """
        email = self.cleaned_data['email']
        email_exists = User.objects.filter(
            email=email
        ).exclude(
            id=self.instance.id
        ).exists()

        if email_exists:
            raise forms.ValidationError(self.error_messages['duplicate_email'])
        return email


class UserCreationForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    error_messages = {
        'duplicate_email': _("A user with that email already exists."),
        'password_mismatch': _("The two password fields didn't match."),
    }
    password1 = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput,
        help_text=_('Enter a password.')
    )
    password2 = forms.CharField(
        label=_('Password confirmation'),
        widget=forms.PasswordInput,
        help_text=_('Enter the same password as above, for verification.')
    )

    class Meta:
        """ Metadata for the model-form. """
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        )

    def clean_email(self):
        """ Clean the email field passed in form-submission. """
        email = self.cleaned_data['email']
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email

        raise forms.ValidationError(self.error_messages['duplicate_email'])

    def clean_password2(self):
        """ Clean the password confirmation field passed in submission. """
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            error_message = self.error_messages['password_mismatch']
            raise forms.ValidationError(error_message)

        return password2

    def save(self, commit=True):
        """ Create the User object from the submitted form data. """
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save(update_fields=['password', ])
        return user
