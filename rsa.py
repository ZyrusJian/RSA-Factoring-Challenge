#!/usr/bin/python3
import argparse
import os
import time
import math
import random


def is_prime(n):
    """
    Check if a number n is prime.

    Args:
        n (int): The number to check.

    Returns:
        True if n is prime, False otherwise.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n))+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True


def generate_prime(bits):
    """
    Generate a prime number with the given number of bits.

    Args:
        bits (int): The number of bits for the prime number.

    Returns:
        A prime number with the given number of bits.
    """
    while True:
        n = random.getrandbits(bits)
        if is_prime(n):
            return n


def factorize(n):
    """
    Factorize a number n into a product of two prime numbers.

    Args:
        n (int): The number to factorize.

    Returns:
        A tuple of two prime numbers that are factors of n.
    """
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0 and is_prime(i) and is_prime(n // i):
            return (i, n // i)
    return None


def main():
    """
    Parse command-line arguments and factorize the number in the input file.
    """
    parser = argparse.ArgumentParser(
            description='Factorize a number into two prime numbers.')
    parser.add_argument('file', type=str, help='the input file')
    args = parser.parse_args()

    if not os.path.isfile(args.file):
        print(f'Error: {args.file} does not exist.')
        return

    with open(args.file, 'r') as f:
        n = int(f.readline().strip())

    p, q = factorize(n)
    if p is not None and q is not None:
        print(f'{n}={p}*{q}')
    else:
        print(f'Error: {n} cannot be factorized into two prime numbers.')


if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print(f'Time taken: {end_time - start_time:.3f} seconds.')
