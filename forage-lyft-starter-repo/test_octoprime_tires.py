import unittest
from tire.tire_types.octoprime_tires import OctoPrimeTires

class TestOctoPrimeTires(unittest.TestCase):

    def test_needs_service_true(self):
        # Sum of wear levels is 3.0 or more, service needed
        tires = OctoPrimeTires([1.0, 1.0, 1.0, 0.1])
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        # Sum of wear levels is less than 3.0, no service needed
        tires = OctoPrimeTires([0.5, 0.5, 0.5, 0.5])
        self.assertFalse(tires.needs_service())

# This allows the test to be run from the command line
if __name__ == '__main__':
    unittest.main()
