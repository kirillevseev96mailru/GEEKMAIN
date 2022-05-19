import random
import sys

MIN_ITEM = 0
MAX_ITEM = 100

n = int(input('Ввведите значение N: '))
maxi = -100000
mini = 100000

for i in range(n):
    x = random.randint(MIN_ITEM, MAX_ITEM)
    if x >= maxi:
        maxi = x
    if x <= mini:
        mini = x
print(mini, maxi)

Memory_expended = sys.getsizeof(MIN_ITEM) + sys.getsizeof(MAX_ITEM) + sys.getsizeof(mini)
Memory_expended = sys.getsizeof(maxi) + sys.getsizeof(n) + sys.getsizeof(x) + sys.getsizeof(i)


print(f'Затраченная память равна: {Memory_expended}')

''' Решаем задачу по поиску МИН и МАКС в последовательности N разными способами и тестируем их на затраты памяти.
    Это второй способ, затраты памяти не зависят от N, код тратит одно и то же кол-во памяти
'''