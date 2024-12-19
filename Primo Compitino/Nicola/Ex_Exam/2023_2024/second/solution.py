import base64

def replace_chars(text, dict):
    replaced_text = ""
    for c in text:
        replaced_text += dict.get(c, c)

    return replaced_text



with open("cypher_text.txt", "r") as f:
    ZO_text = f.read()
    f.close()

ZO_dict = {"Z":"0", "O":"1"}
text = replace_chars(ZO_text, ZO_dict)

#ZO_semi_bin_text = ZO_text.replace("Z","0")
#ZO_bin_text = ZO_semi_bin_text.replace("O","1")
text = text.split(" ")
message = ""

for e in text:
    message += chr(int(e,2))

base64Decode = base64.b64decode(message)
#ZO_b64_text = base64.decode(ZO_chr_text)

print(base64Decode)