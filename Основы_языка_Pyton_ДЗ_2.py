#Задание 1

M1 = []
M1.append(21)
M1.append("ABCD")
M1.append(12.1)
M1.append(True)
for i in range(0,4):
    print(type(M1[i]))

#Задание 2

M2 = []
for i in range(0,10):
    B2 = input("Введите элемент массива: ")
    M2.append(B2)
    print(M2)

if len(M2) % 2 == 0:
    for i in range(0,len(M2),2):
        C2 = M2[i]
        M2[i] = M2[i+1]
        M2[i+1] = C2
        print(M2)
else:
    for i in range(0,len(M2)-1,2):
        C2 = M2[i]
        M2[i] = M2[i+1]
        M2[i+1] = C2
        print(M2)

#Задание 3

seasons_list = ['winter', 'spring', 'summer', 'autumn']
seasons_dict = {1 : 'winter', 2 : 'spring', 3 : 'summer', 4 : 'autumn'}
month = int(input("Введите месяц по номеру: "))
if month == 1 or month == 2 or month == 12:
    print(seasons_dict.get(1), " - ", seasons_list[0])
elif month == 3 or month == 4 or month ==5:
    print(seasons_dict.get(2), " - ", seasons_list[1])
elif month == 6 or month == 7 or month == 8:
    print(seasons_dict.get(3), " - ", seasons_list[2])
elif month == 9 or month == 10 or month == 11:
    print(seasons_dict.get(4), " - ", seasons_list[3])
else:
    print("Такого месяца нет!")


#Задание 4

M3 = input('Введите строку: ').split()

for i, el in enumerate(M3, 1):
    print(i, el[0:10])

#Задание 5

M4 = [7, 5, 4, 4, 2, 1]
New_element = 0
the_end = 99999

while New_element != the_end:
    New_element = int(input("Введите значение, если закончили список введите '99999': "))
    if New_element != 99999:
        M4.append(New_element)
        M4.sort(reverse=True)
        print(f"Новый список: {M4}")





