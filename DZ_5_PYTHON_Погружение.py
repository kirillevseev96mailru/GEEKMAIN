def fun_way(string_way):
    pos = string_way.find('.')
    file_extension = string_way[pos + 1:]
    name_file = (string_way.split('\\')[-1].replace(f'.{string_way[pos + 1:]}', ''))
    path_file = string_way.split('.')[0].replace(f'\{name_file}', '')

    yield (path_file, name_file, file_extension)


string_way = 'C:\ALLUsers\kiril\PycharmProjects\_task_1.py'
generator_path = fun_way(string_way)
for i in generator_path:
    print(i)

print('*' * 50)

names = ['Коля', 'Вова', 'Иван', 'Даня', 'Петрович']
rates = [20, 40, 50, 60, 70]
percents = ['45.33%', '12.24%', '1.23%', '77.25%', '99.25%']
PERC = 100

res_dict = {names[i]: (rates[i] + ((rates[i] * float(percents[i][:-1])) / PERC)) for i in range(0, len(names))}
print(res_dict)

print('*' * 50)

def nfib(n):
    a, b = 0, 1
    for __ in range(n):
        yield a
        a, b = b, a + b

res2 = [x for x in nfib(20)]
print(res2)