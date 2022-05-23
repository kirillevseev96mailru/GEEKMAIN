import random

def dwarves_fun(array):
    l = len(array)
    index = 1
    i = 0
    while i < l-1:
        if array[i] <= array[i+1]:
            i, index = index, index + 1
        else:
            array[i], array[i+1] = array[i+1], array[i]
            i = i -1
            if i < 0:
                i, index = index, index + 1

MIN_ITEM = -1000
MAX_ITEM = 1000

m = int(input('Ввведите значение M: '))
len_array = m * 2 + 1
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(len_array)]
print(array)
dwarves_fun(array)
print(array)
print(f'Медиана = {array[m]}')