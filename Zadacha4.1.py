import timeit
import cProfile

''' Задача: найдите среди множества чисел минимальное и максимальное'''


def search_mini_and_maxi_01(n):
    array = [i for i in range(n)]
    array.sort()
    return (array[0], (array[len(array) - 1]) )


def search_mini_and_maxi_02(n):
    array = [i for i in range(n)]
    maxi = -100000
    mini = 100000
    for i in range(len(array)):
        if array[i] >= maxi:
            maxi = array[i]
        if array[i] <= mini:
            mini = array[i]
    return (mini, maxi)

def search_mini_and_maxi_03(n):
    maxi = -100000
    mini = 100000
    for i in range(1, n+1):
        if i >= maxi:
            maxi = i
        if i <= mini:
            mini = i
    return (mini, maxi)


n = 10
MIN_ITEM = -100000
MAX_ITEM = 100000



print(timeit.timeit('search_mini_and_maxi_01(10)', number=1000, globals=globals())) # 0.0006070000000000034
print(timeit.timeit('search_mini_and_maxi_01(100)', number=1000, globals=globals())) # 0.002333799999999997
print(timeit.timeit('search_mini_and_maxi_01(1000)', number=1000, globals=globals())) # 0.020984299999999997
print(timeit.timeit('search_mini_and_maxi_01(10000)', number=1000, globals=globals())) # 0.19668370000000002
print(timeit.timeit('search_mini_and_maxi_01(100000)', number=1000, globals=globals())) # 3.169056

''' Решая поставленную задачу с помошью функции 1 , мы наблюдаем линейную зависимость, 
    время увеличивается во столько раз, во сколько "N" '''


print(timeit.timeit('search_mini_and_maxi_02(10)', number=1000, globals=globals())) # 0.0011885000000000367
print(timeit.timeit('search_mini_and_maxi_02(100)', number=1000, globals=globals())) # 0.006833199999999984
print(timeit.timeit('search_mini_and_maxi_02(1000)', number=1000, globals=globals())) # 0.07299239999999996
print(timeit.timeit('search_mini_and_maxi_02(10000)', number=1000, globals=globals())) # 0.7441317000000001
print(timeit.timeit('search_mini_and_maxi_02(100000)', number=1000, globals=globals())) # 8.1144491


''' Решая поставленную задачу с помошью функции 2 , мы наблюдаем линейную зависимость, 
    время увеличивается во столько раз, во сколько "N" '''


print(timeit.timeit('search_mini_and_maxi_03(10)', number=1000, globals=globals())) # 0.0006063999999987857
print(timeit.timeit('search_mini_and_maxi_03(100)', number=1000, globals=globals())) # 0.002984899999999513
print(timeit.timeit('search_mini_and_maxi_03(1000)', number=1000, globals=globals())) # 0.03306839999999944
print(timeit.timeit('search_mini_and_maxi_03(10000)', number=1000, globals=globals())) # 0.3383372999999992
print(timeit.timeit('search_mini_and_maxi_03(100000)', number=1000, globals=globals())) # 3.2200941000000007


''' Решая поставленную задачу с помошью функции 3 , мы наблюдаем линейную зависимость, 
    время увеличивается во столько раз, во сколько "N" '''


print(cProfile.run('search_mini_and_maxi_01(10000000)'))

''' 
    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.073    0.073    0.433    0.433 <string>:1(<module>)
        1    0.000    0.000    0.360    0.360 Zadacha4.1.py:8(search_mini_and_maxi_01)
        1    0.315    0.315    0.315    0.315 Zadacha4.1.py:9(<listcomp>)
        1    0.000    0.000    0.433    0.433 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.045    0.045    0.045    0.045 {method 'sort' of 'list' objects}

'''

print(cProfile.run('search_mini_and_maxi_02(10000000)'))

'''
     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.073    0.073    0.935    0.935 <string>:1(<module>)
        1    0.549    0.549    0.863    0.863 Zadacha4.1.py:14(search_mini_and_maxi_02)
        1    0.314    0.314    0.314    0.314 Zadacha4.1.py:15(<listcomp>)
        1    0.000    0.000    0.935    0.935 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects} 

'''

print(cProfile.run('search_mini_and_maxi_03(10000000)'))

''' 
    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.328    0.328 <string>:1(<module>)
        1    0.328    0.328    0.328    0.328 Zadacha4.1.py:25(search_mini_and_maxi_03)
        1    0.000    0.000    0.328    0.328 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


'''

''' 
 По тесту timeit видно, что функция №1 решает за меньшее кол-во времени, хоть и не на очень большое, сравнивая с функцией №3.
 По тесту cProfile видно, что у функции №3 лучшие показатели 
 По двум тестам видно, что функция №3 имеет оптимальный способ решения поставленной задачи
 
'''