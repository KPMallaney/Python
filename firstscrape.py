
from urllib2 import urlopen, URLError, Request
from bs4 import BeautifulSoup

try:
    html = urlopen("http://www.pythonscraping.com/pages/page1.html")
except HTTPError as e:
    print 'The server couldn\'t fulfill the request.'
    print 'Error code: ', e.code
except URLError as e:
    print 'We failed to reach a server.'
    print 'Reason: ', e.reason
else:
   bsObj = BeautifulSoup(html, 'html.parser')
   print(bsObj.h1)
  
