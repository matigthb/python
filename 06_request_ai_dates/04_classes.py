#Clases

class Auto:
    tipo = "vehículo de cuatro ruedas"

    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def arrancar(self):
        print(f"El auto {self.marca} {self.modelo} arrancó.")

mi_auto = Auto("Toyota", "Corolla", "rojo")
mi_auto.arrancar()

otro_auto = Auto("Ford", "Fiesta", "azul")
otro_auto.arrancar()

import requests

OPENAI_KEY = "XXXXXXXXXXXXXXXXXX"

class API:
    def __init__(self, api_key, url, model):
        self.api_key = api_key
        self.url = url
        self.model = model

    def call(self, prompt):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        data = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}]
        }

        response = requests.post(self.url, json=data, headers=headers)
        res_json = response.json()
        print(res_json["choices"][0]["message"]["content"])
    
openai_api = API(OPENAI_KEY, "https://api.openai.com/v1/chat/completions", "gpt-4o-mini")

openai_api.call("Escribe un poema sobre la programación")