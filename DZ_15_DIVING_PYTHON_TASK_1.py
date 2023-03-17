'''
    Решить задачи, которые не успели решить на семинаре.
    Возьмите любые 1-3 задачи из прошлых домашних заданий. Добавьте к ним логирование ошибок и полезной информации.
    Также реализуйте возможность запуска из командной строки с передачей параметров.
'''
import logging
import argparse

FORMAT = '{levelname} - {asctime} - {funcName} - {msg}'
logging.basicConfig(level=logging.INFO, filename='Work_Class_Triangle.log', encoding='utf-8',  format=FORMAT, style='{')
logger = logging.getLogger(__name__)


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


class Triangle:
    def __init__(self, a: int, b: int, c: int):
        self.side1 = a
        self.side2 = b
        self.side3 = c

    def which_tri_exactly(self):
        if (self.side1 < 0) or (self.side2 < 0) or (self.side3 < 0):
            logger.error(f'Вы ввели стороны: ({self.side1}, {self.side2}, {self.side3}), при отрицательной(-ых) '
                         f'стороне(-ах) треугольник не может существовать')
            return SideTriangleError(self.side1, self.side2, self.side3)
        elif self.side1 + self.side2 <= self.side3 or self.side1 + self.side3 <= self.side2 or self.side2 + self.side3 <= self.side1:
            logger.error(f'Вы ввели стороны: ({self.side1}, {self.side2}, {self.side3}), при таких сторонах треугольник '
                         f'не может существовать')
            return TriangleError(self.side1, self.side2, self.side3)
        elif self.side1 != self.side2 and self.side1 != self.side3 and self.side2 != self.side3:
            logger.info(f'Разносторонний треугольник со сторонами: ({self.side1}, {self.side2}, {self.side3})')
            return f'Разносторонний треугольник со сторонами: ({self.side1}, {self.side2}, {self.side3})'
        elif self.side1 == self.side2 == self.side3:
            logger.info(f'Равносторонний треугольник со сторонами: ({self.side1}, {self.side2}, {self.side3})')
            return f'Равносторонний треугольник со сторонами: ({self.side1}, {self.side2}, {self.side3})'
        else:
            logger.info(f'Равнобедренный треугольник со сторонами: ({self.side1}, {self.side2}, {self.side3})')
            return f'Равнобедренный треугольник со сторонами: ({self.side1}, {self.side2}, {self.side3})'


def parser_func_1():
    parser = argparse.ArgumentParser(description='Получаем 3 числа')
    parser.add_argument('-s_1', '--side_1')
    parser.add_argument('-s_2', '--side_2')
    parser.add_argument('-s_3', '--side_3')
    args = parser.parse_args()
    obj = Triangle(int(args.side_1), int(args.side_2), int(args.side_3))
    return obj.which_tri_exactly()


if __name__ == '__main__':
    ob1 = Triangle(4, 4, 4)
    ob1.which_tri_exactly()
    ob1 = Triangle(3, 4, 5)
    ob1.which_tri_exactly()
    ob1 = Triangle(1, 4, 4)
    ob1.which_tri_exactly()
    ob1 = Triangle(1, 4, 1)
    ob1.which_tri_exactly()
    ob1 = Triangle(1, 4, -5)
    ob1.which_tri_exactly()
    parser_func_1()
