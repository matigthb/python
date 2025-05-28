##print("Hola, cual es tu nombre?")
##nombre = input()

nombre = input("Hola, cual es tu nombre?\n")
print(f"Hola {nombre}, te estabamos esperando...")

age = input("Cuantos años tienes?\n")
print(f"En 25 años tendrás {int(age) + 25} años.")

print("Valores")
country, city = input("En que país y ciudad vives?\n").split()

print(f"Vives en {country}, {city}")