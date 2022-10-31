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

output = json.dumps(data)
