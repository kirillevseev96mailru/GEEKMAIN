#Zadacha №3

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

mini = 1000000000
maxi = 0
indexmini = 0
indexmaxi = 0

for i in range(len(array)):
    if array[i] >= maxi:
        maxi = array[i]
        indexmaxi = i
    if array[i] <= mini:
        mini = array[i]
        indexmini = i

print(array)

array[indexmini] = maxi
array[indexmaxi] = mini

print(array)