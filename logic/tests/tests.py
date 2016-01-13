import unittest
from logic.functions import Processing
# On test, this import function does not work. Error: ImportError: no module named 'logic'.
# It is not a module, it is a package.


class FunctionTestCase(unittest.TestCase):
    """Conducts tests for logic/functions.py"""

    def setUp(self):
        self.processing = Processing()

    def average_test(self):
        processing = Processing()

        assert processing.average(5, 10, 15) == 10

    def tearDown(self):
        pass
