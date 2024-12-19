#-------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------
def intToBinary(number):    #returns the binary value of the number
    return format(number,'b')

def binaryToInt(number):
    return int(str(number),2)   #Simply returns the integer number 

def bit_to_string(binText):
    binText = binText.replace(" ", "")
    return "".join(chr(int(binText[8*i:8*i+8] , 2)) for i in range(len(binText)//8))

#-----------------------------------------EXAMPLE-------------------------------------------------------
n = 100 
print(intToBinary(n)) #Output: 1100100

n = 1101010111010100011001
print(binaryToInt(n)) #Output: 3503385

s = "01001000 01100101 01101100 01101100 01101111 00100000 01010111 01101111 01110010 01101100 01100100 "
s = s.replace(" ", "")
print(bit_to_string(s)) #Output: Hello World!

#-------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------

import base64

def base64ToText(t):    #Simply returns the text decoded 
    return base64.b64decode(t).decode('UTF-8')

#------------------------------------Example------------------------------------
s = "UHl0aG9uIGlzIGZ1bg=="  
print(base64ToText(s)) #Print result: Python is fun 

#-------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------

from collections import Counter

def getFreq(text):  #Gets the frequecies of every character given a string
    text = text.replace(" ", "") # Removes all the spaces
    return Counter(text)

#---------------------------EXAMPLE----------------------------
example = "Getting to know what Counter functions does"
print(getFreq(example))
#Output: Counter({'t': 6, 'n': 5, 'o': 5, 'e': 3, 'i': 2, 'w': 2, 'u': 2, 's': 2, 'G': 1,
#                 'g': 1, 'k': 1, 'h': 1, 'a': 1, 'C': 1, 'r': 1, 'f': 1, 'c': 1, 'd': 1})

#-------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------


def convertBinaryToText(binaryText): #Version that includes the spaces in the binaryText passed to the function
    convertedText = ""
    values = binaryText.split()
    for c in values:
        convertedText+= chr(int(c,2))
    return convertedText

def binaryToText(binaryText): #version that needs to be used when there are no group of 8 bits
    return ''.join(chr(int(''.join(c), 2)) for c in zip(*[iter(binaryText)]*8))

def stringToBinary(text): #Converts a string in a sequence of bits
    res = ''.join(format(ord(i), '08b') for i in text)
    return res

#-------------------------------------EXAMPLE-------------------------------------------
example = "01001000 01100101 01101100 01101100 01101111 00100000 01010111 01101111 01110010 01101100 01100100 00100001"
         #010010000110010101101100011011000110111100100000010101110110111101110010011011000110010000100001
print(convertBinaryToText(example)) #Output: Hello World!

secondExample = "01010000011110010111010001101000011011110110111000100000011010010111001100100000011001100111010101101110"
print(binaryToText(secondExample)) #Output: Python is fun

bits = stringToBinary("BitsToString")
print(bits) #Output : 010000100110100101110100011100110101010001101111010100110111010001110010011010010110111001100111
            #You can check if the output is correct using online tools with ASCII Character Encoding

#-------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------

def ceaserCipher (s, shift): #s is a string, shift is the key used to shift the characters
    result = ""
    for char in s:
        if ord(char)>= 65 and ord(char) <=90:   #Checks if the character is from A to Z
            result += chr((ord(char) - 65 + shift)%26 + 65)
        elif ord(char) >=97 and ord(char) <=122:
            result += chr((ord(char) - 97 + shift)%26 + 97) #Checks if the character is from a to z
        else:
            result+=char #Special simbols will be avoided and not shifted
    return result

def ceaserCipherBrutal(s, shift): #Called this function brutal because every character will be shifted
    result = ""
    for char in s:
        result+= chr(ord(char)+ shift) #Here every character is shifted
    return result

#-------------------------------------------------Examples#-------------------------------------------------
s = "}{[l^KlwOmwZjmOKW9"    #Example of ceaserCipherBrutal 
for i in range (-30, 30):
    print("Level:", i, ceaserCipherBrutal(s, i), "\n")


st = "Hello World"       #Example of ceaserCipher
for i in range (0,10):
    print("Level:", i,ceaserCipher(st, i),"\n")


encrypted = "Olssv Dvysk" #If for example we know the shift, we can decrypt it using ceasercipher function passing -shift
shift = 7
print(ceaserCipher(encrypted, -7))

#-------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------

import base64 #Useful only for the last example

def xorInt (num, key):
    return num ^ key #xor between two integers

def xorString(s1, s2): #Returns the xor of two strings
    xor = "".join([chr(ord(x) ^ ord(y)) for x, y in zip(s1, s2)])
    return xor

#--------------------------EXAMPLE------------------------------------------------
num = 20
key = 4
print(xorInt(num, key)) #It prints 16

encodedFlag = "I3gDKVh1Lh4EVyMDBFo=" #Encypted flag with Base64
Key = "e4Bne4Bne4Bne4"  #Key used for the xor
translated = base64.b64decode(encodedFlag).decode('UTF-8') #Decode the encodedFlag 
print(xorString(translated, Key)) #Output: FLAG=Alpacaman
#--------------------------------------------------------------------------------