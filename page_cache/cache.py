__author__ = 'shenoisz'

from django.conf import settings
from django.template import loader

class cache( ):

    def add( self, page, request, page_index, cache_index ):

        pages = settings.PAGE_CACHE
        try:
            if pages.get( page_index )[1] == cache_index:
                return pages
            else:
                template = loader.get_template( page )
                pages[ page_index ] = [template.render( request ), cache_index]
                #print('else')
                return pages
        except:
            template = loader.get_template( page )
            pages[ page_index ] = [template.render( request ), cache_index]
            #print('except')
            return pages