def nombreChiffre(n):
    a=[]
    b=0
    n=str(n)
    for i in range(0,len(n)):
        b=n[i]
        a.append(int(b))
    return a
