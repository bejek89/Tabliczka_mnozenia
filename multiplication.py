#!/usr/bin/python

import random

# Mnożenie do 500
def mulitiplication():
     while True:
          a = random.randint(1, 100)
          b = random.randint(1, 100)
          if a * b > 500:
               continue
          else:
               return f'{a} * {b} = {a * b}'


