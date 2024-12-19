import base64

alpha2morse = {'A': '.-', 'B': '-...', 'C': '-.-.',
'D': '-..', 'E': '.', 'F': '..-.',
'G': '--.', 'H': '....', 'I': '..',
'J': '.---', 'K': '-.-', 'L': '.-..',
'M': '--', 'N': '-.', 'O': '---',
'P': '.--.', 'Q': '--.-', 'R': '.-.',
'S': '...', 'T': '-', 'U': '..-',
'V': '...-', 'W': '.--', 'X': '-..-',
'Y': '-.--', 'Z': '--..',
'0': '-----', '1': '.----', '2': '..---',
'3': '...--', '4': '....-', '5': '.....',
'6': '-....', '7': '--...', '8': '---..',
'9': '----.' }

with open("zero_one") as challenge:
    input = challenge.read()

input = input.replace(' ', '')
input = input.replace('ZERO', '0')
input = input.replace('ONE', '1')
input = input.strip()

result1 = ''.join(chr(int(input[i:i+8], 2)) for i in range(0, len(input), 8))

#result2 = ''.join(chr(int(input[i*8:i*8+2], 2)) for i in range(len(input)//8))
print(result1)

decoded = base64.b64decode(result1).decode('ascii')

print(decoded)
#print(decoded.split())

morse2alpha = {value:key for key,value in alpha2morse.items()}
decoded2 = ''.join(morse2alpha.get(i_morse) for i_morse in decoded.split())
print(decoded2)