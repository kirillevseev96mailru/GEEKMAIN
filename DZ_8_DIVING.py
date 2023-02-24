'''

Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
* Для дочерних объектов указывайте родительскую директорию.
* Для каждого объекта укажите файл это или директория.
* Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов.

'''
from pathlib import Path
import os
import csv
import json
import pickle


def bypass_files(path_to_files: str, file: Path, json_file: Path) -> None:
    for i in os.listdir(path_to_files):
        name_dir = path_to_files.split("\\")[-1]
        if os.path.isfile(path_to_files + '\\' + i):
            with open(file, 'a', encoding='utf-8') as f:
                path_to_file = path_to_files + "\\" + i
                f.write(f'{name_dir}:{i}:file:{os.path.getsize(path_to_file)}\n')
        if os.path.isdir(path_to_files + '\\' + i):
            with open(file, 'a', encoding='utf-8') as f:
                path_to_file = path_to_files + "\\" + i
                f.write(f'{name_dir}:{i}:dir:{os.path.getsize(path_to_file)}\n')
            bypass_files(path_to_files + '\\' + i, file, json_file)


def redoing_in_json(file: Path, json_file: Path) -> None:
    line_count = sum(1 for _ in open(file))
    with open(file, 'r', encoding='utf-8') as f:
#        main_folder_size = os.path.getsize(r'C:\Users\kiril\PycharmProjects\GEEKBRAINS2\DIVING_PYTHON_2023')
        json_file_dict = {'DIVING_PYTHON_2023': {}}
        for i in range(line_count):
            line = f.readline()
            if line != '':
                name_dir, name, file_or_dir, size = line.split(':')
                if name_dir == 'DIVING_PYTHON_2023':
                    if file_or_dir == 'file':
                        json_file_dict[name_dir].update({str(name): [file_or_dir, int(size)]})
                    elif file_or_dir == 'dir':
                        json_file_dict['DIVING_PYTHON_2023'].update({str('His_' + name): [file_or_dir, int(size)]})
                        json_file_dict['DIVING_PYTHON_2023'][name] = {}
                else:
                    json_file_dict['DIVING_PYTHON_2023'][name_dir].update({str('His_' + name): [file_or_dir, int(size)]})
                with open(json_file, 'w', encoding='utf-8') as f_j:
                    json.dump(json_file_dict, f_j, indent=2)


def redoing_in_csv(file: Path, CSV_File: Path) -> None:
    rows = []
    line_count = sum(1 for _ in open(file))
    with open(file, 'r', encoding='utf-8') as f:
        for i in range(line_count):
            line = f.readline()
            if line != '':
                name_dir, name, file_or_dir, size = line.split(':')
                rows.append({'Name_dir': name_dir, 'Name': name, 'file_or_dir': file_or_dir, 'Size': int(size)})

    with open(CSV_File, 'w', newline='', encoding='utf-8') as f_csv:
        fieldnames = ['Name_dir', 'Name', 'file_or_dir', 'Size']
        writer = csv.DictWriter(f_csv, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def redoing_in_pickle(file: Path, pickle_file: Path) -> None:
    rows = []
    line_count = sum(1 for _ in open(file))
    with open(file, 'r', encoding='utf-8') as f:
        for i in range(line_count):
            line = f.readline()
            if line != '':
                name_dir, name, file_or_dir, size = line.split(':')
                rows.append({'Name_dir': name_dir, 'Name': name, 'file_or_dir': file_or_dir, 'Size': int(size)})

    with open(pickle_file, 'wb') as f_pi:
        pickle.dump(rows, f_pi)


if __name__ == '__main__':
    path_to_files = r'C:\Users\kiril\PycharmProjects\GEEKBRAINS2\DIVING_PYTHON_2023'
    file_dirs_and_files = ''
    bypass_files(path_to_files, Path('../file_dirs_and_files'), Path('../json_file_dirs_and_files'))
    redoing_in_csv(Path('../file_dirs_and_files'), Path('../csv_file_dirs_and_files.csv'))
    redoing_in_json(Path('../file_dirs_and_files'), Path('../json_file_dirs_and_files.json'))
    redoing_in_pickle(Path('../file_dirs_and_files'), Path('../pickle_file_dirs_and_files.pickle'))
