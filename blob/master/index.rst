.. django-pages-cache documentation master file, created by
   sphinx-quickstart on Sun Jul 10 14:16:19 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to django-pages-cache's documentation!
==============================================


============
Installation
============

settings
--------

:

    MIDDLEWARE_CLASSES = [
        # add middleware
        'pages_cache.middleware.PagesRequests.GetPageRequest'
    ]

Getting Started
===============

Using class CacheViews
----------------------

:

    from django.shortcuts import render

    # Django pages cache
    from pages_cache.pages_decorators import CacheViews

    # Create your views here.

    register = CacheViews( )

    @register.cache_view( key_prefix='home-index' )
    def home( request ):

        return render( request, 'index.html' )
 

Using class CacheViews with expire
----------------------------------

:

    from django.shortcuts import render

    # Django pages cache
    from pages_cache.pages_decorators import CacheViews

    # Create your views here.

    register = CacheViews( )

    @register.cache_view( 
            key_prefix='home-index', 
            expire=60 * 15 
        )
    def home( request ):

        return render( request, 'index.html' )


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`