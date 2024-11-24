"""
Read the data from one of the task02 text files.
The data from this file contains 3 data on each line.  Determine how many lines of this file contains Pythagorean triples.
Pythagorean triples are data where all of the sides are integers, and the 3 sides form a right triangle.
The triples contained are : { 2a : 6, 2b: 4, 2c: 11}
"""
def isPythagoras(a, b, c):
    a, b, c = sorted([a, b, c])
    return a**2 + b**2 == c**2

def triple(file_path):
    file = open(file_path, 'r')

    data = [int(line.strip()) for line in file.readlines() if line.strip().isdigit()] #prepare data
    
    count = 0
    for i in range(0, len(data) - 2, 3):
        a, b, c = data[i], data[i+1], data[i+2]
        if isPythagoras(a, b, c):
            count += 1

    return count
            
def main():
    output = {
        '2a': triple('task02a.txt'),
        '2b': triple('task02b.txt'),
        '2c': triple('task02c.txt')
    }

    print(output)

main()