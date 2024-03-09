#!/bin/python3

import requests, urllib, base64

site = "http://natas28.natas.labs.overthewire.org/"
auth = ("natas28", "skrwxciAe6Dnb0VfFDzDEHcCzQmv3Gd4")
s = requests.Session()
s.auth = auth

query = ""
while len(query) < 32:
    params = {'query': query}
    res = s.get(site, params=params)
    value = urllib.parse.unquote(res.url.split('=')[1])
    print("%2d bytes %d len %s" % (len(query), len(base64.b64decode(value)), value))
    query += "a"