# Django page cache #

# settings:

PAGE_CACHE = { }

# views:

from django.template.response import HttpResponse, RequestContext
from page_cache.cache import cache


page_index = 'index'
cache_index = 1
pages = cache( )
template = pages.add(<br>
    'capa/index.html',<br>
    request,<br>
    page_index,<br>
    cache_index<br>
)

return HttpResponse( template.get( page_index )[0] )
    
# add yours context request:    

c = RequestContext(request, {<br>
    'user':user,<br>
    'posts':posts,<br>
    'title':title,<br>
    'menu':menu,<br>
 })<br>

page_index = 'index'<br>
    cache_index = 1<br>
    pages = cache( )<br>
    template = pages.add(<br>
    'capa/index.html',<br>
    c,<br>
    page_index,<br>
    cache_index<br>
)<br>

