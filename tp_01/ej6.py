# Consigna: Dada una secuencia de caracteres, obtener dicha secuencia invertida


# [DISCLAIMER]: Soy consciente de que esta no es la manera más eficiente de invertir una cadena en Python. 
# Sin embargo, como estoy explorando las capacidades del lenguaje, quiero experimentar con lo que ofrece. 
# Se utiliza el bloqueo de hilos (threading.Lock) para evitar errores de concurrencia, dado que la lógica 
# se apoya en el uso de atributos estáticos compartidos.
# Si tuviera hilos, el GIL podría pausar un hilo a mitad de la recursión 
# y darle paso a otro, lo que rompería las variables estáticas si no usara el Lock
# En este caso el Lock es totalmente redundante.

import sys
import argparse
import threading

class Reverser:
    __idx = 0
    __reverseWord = ""
    __entry = True
    __lock = threading.Lock()

    @staticmethod
    def reverse(word):
        with Reverser.__lock:
            return Reverser.__reverse(word)

    @staticmethod
    def __reverse(word):

        if Reverser.__entry: 
            Reverser.__entry = False
            Reverser.__idx = len(word) - 1
            Reverser.__reverseWord = ""
        
        if Reverser.__idx == -1:
            Reverser.__entry = True
            return Reverser.__reverseWord

        Reverser.__reverseWord += word[Reverser.__idx]
        Reverser.__idx -= 1

        return Reverser.__reverse(word)


parser = argparse.ArgumentParser(description="Word")
parser.add_argument("word", help="Write a word")

args = parser.parse_args()

word = args.word

print(Reverser.reverse(word))