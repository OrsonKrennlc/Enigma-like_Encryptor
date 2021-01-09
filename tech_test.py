codebook={"a":"a",
          "b":"b",
          "c":"c",
          "d":"d",
          "e":"e",
          "f":"f",
          "g":"g",
          "h":"h",
          "i":"i",
          "j":"j",
          "k":"k",
          "l":"l",
          "m":"m",
          "n":"n",
          "o":"o",
          "p":"p",
          "q":"q",
          "r":"r",
          "s":"s",
          "t":"t",
          "u":"u",
          "v":"v",
          "w":"w",
          "x":"x",
          "y":"y",
          "z":"z",}

def panning(codebook):
    cbtem = str(codebook)
    newcb = {}
    newcb[cbtem[2]] = cbtem[257]
    for j in range(2, 26, 1):
        newcb[cbtem[10 * j - 8]] = cbtem[10 * (j - 1) - 3]
    newcb[cbtem[252]] = cbtem[247]
    return(newcb)

x=str(input())
y=""
y+=codebook[x[0]]
for i in range(1,len(x)):
    codebook.update(panning(codebook))
    if x[i]!=".":
        y+=codebook[x[i]]
    else:
        y+="."
print(y)