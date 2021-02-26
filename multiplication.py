#!/usr/bin/python

import random
import PyQt5

# Mnożenie do 500
def mulitiplication():
     while True:
          a = random.randint(2, 100)
          b = random.randint(2, 100)
          if a * b > 300:
               continue
          else:
               break
     return f'{a} * {b} = ?'


print('Rozwiąż zadanie')
print(mulitiplication())
input()

