import logging
import argparse

FORMAT = '{levelname} - {asctime} - {funcName} - {msg}'
logging.basicConfig(level=logging.INFO, filename='Work_Class_SimpleNum.log', encoding='utf-8',  format=FORMAT, style='{')
logger = logging.getLogger(__name__)


class ProjectException(Exception):
    pass


class SimpleNumError(ProjectException):
    def __init__(self, a: int):
        self.a = a

    def __str__(self):
        return f'Вы ввели число: "{self.a}", оно не является простым, так как имеет больше 2-х делителей'


class SimpleNum:
    def __init__(self, num: int):
        self.num = num

    def simplicity_check(self):
        k = 0
        for i in range(2, self.num // 2+1):
            if self.num % i == 0:
                k = k+1
        if k > 0:
            logger.error(f'Вы ввели число: "{self.num}", оно не является простым, так как имеет больше 2-х делителей')
            return SimpleNumError(self.num)
        else:
            logger.info(f'Число "{self.num}" простое')
            return f'Число "{self.num}" простое'


def parser_func_2():
    parser = argparse.ArgumentParser(description='Получаем число')
    parser.add_argument('-n', '--num')
    args = parser.parse_args()
    obj = SimpleNum(int(args.num))
    return obj.simplicity_check()


if __name__ == '__main__':
    ob2 = SimpleNum(4)
    ob2.simplicity_check()
    ob2 = SimpleNum(2)
    ob2.simplicity_check()
    ob2 = SimpleNum(5)
    ob2.simplicity_check()
    ob2 = SimpleNum(6)
    ob2.simplicity_check()
    print(parser_func_2())