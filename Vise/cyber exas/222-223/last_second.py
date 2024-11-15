import string
import itertools    # if you want, it is not necessary

XOR_KEY='??' # can be only letters

ALFABET=string.printable

# read the file with the encrypted message
with open('encrypted', 'r') as f:
    encrypted_message=f.read()
    
def xorString(s1, s2): #Returns the xor of two strings
	
    xor = "".join([chr(ord(x) ^ ord(y)) for x, y in zip(s1, s2)])
    return xor

def binaryToText(binaryText): #version that needs to be used when there are no group of 8 bits
    return ''.join(chr(int(''.join(c), 2)) for c in zip(*[iter(binaryText)]*8))
    
def XORencode(message, KEY):
    rep = len(message)//len(KEY) + 1
    key = (KEY*rep)[:len(message)] # adjust the key len
    xored = ''.join([chr(ord(a) ^ ord(b)) for a,b in zip(message, key)])
    return xored

#--------------------------EXAMPLE------------------------------------------------
encodedFlag = encrypted_message #Encypted flag with Base64



for i in range(len(ALFABET)):
	for j in range(len(ALFABET)):
		key=""+ALFABET[i]+ALFABET[j]
		res=XORencode(encodedFlag, key)
		#res=binaryToText(res)
		if "spritz" in res:
			print(res)