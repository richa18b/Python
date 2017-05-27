import random
import sys
import os

#We cannot change a tuple after it is created -- Major difference from lists

pi_tuple = (3,1,4,1,5,9)

print(pi_tuple)
print("length = ",len(pi_tuple))

new_list = list(pi_tuple)

print(new_list)
new_list.append(2)
print(new_list)

new_tuple = tuple(new_list)
print(new_tuple)
print("min = ",min(new_tuple))
print("max = ",max(new_tuple))
