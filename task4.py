#!python3
# Advanced Dungeons and Dragons

"""
the file task04.txt contains a matrix of values
The row indicates the level of fighter. Row 1 is for a level 1 fighter, row 2 is for a level 2 fighter and so on

In each row, the numers indicate the target number needed out of 20 to land a hit on a specific Armor Class, starting with
10 on the left, followed by 9, then 8, all the way to -10 on the far right.

Create a function that reads the specific value for a specific level and an armor class, and prints the target number needed.

"""

def target(lvl,ac):
    file = open('task04.txt','r').read()
    
    matrix = [list(map(int, i.split())) for i in file.strip().split('\n')]
    return matrix[lvl-1][10-ac]


def tests():
    assert target(3,7) == 13
    assert target(9,-1) == 17
    assert target(13,-10) == 20

if __name__=="__main__":
    tests()