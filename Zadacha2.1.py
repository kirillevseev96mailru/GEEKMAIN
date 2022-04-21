''' https://drive.google.com/file/d/1uCH2yvJDFVAtpP7GWju5qmPlVEcqhSUz/view?usp=sharing '''

ch1 = int(input('Введите первое число: '))
ch2 = int(input('Введите второе число: '))
znak = str(input('Введите арефмитичесий знак (+, -, *, /): '))

if (ch2 == 0) and (znak == '/'):
    print('Вы ввели "0",при делении, это не верно! :)')
elif (znak == '+'):
    print(ch1 + ch2)
elif (znak == '-'):
    print(ch1 - ch2)
elif (znak == '*'):
    print(ch1 * ch2)
else:
    print(ch1/ch2)