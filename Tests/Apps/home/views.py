from django.shortcuts import render
from django.views.generic.base import View
# shenoisz
from pages_cache.pages_decorators import CacheViews
# Create your views here.

register = CacheViews( )

class Home( View ):
    # add cache
    @register.cache_view( 
        key_prefix='home-index', 
        expire=60 * 15 
    )
    def get ( self, request, *args, **kwargs ):

        return render( request, 'index.html')


class HomePage( View ):
    
    def get ( self, request, *args, **kwargs ):

        return render( request, 'page.html')  


class ClearCache( View ):

    def get ( self, request, *args, **kwargs ):
        
        register.clear_cache( key_prefix='home-index' ) 

        return render( request, 'clear.html' )                 