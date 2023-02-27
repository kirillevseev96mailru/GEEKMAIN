from typing import Callable
from random import randint
import csv
import json
from pathlib import Path
import math



def doing_file_csv(count_str: int, CSV_File: Path) -> None:
    rows = []
    for _ in range(count_str):
        Random_N_1 = randint(-1000, 1000)
        Random_N_2 = randint(-1000, 1000)
        Random_N_3 = randint(-1000, 1000)
        rows.append({'Random_N_1': Random_N_1, 'Random_N_2': Random_N_2, 'Random_N_3': Random_N_3})
    with open(CSV_File, 'w', newline='', encoding='utf-8') as f_csv:
        fieldnames = ['Random_N_1', 'Random_N_2', 'Random_N_3']
        writer = csv.DictWriter(f_csv, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def decorator(func: Callable):
    doing_file_csv(randint(100, 1000), Path('Lesson_9.csv'))
    def wrapper(*args, **kwargs):
        CSV_File = Path('Lesson_9.csv')
        JSON_File = Path('Lesson_9.json')
        json_list = []
        with open(CSV_File, 'r', encoding='utf-8') as csv_f:
            reader = csv.reader(csv_f)
            for i, row in enumerate(reader):
                if i == 0:
                    continue
                dict_json = {}
                Random_N_1, Random_N_2, Random_N_3 = row
                result = func(float(Random_N_1), float(Random_N_2), float(Random_N_3))
                dict_json[result] = (float(Random_N_1), float(Random_N_2), float(Random_N_3))
                json_list.append(dict_json)
        with open(JSON_File, 'w', encoding='utf-8') as json_f:
            json.dump(json_list, json_f, indent=2)
        return result
    return wrapper


@decorator
def finding_the_roots(a: int, b: int, c: int):
    discr = b ** 2 - 4 * a * c
    result = ''
    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        result = "x1 = %.2f \nx2 = %.2f" % (x1, x2)
    elif discr == 0:
        x = -b / (2 * a)
        result = "x = %.2f" % x
    elif True:
        result = "Корней нет"
    return result


finding_the_roots()