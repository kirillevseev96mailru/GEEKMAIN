from time import time
from collections import deque


class Factorial:
    def __init__(self):
        self.memory = []

    def __call__(self, n):
        result = 1
        for i in range(2, n + 1):
            result *= i
        self.memory.append({n: result})

        return result

    def view(self):
        return self.memory


class MyStr(str):
    def __new__(cls, value, author):
        instance = super().__new__(cls, value)
        instance.author = author
        instance.time = time()
        return instance

    def __str__(self):
        return f'Строка {self!r} написана автором {self.author}'


class Archive:
    instance = None
    count_archive = []
    text_archive = []

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        else:
            cls.instance.count_archive.append(cls.instance)
            cls.instance.text_archive.append(cls.instance.text)
        return cls.instance

    def __init__(self, text):
        self.text = text

