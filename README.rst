===================
django-simple-pages
===================

|travis| |codacy| |coverage| |pypi|

.. |travis| image:: https://travis-ci.org/teapow/django-simple-pages.svg?branch=master
   :target: https://travis-ci.org/teapow/django-simple-pages

.. |codacy| image:: https://api.codacy.com/project/badge/Grade/9be353b72b944c788f886934fafe9742
   :target: https://www.codacy.com/app/teapow/django-simple-pages

.. |coverage| image:: https://api.codacy.com/project/badge/Coverage/9be353b72b944c788f886934fafe9742
   :target: https://www.codacy.com/app/teapow/django-envi

.. |pypi| image:: https://badge.fury.io/py/django-simple-pages.svg
    :target: https://badge.fury.io/py/django-simple-pages


`django-simple-pages` allows you to store HTML documents in models, which can
be served automatically without the need for hard-coded URL patterns.

Example use cases include:

* Serving a static website.
* Handling redirects for relocated resources.
* Verifying site ownership for Google Search Console.


Quick-start
===========

1. Install ``pip install django-simple-pages``.
2. Add ``simple_pages`` to ``INSTALLED_APPS``.
3. Add ``simple_pages.middleware.PageFallbackMiddleware`` to ``MIDDLEWARE``.
4. Run ``python manage.py migrate simple_pages``.


Usage
=====

Simply navigate to ``/admin`` and create a new ``Page`` object. A ``Page``
consists of the following attributes:

* **title:** The title of the page. This is rendered in the ``<title>`` tag
  if ``template_name`` is set to ``simple_pages/default.html``.

* **access_url:** The URL to access this page. All URLs should start with a
  leading slash.

* redirect_url: The URL to redirect to. If set, ``content`` will not be
  rendered.

* enabled: When set to True, this page is active. Setting this value to
  False means that you will see a 404 if you navigate to the page's
  ``access_url``.

* template_name: The path to the template used to render ``content``.
  Supported values include:

  * ``simple_pages/default.html``: Renders a ``<head>`` containing a
    ``<title>`` tag, and a ``<body>`` containing the page's ``content``.

  * ``simple_pages/raw.html``: Renders the page's ``content`` only.

Note: **Bold** attributes are required.


Changelog
=========

+----------------+-----------------------------------------------------------+
| Version        | Description                                               |
+================+===========================================================+
| 0.1.1          | Fixes incorrect help_text on Page.template_name.          |
+----------------+-----------------------------------------------------------+
| 0.1            | Initial version.                                          |
+----------------+-----------------------------------------------------------+
