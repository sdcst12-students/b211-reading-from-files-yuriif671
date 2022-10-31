#!python3
"""
Note that json data is a really useful way of storing your variables to a file, and then retrieving them at a later date
"""

import json
data = [
        {
          'name' : 'Benjamin',
          'breed': 'Cat',
          'color': 'Black'
        },
        {
          'name' : 'Casey',
          'breed': 'Cat',
          'color': 'Tabby'
        },
        {
          'name' : 'Chili',
          'breed': 'Dog',
          'color': 'Tricolor'
        }
      ]

def writeData():
    output = json.dumps(data)


def main():
    choice = None
    while choice != "X":
        while choice not in ["W","R","X"]:
            choice = input("Do you want to read or write data [w/r]")
            choice = choice.strip()
            choice = choice.upper()
        if choice == "W":
            writeData()
        elif choice == "R":
            readData()
    if

if __name__ == "__main__":
    main()
