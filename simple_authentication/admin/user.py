from django.contrib.auth import login
from django.contrib.auth.admin import UserAdmin as _UserAdmin
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _

from ..forms.admin import UserChangeForm, UserCreationForm


class UserAdmin(_UserAdmin):
    """ Admin for the User model of the authentication app. """
    form = UserChangeForm
    add_form = UserCreationForm
    add_form_template = 'admin/authentication/user/add_form.html'
    add_fieldsets = (
        (_("Primary fields"), {
            'fields': (
                'email',
                'first_name',
                'last_name',
                'password1',
                'password2',
            ),
        }),
    )
    fieldsets = (
        (_("Primary fields"), {
            'fields': (
                'email',
                'first_name',
                'last_name',
                'password',
                'force_password_change',
            )
        }),
        (_("Permissions"), {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            )
        }),
        (_("Additional information"), {
            'fields': (
                'last_login',
                'date_joined',
            )
        }),
    )
    ordering = (
        'email',
    )
    list_display = (
        'pk',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff',
        'is_superuser',
    )
    list_filter = (
        'is_active',
        'is_staff',
        'is_superuser',
        'date_joined',
    )
    search_fields = (
        'id',
        'email',
        'first_name',
        'last_name',
    )
    readonly_fields = (
        'date_joined',
        'last_login',
    )
    filter_horizontal = (
        'groups',
        'user_permissions',
    )

    def hijack(self, request, queryset):
        """
        Admin action, hijack a selected user, logging in as them without
        needing to know or change any password details etc.
        """
        if queryset.count() > 1:
            messages.error(request, _('You can only log-in as one user!'))
            return HttpResponseRedirect(request.get_full_path())

        user = queryset[0]
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request, user)
        return HttpResponseRedirect('/')
    hijack.short_description = _('Log in as selected user')

    actions = [
        'hijack'
    ]
