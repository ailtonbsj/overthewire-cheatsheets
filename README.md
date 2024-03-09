# OverTheWire Cheatsheets and Write-ups

Some stuffs learned in wargames from OverTheWires CTFs.

- [Bandit](00-bandit/)

## Bandit cheatsheets

```bash
# Readme file with -
cat < -file

# Find files by size in bytes
find . -size 1033c

# Find files by user and groups
find / -user yourUser -group yourGroup

# Find files by user, group and size
find / -size 33c -group root -user root

# List all string from a binary file
strings raw.bin
cat raw.bin | strings

# Rot13 Caesar chiper with tr
tr 'A-Za-z' 'N-ZA-Mn-za-m' <<< "Pass"

# Umcompress fiel to show in terminal
zcat myfile.zip # Identical: gunzip -c
bzcat myfile.bzip # Identical: bzip2 -dc

# SSH without password
ssh -i privatekey.file user@domain.name -p 22

# Send data to a TCP port
echo "data" | nc domain.name 8080

# Connect to an server using SSL Encryption
openssl s_client -connect localhost:8080

# Connect to an server using SSL Encryption passing input data
openssl s_client -ign_eof -connect localhost:8080 <<< "data"
echo "data" | openssl s_client -ign_eof -connect localhost:8080

# Scan for open ports
nmap -p 31000-32000 localhost

# Scan for open ports and check if using SSL
nmap -p 31000-32000 --script ssl-enum-ciphers localhost

# Use netcat as a server
nc -l -p 3000

# See diference between files
diff file.old file.new

# Run ssh without execute .bashrc or .profile
ssh user@host -p 22 /bin/bash

# Crontab File format manual
man 5 crontab

# Make a temporary folder
mktemp -d

# Generate sequence 0..10 with 0000 format
seq -f "%04g" 0 10

# Gaining access to vim with more
# Press key v

# Gaining shell access with vim
# Type ":set shell=/bin/bash" and enter
# Type ":shell" and enter

# Show information about an tag
git show mytag-v1.0-rc

# Shortcut to bash
$0
```