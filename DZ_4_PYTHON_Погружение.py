#Задача№1
def task_1(list_1):
    list_from_set = []
    for num in int_list:
        if int_list.count(num) > 1 and num not in list_from_set:
            list_from_set.append(num)
    return list_from_set

int_list = [1, 1, 0, 2, 5, 5, 6, 7, 9, 0]
print(int_list)
print(task_1(int_list))

#Задача№2
import re

def task_2(string_1):
    dictionary_from_tuple = {}
    for word in re.split(' |,|:|;|\n', string_1):
        dictionary_from_tuple[word] = dictionary_from_tuple.setdefault(word, 0) + 1
    sorted_dictionary_from_tuple = {}
    sorted_keys = sorted(dictionary_from_tuple, key=dictionary_from_tuple.get)
    for i in sorted_keys:
        sorted_dictionary_from_tuple[i] = dictionary_from_tuple[i]
    data = []
    for key in sorted_dictionary_from_tuple:
        data.append(key)
    num_1 = len(data) - 1
    num_2 = 1
    while num_2 < 11:
        print(f'{num_2} - {data[num_1]} - {sorted_dictionary_from_tuple[data[num_1]]}')
        num_2 += 1
        num_1 -= 1

random_string = """She sells sea shells on a a a a a a a a a a a a a a a a a a a a the sea shore 
The shells that she sells are sea shells Im sure.
So if she sells sea shells on the sea shore,
Im sure that the shells are b b b b b b b b b b b b b b b b b b b sea shore shells."""
task_2(random_string)


#Задача№3
from random import randint


BACKPACK_CAPACITY = 9.0


def task_3(dictionary):
    res = 0.0
    array_of_keys = []
    array_of_values = []
    for key in dictionary:
        array_of_keys.append(key)
    for key in dictionary:
        array_of_values.append(dictionary[key])
    while res < BACKPACK_CAPACITY and len(array_of_keys) > 1:
        k = randint(0, len(array_of_keys) - 1)
        res = res + float(array_of_values[k])
        while res > BACKPACK_CAPACITY and len(array_of_keys) > 1:
            res = res - float(array_of_values[k])
            array_of_keys.remove(array_of_keys[k])
            k = randint(0, len(array_of_keys) - 1)
            res = res + float(array_of_values[k])
        print(f'{res} <- {array_of_keys[k]}({array_of_values[k]})')
        array_of_keys.remove(array_of_keys[k])
    print(res, ' ', BACKPACK_CAPACITY)

dictionary = {'Газовая горелка': '0.5', 'Кофта': '1', 'Фонарик': '1', 'Палатка': '5',
              'Зажигалка': '0.1', 'Книга': '2', 'Компас': '0.5', 'Колонка': '2'}
task_3(dictionary)