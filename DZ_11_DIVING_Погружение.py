'''
    Создайте класс Матрица. Добавьте методы для вывода на печать, сравнения, сложения и *умножения матриц.
'''
class AddSubMatrix(object):
    '''Класс для работы с матрицами'''
    def __init__(self, list_of_lists):
        self.matrix = list_of_lists


    def __str__(self):
        for row in self.matrix:
            for i in row:
                print(f"{i:4}", end="")
            print()
        return ''


    def __add__(self, other):
        '''Делаем проверку на то, что матрицы одинакового размера и складываем их'''
        if len(self.matrix) != len(other.matrix):
            return 'матрицы не согласованы'
        else:
            for i in range(len(self.matrix)):
                for i_2 in range(len(other.matrix[i])):
                    self.matrix[i][i_2] = self.matrix[i][i_2] + other.matrix[i][i_2]
            return AddSubMatrix.__str__(self)


    def __mul__(self, other):
        '''Делаем проверку на то, что матрицы одинакового размера и умножаем их'''
        if len(self.matrix) != len(other.matrix):
            return 'матрицы не согласованы'
        else:
            for i in range(len(self.matrix)):
                for i_2 in range(len(other.matrix[i])):
                    self.matrix[i][i_2] = self.matrix[i][i_2] * other.matrix[i][i_2]
            return AddSubMatrix.__str__(self)


    def __eq__(self, other):
        '''Понятия "Больше", "Меньше" к матрицам не применимы'''
        if len(self.matrix) != len(other.matrix):
            return 'матрицы не согласованы'
        else:
            for i in range(len(self.matrix)):
                for i_2 in range(len(other.matrix[i])):
                    if self.matrix[i][i_2] != other.matrix[i][i_2]:
                        return False
            return True




if __name__ == '__main__':
    obj1 = AddSubMatrix([[-1, 0, 1], [-1, 0, 1], [0, 1, -1], [1, 1, -1]])
    obj2 = AddSubMatrix([[-1, 0, 1], [-1, 0, 1], [0, 1, -1], [1, 1, -1]])
    print(obj1.__eq__(obj2))
    print(obj1.__add__(obj2))
    print(obj1.__add__(obj2))
    print(obj1.__mul__(obj2))
    print(obj1.__eq__(obj2))
    print(help(obj1))
