#Zadacha №6

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 10000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

mini = 1000000000
maxi = 0
indexmini = 0
indexmaxi = 0
sum = 0
for i in range(len(array)):
    if array[i] >= maxi:
        maxi = array[i]
        indexmaxi = i
    if array[i] <= mini:
        mini = array[i]
        indexmini = i

for i in range(indexmini+1,indexmaxi):
    sum += array[i]

print(f'Сумма чисел между МАКС({maxi}) и МИН({mini}) = {sum}')
