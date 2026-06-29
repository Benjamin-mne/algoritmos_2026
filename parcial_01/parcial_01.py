import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

from common.List import List
from common.Queue import Queue
from super_heroes_data import superheroes

# Datos & Estructuras

class MarvelCharacter:
    def __init__(self, name, alias, real_name, short_bio, first_appearance, is_villain):
        self.name = name
        self.alias = alias
        self.real_name = real_name
        self.bio = short_bio
        self.first_appearance = first_appearance
        self.is_villain = is_villain

    def __str__(self):
        real = self.real_name if self.real_name else "N/A"
        return f"{self.name} ({real}) - {self.first_appearance}"

characters = List()

# Criterios List

def by_name(character):
    return character.name

def by_real_name(character):
    return character.real_name if character.real_name else ""

def by_first_appearance(character):
    return character.first_appearance


characters.add_criterion("name", by_name)
characters.add_criterion("real_name", by_real_name)
characters.add_criterion("first_appearance", by_first_appearance)

for hero in superheroes:
    characters.append(MarvelCharacter(**hero))


# Ejercicio 1 
print("\n[EJERCICIO 1]\n")

heroes_list = [
    "Iron Man", "Capitan America", "Thor", "Hulk",
    "Black Widow", "Hawkeye", "Spiderman", "Black Panther",
    "Doctor Strange", "Scarlet Witch", "Vision", "Ant Man",
    "Captain Marvel", "Falcon", "Winter Soldier"
]

# Funcion recursiva  para buscar, determinar si Capitan America esta en la lista.
def find_capitan_america(heroes, index=0):
    if index >= len(heroes):
        return False
    if heroes[index] == "Capitan America":
        return True
    return find_capitan_america(heroes, index + 1)

print("\nCapitan America está en la lista: ")
resultado = find_capitan_america(heroes_list)
print(f"  {'Sí' if resultado else 'No'}, Capitan America {'está' if resultado else 'no está'} en la lista.")


# Funcion recursiva para listar los superheroes de la lista.
def listar_heroes(heroes, index=0):
    if index >= len(heroes):
        return
    print(f"  {index + 1}. {heroes[index]}")
    listar_heroes(heroes, index + 1)


print("\nListado de superhéroes: ")
listar_heroes(heroes_list)

# Ejercicio 2
print("\n[EJERCICIO 2]\n")

# Listado ordenado de manera ascendente por nombre de los personajes
print("\nPersonajes ordenados por nombre: ")
characters.sort_by_criterion(key_criterion="name")
characters.show()

# Determinar en que posicion esta The Thing y Rocket Raccoon
print("\nPosición de The Thing y Rocket Raccoon: ")
pos_thing = characters.search("The Thing", "name")
pos_rocket = characters.search("Rocket Raccoon", "name")
print(f"  The Thing se encuentra en la posición: {pos_thing}")
print(f"  Rocket Raccoon se encuentra en la posición: {pos_rocket}")

# Listar todos los villanos de la lista
print("\nVillanos de la lista: ")
for character in characters:
    if character.is_villain:
        print(f"  {character.name}")

# Poner todos los villanos en una cola para determinar luego cuales aparecieron antes de 1980
print("\nVillanos que aparecieron antes de 1980: ")
villains_queue = Queue()
for character in characters:
    if character.is_villain:
        villains_queue.arrive(character)

for _ in range(villains_queue.size()):
    current = villains_queue.move_to_end()
    if current.first_appearance < 1980:
        print(f"  {current.name} ({current.first_appearance})")

# Listar los superheores que comienzan con  Bl, G, My, y W
print("\nSuperhéroes que comienzan con Bl, G, My, W: ")
for character in characters:
    if not character.is_villain and character.name.startswith(("Bl", "G", "My", "W")):
        print(f"  {character.name}")

# Listado de personajes ordenado por nombre real de manera ascendente de los personajes
print("\nPersonajes ordenados por nombre real: ")
characters.sort_by_criterion(key_criterion="real_name")
characters.show()

# Listado de superheroes ordenados por fecha de aparación
print("\nPersonajes ordenados por fecha de aparición: ")
characters.sort_by_criterion(key_criterion="first_appearance")
characters.show()

# Modificar el nombre real de Ant Man a Scott Lang.
print("\nModificar nombre real de Ant Man: ")
ant_man_index = characters.search("Ant Man", "name")
if ant_man_index is not None:
    old_name = characters[ant_man_index].real_name
    characters[ant_man_index].real_name = "Scott Lang"
    print(f"  Ant Man: nombre real modificado de '{old_name}' a 'Scott Lang'")
else:
    print("  Ant Man no encontrado en la lista.")

# Mostrar los personajes que en su biografia incluyan la palabra time-traveling o suit
print('\nPersonajes con "time-traveling" o "suit" en su biografía: ')
characters.filter_contain_on_bio(["time-traveling", "suit"])

# Eliminar a Electro y Baron Zemo de la lista y mostrar su información si estaba en la lista
print("\nEliminar a Electro y Baron Zemo: ")
deleted_electro = characters.delete_value("Electro", "name")
deleted_zemo = characters.delete_value("Baron Zemo", "name")

if deleted_electro:
    print(f"  Eliminado: {deleted_electro.name} ({deleted_electro.real_name})")
else:
    print("  Electro no encontrado en la lista.")

if deleted_zemo:
    print(f"  Eliminado: {deleted_zemo.name} ({deleted_zemo.real_name})")
else:
    print("  Baron Zemo no encontrado en la lista.")
