**************
Getting Started
**************


Using class CacheViews
======================

.. highlight:: python

Example::

    from django.shortcuts import render

    # Django pages cache
    from pages_cache.pages_decorators import CacheViews

    # Create your views here.

    register = CacheViews( )

    @register.cache_view( key_prefix='home-index' )
    def home( request ):

        return render( request, 'index.html' )


Using class CacheViews with expire
==================================

.. highlight:: python

Example::

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
