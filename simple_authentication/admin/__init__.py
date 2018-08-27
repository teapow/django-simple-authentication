from django.contrib import admin
from django.contrib.auth.models import Group as _Group

from ..admin.user import UserAdmin
from ..admin.group import GroupAdmin
from ..models import User, Group


admin.site.unregister(_Group)
admin.site.register(User, UserAdmin)
admin.site.register(Group, GroupAdmin)
