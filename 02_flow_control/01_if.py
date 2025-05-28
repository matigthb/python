
#edad = 1424

#if edad >= 18:
#    print("Mayor de edad")
#else:
#    print("No mayor de edad")

#nota = 7

#if nota >= 9:
#    print("Muy bien!")
#elif nota >= 7:
#    print("Bien")
#elif nota >= 5:
#    print("Aprobado")
#else:
#   print("Desaprobado")


#if edad >= 18 and nota > 7:
#    print("Sos mayor de edad y tenes mas de 7 de nota")
#else:
#    print("no sos mayor de edad o no te sacaste mas de 7") 


#condicion = True

#mensaje = "Condicion cumplida" if condicion else "Condicion no cumplida"

#print(mensaje)


###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

numero1 = input("Ingrese el primer numero: ")
numero2 = input("Ingrese el segundo numero: ")

if numero1 == numero2:
    print("Son iguales")
elif numero1 > numero2:
    print("El primer numero es mayor.")
else:
    print("El segundo numero es mayor")

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)