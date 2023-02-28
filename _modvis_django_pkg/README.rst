==============
_modvis_django_pkg
==============

Modvis is a Django app that can be installed in an existing Django project
Documentation: https://toddpy-django-cityloc-pkg.readthedocs.io/en/latest/

Installation
------------

1. Add "_modvis_django_pkg" to your INSTALLED_APPS setting in settings.py:
    INSTALLED_APPS = [
        ...
        
        '_modvis_django',

    ]

2. Include the _modvis_django URLconf in your project urls.py like this::
    path('', include('_modvis_django.urls')),

3. Start the development server and visit http://127.0.0.1:8000/