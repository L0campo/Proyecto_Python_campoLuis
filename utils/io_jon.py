
import os
import json

os.system('cls' if os.name == 'nt' else 'clear')

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pasuar():
    input("precione Enter para continuar...")


def leer_json(ruta):
        if not os.path.exists(ruta):
            return {}
        with open(ruta, "r", encoding="utf-8") as f:
            return json.load(f)


def escribir_json(ruta):
        if not os.path.exists(ruta):
            return {}
        with open(ruta, "r", encoding="utf-8") as f:
            return json.load(f)
