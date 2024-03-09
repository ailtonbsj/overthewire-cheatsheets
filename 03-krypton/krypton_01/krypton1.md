# Trick

```bash
ssh krypton1@krypton.labs.overthewire.org -p 2231
cd /krypton/krypton1

cat krypton2 | tr 'A-Za-z' 'N-ZA-Mn-za-m'
# Alternative:
echo "YRIRY GJB CNFFJBEQ EBGGRA" | python caesar.py -d -o 13
```

# Flag

```
ROTTEN
```
