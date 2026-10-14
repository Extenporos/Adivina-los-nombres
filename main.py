# Adivina el nombre
import math
import select
import sys
import time
import random

abecedario=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
letra_seleccionada=random.choice(abecedario)

def RevolverNombres(archivo:str):
    import json

    with open(archivo, "r", encoding="utf-8") as jsonf:
        datos=json.load(jsonf)
    
    nombres = datos["Masculino"] + datos["Femenino"]
    random.shuffle(nombres)
    datos_filtrados = [
        n for n in nombres
        if n.lower().startswith(letra_seleccionada.lower())
    ]
    datos_seleccionados=datos_filtrados[:78]
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
nombres=RevolverNombres("nombres.json")
nombres_acertados=[]

print("Adivina los Nombres!!")
print(f"Hay {len(nombres)} posibles nombres que empiezan con {letra_seleccionada}...")

if len(nombres) == 0:
    print(f"Uh Oh! Aparentemente no hay nombres con {letra_seleccionada}, intenta volver a correr el juego.")
fin_del_juego = time.monotonic() + timer
while timer > 0 and nombres:
    timer = max(0, math.ceil(fin_del_juego - time.monotonic()))
    if timer == 0:
        break
    print(f"\rTiempo Restante: {timer} | Nombre: ", end="", flush=True)
    entrada_disponible, _, _ = select.select([sys.stdin], [], [], min(1, timer))
    if not entrada_disponible:
        continue

    nombre = sys.stdin.readline().strip()
    if nombre in nombres:
        nombres_acertados.append(nombre)
        nombres.remove(nombre)
    elif nombre in nombres_acertados:
        print(f"{nombre} ya fue acertado.")
    print(f"\nAcertados: {nombres_acertados}.")

print()
if nombres:
    print("Perdiste, que mala suerte!")
    print(f"Acertados: {nombres_acertados}")
    print(f"Sin Acertar: {nombres}")
else:
    print("Ganaste!")
    print("Acertaste todos los nombres!")
    print(f"De los cuales son: {nombres_acertados}")
