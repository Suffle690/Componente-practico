import json
import os


class GestorJSON:

    def __init__(self, ruta):
        self.ruta = ruta

    def leer(self):
        if not os.path.exists(self.ruta):
            return []

        with open(self.ruta, "r", encoding="utf-8") as archivo:
            return json.load(archivo)

    def guardar(self, datos):
        with open(self.ruta, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)