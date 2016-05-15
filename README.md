<h1 style="color: #a4c7f7;">Django page cache</h1>

# settings:

PAGE_CACHE = { }

# views:

from django.template.response import HttpResponse, RequestContext<br>
from page_cache.cache import cache<br><br>


page_index = 'index'
cache_index = 1
pages = cache( )
template = pages.add(<br>
&nbsp;&nbsp;&nbsp;'capa/index.html',<br>
&nbsp;&nbsp;&nbsp;request,<br>
&nbsp;&nbsp;&nbsp;page_index,<br>
&nbsp;&nbsp;&nbsp;cache_index<br>
)

return HttpResponse( template.get( page_index )[0] )
    
# add yours context request:    

c = RequestContext(request, {<br>
&nbsp;&nbsp;&nbsp;'user':user,<br>
&nbsp;&nbsp;&nbsp;'posts':posts,<br>
&nbsp;&nbsp;&nbsp;'title':title,<br>
&nbsp;&nbsp;&nbsp;'menu':menu,<br>
 })<br>

page_index = 'index'<br>
cache_index = 1<br>
pages = cache( )<br>
template = pages.add(<br>
&nbsp;&nbsp;&nbsp;'capa/index.html',<br>
&nbsp;&nbsp;&nbsp;c,<br>
&nbsp;&nbsp;&nbsp;page_index,<br>
&nbsp;&nbsp;&nbsp;cache_index<br>
)<br>

