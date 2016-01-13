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

    def test_sample(self):
        self.failUnlessEqual(2, 2)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
