

def depot(n):
    if n==1:
        return 1
    else :
        return(depot(n-1)+1.01)


def jour(n):
    L=["Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi","Dimanche"]
    return L[n%7-1]



def contenu(n):
    c=0
    for i in range(0,n-1):
        if n>0:
            c=c+depot(n)
    return c



def tirelire():
    n=0
    while(contenu(n)<=1500):
            n=n+1
    return contenu(n),jour(n)
    
