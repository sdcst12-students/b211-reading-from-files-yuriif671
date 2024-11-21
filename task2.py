"""
Read the data from one of the task02 text files.
The data from this file contains 3 numbers on each line.  Determine how many lines of this file contains Pythagorean triples.
Pythagorean triples are numbers where all of the sides are integers, and the 3 sides form a right triangle.
The triples contained are : { 2a : 6, 2b: 4, 2c: 11}
"""
import itertools

def is_pythagorean_triple(a, b, c):
    # Sort the numbers so that c is always the largest
    a, b, c = sorted([a, b, c])
    return a**2 + b**2 == c**2

def check_batches_of_three(file_path):
    with open(file_path, 'r') as file:
        numbers = [int(line.strip()) for line in file.readlines() if line.strip().isdigit()]
    
    count = 0
    # Iterate through the numbers in batches of 3
    for i in range(0, len(numbers) - 2, 3):  # Iterate by stepping 3 numbers
        a, b, c = numbers[i], numbers[i+1], numbers[i+2]
        if is_pythagorean_triple(a, b, c):
            count += 1

    return count
            
def main():
    output = {
        '2a': check_batches_of_three('task02a.txt'),
        '2b': check_batches_of_three('task02b.txt'),
        '2c': check_batches_of_three('task02c.txt')
    }

    print(output)

main()