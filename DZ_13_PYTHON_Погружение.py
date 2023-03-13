'''
    Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
    Напишите к ним классы исключения с выводом подробной информации.
    Поднимайте исключения внутри основного кода.
    Например нельзя создавать прямоугольник со сторонами отрицательной длины.
'''


class ProjectException(Exception):
    pass


class SideTriangleError(ProjectException):
    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f'Вы ввели стороны: ({self.a}, {self.b}, {self.c}), при отрицательной(-ых) стороне(-ах) треугольник ' \
               f'не может существовать'


class TriangleError(ProjectException):
    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f'Вы ввели стороны: ({self.a}, {self.b}, {self.c}), при таких сторонах треугольник не может существовать'


class SimpleNumError(ProjectException):
    def __init__(self, a: int):
        self.a = a

    def __str__(self):
        return f'Вы ввели число: "{self.a}", оно не является простым, так как имеет больше 2-х делителей'


class DateTimeError(ProjectException):
    def __init__(self, a):
        self.a = a

    def __str__(self):
        return f'Вы ввели некорректную дату: {self.a}'


class Triangle:
    def __init__(self, a: int, b: int, c: int):
        self.side1 = a
        self.side2 = b
        self.side3 = c

    def which_tri_exactly(self):
        if (self.side1 < 0) or (self.side2 < 0) or (self.side3 < 0):
            raise SideTriangleError(self.side1, self.side2, self.side3)
        elif self.side1 + self.side2 <= self.side3 or self.side1 + self.side3 <= self.side2 or self.side2 + self.side3 <= self.side1:
            raise TriangleError(self.side1, self.side2, self.side3)
        elif self.side1 != self.side2 and self.side1 != self.side3 and self.side2 != self.side3:
            print("Разносторонний")
        elif self.side1 == self.side2 == self.side3:
            print("Равносторонний")
        else:
            print("Равнобедренный")


class SimpleNum:
    def __init__(self, num: int):
        self.num = num

    def simplicity_check(self):
        k = 0
        for i in range(2, self.num // 2+1):
            if self.num % i == 0:
                k = k+1
        if k > 0:
            raise SimpleNumError(self.num)
        else:
            return f'Число "{self.num}" простое'


class WhatIsWrongWithThisDate:
    def __init__(self, date_input):
        self.date_input = date_input
        self.day = int(date_input.split('.')[0])
        self.month = int(date_input.split('.')[1])
        self.year = int(date_input.split('.')[2])

    def this_year_is_a_leap_year(self):
        if self.year % 4 != 0:
            return False
        elif self.year % 100 == 0:
            if self.year % 400 == 0:
                return True
            else:
                return False
        else:
            return True

    def date_time_correct(self):
        if (self.year <= 9999) and (self.year >= 1):
            if (self.month in [1, 3, 5, 7, 8, 10, 12]) and self.day <= 31:
                return f'Дата {self.date_input} корректна'
            elif (self.month in [4, 6, 9, 10]) and self.day <= 30:
                return f'Дата {self.date_input} корректна'
            elif self.month == 2 and self.day <= 28:
                return f'Дата {self.date_input} корректна'
            elif ((self.year % 4 == 0 and self.year % 100 != 0) or
                (self.year % 4 == 0 and self.year % 100 == 0 and self.year % 400 == 0)) and \
                (self.month == 2) and (self.day <= 29):
                return f'Дата {self.date_input} корректна'
            else:
                raise DateTimeError(self.date_input)
        else:
            raise DateTimeError(self.date_input)


if __name__ == '__main__':
    ob1 = Triangle(1, 4, 4)
    ob1.which_tri_exactly()
    ob2 = SimpleNum(2)
    print(ob2.simplicity_check())
    ob3 = WhatIsWrongWithThisDate('13.16.2002')
    print(ob3.date_time_correct())
