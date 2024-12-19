with open("encrpyted.txt") as text:
    s_text = text.read()

puzzle = "MKXU IDKMI DM BDASKMI NLU XCPJNDICFQ! K VDMGUC KW PDT GKG NLKB HP LFMG DC TBUG PDTC CUBDTCXUB. K'Q BTCU MDV PDT VFMN F WAFI BD LUCU KN KB WAFI GDKMINLKBHPLFMGKBQDCUWTMNLFMFMDMAKMUNDDA"

s_text = s_text.replace('K', 'I')
s_text = s_text.replace('Q', 'M')

print(s_text)