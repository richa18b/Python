import random
import sys
import os

#Dictionaries are made up of values with a unique key for each value

'''
You cannot join dictionaries with + as you can in lists
'''

super_heroes = {'Shaktimaan': 'Mukesh Khanna',
                'Batman':'Ben Affleck',
                'Superman':'Brandon Routh',
                'Spiderman':'Tobey Maguire',
                'IronMan':'Robert Downey Jr.'
                  }

print(super_heroes['Shaktimaan'])

del(super_heroes['Batman'])
print(super_heroes)

super_heroes['Spiderman'] = 'Andrew Garfield'
print(super_heroes)

print(len(super_heroes))

print(super_heroes.get('IronMan'))

print(super_heroes.keys())
print(super_heroes.values())