"""Test-specific URLs (referenced from run_tests.py)."""
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(
        regex=r"^admin/",
        view=admin.site.urls,
    ),
]
