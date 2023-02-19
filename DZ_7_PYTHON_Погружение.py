'''
Решить задачи, которые не успели решить на семинаре.
Напишите функцию группового переименования файлов.
Она должна:
принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
принимать параметр количество цифр в порядковом номере.
принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
принимать параметр расширение конечного файла.
принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из
исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.
'''
__all__ = ['rename_files']


from pathlib import Path
from random import choice
from string import ascii_letters, digits
import os


def rename_files(old_file: Path, new_name: str, number_of_digits_in_serial_number: int,
                old_extension: str, new_extension: str, name_range_arr: str):
    NRA1 = int(name_range_arr.split(',')[0])
    NRA2 = int(name_range_arr.split(',')[1])
    print(NRA1, NRA2)
    original_name = ''.join(ascii_letters[NRA1:NRA2])
    file_sequence_number = ''.join(choice(digits) for _ in range(number_of_digits_in_serial_number))
    new_original_name = original_name + '_' + new_name + '_' + file_sequence_number
    new_file = '{}.{}'.format(new_original_name, new_extension)
    with open(old_file, 'r') as f1:
        with open(new_file, 'w') as f2:
            f2.write(f1.read())
    os.remove(old_file)



if __name__ == '__main__':
    folder = r'C:\Users\kiril\PycharmProjects\GEEKBRAINS2\DIVING_PYTHON_2023'
    print('Начинаем переименовывать файлы и менять их разрешение!')
    for filename in os.listdir(folder):
        if filename.split('.')[1] != 'py':
            YES_OR_NO = str(input(f'На очереди файл {filename}, меняем его имя и разрешение?(Да/Нет): '))
            if YES_OR_NO.capitalize() == 'Да':
                new_extension = str(input(f'Введите новое расширение для {filename}: '))
                new_name = str(input(f'Введите новое имя для {filename}: '))
                number_of_digits_in_serial_number = int(input(f'Введите длину порядкового номера для {filename}: '))
                name_range_arr = str(input(f'Введите два числа от 0 до 26 для оригинального имени {filename}, ФОРМАТ("1,7"): '))
                print(name_range_arr)
                old_extension = filename.split('.')[1]
                rename_files(Path(filename), new_name, number_of_digits_in_serial_number, old_extension, new_extension, name_range_arr)

        else:
            print('Это питоновский файл, не очень хочется , чтобы ему меняли разрешение!')


