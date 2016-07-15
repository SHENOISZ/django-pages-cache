__author__ = 'shenoisz'

from django.core.cache import cache
from django.conf import settings
#from django.utils.decorators import available_attrs
#from functools import wraps

class CacheViews( ):
    """
        Class util cache with memcache
    """
    #======================================
    #         add views in cache
    #======================================
    def cache_view( self, *args, **kwargs ):

        expire = kwargs.pop('expire', None)
        key = kwargs.pop('key_prefix', None)
        url = kwargs.pop('key_url', True)
        extras = kwargs.pop('extras', '')
        only = kwargs.pop('only', None)

        def func( view_func ):
            #@wraps( view_func, assigned=available_attrs( view_func ) )
            def get_caching( request, *args, **kwargs ):
                #======================================
                #     if request is GET active cache
                #======================================
                if settings.PAGE_METHOD == "GET":

                    PATH = settings.KEY_PREFIX+ extras
                    response = cache.get( PATH )

                    # if not exist cache
                    if not response:
                        #==================================================
                        # create cache by specific url and save url prefix
                        #==================================================
                        if None != only:
                            response = view_func( request, *args, **kwargs )

                            if type( only ) == list:
                                for on in only:
                                    if on == PATH:
                                        cache.set( on, response, expire )
                            else:
                                if only == PATH:
                                    cache.set( only, response, expire )
                        else:
                            #=========================================
                            # create cache by url and save url prefix
                            #=========================================
                            if url:

                                lista = cache.get( key )
                                if not lista: lista = { }
                                lista[PATH] = PATH
                                response = view_func( request, *args, **kwargs )
                                cache.set( key, lista, expire )
                                cache.set( PATH, response, expire )

                            else:
                            #======================================
                            #        create cache by prefix
                            #======================================
                                response = view_func( request, *args, **kwargs )
                                cache.set( key, response, expire )

                        return response

                    else:
                        # if exist cache
                        return response
                else:
                    # sent original page in request POST, DELETE, UPDATE
                    response = view_func( request, *args, **kwargs )
                    return response

                return response

            return get_caching

        return func
    #======================================
    #          clear cache by url
    #======================================
    def clear_cache_url( self, url=None ):

        if None != url:

            if type( url ) == list:
                for u in url:
                    cache.delete( u )
            else:
                cache.delete( url )
        else:
            return False

    #======================================
    #          clear cache by key
    #======================================
    def clear_cache( self, key_prefix=None, view='', never='' ):

        if None != key_prefix:

            caches = cache.get( key_prefix )

            if None != caches:

                if type( never ) == list:
                    for n in never:
                        try:
                            del caches[n]
                        except:pass
                else:
                    try:
                        del caches[never]
                    except:pass

                for key in caches:
                    cache.delete( caches[key] )

                cache.delete( key_prefix )

                return True

            print('==============================================')
            print(' Key Prefix not exist in views = '+ view +'  ')
            print('==============================================')

            return False

    #======================================
    #        clear caches all
    #======================================
    def clear_all( self ):
        cache.clear( )

    def get_key_prefix(self, key_prefix=None):

        if None != key_prefix:

            caches = cache.get( key_prefix )
            return caches

        else:
            return None

