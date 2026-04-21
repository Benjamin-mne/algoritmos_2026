# Desarrollar un algoritmo que permita convertir un número entero en sistema decimal a sistema binario.

import argparse
import sys

def decimal_to_binary(n: int) -> str:
    if n == 0:
        return "0"
    
    def __decimal_to_binary(n: int) -> str:
        if n == 0:
            return ""
        return __decimal_to_binary(n // 2) + str(n % 2)
    
    return __decimal_to_binary(n)

def validate_non_negative(value):
    try:
        ivalue = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"'{value}' is not a valid integer")
        
    if ivalue < 0:
        raise argparse.ArgumentTypeError(f"{value} must be a non-negative integer")
    return ivalue

parser = argparse.ArgumentParser(description="Convert a decimal integer to binary.")
parser.add_argument(
    "number", 
    type=validate_non_negative, 
    help="The decimal number to convert"
)

try:
    args = parser.parse_args()
    result = decimal_to_binary(args.number)
    print(result)
except RecursionError:
    print("Error: The number is too large for the recursion limit.")
except Exception as e:
    print(f"Unexpected error: {e}")
