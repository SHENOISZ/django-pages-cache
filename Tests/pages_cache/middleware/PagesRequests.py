__author__ = 'shenoisz'

from django.conf import settings

class GetPageRequest( object ):

    #=======================================================
    #      add host, session and url for cache util
    #=======================================================
    def process_request( self, request ):

        settings.PAGE_CACHE_HOST = request.META['HTTP_HOST']
        settings.PAGE_METHOD = request.method
        settings.PAGE_URL = request.get_full_path( )
        settings.PAGE_SESSION = ''
        #=============================================
        #      if user logged add your session
        #=============================================
        if request.user.is_authenticated( ):

            settings.PAGE_SESSION = '|'+ str( request.META['HTTP_COOKIE'] ).replace(' ', '')

        #======================================
        #        create key for cache
        #======================================
        settings.KEY_PREFIX = (
            str( settings.PAGE_CACHE_HOST )+
            str( settings.PAGE_URL )+
            str( settings.PAGE_SESSION )
        )

    def process_response( self, request, response ):
        return response

