import urllib
import lxml.html
import urlparse
import sys

def get_dom(url):
    connection = urllib.urlopen(url)
    return lxml.html.fromstring(connection.read())

def get_links(url):
    return resolve_links((link for link in get_dom(url).xpath('//a/@href')))

def guess_root(links):
    for link in links:
        if link.startswith('http'):
            parsed_link = urlparse.urlparse(link)
            scheme = parsed_link.scheme + '://'
            netloc = parsed_link.netloc
            return scheme + netloc

def resolve_links(links):
    root = guess_root(links)
    for link in links:
        if not link.startswith('http'):
            link = urlparse.urljoin(root, link)
        yield link  

f = open('out.txt', 'w')

for link in get_links('http://www.paychex.com'):
	print >> f, link  # or f.write('...\n')    

f.close()
