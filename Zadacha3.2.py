#Zadacha №2
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
array2 = []

for i in range(len(array1)):
    if array1[i] % 2 == 0:
        array2.append(i)

print(array1)
print(array2)