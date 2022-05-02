import timeit
import cProfile


def the_Sieve_algorithm(n, array_one):
    array_one[1]=0
    i = 2
    while i < n ** 0.5:
        if array_one[i] != 0:
            j = i ** 2
            while j <= n:
                array_one[j] = 0
                j = j + i
        i = i + 1
    array_one = [i for i in array_one if array_one[i] != 0]
    return array_one


def Not_a_sieve_algorithm(p):
    prime_number = 0
    k = 0
    i = 2
    while True:
        f = 0
        for j in range(1, round(i ** 0.5) + 1):
            if i % j == 0:
                f = f + 1
        if f == 1:
            k = k + 1
            prime_number = i
        if k == p:
            break
        i = i + 1
    return prime_number

n = int(input('Введите размер решета: '))
p = int(input('Введите порядковый номер простого числа: '))
array = [i for i in range(n + 1)]

print(timeit.timeit('the_Sieve_algorithm(n, array)', number=1000, globals=globals())) #ПРИ n = 10  0.0016647999999999108
print(timeit.timeit('the_Sieve_algorithm(n, array)', number=1000, globals=globals())) #ПРИ n = 100  0.009285500000000058
print(timeit.timeit('the_Sieve_algorithm(n, array)', number=1000, globals=globals())) #ПРИ n = 1000 0.08606590000000036
print(timeit.timeit('the_Sieve_algorithm(n, array)', number=1000, globals=globals())) #ПРИ n = 10000 0.9804824999999999
print(timeit.timeit('the_Sieve_algorithm(n, array)', number=1000, globals=globals())) #ПРИ n = 100000 10.1760714

''' Решая поставленную задачу с помошью функции "the_Sieve_algorithm" , мы наблюдаем линейную зависимость, 
    время увеличивается во столько раз, во сколько "N"  '''

print(timeit.timeit('Not_a_sieve_algorithm(p)', number=1000, globals=globals())) #ПРИ p = 10  0.016220599999999807
print(timeit.timeit('Not_a_sieve_algorithm(p)', number=1000, globals=globals())) #ПРИ p = 100  0.45559740000000004
print(timeit.timeit('Not_a_sieve_algorithm(p)', number=1000, globals=globals())) #ПРИ p = 1000 14.5398374
print(timeit.timeit('Not_a_sieve_algorithm(p)', number=1000, globals=globals())) #ПРИ p = 10000 571.0387772

''' Решая поставленную задачу с помошью функции "Not_a_sieve_algorithm" , мы наблюдаем не линейную зависимость, 
    время увеличивается в большее кол-во раз(+- в 50), нежели "P" '''

print(cProfile.run('the_Sieve_algorithm(n, array)')) #При n = 1_000_000

'''
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    0.147    0.147 <string>:1(<module>)
        1    0.025    0.025    0.025    0.025 Zadacha_4.2_Resheto.py:15(<listcomp>)
        1    0.121    0.121    0.147    0.147 Zadacha_4.2_Resheto.py:5(the_Sieve_algorithm)
        1    0.000    0.000    0.147    0.147 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''

print(cProfile.run('Not_a_sieve_algorithm(p)')) #При p = 10_000

'''
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.583    0.583 <string>:1(<module>)
        1    0.572    0.572    0.583    0.583 Zadacha_4.2_Resheto.py:19(Not_a_sieve_algorithm)
        1    0.000    0.000    0.584    0.584 {built-in method builtins.exec}
   104728    0.011    0.000    0.011    0.000 {built-in method builtins.round}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''


''' По двум тестам(cProfile, timeit) мы видим, что функция "the_Sieve_algorithm" имеет оптимальный способ решения поставленной задачи
    Также проанализировав функцию "the_Sieve_algorithm" мы видим, что она решает за O(n) '''