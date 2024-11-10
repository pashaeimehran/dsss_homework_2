import unittest
from math_quiz import generate_random_integer, generate_random_operator, calculate_expression


class TestMathGame(unittest.TestCase):

    def test_generate_random_integer(self):
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val, f"Generated number {rand_num} is out of range.")

    def test_generate_random_operator(self):
        valid_operators = ['+', '-', '*']
        for _ in range(1000):
            operator = generate_random_operator()
            self.assertIn(operator, valid_operators, f"Generated operator {operator} is not valid.")

    def test_calculate_expression(self):
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (10, 3, '-', '10 - 3', 7),
            (4, 2, '*', '4 * 2', 8)
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, result = calculate_expression(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(result, expected_answer)


if __name__ == "__main__":
    unittest.main()
