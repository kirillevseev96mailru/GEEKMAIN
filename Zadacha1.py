''' https://drive.google.com/file/d/1UOu20uU8OindLjzxJdAwe3uWceFlYw81/view?usp=sharing '''

a = int(input('Введите 3-хзначное число: '))
c1 = a // 100
c2 = a % 100 // 10
c3 = a % 10
Sum = c1 + c2 + c3
Pro = c1 * c2 * c3
print('Сумма и произведение: ', Sum ,',', Pro)


