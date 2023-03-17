import logging
import argparse

FORMAT = '{levelname} - {asctime} - {funcName} - {msg}'
logging.basicConfig(level=logging.INFO, filename='Work_Class_WhatIsWrongWithThisDate.log', encoding='utf-8',
                    format=FORMAT, style='{')
logger = logging.getLogger(__name__)


class ProjectException(Exception):
    pass


class DateTimeError(ProjectException):
    def __init__(self, a):
        self.a = a

    def __str__(self):
        return f'Вы ввели некорректную дату: {self.a}'


class WhatIsWrongWithThisDate:
    def __init__(self, date_input):
        self.date_input = date_input
        self.day = int(date_input.split('.')[0])
        self.month = int(date_input.split('.')[1])
        self.year = int(date_input.split('.')[2])

    def date_time_correct(self):
        if (self.year <= 9999) and (self.year >= 1):
            if (self.month in [1, 3, 5, 7, 8, 10, 12]) and self.day <= 31:
                logger.info(f'Дата {self.date_input} корректна')
                return f'Дата {self.date_input} корректна'
            elif (self.month in [4, 6, 9, 10]) and self.day <= 30:
                logger.info(f'Дата {self.date_input} корректна')
                return f'Дата {self.date_input} корректна'
            elif self.month == 2 and self.day <= 28:
                logger.info(f'Дата {self.date_input} корректна')
                return f'Дата {self.date_input} корректна'
            elif ((self.year % 4 == 0 and self.year % 100 != 0) or
                (self.year % 4 == 0 and self.year % 100 == 0 and self.year % 400 == 0)) and \
                (self.month == 2) and (self.day <= 29):
                logger.info(f'Дата {self.date_input} корректна')
                return f'Дата {self.date_input} корректна'
            else:
                logger.error(f'Вы ввели некорректную дату: {self.date_input}')
                return DateTimeError(self.date_input)
        else:
            logger.error(f'Вы ввели некорректную дату: {self.date_input}')
            return DateTimeError(self.date_input)


def parser_func_2():
    parser = argparse.ArgumentParser(description='Получаем дату datetime из строки')
    parser.add_argument('-d', '--DATE')
    args = parser.parse_args()
    obj = WhatIsWrongWithThisDate(args.DATE)
    return obj.date_time_correct()


if __name__ == '__main__':
    ob3 = WhatIsWrongWithThisDate('13.12.2002')
    ob3.date_time_correct()
    ob3 = WhatIsWrongWithThisDate('13.16.2002')
    ob3.date_time_correct()
    ob3 = WhatIsWrongWithThisDate('13.1236.200221421')
    ob3.date_time_correct()
    ob3 = WhatIsWrongWithThisDate('-13.16.2002')
    ob3.date_time_correct()
    print(parser_func_2())