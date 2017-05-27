import random
import sys
import os

age = 21

if age >= 21 :
    print('You are old enough to drive a tractor')
elif age >=16 :
    print('You are old enough to drive a car')
else :
    print('You are not old enough to drive')

#WE can combine conditions with logical operators and, or, not
age2 = 30

if(( age2 >= 1) and ( age2 <=18)) :
    print('You get a birthday')
elif (age2==21) or (age2 >=65) :
    print('You get a birthday')
elif not(age2==30) :
    print("You don't get a birthday")
else :
    print('You get a birthday party!! Yeah!!')

