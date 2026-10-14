# Adivina el nombre
import time

def RevolverNombres(archivo):
    import json
    import random

    with open(archivo, "r", encoding="utf-8") as jsonf:
        datos=json.load(jsonf)
    random.shuffle(datos)
    datos_seleccionados=datos[1:78]
    return datos_seleccionados

nombres_seleccionados = []
timer=0
print("""|-----Opciones-----|
|1. 25 segundos    |
|2. 30 segundos    |
|3. 45 segundos    |
|4. 1 minuto       |""")
tiempo_total=input("Cuanto tiempo quieres? (Selecciona una de las opciones): ")
if tiempo_total == "1":
    timer=25
elif tiempo_total == "2":
    timer=30
elif tiempo_total == "3":
    timer=45
elif tiempo_total == "4":
    timer=60
else:
    print("Opcion Desconocida. Intenta de nuevo.")

print("Adivina los Nombres!!")
while timer < 0:
    print(f"\rTiempo Restante: {timer}", end="", flush=True)
    timer - 1
    nombre=input(": ")