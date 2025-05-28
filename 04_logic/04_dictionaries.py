#colecciones de pares clave valor

persona = {
    "nombre": "matias",
    "edad" : 21,
    "pais" : "argentina",
    "es_admin" : True,
    "socials": {
        "twitter": "matitwitter",
        "instagram": "matiinstagram"
    }
}



print(persona["nombre"])
print(persona["socials"]["twitter"])
print(persona["es_admin"])

persona["socials"]["twitter"] = "matitwitternuevo"

print(persona["socials"]["twitter"])

# del persona["pais"]
# o

pais = persona.pop("pais")

print(f"Vive en {pais}")
print(persona)


#sobreescribir un dict

a = { "name": "matias", "edad": 21}
b = { "name": "juan", "edad": 25}

a.update(b)
print(a)
print(b)

#comprobar si existe una propiedad
print("name" in a)

#todos las claves
print(persona.keys())

#todos los valores
print(persona.values())

#obtener todo
print(persona.items())

for key, value in persona:
    print(f"Clave: {key} Valor: {value}")