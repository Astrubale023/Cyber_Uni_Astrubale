import base64

def base64ToText(t):    #Simply returns the text decoded 
    return base64.b64decode(t).decode('UTF-8', errors="ignore")

def caesar_cracker(t, from_ = -30, to_ = +30):
    for i in range(from_, to_):
        curr_step = ''.join([chr(ord(c) + i) for c in t])

        print(f"Step {i} - {curr_step}")

#-------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------

hint = len(base64ToText("Q2Flc2FyCg=="))
puzzle = "fYZ7ipGIjFtsXpNLbHdPbXdaam1PS1c5lQ=="

puzzle_dec = base64ToText(puzzle)
print(puzzle_dec)
caesar_cracker(puzzle_dec)