# Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se conoce
# el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino F) 
# –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Romanoff, Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:

# a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
# b. mostrar los nombre de los superhéroes femeninos;
# c. mostrar los nombres de los personajes masculinos;
# d. determinar el nombre del superhéroe del personaje Scott Lang;
# e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan con la letra S;
# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroes.

import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

from common.Queue import Queue

class Character:
    def __init__(self, name: str, heroName: str, gender: str):
        self.name = name
        self.heroName = heroName
        self.gender = gender


charactersData = [
    Character("Tony Stark", "Iron Man", "M"),    
    Character("Steve Rogers", "Capitán América", "M"),    
    Character("Natasha Romanoff", "Black Widow", "F"),    
    Character("Carol Danvers", "Capitana Marvel", "F"),    
    Character("Scott Lang", "Ant-Man", "M"),    
    Character("Sam Wilson", "Falcon", "M"),    
]

characters = Queue()

for i in range(len(charactersData)):
    characters.arrive(charactersData[i])

aux_queue = Queue()

# =================================================================

# Variables para almacenar respuestas específicas
capitana_marvel_real_name = None
scott_lang_hero_name = None
carol_danvers_found = False
carol_danvers_hero = None

# Listas para acumular las consignas de tipo "mostrar listado"
female_heroes = []
male_characters = []
starts_with_S = []

for _ in range(characters.size()):
    current = characters.attention()
    
    # a. Determinar el nombre real de Capitana Marvel
    if current.heroName == "Capitana Marvel":
        capitana_marvel_real_name = current.name
        
    # b. Mostrar los nombres de los superhéroes femeninos
    if current.gender == "F":
        female_heroes.append(current.heroName)
        
    # c. Mostrar los nombres de los personajes masculinos
    if current.gender == "M":
        male_characters.append(current.name)
        
    # d. Determinar el nombre del superhéroe de Scott Lang
    if current.name == "Scott Lang":
        scott_lang_hero_name = current.heroName
        
    # e. Personajes o superhéroes cuyo nombre empieza con 'S'
    if current.name.startswith("S") or current.heroName.startswith("S"):
        starts_with_S.append(f"Personaje: {current.name} | Superhéroe: {current.heroName} ({current.gender})")
        
    # f. Determinar si Carol Danvers está e indicar su superhéroe
    if current.name == "Carol Danvers":
        carol_danvers_found = True
        carol_danvers_hero = current.heroName

    # Guardamos en la cola auxiliar para no perder el dato
    aux_queue.arrive(current)

# Reintegrar todo a la cola original para dejarla intacta
for _ in range(aux_queue.size()):
    characters.arrive(aux_queue.attention())

# =================================================================
print("=== RESULTADOS DEL MCU ===")

# a. Determinar el nombre del personaje de la superhéroe Capitana Marvel
print(f"\na. El nombre real de Capitana Marvel es: {capitana_marvel_real_name}")

# b. Mostrar los nombres de los superhéroes femeninos
print(f"\nb. Superhéroes femeninos: {', '.join(female_heroes)}")

# c. Mostrar los nombres de los personajes masculinos
print(f"\nc. Personajes masculinos: {', '.join(male_characters)}")

# d. Determinar el nombre del superhéroe del personaje Scott Lang
print(f"\nd. El superhéroe de Scott Lang es: {scott_lang_hero_name}")

# e. Mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan con la letra S
print("\ne. Personajes o superhéroes que empiezan con 'S':")
for data in starts_with_S:
    print(f"  - {data}")

# f. Determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroe
print(f"\nf. ¿Carol Danvers está en la cola?: {'Sí' if carol_danvers_found else 'No'}")
if carol_danvers_found:
    print(f"   Su nombre de superhéroe es: {carol_danvers_hero}")