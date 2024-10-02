import unittest
from lib import count_common_elements

class TestCountCommonElements(unittest.TestCase):
    def test_common_elements_multiple_lists(self):
        # Тест с несколькими списками с общими элементами
        self.assertEqual(count_common_elements([1, 2, 3], [3, 4, 5], [3, 6, 7]), 1)

    def test_no_common_elements(self):
        # Тест с отсутствием общих элементов
        self.assertEqual(count_common_elements([1, 2, 3], [4, 5, 6], [7, 8, 9]), 0)

    def test_all_elements_common(self):
        # Тест, когда все элементы общие
        self.assertEqual(count_common_elements([1, 2], [1, 2], [1, 2]), 2)

    def test_single_list(self):
        # Тест с одним списком (все элементы считаются общими)
        self.assertEqual(count_common_elements([1, 2, 3]), 3)

    def test_empty_lists(self):
        # Тест с пустыми списками
        self.assertEqual(count_common_elements([], [], []), 0)

    def test_lists_with_duplicates(self):
        # Тест, когда списки содержат дубликаты, но обрабатываются как множества
        self.assertEqual(count_common_elements([1, 1, 2, 3], [1, 1, 4], [1, 5]), 1)

    def test_no_lists(self):
        # Тест с отсутствием списков
        with self.assertRaises(IndexError):
            count_common_elements()

if __name__ == '__main__':
    unittest.main()
