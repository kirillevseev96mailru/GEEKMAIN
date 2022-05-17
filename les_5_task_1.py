import collections

сompany = collections.namedtuple('company', ['С1', 'С2', 'С3', 'С4'])
the_company = {}
n = int(input("Количество предприятий: "))


for i in range(n):
    name = input('Название ' + str(i+1) + ' компании: ')
    profit_1 = int(input('Прибыль за 1 квартал: '))
    profit_2 = int(input('Прибыль за 2 квартал: '))
    profit_3 = int(input('Прибыль за 3 квартал: '))
    profit_4 = int(input('Прибыль за 4 квартал: '))
    the_company[name] = сompany(
        С1=profit_1,
        С2=profit_2,
        С3=profit_3,
        С4=profit_4
    )

max_average_profit = 0
the_company_with_max_profit = ''
min_average_profit = 1000000000000000
the_company_with_min_profit = ''


for name, profit in the_company.items():
    if sum(profit)/4 > max_average_profit:
        max_average_profit = sum(profit)/4
        the_company_with_max_profit = name
    if sum(profit)/4 < min_average_profit:
        min_average_profit = sum(profit)/4
        the_company_with_min_profit = name
    print(f'Компания: {name} , прибыль за 4 квартала(год) - {sum(profit)} , средняя прибыль в квартал - {sum(profit)/4}')

print(f'Компания {the_company_with_max_profit} имеет наибольший средний заработок: {max_average_profit}')
print(f'Компания {the_company_with_min_profit} имеет наименьший средний заработок: {min_average_profit}')