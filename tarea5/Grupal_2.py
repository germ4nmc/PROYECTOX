import random
caracteres=['0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_']
lista = ["Antonio","Germán","Marcelo",40,28,25]
for n in range(0,100):
string_aleatorio = 'Trabajo grupal 2'
largo = random.randint(1, 20)
for i in range(0, largo):
string_aleatorio += random.choice(caracteres)
lista.append(string_aleatorio)
print(lista)