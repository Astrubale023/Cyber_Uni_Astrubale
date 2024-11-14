import string
import random

vocabolary = list(string.ascii_letters) + list(string.digits)
psw_size = 10

password = "".join(random.choice(vocabolary) for i in range(psw_size))

print(f"{password}")