import random

def fun_Bubble(array):

    k = 1
    while k < len(array):
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]

        k += 1

    return (array)

MIN_ITEM = -100
MAX_ITEM = 99

n = int(input('Ввведите значение N: '))
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(n)]

print(array)
print(fun_Bubble(array))