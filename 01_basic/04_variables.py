#no hace falta aclarar el tipo

nombre = "Matias"

print(nombre)


age = 20
print(age)

age = 99
print(age)

tipo_de_sangre = 0
print(type(tipo_de_sangre))

tipo_de_sangre = "AB+"
print(type(tipo_de_sangre))


print(f"Hola mi nombre es {nombre}, tengo {int(age)-80} años")

name, age, city = "name", 20, "Buenos Aires" #NO RECOMENDADA FORMA DE DECLARAR VARIABLES

#convencion de nombres de variables = snake_case
nombre_variable_1 = "Bien"

MI_CONSTANTE = 3.14 #NO HAY CONSTANTES EN PYTHON, SE PUEDEN HACER SIMULADAS PERO NO EXISTE, AL USAR MAYUSCULAS SE SOBREENTIENDE QUE NO DEBERIAS CAMBIARLO PQ ES CONSTANTE(?)


is_user_logged_in : bool = True
print(is_user_logged_in)

is_user_logged_in = 42
print(is_user_logged_in)