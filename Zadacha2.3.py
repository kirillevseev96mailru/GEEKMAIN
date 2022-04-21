''' https://drive.google.com/file/d/1KCYska7caizDCvnwMx5WwMtCvhYT3MHL/view?usp=sharing '''
chislo1 = int(input('Введите число: '))
chislo2 = 0
while chislo1 != 0:
    chislo2 = chislo2*10 + (chislo1 % 10)
    chislo1 = chislo1 // 10
print(f'Перевернутое число: {chislo2}')
