keys = [(1,9,4),(4,2,8),(4,8,3),(7,1,5),(8,10,1)]

with open("book.txt") as book:
    text = book.read()

paragraphs = text.split("\n\n")

for i in range(len(paragraphs)):
    par = paragraphs[i]
    par = par.split("\n")
    for j in range(len(par)):
        line = par[j]
        line = line.split(" ")
        par[j] = line
    paragraphs[i] = par

for k in keys:
    print(f"{paragraphs[k[0]-1][k[1]-1][k[2]-1]}")
