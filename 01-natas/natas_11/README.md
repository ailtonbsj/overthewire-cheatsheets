# Tricks

## Header
```
Cookie: data=MGw7JCQ5OC04PT8jOSpqdmkgJ25nbCorKCEkIzlscm5ofnh8e354bjY%3D
```

## REPL: `php -a`
```php
$a = urldecode('MGw7JCQ5OC04PT8jOSpqdmkgJ25nbCorKCEkIzlscm5ofnh8e354bjY%3D');
$b = base64_decode($a);
$data = array( "showpassword"=>"no", "bgcolor"=>"#000000");
function xor_decode($out, $in) {
    $keyN = '';
    for($i=0;$i<strlen($in);$i++){
        for($j = 0;$j<255;$j++){
            $k = sprintf('%c',$j)[0];
            if(($out[$i] ^ $k) == $in[$i]) {
                $keyN[$i] = $k;
                break;
            }
        }
    }
    echo $keyN; 
}
xor_decode($b, json_encode($data));
```

## REPL: `php -a`
```php
$data = array( "showpassword"=>"yes", "bgcolor"=>"#000000");
function xor_decode($in) {
    $key = 'KNHL';
    $text = $in;
    $out = '';
    for($i=0;$i<strlen($text);$i++) {
        $out .= $text[$i] ^ $key[$i % strlen($key)];
    }
    $keyN = '';
    for($i=0;$i<strlen($in);$i++){
        for($j = 0;$j<255;$j++){
            $k = sprintf('%c',$j)[0];
            if(($out[$i] ^ $k) == $in[$i]) {
                $keyN[$i] = $k;
                break;
            }
        }
    }
    return $out;
}
echo urlencode(base64_encode(xor_decode(json_encode($data))));
```

## Header
```
Cookie: data=MGw7JCQ5OC04PT8jOSpqdmk3LT9pYmouLC0nICQ8anZpbXh8e354fGkz
```

# Flag

```
YWqo0pjpcXzSIl5NMAVxg12QxeC1w9QG
```