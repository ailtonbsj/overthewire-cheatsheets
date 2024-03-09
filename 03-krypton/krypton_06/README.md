# Trick

```bash
mkdir /tmp/tmp6end && cd $_
ln -s /krypton/krypton6/keyfile.dat
python3 -c "print('A'*100)" > a
/krypton/krypton6/encrypt6 a b

cat b
# KEY = EICTDGYIYZKTHNSIRFXYCPFUEOCKRN

# CIPHER:
cat /krypton/krypton6/krypton7
# Use vigenere cipher online tool
```

# Flag

```
LFSRISNOTRANDOM
```

# Reference

[https://www.dcode.fr/vigenere-cipher](https://www.dcode.fr/vigenere-cipher)