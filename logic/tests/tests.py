import unittest
from logic.functions import Processing



class FunctionTestCase(unittest.TestCase):
    """Conducts tests for logic/functions.py"""

    def setUp(self):
        self.processing = Processing()

    def average_test(self):
        processing = Processing()

        assert processing.average(5, 10, 15) == 10 and not 30

    def tearDown(self):
        pass
