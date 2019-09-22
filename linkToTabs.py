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

# 2. we need to find the links (<a>) with a URL (href=...). Mind that if you
#    don't include the RE, you may also catch internal links.
for tag in soup('a',  attrs = {'href':re.compile('^http(s)?://')}):
    #    We have 2 options now: Open links in new tabs as we find them
    #                           Or store them in a list and open them later
    #    To save time, here we'll do the former.
    webbrowser.open_new_tab(tag.get('href'))

# Tadaa!
