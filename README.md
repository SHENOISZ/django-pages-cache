# Django page cache #

# settings:

PAGE_CACHE = { }

# views:

from django.template.response import HttpResponse, RequestContext
from page_cache.cache import cache


page_index = 'index'
cache_index = 1
pages = cache( )
template = pages.add(
'capa/index.html',
request,
page_index,
cache_index
)

return HttpResponse( template.get( page_index )[0] )
    
# add yours context request:    

c = RequestContext(request, {
'user':user,
'posts':posts,
'title':title,
'menu':menu,
 })

page_index = 'index'
cache_index = 1
pages = cache( )
template = pages.add(
'capa/index.html',
c,
page_index,
cache_index
)

