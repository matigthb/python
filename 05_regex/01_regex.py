"""
    Expresiones regulares son una secuencia de caracteres que forman un patron de busqueda, se utilizan para la busqueda de cadenas de texto, validacion etc

    ejemplos:
    -Busqueda avanzada en textos grandes
    -Validación de datos (asegurarte de que los datos que ingresa el usuario sean correctos.)
    -Manipulación del texto: Extraer, reemplazar y modificar partes de textos

"""
#importar modulo
import re

#crear patron de string que describe lo que buscamos
pattern = "Hola"

#texto donde vamos a buscar
text= "Holsda mundo"

#usar la funcion de busqueda de regex
result= re.search(pattern, text)

if result:
    print("Se encontró el resultado.")
else:
    print("No se encontró el resultado")

print(result.group()) #devuelve la cadena que coincida con el pattern

print(result.start()) #devuelve posición inicial de la coincidencia

print(result.end()) #devuelve la posición final de la coincidencia

#---------------------------------------------------------------

#Encontrar todas las coincidencias
# .findall() devuelve la lista con todas las coincidencias

text = "Python esta muy bueno, Python me gusta. Aunque Python no es tan dificil, ojo con Python."

pattern = "Python"

matches = re.findall(pattern,text)

print(matches)

# Operador . para significar cualquier caracter 

text = "Pyfhon esta muy bueno, Python me gusta. Aunque Pyjhon no es tan dificil, ojo con Pyrhon."

pattern = "Py.hon"

matches = re.findall(pattern,text)

print(matches)

#----------------------------------------------------------------------
# iter() iterador que contiene las propiedades de los resultados de la busqueda

text = "Pyfhon esta muy bueno, Python me gusta. Aunque Pyjhon no es tan dificil, ojo con Pyrhon."

pattern = "Py.hon"

matches = re.finditer(pattern,text)

for match in matches:
    print(match.group(), match.start(), match.end())


#----------------------------------------------------------------------
# re.IGNORECASE para ignorar el casing, y encontrar tanto mayuscula como minuscula

text = "pyfhon esta muy bueno, Python me gusta. Aunque Pyjhon no es tan dificil, ojo con Pyrhon."

pattern = "Py.hon"

matches = re.finditer(pattern,text, re.IGNORECASE)

for match in matches:
    print(match.group(), match.start(), match.end())


#-----------------------------------------------------------------------
# .sub() para reemplazar todas las coincidencias de un patron en el texto con algo distinto

text = "Hola mundo! Hola de nuevo! Hola!"
pattern = "Hola" 
replacement = "Chau"

new_txt = re.sub(pattern, replacement, text)
print(new_txt)