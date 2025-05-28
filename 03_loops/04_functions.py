#def nombre_de_la_funcion(param, param2):
    #docstring

    #cuerpo de funcion

    #return (opcional)

def saludar():
    """saluda al usuario"""
    print("Hola")


saludar()


def multiplicar(a = 2,b = 2):
    return a * b

print(multiplicar())
print(multiplicar(2))
print(multiplicar(2,3))

def describir_persona(edad, nombre, sexo):
    print(f"edad {edad} nombre {nombre} sexo {sexo}")

describir_persona(nombre="matias", edad=25, sexo="gato")

# Argumentos de long de variable

def sumar_numeros(*args):
    suma = 0

    for nro in args:
        suma+= nro
    return suma

print(sumar_numeros(1,5,9,8,6,45,8,7,8,8,4,45,5,5,25,4,5,5,2,4))


#Argumentos clave valor
def mostrar_info(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="matias", edad=21, ciudad="Wilde")
mostrar_info(nombre="juan", edad=24, gatos=2, pais="Holanda")
mostrar_info(nombre="sofia", edad=19, computadora=True)
