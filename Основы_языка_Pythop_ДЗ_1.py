# Задача №2

entered_time = int(input('Введите кол-во секунд: '))
hours =  entered_time // 3600
minutes = (entered_time % 3600) // 60
seconds = (entered_time % 3600) % 60
if hours > 24:
    print('Количество полученных часов превышает количество часов в сутка, скоректируйте ввод.')
else:
    print(f'Московское время: {hours}:{minutes}:{seconds}')


# Задача №3

tusk_3_n = int(input('Введите число n: '))
print(tusk_3_n + tusk_3_n * 10 + tusk_3_n + tusk_3_n * 100 + tusk_3_n * 10 + tusk_3_n)

# Задача №4

tusk_4_n = int(input('Введите число n: '))
tusk_4_max = -1
while tusk_4_n > 0:
    if (tusk_4_n % 10) > tusk_4_max:
        tusk_4_max = tusk_4_n % 10
    tusk_4_n = tusk_4_n // 10
print(tusk_4_max)

# Задача №5

tusk_5_plus = int(input('Введите значение прибыли: '))
tusk_5_minus = int(input('Введите значение издержек: '))
tusk_5_people = int(input('Ввдите количество работников: '))
if tusk_5_plus > tusk_5_minus:
     print('Выручка больше издержек')
     tusk_5_clear_plus = tusk_5_plus - tusk_5_minus
     tusk_5_rent = tusk_5_clear_plus/tusk_5_plus
     print('Рентабельность {} выручки {}: {:.2f}' .format('нашей','составила',tusk_5_rent))
     tusk_5_clear_for_person = float(tusk_5_clear_plus/tusk_5_people)
     print('Прибыль фирмы в расчете на одного сотрудника: %s'%tusk_5_clear_for_person)
else:
     print('Фирма работает в убыток')


# Задача №7

tusk_7_a = int(input('Введите a километров: '))
tusk_7_b = int(input('Введите b километров: '))
tusk_7_k = 0
if tusk_7_a >= tusk_7_b:
    print('0 дней')
else:
    while tusk_7_a < tusk_7_b:
        tusk_7_k += 1
        tusk_7_a = tusk_7_a * (110/100)
        print(f'День {tusk_7_k}, результат: {tusk_7_a}')
print(f'Кол-во дней через которые он достигнет цели = {tusk_7_k}')