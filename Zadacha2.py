'''https://drive.google.com/file/d/1kY3RxNzwI0yDLhmiE16lE53BNScanOmh/view?usp=sharing
    Эта блок-схема была красивая, но пришлось пожертвовать ее красотой, чтобы было видно значение и т.д. '''

c1 = int(input('Введите первое число: '))
c2 = int(input('Введите второе число: '))
c3 = int(input('Введите третье число: '))
Sred = 0
if (c1 > c2) and (c1 > c3):
    if (c2 > c3):
        Sred = c2
        print('Среднее число: ',c2)
    else:
        Sred = c3
        print('Среднее число: ', c3)

elif (c3 > c2) and (c3 > c1):
    if (c2 > c1):
        Sred = c2
        print('Среднее число: ',c2)
    else:
        Sred = c1
        print('Среднее число: ', c1)

elif (c2 > c1) and (c2 > c3):
    if (c1 > c3):
        Sred = c1
        print('Среднее число: ',c1)
    else:
        Sred = c3
        print('Среднее число: ', c3)
