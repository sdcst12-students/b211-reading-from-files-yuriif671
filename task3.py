#!python
# Sum of Values

"""
The file task03.txt contains a lot of data.  Each cluster of data is the number of points for that particular group.  Each blank line indicates a separator before the next group.
Read the contents of task03.txt into your program and determine the points value of the cluster with largest sum.

For sample data task03.txt, the largest sum should be 68787
"""

def is_pythagorean_triple(a, b, c):
    # Sort the numbers so that c is always the largest
    a, b, c = sorted([a, b, c])
    return a**2 + b**2 == c**2

def find_pythagorean_triples(file_path):
    # Read the numbers from the file
    with open(file_path, 'r') as file:
        numbers = [int(line.strip()) for line in file.readlines() if line.strip().isdigit()]

    # Generate all combinations of 3 numbers
    for triplet in itertools.combinations(numbers, 3):
        a, b, c = triplet
        if is_pythagorean_triple(a, b, c):
            print(f"Pythagorean triple found: {a}, {b}, {c}")

# Usage example
file_path = 'your_file.txt'  # Replace with your file path
find_pythagorean_triples(file_path)