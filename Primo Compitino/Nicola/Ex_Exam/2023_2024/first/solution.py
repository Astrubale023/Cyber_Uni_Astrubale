def extend_key(key, len_cipher):
    # Estende la chiave alla lunghezza del testo cifrato
    return "".join(key[i % len(key)] for i in range(len_cipher))

def decryption(crypted_text, key):
    plain_text = ""
    offset = 97

    for i in range(len(crypted_text)):
        char_crypt = crypted_text[i]
        char_key = key[i]

        if char_crypt.isalpha():
            decrypted_char = chr((ord(char_crypt) - ord(char_key)) % 26 + offset)
            plain_text += decrypted_char
        else:
            plain_text += char_crypt

    return plain_text


char_test = 'a'
if char_test.isalpha():
    print("bella")


# key used for the encryption
k = "tellmewhy"

# this is the encrypted message
flag = 'ltctfd{p-peye-mp-raee-ieu}'

k = extend_key(k, len(flag))

plain = decryption(flag, k)
print(f"Plain text: {plain}")