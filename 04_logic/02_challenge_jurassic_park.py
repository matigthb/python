"""
En Jurassic Park, se ha observado que los dinosaurios carnívoros, como el temible T-Rex, depositan un número par de huevos. Imagina que tienes una lista de números
enteros en la que cada número representa la cantidad de huevos puestos por un dinosaurio en el parque.

Importante: Solo se consideran los huevos de los dinosaurios carnívoros (T-Rex) aquellos números que son pares.

Objetivo:
Escribe una función en Python que reciba una lista de números enteros y devuelva la suma total de los huevos que pertenecen a los dinosaurios carnívoros 
(es decir, la suma de todos los números pares en la lista).

"""

def count_carnivore_dinosaur_eggs(eggs_list) -> int:
    """ Devuelve la suma de huevos de dinosaurios carnivoros que se encuentren en la lista recibida """
    eggs_total = 0

    for eggs in eggs_list:
        if eggs % 2 == 0:
            eggs_total += eggs
    
    return eggs_total


eggs_list = [1,4,5,7,8]

print(count_carnivore_dinosaur_eggs(eggs_list))