__all__ = ['terrible_queens', 'date_time_correct']


from random import randint
from sys import argv


def terrible_queens():
    counter_answers = 0
    correct_answer = []
    while counter_answers < 4:
        coordinate_x = [0] * 8
        coordinate_y = [0] * 8
        result = 'NO'
        while result == 'NO':
            for queen_number in range(0, 8):
                coordinate_x[queen_number], coordinate_y[queen_number] = queen_number, randint(1, 8)
            flag = 1
            for i in range(0,8):
                for j in range(i+1, 8):
                    if (coordinate_y[i] == coordinate_y[j] or
                        abs(coordinate_x[i]-coordinate_x[j]) == abs(coordinate_y[i]-coordinate_y[j])):
                        flag = 0
            if flag == 1:
                result = 'YES'
        # ПРОВЕРКА НА СОВПАДЕНИЯ РЕШЕНИЙ
        if result == 'YES' and counter_answers == 0:
            correct_answer.append(coordinate_y)
            counter_answers += 1
        elif result == 'YES':
            for answers in range(0, counter_answers):
                flag_2 = 0
                if (False in [correct_answer[answers][i] == coordinate_y[i] for i in range(len(coordinate_y))]) == False:
                    flag_2 = 1
            if flag_2 == 0:
                correct_answer.append(coordinate_y)
                counter_answers += 1
    return correct_answer


def _This_year_is_a_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    else:
        return True


def date_time_correct(date_input: str):
    day = int(date_input.split('.')[0])
    month = int(date_input.split('.')[1])
    year = int(date_input.split('.')[2])
    if year <= 9999  and year >= 1:
        if (month in [1, 3, 5, 7, 8, 10, 12]) and day <= 31:
            print('True')
            return True
        elif (month in [4, 6, 9, 10]) and day <= 30:
            print('True')
            return True
        elif month == 2 and day <= 28:
            print('True')
            return True
        elif _This_year_is_a_leap_year(year) and (month == 2) and (day <= 29):
            print('True')
            return True
        else:
            print('False')
            return False
    else:
        print('False')
        return False


#!!!Для вызова через терминал!!!
# Print добавил, чтобы в терминале выводилось true или False
#if __name__ == "__main__":
#    date_time_correct(str(argv[1]))

print(terrible_queens(), ' - Верные 4 варианта расстановки')
date_input = str(input('Введите дату формата DD.MM.YYYY: '))
print(date_time_correct(date_input))