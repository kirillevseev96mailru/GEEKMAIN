'''
    https://drive.google.com/file/d/18MMpZqDR4Gl0N9eMcEkGuCfsZTI2_wxQ/view?usp=sharing
    Здесь я решаю задачу №7 рекурсией!!!
'''

def POSLED(n):
    if n == 1:
        return n
    elif n > 0:
        return n + POSLED(n-1)

n = int(input('Введите число n: '))

sum1 = POSLED(n)
sum2 = (n * (n+1) / 2)

if sum1 == sum2:
    print(f'Все верно! Они равны! Сумма равна: {sum1}')
else:
    print(f'ОНИ НЕ РАВНЫ! Породокс: {sum1} = {sum1}')
