import random
import sys

MIN_ITEM = 0
MAX_ITEM = 100

n = int(input('Ввведите значение N: '))
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(n)]

maxi = -100000
mini = 100000
for i in range(len(array)):
    if array[i] >= maxi:
        maxi = array[i]
    if array[i] <= mini:
        mini = array[i]

print(mini, maxi)

Memory_expended = sys.getsizeof(MIN_ITEM) + sys.getsizeof(MAX_ITEM) + sys.getsizeof(mini)
Memory_expended = sys.getsizeof(maxi) + sys.getsizeof(n) + sys.getsizeof(array) + sys.getsizeof(i)


print(f'Затраченная память равна: {Memory_expended}')


''' Решаем задачу по поиску МИН и МАКС в последовательности N разными способами и тестируем их на затраты памяти.
    Это первый способ, затраты памяти напрямую зависят от размера N, другие обьекты тратят одно и то же кол-во памяти вне зависимости от N
'''