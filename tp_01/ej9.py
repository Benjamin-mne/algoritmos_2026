import argparse
import sys

def integer_log(n: int, b: int) -> int:
    if n <= 0:
        raise ValueError("The number n must be greater than 0.")
    if b <= 1:
        raise ValueError("The base b must be greater than 1.")

    def __integer_log(n: int, b: int) -> int:
        if n < b:
            return 0

        return 1 + __integer_log(n // b, b)
    
    return __integer_log(n, b)

def validate_positive_int(value):
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError(f"{value} must be a positive integer.")
    return ivalue

def validate_base(value):
    ivalue = int(value)
    if ivalue <= 1:
        raise argparse.ArgumentTypeError(f"Base {value} must be greater than 1.")
    return ivalue

parser = argparse.ArgumentParser(description="Calculate the integer logarithm of n base b.")
parser.add_argument("n", type=validate_positive_int, help="The number (n > 0)")
parser.add_argument("b", type=validate_base, help="The base (b > 1)")

try:
    args = parser.parse_args()
    result = integer_log(args.n, args.b)
    print(result)
except RecursionError:
    print("Error: The number is too large for the current recursion limit.")
except Exception as e:
    print(f"Error: {e}")
