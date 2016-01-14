import unittest
from logic.functions import Processing


class FunctionTestCase(unittest.TestCase):
    """Conducts tests for logic folder."""

    def setUp(self):
        self.processing = Processing()

    def test_average(self):
        self.assertEqual(self.processing.average(5, 10, 15), 10)

    def test_median(self):
        self.assertEqual(self.processing.median(1, 2, 3, 4, 5), 3)

    def test_iqr(self):
        self.assertEqual(self.processing.iqr(3, 4, 4, 5, 6, 8, 8), 4)

    def test_STDev(self):
        self.assertAlmostEqual(self.processing.standardDeviation(5, 5, 4, 3, 3), 0.89, 0.01)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
