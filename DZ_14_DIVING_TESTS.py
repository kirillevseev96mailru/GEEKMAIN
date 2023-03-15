from DZ_14_PYTHON_Погружение import Archive, MyStr, Factorial
import unittest
import pytest


class TestUnitMyStr(unittest.TestCase):
    def setUp(self) -> None:
        print('setUp start')
        self.r1 = MyStr('Hello world!', 'prepod')

    def test_unit_right_output_1(self):
        self.assertEqual(self.r1, 'Hello world!')

    def test_unit_right_name(self):
        self.assertEqual(self.r1.author, 'prepod')

    def test_unit_right_output_2(self):
        self.assertEqual(self.r1.upper(), 'HELLO WORLD!')


def test_doc_archive(char: str) -> str:
    """
    >>> test_doc_archive('a')
    'a, []'
    >>> test_doc_archive('b')
    "b, ['a']"
    >>> test_doc_archive('c')
    "c, ['a', 'b']"
    """
    ob = Archive(char)
    result = f'{ob.text}, {ob.text_archive}'
    return result


def test_py_right_output_1():
    f1 = Factorial()
    assert f1(5) == 120
    assert f1.view() == [{5: 120}]


def test_py_right_output_2():
    f2 = Factorial()
    assert f2(3) == 6
    assert f2.view() == [{3: 6}]
    assert f2(5) == 120
    assert f2.view() == [{3: 6}, {5: 120}]


def test_py_right_output_3():
    f2 = Factorial()
    assert f2(3) == 6
    assert f2(6) == 720
    assert f2(5) == 120
    assert f2(4) == 24
    assert f2.view() == [{3: 6}, {6: 720}, {5: 120}, {4: 24}]


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    unittest.main(verbosity=2)
    pytest.main(['-vv'])
