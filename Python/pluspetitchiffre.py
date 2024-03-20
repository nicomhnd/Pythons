



def pluspetitchiffre(n):
    n=str(n) #On transforme la valeur le nombre en chaine de caractère
    b=n[0] #On a attribue le premier chiffre du nombre dans une variable : il servira de comparatif
    for i in range(1,len(n)):
        if n[i]<b: #Condition : on vérifie si l'index suivant est inférieur a la valeur b
            b=n[i] #Si c'est le cas, on change la valeur du comparatif
            c=n[i] #On garde la variable la plus petite 
        else:
            c=b #Sinon, on garde la valeur de b comme valeur la plus petite
    return c
            
            
        
        
