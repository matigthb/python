# Quantifiers

# Se utilizan para especificar cuantas ocurrencias de un caracter o grupo de caracteres se deben encontrar en una cadena 

import re

# 01 - *

# 0 o mas veces

text = "aaannna"

pattern = "a*"

matches = re.findall(pattern, text)
print(matches)

# PRACTICA

# Cuantas palabras tienen de 0 a mas "a" y despues una "b"

text = "abrazo amar babero aaaabuela aaaab     "

pattern = r"[a]*b\b"

found = re.findall(pattern, text)
print(found)   


# 02 - +

# Una o mas veces de ocurrencia

text = "dddd aaa ccc bb"
pattern = r"a+"
matches = re.findall(pattern, text)
print(matches)

# 03 - ? 

# Cero o una vez

text = "aaabacb"
pattern = r"a?b"
matches = re.findall(pattern, text)
print(matches)

# EJEMPLO

phone = "+54 1123456789"
pattern = r"[\+|0]?54 \d{10}"

# 04 - {n} Exactamente n veces

text = "aaaaaa aa aaa"
pattern = r"a{3}"
matches = re.findall(pattern,text)
print(matches)

# {n, m} De n a m veces

text = "aaaaaa aa aaa"
pattern = r"a{3,2}"
matches = re.findall(pattern,text)
print(matches)

#PRACTICA

#Encontrar las palabras de 4 a 6 letras en el texto

text = "ala casa árbol león cinco murcielago diccionario cuadro manta"
pattern = r"\b\w{4,6}\b"
matches = re.findall(pattern,text)
print(matches)

#Encontrar las palabras de mas de 6 letras en el texto

text = "ala casa árbol león cinco murcielago diccionario cuadro manta"
pattern = r"\b\w{6,}\b"
matches = re.findall(pattern,text)
print(matches)