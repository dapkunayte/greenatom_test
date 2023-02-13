# Написать функцию, которая выполняет сравнение версий
import unittest


def version_comparison(version_1, version_2: str) -> int:
    if type(version_1) != str or type(version_2) != str:
        return "error"  # базовая обработка ошибок (если получены нестроковые данные)
    try:
        v1_list = list(map(int, version_1.split(".")))
        v2_list = list(map(int, version_2.split(".")))
    except ValueError:
        return "error"  # если версия не удовлетворяет формату (числа, разделённые точкой)
    len_v1, len_v2 = len(v1_list), len(v2_list)
    min_len = min(len_v2, len_v1)
    for i in range(min_len):
        if v1_list[i] > v2_list[i]:
            return -1
        elif v1_list[i] < v2_list[i]:
            return 1
    if len_v1 == len_v2:
        return 0
    elif len_v1 > len_v2:
        return -1
    else:
        return 1


# немного тестов для проверки работы функции:)
class VersionComparisonTestCase(unittest.TestCase):
    """Тесты для функции version_comparison"""

    def test_version_1_unequal_length(self):
        comparison_result = version_comparison("2.5.1", "2.4")
        self.assertEqual(comparison_result, -1)

    def test_version_1_equal_length(self):
        comparison_result = version_comparison("2.5.2", "2.5.1")
        self.assertEqual(comparison_result, -1)

    def test_version_2_unequal_length(self):
        comparison_result = version_comparison("2.4.1", "2.5")
        self.assertEqual(comparison_result, -1)

    def test_version_2_equal_length(self):
        comparison_result = version_comparison("2.5.1", "2.5.2")
        self.assertEqual(comparison_result, -1)

    def test_versions_equal_1(self):
        comparison_result = version_comparison("2.5.1", "2.5.1")
        self.assertEqual(comparison_result, 0)

    def test_versions_equal_2(self):
        comparison_result = version_comparison("1.5", "1.5")
        self.assertEqual(comparison_result, 0)

    def test_version_1_error_format(self):
        comparison_result = version_comparison("1.bye", "1.1")
        self.assertEqual(comparison_result, "error")

    def test_version_2_error_format(self):
        comparison_result = version_comparison("1.2", "1.error")
        self.assertEqual(comparison_result, "error")

    def test_version_error_value(self):
        comparison_result = version_comparison(1.2, 1)
        self.assertEqual(comparison_result, "error")
