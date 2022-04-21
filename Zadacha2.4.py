''' https://drive.google.com/file/d/1HWroN6cCeKtUGb2Ld4tv9x36zBcp3SWv/view?usp=sharing '''
n = int(input('Введите число n: '))
sum1 = 0
sum2 = 0
for i in range(1,n+1):
    sum1 = sum1 + i
sum2 = (n * (n+1) / 2)
if sum1 == sum2:
    print(f'Все верно! Они равны! Сумма равна: {sum1}')
else:
    print(f'ОНИ НЕ РАВНЫ! Породокс: {sum1} = {sum1}')