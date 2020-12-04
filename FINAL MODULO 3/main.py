import time
import string
import random


class Inventario:
    def __init__(self):
        especie_flores = ["a", "b", "c", "d"]
        tamano_flores = ["L", "S"]
        for i in range(0,100):
            with open("bodega_flores.txt", "a") as archivo_salida:
                variable = random.choice(especie_flores)
                variable2 = random.choice(tamano_flores)
                variable3 = (variable + variable2)
                archivo_salida.write(variable3 + "\n")
                print(variable3)
                time.sleep(0.002)


class InventarioFlores(Inventario):
    pass
    def declarar_ramo(self, ramo):
        
        if len(ramo) < 8:
            print("formato no valido")
        else:
            pass
            with open("bodega_ramos.txt", "w") as archivo_salida1:
                archivo_salida1.write(ramo)


ramo =InventarioFlores()
bodega = Inventario()
pedido = input("Ingrese el ramo que fabricaremos:")
ramo.declarar_ramo(pedido)