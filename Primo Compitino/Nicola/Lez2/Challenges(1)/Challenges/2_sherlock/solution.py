with open("challenge.txt") as book:
    text = book.read()

secret_msg = ''
for char in text:
    if(char.isupper()):
        secret_msg += char

secret_msg = secret_msg.replace('ZERO','0').replace('ONE', '1')

for i in range(0, len(secret_msg), 8):
    print(chr(int(secret_msg[i:i+8], 2)), end='')