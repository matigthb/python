frutas = ["manzana","banana","pera"]

for fruta in frutas:
    print(fruta) 

cadena = "matias"
for caracter in cadena:
    print(cadena)

for index, fruta in enumerate(frutas):
    print(f"En el indice {index} está {fruta}")

for index, fruta in enumerate(frutas):
    if fruta == "manzana": continue

    print(fruta)

#comprension
frutas_mayus = [fruta.upper() for fruta in frutas]
print(frutas_mayus)

#comprensión con condición
pares = [num for num in [1,2,3,4,5,6,7,8,9,10] if num % 2 == 0]

print(pares)

palabras = ["casa", "arbol", "sol", "elefante", "luna"]

palabras_largas = [palabra for palabra in palabras if len(palabra) > 5]