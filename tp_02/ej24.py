# Dada una pila de personajes de Marvel Cinematic Universe (MCU), 
# de los cuales se dispone de su nombre y la cantidad de películas
# de la saga en la que participó, implementar las funciones
# necesarias para resolver las siguientes actividades:
# (A) determinar en qué posición se encuentran Rocket Raccoon y Groot, 
# tomando como posición uno la cima de la pila;
# (B) determinar los personajes que participaron en más de 5 películas de la saga,
# además indicar la cantidad de películas en la que aparece;
# (C) determinar en cuantas películas participo la Viuda Negra (Black Widow);
# (D) mostrar todos los personajes cuyos nombre empiezan con C, D y G.

import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

from common.Stack import Stack

class PersonajeMCU:
    def __init__(self, nombre, cantidad_peliculas):
        self.nombre = nombre
        self.cantidad_peliculas = cantidad_peliculas

personajes = Stack()
personajes.push(PersonajeMCU("Iron Man", 10))
personajes.push(PersonajeMCU("Captain America", 9))
personajes.push(PersonajeMCU("Rocket Raccoon", 6))
personajes.push(PersonajeMCU("Groot", 6))
personajes.push(PersonajeMCU("Black Widow", 7))


# (A) Determinar en qué posición se encuentran Rocket Raccoon y Groot
def encontrar_posicion(pila, nombre):
    """
    Retorna la posición del personaje en la pila (1 = cima).
    Si no existe, retorna -1.
    """
    stack_aux = Stack()
    posicion = 0
    encontrado = -1
    
    # Desapilar y contar hasta encontrar el personaje
    while pila.size() > 0:
        personaje = pila.pop()
        posicion += 1
        stack_aux.push(personaje)
        
        if personaje.nombre == nombre and encontrado == -1:
            encontrado = posicion
    
    # Restaurar la pila original
    while stack_aux.size() > 0:
        pila.push(stack_aux.pop())
    
    return encontrado

print("=== (A) Posiciones de Rocket Raccoon y Groot ===")
pos_rocket = encontrar_posicion(personajes, "Rocket Raccoon")
pos_groot = encontrar_posicion(personajes, "Groot")
print(f"Rocket Raccoon se encuentra en la posición: {pos_rocket}")
print(f"Groot se encuentra en la posición: {pos_groot}")
print()


# (B) Personajes con más de 5 películas
def personajes_mas_de_5_peliculas(pila):
    """
    Retorna una lista con los personajes que participaron en más de 5 películas.
    """
    stack_aux = Stack()
    resultado = []
    
    # Desapilar y evaluar cada personaje
    while pila.size() > 0:
        personaje = pila.pop()
        stack_aux.push(personaje)
        
        if personaje.cantidad_peliculas > 5:
            resultado.append(personaje)
    
    # Restaurar la pila original
    while stack_aux.size() > 0:
        pila.push(stack_aux.pop())
    
    return resultado

print("=== (B) Personajes con más de 5 películas ===")
personajes_top = personajes_mas_de_5_peliculas(personajes)
for personaje in personajes_top:
    print(f"{personaje.nombre}: {personaje.cantidad_peliculas} películas")
print()


# (C) Películas en las que participó la Viuda Negra
def contar_peliculas_personaje(pila, nombre):
    """
    Retorna la cantidad de películas en las que participó el personaje.
    Si no existe, retorna 0.
    """
    stack_aux = Stack()
    cantidad = 0
    
    # Desapilar y buscar el personaje
    while pila.size() > 0:
        personaje = pila.pop()
        stack_aux.push(personaje)
        
        if personaje.nombre == nombre:
            cantidad = personaje.cantidad_peliculas
    
    # Restaurar la pila original
    while stack_aux.size() > 0:
        pila.push(stack_aux.pop())
    
    return cantidad

print("=== (C) Películas de Black Widow ===")
peliculas_black_widow = contar_peliculas_personaje(personajes, "Black Widow")
print(f"Black Widow participó en {peliculas_black_widow} películas")
print()


# (D) Personajes cuyos nombres empiezan con C, D y G
def personajes_por_inicial(pila, iniciales):
    """
    Retorna una lista con personajes cuyos nombres empiezan con las iniciales especificadas.
    """
    stack_aux = Stack()
    resultado = []
    
    # Desapilar y filtrar por inicial
    while pila.size() > 0:
        personaje = pila.pop()
        stack_aux.push(personaje)
        
        if personaje.nombre[0] in iniciales:
            resultado.append(personaje)
    
    # Restaurar la pila original
    while stack_aux.size() > 0:
        pila.push(stack_aux.pop())
    
    return resultado

print("=== (D) Personajes con nombres que empiezan con C, D y G ===")
personajes_cdg = personajes_por_inicial(personajes, ['C', 'D', 'G'])
if personajes_cdg:
    for personaje in personajes_cdg:
        print(f"- {personaje.nombre}")
else:
    print("No hay personajes con nombres que empiezan con C, D o G")