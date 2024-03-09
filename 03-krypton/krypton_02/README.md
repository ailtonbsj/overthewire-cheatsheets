# Trick

```bash
ssh krypton2@krypton.labs.overthewire.org -p 2231
cd /krypton/krypton2

for i in {0..23}; do echo "OMQEMDUEQMEK" | python caesar.py -d -o $i; done
```

# Flag

```
CAESARISEASY
```

# Reference

[https://www.dcode.fr/caesar-cipher](https://www.dcode.fr/caesar-cipher)