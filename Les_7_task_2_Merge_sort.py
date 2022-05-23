import random

def Merge(left_m,right_m):
    new_array = []
    i = 0
    j = 0
    while i < len(left_m) and j < len(right_m):
        if left_m[i] > right_m[j]:
            new_array.append(left_m[i])
            i += 1
        else:
            new_array.append(right_m[j])
            j += 1

    if i < len(left_m):
        new_array += left_m[i:]
    if j < len(right_m):
        new_array += right_m[j:]
    return new_array


def Merge_fun(array):
    if len(array) == 1:
        return array
    middle = len(array) // 2
    left = Merge_fun(array[:middle])
    right = Merge_fun(array[middle:])

    return(Merge(left,right))


MIN_ITEM = 0
MAX_ITEM = 49

n = int(input('Ввведите значение N: '))
simple_array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(n)]
print(simple_array)
print(Merge_fun(simple_array))