''' https://drive.google.com/file/d/1ni-Sp1QQYKnUumiM0b8UUEI9adLVDTSQ/view?usp=sharing '''
x1 = int(input('Введите значение x1: '))
x2 = int(input('Введите значение x2: '))
y1 = int(input('Введите значение y1: '))
y2 = int(input('Введите значение y2: '))
k = (y1 - y2)/(x1 -x2)
b = y2 - (k * x2)
print("y = {} * x + {}".format(k,b))