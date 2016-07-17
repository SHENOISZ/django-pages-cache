************************
Installation & Settings
************************

pip
===

Example::

    pip install django-pages-cache

settings
========

.. highlight:: python

Example::

    MIDDLEWARE_CLASSES = [
        # add middleware
        'pages_cache.middleware.PagesRequests.GetPageRequest'
    ]
