**************
A little more
**************

Using class CacheViews with extras
===================================       

.. highlight:: python

Example::

    from django.shortcuts import render

    # Django pages cache
    from pages_cache.pages_decorators import CacheViews

    # Create your views here.

    register = CacheViews( )

    # function fictitious of test mobile
    def similation( fake ):

        if fake == 'mobile':

            return 'mobile' 

        return 'desktop'       

    @register.cache_view(
            key_prefix='home-index',
            extras=similation( )
        )
    def home( request ):

        return render( request, 'index.html' )


Clear all cache with class CacheViews
===================================== 

Clear a view using ``clear_all( )``    

.. highlight:: python

Example::

    from django.shortcuts import render

    # Django pages cache
    from pages_cache.pages_decorators import CacheViews

    # Create your views here.

    cached = CacheViews( )

    def clear( request ):

        cached.clear_all( ) 

        return render( request, 'clear.html' )


Clear cache with class CacheViews using never for exception
============================================================ 

Clear a view using ``clear_cache( )``    

.. highlight:: python

Example::

    from django.shortcuts import render

    # Django pages cache
    from pages_cache.pages_decorators import CacheViews

    # Create your views here.

    cached = CacheViews( )

    def clear( request ):

        # clear all cache except url www.test.com:8000/detalhes
        cached.clear_cache( key_prefix='home-detalhes', never='www.test.com:8000/detalhes' )

        return render( request, 'clear.html' )       

Using list::

    from django.shortcuts import render

    # Django pages cache
    from pages_cache.pages_decorators import CacheViews

    # Create your views here.

    cached = CacheViews( )

    def clear( request ):

        url = [
            'pt.test.com:8000/detalhes', 
            'www.test.com:8000/detalhes', 
            'en.test.com:8000/detalhes'
        ]

        # clear all cache except url
        cached.clear_cache( key_prefix='home-detalhes', never=url )

        return render( request, 'clear.html' )          


Get all key prefix of views
============================

Clear a view using ``get_key_prefix( )``    

.. highlight:: python

Example::

    from django.shortcuts import render

    # Django pages cache
    from pages_cache.pages_decorators import CacheViews

    # Create your views here.

    cached = CacheViews( )

    def get_keys( request ):

        caches =  cached.get_key_prefix( key_prefix='home-index' )

        print( caches ) # display key prefix in terminal

        return render( 
                request, 
                'clear.html', 
                {'caches': caches} 
            )        