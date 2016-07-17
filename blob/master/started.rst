****************
Getting Started
****************


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


Using class CacheViews with specific url
=========================================

.. highlight:: python

Example::

    from django.shortcuts import render

    # Django pages cache
    from pages_cache.pages_decorators import CacheViews

    # Create your views here.

    register = CacheViews( )

    @register.cache_view(
            only='www.test.com:8000/detalhes'
        )
    def home( request ):

        return render( request, 'index.html' )


Using class CacheViews with specific url and list
================================================= 

.. highlight:: python

Example::

    from django.shortcuts import render

    # Django pages cache
    from pages_cache.pages_decorators import CacheViews

    # Create your views here.

    register = CacheViews( )

    url_prefix = url = [
        'pt.test.com:8000/detalhes', 
        'www.test.com:8000/detalhes', 
        'en.test.com:8000/detalhes'
    ]

    @register.cache_view( only=url_prefix )
    def home( request ):

        return render( request, 'index.html' )    

Using expire::         


    from django.shortcuts import render

    # Django pages cache
    from pages_cache.pages_decorators import CacheViews

    # Create your views here.

    register = CacheViews( )

    url_prefix = url = [
        'pt.test.com:8000/detalhes', 
        'www.test.com:8000/detalhes', 
        'en.test.com:8000/detalhes'
    ]

    @register.cache_view( 
            only=url_prefix, 
            expire=60 * 15
        )
    def home( request ):

        return render( request, 'index.html' )   


Using class CacheViews with class-based views
=============================================

.. highlight:: python

Example::

    from django.shortcuts import render

    # Django pages cache
    from pages_cache.pages_decorators import CacheViews

    # Create your views here.

    register = CacheViews( )

    class Home( View ):

        @register.cache_view( 
            key_prefix='home-index'
        )
        def get ( self, request, *args, **kwargs ):

            return render( request, 'index.html')

Using expire::

    from django.shortcuts import render

    # Django pages cache
    from pages_cache.pages_decorators import CacheViews

    # Create your views here.

    register = CacheViews( )

    class Home( View ):

        @register.cache_view( 
            key_prefix='home-index', 
            expire=60 * 15 
        )
        def get ( self, request, *args, **kwargs ):

            return render( request, 'index.html')            


Using class CacheViews with unique key prefix for all requests
==============================================================        

.. highlight:: python

Example::

    from django.shortcuts import render

    # Django pages cache
    from pages_cache.pages_decorators import CacheViews

    # Create your views here.

    register = CacheViews( )

    @register.cache_view(
            key_prefix='home-index',
            key_url=False
        )
    def home( request ):

        return render( request, 'index.html' )