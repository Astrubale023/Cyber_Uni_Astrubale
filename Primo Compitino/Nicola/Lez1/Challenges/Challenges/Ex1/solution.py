
input = 'abc'
key = 2
otput = 'cde'

test_output = "".join(chr(ord(c_inp) + key) for c_inp in input)

print(f"Input: {input}\nOutput: {otput}\nTest->{test_output}")