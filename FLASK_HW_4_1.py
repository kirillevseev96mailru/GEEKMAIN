'''
    Напишите программу на Python, которая будет находить сумму элементов массива из 1000000 целых чисел.
    Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
    Массив должен быть заполнен случайными целыми числами от 1 до 100.
    При решении задачи нужно использовать многопоточность, многопроцессорность и асинхронность.
    В каждом решении нужно вывести время выполнения вычислений.
'''

from random import randint
import threading
import multiprocessing
import asyncio

sum_nums_multip = 0


def summation_theards(array, first_num, last_num):
    global sum_nums_threads
    for i in range(first_num, last_num + 1):
        sum_nums_threads = sum_nums_threads + array[i]
    print(f'Значение суммы: {sum_nums_threads}')


def summation_multiprocessing(array, first_num, last_num):
    global sum_nums_multip
    for i in range(first_num, last_num + 1):
        sum_nums_multip = sum_nums_multip + array[i]
    print(f'Значение суммы: {sum_nums_multip}')


async def summation_asyncio(array, first_num, last_num):
    global sum_nums_asyncio
    for i in range(first_num, last_num + 1):
        sum_nums_asyncio = sum_nums_asyncio + array[i]
    print(f'Значение суммы: {sum_nums_asyncio}')


if __name__ == '__main__':

    threads = []
    array = []
    sum_nums_threads = 0

    for _ in range(10000):
        array.append(randint(1, 100))

    for i in range(4):
        t = threading.Thread(target=summation_theards, args=(array, i*2500, i*2500+2500-1))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(50*'*')
    threads = []

    for i in range(4):
        p = multiprocessing.Process(target=summation_multiprocessing, args=(array, i*2500, i*2500+2500-1))
        threads.append(p)
        p.start()

    for p in threads:
        p.join()

    print(50 * '*')
    sum_nums_asyncio = 0
    tasks = []

    for i in range(4):
        task = asyncio.ensure_future(summation_asyncio(array, i*2500, i*2500+2500-1))
        tasks.append(task)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
