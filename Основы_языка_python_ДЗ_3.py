#Задача №1
def fun1(a,b):
    if b == 0:
        return "ERROR"
    elif a == 0:
        return 0
    else:
        c = a / b
        return (c)

a1 = int(input("Введите чеслитель: "))
b1 = int(input("Введите знаменатель: "))
print(fun1(a1,b1))

#Задача №2
def fun2(name, surname, year_of_birth, city, email, phone):
    print(f'Информация о пользователе \n'
          f'Имя: {name} \n'
          f'Фамилия: {surname}\n'
          f'Год рождения: {year_of_birth}\n'
          f'Город проживания: {city}\n'
          f'Почти: {email}\n'
          f'Телефон: {phone}\n')
name = str(input("Введите свое имя: "))
surname = str(input("Введите свою фамилию: "))
year_of_birth = int(input("Введите свой год рождения: "))
email = str(input("Введите свою почту: "))
city = str(input("Введите название своего города: "))
phone = int(input("Введите свой телефон: "))
fun2(name, surname, year_of_birth, city, email, phone)


#Задача №3
def fun3(a,b,c):
    sum = a + b + c - min(a,b,c)
    return sum

a3 = int(input("Введите 1-ое число: "))
b3 = int(input("Введите 2-ое число: "))
c3 = int(input("Введите 3-ие число: "))

print(fun3(a3,b3,c3))

#Задача №4
def fun4(x,y):
    y = y * (-1)
    new_x_1 = x ** y
    new_x_2 = 1
    for i in range(0,y):
        new_x_2 = new_x_2 * x
    if new_x_1 == new_x_2:
        return new_x_2
x4 = int(input("Введите X: "))
y4 = int(input("Введите Y: "))
print(fun4(x4,y4))

#Задача №5
def fun5(*nums):
    sum = 0
    symbol = False
    for num in nums:
        try:
            if num:
                sum += float(num)
        except ValueError:
            symbol = True
    return sum, symbol

general_sum_5 = 0

while True:
    numbers_string = input('Введите числа через пробел: ').split(' ')
    sum, stop_symbol = fun5(*numbers_string)
    general_sum_5 += sum
    print(f'сумма {general_sum_5}')

    if stop_symbol:
        break


#Задача №6
def fun6(word):
    return word.title()
word = str(input("Input words "))
print(fun5(word))

