import random
import sys

MIN_ITEM = 0
MAX_ITEM = 100

n = int(input('Ввведите значение N: '))

array1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(n)]

mini = min(array1)
maxi = max(array1)
print(mini, maxi)

Memory_expended = sys.getsizeof(MIN_ITEM) + sys.getsizeof(MAX_ITEM) + sys.getsizeof(mini)
Memory_expended = sys.getsizeof(maxi) + sys.getsizeof(n) + sys.getsizeof(array1)


print(f'Затраченная память равна: {Memory_expended}')

''' 
    Версия OC: 21H2
    Версия PyCharm 2021.3.3
    
    Решаем задачу по поиску МИН и МАКС в последовательности N разными способами и тестируем их на затраты памяти.
    Это третий способ, затраты памяти напрямую зависят от размера N , другие обьекты тратят одно и то же кол-во памяти вне зависимости от N
    
    1 и 3 решение затрачивают почти одинаковое кол-во памяти(8900+- при N = 1000) и зависят от N, но они решают 
    поставленную задачу гораздо быстрее нежели 2.
    2 тратит одно и то же кол-во памяти(112 при N = 1000) вне зависимости от N.
    Делаем вывод, что 2 намного выгоднее, если нас интересуют минимальные затраты по памяти.
    
    
'''