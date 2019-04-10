
def f1(zahl):
    L=[]
    z=zahl
    for i in range(0,8):
        L.append(zahl%2)
        zahl = zahl >>1
    L.reverse()
    print("Die Zahl %d binär: "%(z),L)

zahl = 15
f1(zahl)
f1(~zahl)
f1(~zahl+1)

