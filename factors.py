#!/usr/bin/python3
import argparse
import os
import time
import math


def factorize(n):
    """
    Factorize a number n into a product of two smaller numbers.

    Args:
        n (int): The number to factorize.

    Returns:
        A tuple of two integers that are factors of n.
    """
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return (i, n // i)
    return None


def main():
    """
    Parse command-line arguments and factorize the numbers in the input file.
    """
    parser = argparse.ArgumentParser(
            description='Factorize numbers in a file.')
    parser.add_argument('file', type=str, help='the input file')
    args = parser.parse_args()

    if not os.path.isfile(args.file):
        print(f'Error: {args.file} does not exist.')
        return

    with open(args.file, 'r') as f:
        numbers = [int(line.strip()) for line in f.readlines()]

    for n in numbers:
        factors = factorize(n)
        if factors is not None:
            print(f'{n}={factors[0]}*{factors[1]}')


if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print(f'Time taken: {end_time - start_time:.3f} seconds.')
