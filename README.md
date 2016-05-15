# Django page cache #

# settings:

PAGE_CACHE = { }

Add in INSTALLED_APPS

# views:

from django.template.response import HttpResponse, RequestContext<br>
from page_cache.cache import cache<br><br>


page_index = 'index'<br>
cache_index = 1<br>
pages = cache( )<br>
template = pages.add(<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'capa/index.html',<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;request,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;page_index,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cache_index<br>
)

return HttpResponse( template.get( page_index )[0] )
    
# add yours context request:    

c = RequestContext(request, {<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'user':user,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'posts':posts,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'title':title,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'menu':menu,<br>
 })<br>

page_index = 'index'<br>
cache_index = 1<br>
pages = cache( )<br>
template = pages.add(<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'capa/index.html',<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;c,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;page_index,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cache_index<br>
)<br>

# license

Copyright (c) 2016 Marcelo Rodrigues

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

