import unittest
from logic.functions import Processing


class FunctionTestCase(unittest.TestCase):
    """Conducts tests for logic folder."""

    def setUp(self):
        self.processing = Processing()

    def average_test(self):
        self.assertEqual(self.processing.average(5, 10, 15), 10)

    def median_test(self):
        self.assertEqual(self.processing.median(1, 2, 3, 4, 5), 3)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
