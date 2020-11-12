#TAREA GRUPAL N°6

import random as rd
palabras=["impostor", "capuccino", "helado", "profesor", "jugar"]
indice = rd.randint(0,len(palabras)-1) #0 1 2 3 4 5
pal=palabras[indice]
palMayus=pal.upper() #impostor
letraPri=palMayus[0] #I
letraUlt=palMayus[-1] #R
n=len(palMayus)-2
subGuion=n *" _ "
pista= letraPri+subGuion+letraUlt
print(pista)
paraUser=input("Adivine la palabra: ").upper()
condicion= paraUser == palMayus
print("¿Ganó?: ",condicion)

