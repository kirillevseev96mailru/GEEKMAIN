''' https://drive.google.com/file/d/1x4PRufK-MqmOXTj4D3XtlGDfPtcXDHa8/view?usp=sharing '''
n = int(input('Введите число: '))
cc = 0
cn = 0
x = 0
while n != 0:
    x = n % 10
    n = n // 10
    if (x % 2 == 0):
        cc = cc + 1
    else:
        cn = cn + 1

print(f'Кол-во нечетных цифр: {cn} , кол-во четных цифр: {cc}')