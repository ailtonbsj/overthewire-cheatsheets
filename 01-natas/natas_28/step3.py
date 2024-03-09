#!/bin/python3

import requests, urllib, base64, string

site = "http://natas28.natas.labs.overthewire.org/"
auth = ("natas28", "skrwxciAe6Dnb0VfFDzDEHcCzQmv3Gd4")
s = requests.Session()
s.auth = auth

query = "aaaaaaaaa"
chars = string.punctuation
# chars = "\"'\\"

for char in chars:
    params = {'query': query+char}
    res = s.get(site, params=params)
    value = urllib.parse.unquote(res.url.split('=')[1])
    print("%s | %s" % (query+char, value))