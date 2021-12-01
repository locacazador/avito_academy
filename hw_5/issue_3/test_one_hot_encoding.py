import unittest

from one_hot_ecndoing import fit_transform


class TestOneHotEncoder(unittest.TestCase):
    """
    Unit test for fit_transform method
    """

    def test_empty_args(self):
        """
        Check if exception is raised with no argument
        """
        with self.assertRaises(TypeError):
            fit_transform()

    def test_success_equal(self):
        """
        Test if correct output of method in case of multiple elements
        """
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        expected_result = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0])
        ]
        self.assertEqual(fit_transform(cities), expected_result)

    def test_success_in(self):
        """
        Test if correct output is a part of final result
        """
        cities = ['Moscow', 'New York', 'Moscow', 'London'] * 10
        expected_part_result = ('London', [1, 0, 0])
        actual_result = fit_transform(cities)
        self.assertIn(expected_part_result, actual_result)

    def test_success_one_string(self):
        """
        Test if correct output in case of single string
        """
        city = 'Balashikha'
        expected_result = [('Balashikha', [1])]
        actual_result = fit_transform(city)
        self.assertEqual(actual_result, expected_result)

    def test_not_in_multiple_strings(self):
        """
        Test whether provided one-hot not in result
        """
        cities = ['a', 'b', 'c', 'a', 'b']
        expected_not_in = ('b', [1, 0, 0])
        actual_result = fit_transform(cities)
        self.assertNotIn(expected_not_in, actual_result)

    def test_empty_list_success(self):
        """
        Test empty list
        """
        empty_list = []
        one_hot_empty_list = fit_transform(empty_list)
        self.assertEqual(empty_list, one_hot_empty_list)


if __name__ == '__main__':
    unittest.main()
