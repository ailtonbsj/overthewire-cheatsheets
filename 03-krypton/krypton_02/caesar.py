import sys

chars = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz']

def encode(message, offset=13):
    enc_chars = str.maketrans(
        f'{chars[0]}{chars[1]}',
        f'{chars[0][offset:]}{chars[0][:offset]}{chars[1][offset:]}{chars[1][:offset]}'
    )
    return str.translate(message, enc_chars)

def decode(message, offset=13):
    dec_chars = str.maketrans(
        f'{chars[0][offset:]}{chars[0][:offset]}{chars[1][offset:]}{chars[1][:offset]}',
        f'{chars[0]}{chars[1]}'
    )
    return str.translate(message, dec_chars)

def usage():
    print("""USAGE: caesar [-e | -d] -o [value]

-e          to encrypt stdin streamming
-d          to decrypt stdin streamming
-o          offset characters. 13 for rot13.

EXAMPLES:
echo "HELLO WORLD" | python caesar.py -e -o 13
python caesar.py -d -o 13 <<< "URYYB JBEYQ"
""")

if len(sys.argv) < 3:
    usage()
    exit()

isEncoding = False
if sys.argv[1] == "-e":
    isEncoding = True
elif sys.argv[1] == "-d":
    isEncoding = False

shift = 13
if sys.argv[2] == "-o":
    shift = int(sys.argv[3])

for line in sys.stdin:
    if isEncoding:
        print(encode(line, shift))
    else:
        print(decode(line, shift))
