# Consigna: Desarrollar un algoritmo que permita calcular la acum 
# de los n terminos de la serie armonica

import sys
import argparse

def harmonic_series(n: int) -> float:
    # Por defecto, Python tiene un límite de recursión (generalmente 1000) 
    # para evitar que un bucle infinito consuma toda la memoria del sistema
    # y provoque un cierre inesperado (stack overflow). 
    # Voy a modificarlo para calcular un millón de terminos al menos

    MAX_SAFE_LIMIT = 1_000_100 # 1,000,000 de llamadas ≈ 1GB.

    # Ajusta el límite al valor de n, pero sin pasarnos del tope
    sys.setrecursionlimit(min(max(1000, n + 500), MAX_SAFE_LIMIT))

    def __harmonic_series(n, acum = 0.0):
        if n == 0:
            return acum
        
        return __harmonic_series(n - 1, acum + (1 / n))
    
    return __harmonic_series(n)


def validate_positive(value):
    try:
        ivalue = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"'{value}' is not a valid integer")
        
    if ivalue < 0:
        raise argparse.ArgumentTypeError(f"{value} is not a positive integer")
    return ivalue

parser = argparse.ArgumentParser(description="Calculates the sum of the first N terms of the harmonic series.")

parser.add_argument(
    "N_terms", 
    type = validate_positive, 
    help = "Number of terms (positive integer) to calculate"
)

try:
    args = parser.parse_args()
    print(harmonic_series(args.N_terms))
    # print(sys.getrecursionlimit()) 
except RecursionError:
    print("Error: The number is too large for the current recursion limit.")
except Exception as e:
    print(f"Unexpected error: {e}")