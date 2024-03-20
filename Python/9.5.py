nombre=int(input("Entrer un nombres a 3 chiffres :"))
if nombre<100 or nombre >999:
	print("Erreur")
else:
	nombre=str(nombre)
	somme=int(nombre[0])+int(nombre[1])+int(nombre[2])
	print("La somme des chiffres est ",somme)
