# Consigna: El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u
# otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos
# objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con
# ayuda de la fuerza” realizar las siguientes actividades:
#   a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
#   queden más objetos en la mochila
#   b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sacar para encontrarlo;
#   c. Utilizar un vector para representar la mochila


TARGET = "Sable de luz"

def usar_la_fuerza(mochila: list[str]) -> None:
    def __usar_la_fuerza(mochila: list[str], cont: int = -1) -> None:
        if (len(mochila) == 0):
            print("No se encontró un", TARGET)
            return

        current = mochila.pop()
        cont += 1

        if (current == TARGET):
            print(f"{TARGET}, encontrado. Se sacaron {cont} objetos para encontrarlo")
            return 
        
        else:
            return __usar_la_fuerza(mochila, cont)

    __usar_la_fuerza(mochila)


# Stub 
mochilaConSable = [TARGET, "", "", ""]
mochilaSinSable = ["", "", "", ""]

# Ejemplos
print("\nEjemplo 1:")
usar_la_fuerza(mochilaConSable)

print("\nEjemplo 2:")
usar_la_fuerza(mochilaSinSable)
