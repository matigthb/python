import re 

# 01 Corchetes

# Envuelve un grupo de caracteres para coincidir

text="matias78+@gmail.com"
pattern = r"^[\w._%+-]+$"
matches = re.findall(pattern,text)
print(matches)

#buscar todas las vocales

text="matias78+@gmail.com"
pattern = r"[aeiou]"
matches = re.findall(pattern,text)
print(matches)

#una regex para encontrar la palabra man fan y ban pero ignroa al resto

text = "man fan ran san lan ban omniman"
pattern = r"\b[mfb]an\b"
matches = re.findall(pattern,text)
print(matches)

# 02 - "-"

# para declarar rangos

text="matias78+@gmail.com"
pattern = r"[0-9]|[A-Za-záéíóú]"
matches = re.findall(pattern,text)
print(matches)

# Ejercicio final con todo lo aprendido
# Mejorar esto: https://www.computerhope.com/jargon/r/regular-expression.png

## Buscar corner cases que no pasa y arreglarlo:
"lo.que+sea@shopping.online"
"michael@gov.co.uk"

text="michael@gov.co.uk"
# pattern = r"[\w._%+-]+@[\w.-]+\.[a-zA-Z]{2,4}"  ##### Pattern viejo
pattern_fix = r"[\w._%+-]+@[\w.-]+\.[a-zA-Z]{2,}"
matches = re.findall(pattern_fix,text)
print(matches)


# [^]: Coincide con cualquier caracter que no esté dentro de los corchetes
text = "Hola mundo"
pattern = r"[^aeiou]"
matches = re.findall(pattern, text)
print(matches)