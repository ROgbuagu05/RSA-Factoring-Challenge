#!/usr/bin/env python3
"""Module - Factors natural numbers"""

from __future__ import division
import sys
import os

def func_factors(filename):
    """Read and find Factors of every line in file."""
    with open(filename, 'r') as f:
        for line in f:
            num = int(line)
            result = factors(num)
            print("{} = {} * {}".format(num, int(num / resul), resul))
        f.close()

def factors(x):
    """Returns the smallest factor of x."""
    for y in range(1, x + 1):
        if x % y == 0 and y != 1:
            return y

if __name__ == "__main__":
    """main"""
    if not os.path.exists(sys.argv[1]):
        raise FileNotFoundError(f"File '{sys.argv[1]}' does not exist")
    func_factors(sys.argv[1])
