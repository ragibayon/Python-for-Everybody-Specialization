# -*- coding: utf-8 -*-

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

def retrive_name(url,position,repeat):
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    link_tags=[]
    for i in range(repeat):
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        # Retrieve all of the anchor tags
        tags = soup('a')
        link_tags=[]
        for tag in tags:
            link=tag.get('href', None)
            link_tags.append(link)
        url=link_tags[position-1]

    return link_tags[position-1]

# url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
# position=3
# repeat=4
url='http://py4e-data.dr-chuck.net/known_by_Murrun.html'
position=18
repeat=7

required_link=(retrive_name(url,position,repeat))
name=re.search(r'known_by_(\w+).',required_link)[1]
print(name)

