import base64
import string
import binascii

ALPHABET = list(string.printable)   # len = 100
LEN = len(ALPHABET)

def hex_to_ascii(message):
    decoded = binascii.unhexlify(message)
    return decoded

def XORdecode(message, KEY = "c4mPar1"):
    rep = len(message)//len(KEY) + 1
    key = (KEY*rep)[:len(message)] # adjust the key len
    xored = ''.join([chr(ord(a) ^ ord(b)) for a,b in zip(message, key)])
    return xored

def ROTdecode(message, pos):
    rot_dec = ''
    for c in message:
        i = ALPHABET.index(c)
        rot_dec += ALPHABET[(i+pos)%LEN]
    return rot_dec

def base32decode(message):
    message_bytes = message.encode('ascii')
    b32_bytes = base64.b32decode(message_bytes)
    b32_message = b32_bytes.decode('ascii')
    return b32_message

def base64decode(message):
    message_bytes = message.encode('ascii')
    b64_bytes = base64.b64decode(message_bytes)
    b64_message = b64_bytes.decode('ascii')
    return b64_message

with open("encrypted_flag.txt", "r") as f:
    text = f.read()
    f.close()

print("check")

asciix = hex_to_ascii(text).decode('ascii')
xorded = XORdecode(asciix)
decoded = xorded

print("check")

for _ in range(15):
    decoded = ROTdecode(decoded, -3)
    decoded = base32decode(decoded)
    decoded = ROTdecode(decoded, -13)
    decoded = base64decode(decoded)

text = decoded

print(text)