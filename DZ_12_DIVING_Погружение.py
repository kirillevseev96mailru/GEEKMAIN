'''
    Создайте класс студента.
    Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
    Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
    Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
    Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.
'''

from pathlib import Path
import csv
from random import randint


class Text:
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __set__(self, instance, value):
        if self.param1(value) and self.param2(value) is False:
            setattr(instance, self.param_name, value)
        else:
            raise ValueError(f'Вы ввели "{value}" не с большой буквы! Или в "{value}" есть цифры')


class Student:
    surname = Text(str.istitle, str.isdigit)
    name = Text(str.istitle, str.isdigit)
    fatherland = Text(str.istitle, str.isdigit)

    def __init__(self, FIO: str):
        self.surname = FIO.split()[0]
        self.name = FIO.split()[1]
        self.fatherland = FIO.split()[2]

    def __exit__(self):
        '''Формируем информацию об ученике, принимая предмет из файла CSV + рандомно заполняя оценки и результаты тестов'''
        self.csv_file = Path('task.csv').open('r', encoding='utf-8')
        self.School_Subjects = {}
        reader = csv.reader(self.csv_file)
        for i, row in enumerate(reader):
            if i == 0:
                continue
            else:
                count_test = randint(1,5)
                count_evaluations = randint(1,12)
                evaluations = []
                tests = []
                for _ in range(count_evaluations):
                    evaluations.append(randint(2,5))
                for _ in range(count_test):
                    tests.append(randint(0,100))
                self.School_Subjects[str(row)] = (evaluations, tests)

    def InformationOutput(self):
        '''Здесь мы будем выводить информацию об успеваемости ученика'''
        average_estimation = 0
        count_estimation = 0
        print(f'У ученика {self.surname} {self.name} {self.fatherland} следующие результаты:')
        for NameSub in self.School_Subjects:
            if NameSub != None:
                average_point = sum(self.School_Subjects[NameSub][1]) / len(self.School_Subjects[NameSub][1])
                print(f'По предмету {NameSub} средний балл за тесты: {average_point:.2f}')
                average_estimation += sum(self.School_Subjects[NameSub][0])
                count_estimation += len(self.School_Subjects[NameSub][0])
        average_estimation = average_estimation / count_estimation
        print(f'По всем предметам средняя оценка: {average_estimation:.2f}')

    def __str__(self):
        return f'Ученик: {self.surname} {self.name} {self.fatherland}'


if __name__ == '__main__':
    ob1 = Student('Евсеев Кирилл Дмитриевич')
    ob1.__exit__()
    print(ob1.InformationOutput())
    ob2 = Student('Леший Из Туссента')
    ob2.__exit__()
    print(ob2.InformationOutput())

