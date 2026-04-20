# Consigna: Desarrollar una función que permita convertir un número romano en un número decimal.

# Requerimientos: 
# Los símbolos se escriben y leen de izquierda a derecha, de mayor a menor valor.
# Cuando se coloca un símbolo de valor menor a la izquierda de otro, se resta.
# Se permiten como mucho tres repeticiones consecutivas del mismo símbolo.
# Un símbolo que aparece restando solo se puede repetir cuando su repetición esté colocada a más de un símbolo de distancia a su derecha.
# Solo se puede restar un símbolo de tipo 1 (I, X, C, M) sobre el inmediato mayor de tipo 1 o de tipo 5 (V, L, D).
# Los símbolos 5 y sus múltiplos (V, L, D) siempre suman y no pueden estar a la izquierda de uno de mayor valor.
# El símbolo I solo puede restar a V y a X.
# X solo puede restar a L y a C.
# El símbolo C solo puede restar a D y a M.

import sys
import argparse

class Converter:
    conversion_table = {
        "I": {"value": 1, "can_subtract": ["V", "X"], "max_repeats": 3},
        "V": {"value": 5, "can_subtract": [], "max_repeats": 1},
        "X": {"value": 10, "can_subtract": ["L", "C"], "max_repeats": 3},
        "L": {"value": 50, "can_subtract": [], "max_repeats": 1},
        "C": {"value": 100, "can_subtract": ["D", "M"], "max_repeats": 3},
        "D": {"value": 500, "can_subtract": [], "max_repeats": 1},
        "M": {"value": 1000, "can_subtract": [], "max_repeats": 3},
    }

    @staticmethod
    def is_valid_roman(roman: str) -> bool:
        table = Converter.conversion_table

        if not all(c in table for c in roman):
            return False

        repeat_count = 1

        for i in range(len(roman)):
            current = roman[i]

            # max repeats
            if i > 0 and roman[i] == roman[i - 1]:
                repeat_count += 1
                if repeat_count > table[current]["max_repeats"]:
                    return False
            else:
                repeat_count = 1

            # subtraction rules
            if i + 1 < len(roman):
                next_char = roman[i + 1]

                current_val = table[current]["value"]
                next_val = table[next_char]["value"]

                if current_val < next_val:
                    if next_char not in table[current]["can_subtract"]:
                        return False

                    if repeat_count > 1:
                        return False

        return True

    @staticmethod
    def roman_to_decimal(roman: str, index: int = 0) -> int:
        table = Converter.conversion_table

        if index >= len(roman):
            return 0

        current = table[roman[index]]["value"]

        if index + 1 >= len(roman):
            return current

        next_val = table[roman[index + 1]]["value"]

        if current < next_val:
            return (next_val - current) + Converter.roman_to_decimal(roman, index + 2)
        else:
            return current + Converter.roman_to_decimal(roman, index + 1)


parser = argparse.ArgumentParser(description="Roman Number")
parser.add_argument("roman_number", help="Write a roman number")

args = parser.parse_args()

roman = args.roman_number.upper()

if not Converter.is_valid_roman(roman):
    print("Error: wrong roman format")
    sys.exit(1)

print(Converter.roman_to_decimal(roman))