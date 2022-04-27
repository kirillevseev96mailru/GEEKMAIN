#Zadacha №7

import random

SIZE = 10
MIN_ITEM = -1000
MAX_ITEM = 1000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

min = 1000000000
previous_min = 1000000000

for i in range(len(array)):
    if (array[i] <= min):
        previous_min = min
        min = array[i]
    elif (array[i] <= previous_min):
        previous_min = array[i]
print(array)
print(f'Минимальное значение: {min}, Предминимальное значение: {previous_min}')