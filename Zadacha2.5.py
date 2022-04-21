''' https://drive.google.com/file/d/1YmShPYwujG2uFzONYwpWc_DOy_lGfBMV/view?usp=sharing '''
posl = input('Введите последовательность: ')
chislo = input('Введите цифру для поиска: ')
count = 0

for i in posl:
    if i == chislo:
        count = count + 1

print(f'Число {chislo} встречается {count} раза')