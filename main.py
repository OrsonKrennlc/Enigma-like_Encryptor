import tkinter as tk

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
cb1 = {"a": "a",
       "b": "b",
       "c": "c",
       "d": "d",
       "e": "e",
       "f": "f",
       "g": "g",
       "h": "h",
       "i": "i",
       "j": "j",
       "k": "k",
       "l": "l",
       "m": "m",
       "n": "n",
       "o": "o",
       "p": "p",
       "q": "q",
       "r": "r",
       "s": "s",
       "t": "t",
       "u": "u",
       "v": "v",
       "w": "w",
       "x": "x",
       "y": "y",
       "z": "z", }
cb2 = {"a": "a",
       "b": "b",
       "c": "c",
       "d": "d",
       "e": "e",
       "f": "f",
       "g": "g",
       "h": "h",
       "i": "i",
       "j": "j",
       "k": "k",
       "l": "l",
       "m": "m",
       "n": "n",
       "o": "o",
       "p": "p",
       "q": "q",
       "r": "r",
       "s": "s",
       "t": "t",
       "u": "u",
       "v": "v",
       "w": "w",
       "x": "x",
       "y": "y",
       "z": "z", }
cb3 = {"a": "a",
       "b": "b",
       "c": "c",
       "d": "d",
       "e": "e",
       "f": "f",
       "g": "g",
       "h": "h",
       "i": "i",
       "j": "j",
       "k": "k",
       "l": "l",
       "m": "m",
       "n": "n",
       "o": "o",
       "p": "p",
       "q": "q",
       "r": "r",
       "s": "s",
       "t": "t",
       "u": "u",
       "v": "v",
       "w": "w",
       "x": "x",
       "y": "y",
       "z": "z", }

def panning(codebook):
    cbtem = str(codebook)
    newcb = {}
    newcb[cbtem[2]] = cbtem[257]
    for j in range(2, 26, 1):
        newcb[cbtem[10 * j - 8]] = cbtem[10 * (j - 1) - 3]
    newcb[cbtem[252]] = cbtem[247]
    return(newcb)

def coding(x):
    z = x[0:3]
    for i in range(int(z[0])):
        cb1.update(panning(cb1))
    for i in range(int(z[1])):
        cb2.update(panning(cb2))
    for i in range(int(z[2])):
        cb3.update(panning(cb3))

    y = z + ' '
    x = x[4:len(x)]
    for i in range(len(x)):
        if x[i] in codebook.keys():
            m = cb1[x[i]]
            cb1.update(panning(cb1))
            m = cb2[m]
            cb2.update(panning(cb2))
            m = cb3[m]
            cb3.update(panning(cb3))
            y += m
        else:
            y += x[i]
            continue
    cb1.update(codebook)
    cb2.update(codebook)
    cb3.update(codebook)
    print(y)
    return(y)

def decoding(x):
    z = x[0:3]
    for i in range(int(z[0])):
        cb1.update(panning(cb1))
    for i in range(int(z[1])):
        cb2.update(panning(cb2))
    for i in range(int(z[2])):
        cb3.update(panning(cb3))

    y = z + ' '
    x = x[4:len(x)]
    for i in range(len(x)):
        if x[i] in codebook.keys():
            for j in cb3.keys():
                if cb3[j] == x[i]:
                    m = j
                    cb3.update(panning(cb3))
                    break
            for j in cb2.keys():
                if cb2[j] == m:
                    m = j
                    cb2.update(panning(cb2))
                    break
            for j in cb1.keys():
                if cb1[j] == m:
                    m = j
                    cb1.update(panning(cb1))
                    break
            y += m
        else:
            y += x[i]
    cb1.update(codebook)
    cb2.update(codebook)
    cb3.update(codebook)
    print(y)
    return(y)

def coding_fin(x):
    mes=coding(x)
    root = tk.Tk()
    root.title("MESSAGE")
    root.geometry("600x200")
    root.geometry("+220+220")
    message=tk.Message(root,text=mes,width=500,)
    message.pack()
    root.mainloop()

def decoding_fin(x):
    mes=decoding(x)
    root = tk.Tk()
    root.title("MESSAGE")
    root.geometry("600x200")
    root.geometry("+320+320")
    message=tk.Message(root,text=mes,width=500,)
    message.pack()
    root.mainloop()

def inputbox():
    root = tk.Tk()
    root.title("CODING")
    root.geometry("600x200")
    root.geometry("+210+210")
    enter=tk.Entry(root,width=50)
    enter.pack(side="top",pady=20)
    start=tk.Button(root,text="START",height=1,width=10,command=lambda:coding_fin(enter.get()))
    start.pack(side="bottom",pady=20)
    root.mainloop()

def outputbox():
    root = tk.Tk()
    root.title("DECODING")
    root.geometry("600x200")
    root.geometry("+310+310")
    enter=tk.Entry(root,width=50)
    enter.pack(side="top",pady=20)
    start=tk.Button(root,text="START",height=1,width=10,command=lambda:decoding_fin(enter.get()))
    start.pack(side="bottom",pady=20)
    root.mainloop()

root=tk.Tk()
root.title("ENCRYPTION")
root.geometry("200x200")
root.geometry("+200+200")
inputing=tk.Button(root,text="CODING",height=3,width=10,command=lambda:inputbox())
inputing.pack(side="top",pady=20)
outputing=tk.Button(root,text="DECODING",height=3,width=10,command=lambda:outputbox())
outputing.pack(side="bottom",pady=20)
root.mainloop()