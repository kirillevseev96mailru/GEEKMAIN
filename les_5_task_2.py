from collections import Counter


number_1 = str(input('Введите первое число: '))
number_2 = str(input('Введите второе число: '))
dictionary = Counter({'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                      '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
                      0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8',
                      9: '9', 10 : 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'})

mid_sum = 0

sum_number_1 = 0
t = len(str(number_1))
for i in number_1:
    t = t - 1
    sum_number_1 = sum_number_1 + dictionary[f'{i}'] * (16**(t))
mid_sum += sum_number_1


sum_number_2 = 0
t = len(str(number_2))
for i in number_2:
    t = t - 1
    sum_number_2 = sum_number_2 + dictionary[f'{i}'] * (16**(t))
mid_sum += sum_number_2

amount_to_answer = ''


while mid_sum >= 16:
    if mid_sum % 16 < 10:
        amount_to_answer = amount_to_answer + str(dictionary[f'{mid_sum % 16}'])
    else:
        amount_to_answer = amount_to_answer + str(dictionary[mid_sum % 16])
    mid_sum = mid_sum // 16

if mid_sum % 16 < 10:
    amount_to_answer = amount_to_answer + str(dictionary[f'{mid_sum % 16}'])
else:
    amount_to_answer = amount_to_answer + str(dictionary[mid_sum % 16])

amount_to_answer = f'{amount_to_answer}'[::-1]

print(amount_to_answer)