'''
As long as you have a URL, the webbrowser module lets users cut out the step of
opening the browser and directing themselves to a website. Other programs could
use this functionality to do the following:

AIM: Open all links on a page in separate browser tabs.

'''
### LIBRARIES WE'RE GOING TO NEED ###
# WEBBROWSER: to open links in a browser
# RE: to use and parse regular expressions
# ULRLIB: to fetch URLs
# BEAUTIFULSOUP: to web scrape

import webbrowser
import re
import urllib.request as URL
from bs4 import BeautifulSoup

# urlopen() returns the source code of the URL passed
start_page = URL.urlopen('https://teamtreehouse.com')
#print(start_page.read())

# now we need to find the links
# 1. let's create a soup with the source code
soup = BeautifulSoup(start_page, features='lxml')

# 2. we need to find the links (<a>) with a URL (href=...)
for tag in soup('a',  attrs = {'href':re.compile('^http(s)?://')}):
    print(tag.get('href'))
