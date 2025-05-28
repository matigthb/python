import re

# 01 - El punto

# Sirve como comodín para representar cualquier caracter (singular)

text = "casa cosa cisa causa cuesa"
pattern = "c.sa"########

found = re.findall(pattern,text)

if found:
    print(found)
else:
    print("No se encontro")

#---------------------------------------------------------------------
# 03 - "r" 

# Sirve para identificar una regex

text = "Hola mundo, H0la, H$la"
pattern = r"H.la"########

found = re.findall(pattern,text)

if found:
    print(found)
else:
    print("No se encontro")

#---------------------------------------------------------------------
# 04 - "\d" 

# Sirve para buscar digitos

text = "El numero de telefono es 123456789"
pattern = r"\d{9}" ########

found = re.findall(pattern,text)

if found:
    print(found)
else:
    print("No se encontro")


#PRÁCTICA
# Encontrar numero de telefono de argentina

text = "Mi numero de telefono es +5491123456789, agendame"
pattern = r"\+549\d{10}" ########

result = re.search(pattern,text)

if result:
    print(result.group())
else:
    print("No se encontro")

#---------------------------------------------------------------------

# 05 - \w

# Coincide con cualquier caracter alfanumerico (solo letras o numeros)

text = "el_rubius_69"
pattern = r"\w"

found = re.findall(pattern, text)

print(found)

#----------------------------------------------------------------------

# 06 \s coincide con cualquier espacio en blanco como tabulacion, espacio, salto de linea

text = "Hola mundo\nComo estas?\t"
pattern = r"\s"

matches = re.findall(pattern,text)
print(matches)

#----------------------------------------------------------------------

# 07 ^ Coincide con el principio de una cadena

text = "@444_matias"
pattern= r"^\w" #valida que el nombre de usuario empiece (^) con un caracter alfanumerico (\w)

valid = re.search(pattern, text)
if valid:
    print("Valido")
else:
    print("Invalido")

#PRACTICA
text = "+5491123456789"
pattern= r"^\+\d{2,3}" #valida que el telefono empiece (^) con un + y dos o tres numeros

valid = re.search(pattern, text)
if valid:
    print("Valido")
else:
    print("Invalido")

#----------------------------------------------------------------------

# 08 - $

# Para verificar el final de una cadena

text = "Hola mundo"
pattern = r"mundo$"

valid = re.search(pattern, text)
if valid: print("Valido")
else: print("no es valido")

# PRACTICA

text= "micorreo@gmail.com"
pattern = r"^[\w._%+-]+@gmail.com$"

valid = re.search(pattern, text)
if valid: print("Valido")
else: print("no es valido")

# EJERCICIO:
# Tenemos una lista de archivos, necesitamos saber los nombres de los ficheros con extension .txt
files = "file1.txt file2.pdf midu-of.webp secret.txt"

pattern = r"\w{1,9999}\.txt"

count = re.findall(pattern, files)

print(count)

# \b: Coincide con el principio o final de una palabra
text = "casa casada cosa cosas casado casa"
pattern = r"\bc.sa\b"

found = re.findall(pattern, text)
print(found)

# |: Coincidir con una opción u otra
fruits = "platano, piña, manzana, aguacate, palta, pera, aguacate, aguacate"
pattern = r"palta|aguacate|p..a|\b\w{7}\b"

matches = re.findall(pattern, fruits)
print(matches)