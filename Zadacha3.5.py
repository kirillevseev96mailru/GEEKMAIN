#Zadacha №5

import random

SIZE = 10
MIN_ITEM = -1000
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

indexmaxi = 0
maxi = -1000000000000

for i in range(len(array)):
    if (array[i] >= maxi) and (array[i] < 0):
        maxi = array[i]
        indexmaxi = i

print(array)
print(f'Максимальный отрицательный элемент = {maxi}, a его индекс = {indexmaxi}')
