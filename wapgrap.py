from urllib2 import urlopen, URLError, Request
from bs4 import BeautifulSoup

try:
    html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
except HTTPError as e:
    print 'The server couldn\'t fulfill the request.'
    print 'Error code: ', e.code
except URLError as e:
    print 'We failed to reach a server.'
    print 'Reason: ', e.reason
else:
   #bsObj = BeautifulSoup(html, 'html.parser')
   #print(bsObj.h1)
   #print(bsObj.h2)
   bsObj = BeautifulSoup(html, 'html.parser')

# Printing all names with green text
 #nameList = bsObj.findAll("span" , {"class" : "green"})
   #for name in nameList:
    #print(name.get_text())

# Printing both names and red paragraphs
#randList = bsObj.findAll("span" , {"class" : {"green", "red"} })
#for rand in randList:
    #print(rand.get_text())

#counting number of times a name appears
nameList = bsObj.findAll(text = "the prince")
print(len(nameList))
