'''
    Создайте класс-фабрику. Класс принимает тип животного
    (название одного из созданных классов) и параметры для этого типа.
    Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
    Возьмите 1-3 любые задачи из прошлых семинаров, которые вы уже решали. Превратите функции в методы класса.
    Задачи должны решаться через вызов
'''


class Animal:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Bird(Animal):
    def __init__(self, colour, * args):
        self.colour = colour
        super().__init__(*args)

    def get_colour(self):
        return self.colour


class Cat(Animal):
    def __init__(self, cat_breed, *args):
        self.cat_breed = cat_breed
        super().__init__(*args)

    def get_breed(self):
        return self.cat_breed


class Dog(Animal):
    def __init__(self, tail_length, *args):
        self.tail_length = tail_length
        super().__init__(*args)

    def get_tail_length(self):
        return self.tail_length


class Make_Animal:
    def __init__(self, type_of_animal, name, features):
        self.type_of_animal = type_of_animal
        self.features = features
        self.name = name

    def creating_animal(self):
        if self.type_of_animal == 'Dog':
            return Dog(self.name, self.features)
        elif self.type_of_animal == 'Bird':
            return Bird(self.name, self.features)
        elif self.type_of_animal == 'Cat':
            return Cat(self.name, self.features)


class WhatIsWrongWithThisDate:
    def __init__(self, date_input):
        self.date_input = date_input
        self.day = int(date_input.split('.')[0])
        self.month = int(date_input.split('.')[1])
        self.year = int(date_input.split('.')[2])

    def This_year_is_a_leap_year(self):
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
        if self.year <= 9999  and self.year >= 1:
            if (self.month in [1, 3, 5, 7, 8, 10, 12]) and self.day <= 31:
                return True
            elif (self.month in [4, 6, 9, 10]) and self.day <= 30:
                return True
            elif self.month == 2 and self.day <= 28:
                return True
            elif ((self.year % 4 == 0 and self.year % 100 != 0) or
                (self.year % 4 == 0 and self.year % 100 == 0 and self.year % 400 == 0)) and \
                (self.month == 2) and (self.day <= 29):
                return True
            else:
                return False
        else:
            return False



if __name__ == '__main__':
    B = Make_Animal('Bird', 'Coco', 'Red')
    C = B.creating_animal()
    print(C.name)
    print(C.colour)
    D = WhatIsWrongWithThisDate('12.12.2090')
    print(D.This_year_is_a_leap_year())
    print(D.date_time_correct())