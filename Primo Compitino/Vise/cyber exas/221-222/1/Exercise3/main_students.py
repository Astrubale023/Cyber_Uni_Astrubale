import random
import string


def transformation(input):
    	input = list(input)
    	input.append(input[0])
    	input.pop(0)
    	return "".join(input)

def encrypt(input, seed):
    	input = transformation(input)
    	input = list(input)
    	random.seed(seed)
    	input = [chr(ord(x) ^ random.randint(80, 120)) for x in input]
    	input = "".join(input)
    	return input

def detransformationes(input):
	input = list(input)
	last=input.pop(len(input)-1)
	input.insert(0,last)
	return "".join(input)

def decrypt(input, seed):
	input = list(input)
	random.seed(seed)
	input = [chr(ord(x) ^ random.randint(80, 120)) for x in input]
	input = "".join(input)
	input=detransformationes(input)
	return input

with open("./secret.txt", "r") as file:
    	cipher = file.read()

print(len(cipher))

with open("output.txt", "w") as file:
	
	for antonio in range(-20000,20000):
		file.write(decrypt(cipher, antonio))
		file.write("\n")
