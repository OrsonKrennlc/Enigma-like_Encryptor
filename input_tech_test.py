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

cb1=codebook
cb2=codebook
cb3=codebook

def panning(codebook):
    cbtem = str(codebook)
    newcb = {}
    newcb[cbtem[2]] = cbtem[257]
    for j in range(2, 26, 1):
        newcb[cbtem[10 * j - 8]] = cbtem[10 * (j - 1) - 3]
    newcb[cbtem[252]] = cbtem[247]
    return(newcb)

x=str(input())
z=x[0:3]
for i in range(int(z[0])):
    panning(cb1)
for i in range(int(z[1])):
    panning(cb2)
for i in range(int(z[2])):
    panning(cb3)

x=x[3:len(x)]
y=x[3:len(x)]
y+=codebook[x[0]]
for i in range(1,len(x)):
    cb1.update(panning(cb1))
    if x[i]!=".":
        y+=cb1[x[i]]
    else:
        y+=x[i]
    cb1.update(panning(cb1))
    if x[i] != ".":
        y += cb2[x[i]]
    else:
        continue
    cb1.update(panning(cb1))
    if x[i] != ".":
        y += cb3[x[i]]+"-"
    else:
        continue
print(y[0:len(y)-1])
