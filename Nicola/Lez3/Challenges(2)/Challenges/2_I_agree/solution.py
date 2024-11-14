def caesar_cracker(t, from_ = -30, to_ = +30):
    for i in range(from_, to_):
        curr_step = ''.join([chr(ord(c) + i) for c in t])

        print(f"Step {i} - {curr_step}")

ciphred = "vhixoieemksktorywzvhxzijqni"

caesar_cracker(ciphred)

#per trovare la flag usare un brute force online del sistema di cifrature vigenere(l'evoluzione del Caesar)
#flag -> theforceisstrongwiththisone