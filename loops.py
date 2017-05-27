import random
import sys
import os

'''
for loop
'''

for x in range(0, 10) :
    print(x,' ',end='')

print('\n')

grocery_list = ['Tomatoes','Potatoes','Guava']

for x in grocery_list :
    print(x,' ',end=" ")

print('\n')

for x in [2,4,6,8,10] :
    print(x)

print('\n')

num_list = [[1,2,3],[10,20,30],[100,200,300]]

for x in range(0,3) :
    for y in range(0,3) :
        print(num_list[x][y],' ',end=' ')
    print('\n')

'''
while loop
'''

random_num = random.randrange(0,100)

while random_num != 15 :
    print(random_num)
    random_num = random.randrange(0,100)

print('\n')

i = 0

while(i < 10) :
    print("i = ",i)
    i += 1
