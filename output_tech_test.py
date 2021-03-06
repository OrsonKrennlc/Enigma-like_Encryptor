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

cb1={"a":"a",
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
cb2={"a":"a",
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
cb3={"a":"a",
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
z=x[0:3]
for i in range(int(z[0])):
    cb1.update(panning(cb1))
for i in range(int(z[1])):
    cb2.update(panning(cb2))
for i in range(int(z[2])):
    cb3.update(panning(cb3))

y=z+' '
x=x[4:len(x)]
for i in range(len(x)):
    if x[i] in codebook.keys():
        for j in cb3.keys():
            if cb3[j]==x[i]:
                m = j
                cb3.update(panning(cb3))
                break
        for j in cb2.keys():
            if cb2[j]==m:
                m=j
                cb2.update(panning(cb2))
                break
        for j in cb1.keys():
            if cb1[j]==m:
                m=j
                cb1.update(panning(cb1))
                break
        y+=m
    else:
        y+=x[i]

print(y)
