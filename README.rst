============================
django-simple-authentication
============================

|travis| |codacy| |coverage| |pypi|

.. |travis| image:: https://travis-ci.org/teapow/django-simple-authentication.svg?branch=master
   :target: https://travis-ci.org/teapow/django-simple-authentication

.. |codacy| image:: https://api.codacy.com/project/badge/Grade/b3b408b162c14cc0b0d2ba6b46b86396
   :target: https://www.codacy.com/app/teapow/django-simple-authentication

.. |coverage| image:: https://api.codacy.com/project/badge/Coverage/b3b408b162c14cc0b0d2ba6b46b86396
   :target: https://www.codacy.com/app/teapow/django-simple-authentication

.. |pypi| image:: https://badge.fury.io/py/django-simple-authentication.svg
    :target: https://badge.fury.io/py/django-simple-authentication


Django's ``auth.User`` model uses a ``username`` field to uniquely identify a
user. ``django-simple-authentication`` uniquely identifies users with an
email address instead, removing the ``username`` field altogether.

Additionally, ``django-simple-authentication`` offers a feature that forces
users to change their password the next time they log in. This can be done
by setting ``simple_authentication.User.force_password_change`` to ``True``.
The ``ForcePasswordChangeMiddleware`` must be installed for this feature to
work properly.


Quick-start
===========

1. Install: ``pip install django-simple-authentication``.
2. Add: ``simple_authentication`` to ``INSTALLED_APPS``.
3. Add: ``AUTH_USER_MODEL = 'simple_authentication'``.
4. Add: ``simple_authentication.middleware.ForcePasswordChanceMiddleware`` to
   ``MIDDLEWARE``.
5. Make migrations: ``python manage.py makemigrations simple_authentication``.
6. Apply migrations: ``python manage.py migrate simple_authentication``.


Compatibility
=============

``django_simple_authentication`` has been tested on Django versions >= 2.0.
It may work without issue on earlier versions of Django (or Python), but
this is not officially supported.


Changelog
=========

+----------------+-----------------------------------------------------------+
| Version        | Description                                               |
+================+===========================================================+
| 0.1            | Initial version.                                          |
+----------------+-----------------------------------------------------------+
