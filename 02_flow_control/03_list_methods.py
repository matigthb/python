from os import system
if system("clear") != 0: system("cls")

lista1 = ['a','b','c','d','e']

lista1.append('f')
print(lista1)

lista1.insert(1,'@')
print(lista1)

lista1.extend(['g','h'])
print(lista1)

lista1.remove('@')
print(lista1)

lista1.pop() #elimina el ultimo y lo devuelve

lista1.pop(2)

#eliminarlo de una
del lista1[-1]

lista1.clear() #elimina todos los elementos


print("ORDENAMIENTO")

numbers = [3,10,2,8,99,101]

#ordenar la original directamente
numbers.sort()
print(numbers)

#ordenar haciendo una copia
sorted_numbers = sorted(numbers)
print(sorted_numbers)

#ordenar texto con key
frutas = ["manzana", "pera", "limón", "Manzana", "Pera", "Limón"]

frutas.sort(key=str.lower)
print(frutas)

#mas metodos
print(len(frutas)) #tamaño de la lista

print(frutas.count("manzana")) #veces que se repite el objeto en la lista
print("manzana" in frutas) #devuelve bool dependiendo de si el obj esta en la lista o no


# Ejercicio 1: Añadir y modificar elementos
# Crea una lista con los números del 1 al 5.
# Añade el número 6 al final usando append().
# Inserta el número 10 en la posición 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.

listaej1 = [1,2,3,4,5]

listaej1.append(6)

listaej1.insert(1, 10)

listaej1[0] = 0

print("EJ 1")
print(listaej1)

# Ejercicio 2: Combinar y limpiar listas
# Crea dos listas:
lista_a = [1, 2, 3]
lista_b = [4, 5, 6, 1, 2]

# Extiende lista_a con lista_b usando extend().
# Elimina la primera aparición del número 1 en lista_a usando remove().
# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
# Limpia completamente lista_b usando clear().

lista_a.extend(lista_b)
lista_a.remove(1)
print(lista_a.pop(3))
lista_b.clear()

print(lista_a)

# Ejercicio 3: Slicing y eliminación con del
# Crea una lista con los números del 1 al 10.
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
# Imprime la lista resultante.

lista_ej3 = [1,2,3,4,5,6,7,8,9,10]

del lista_ej3[2:5]

print(lista_ej3)

# Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de forma ascendente usando sort().
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
# Comprueba si el número 7 está en la lista usando in.

lista_ej4 = [5, 2, 8, 1, 9, 4, 2]

lista_ej4.sort()

print(lista_ej4.count(2))
print(7 in lista_ej4)
print(lista_ej4)

# Ejercicio 5: Copia vs. Referencia
# Crea una lista llamada original con los números [1, 2, 3].
# Crea una copia de la lista original llamada copia_1 usando slicing.
# Crea otra copia llamada copia_2 usando copy().
# Crea una referencia a la lista original llamada referencia.
# Modifica el primer elemento de la lista referencia a 10.
# Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.

original = [1, 2, 3]

copia_1 = original[:]

copia_2 = original.copy()

referencia = original

referencia[0] = 10

print(original)
print(copia_1)
print(copia_2)
print(referencia)

# Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas.
# Crea una lista con las siguientes cadenas: ["Manzana", "pera", "BANANA", "naranja"].
# Ordena la lista sin diferenciar entre mayúsculas y minúsculas.
 
strings = ["Manzana", "pera", "BANANA", "naranja", "anana"]

strings.sort(key=str.lower)

print(strings)