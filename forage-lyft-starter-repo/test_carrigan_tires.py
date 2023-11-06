import unittest
from tire.tire_types.carrigan_tires import CarriganTires

class TestCarriganTires(unittest.TestCase):

    def test_needs_service_true(self):
        # Case where the service is needed: At least one tire's wear level is at or above 0.9
        tires = CarriganTires([0.9, 0.5, 0.6, 0.7])
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        # Case where the service is not needed: All tires' wear levels are below 0.9
        tires = CarriganTires([0.1, 0.2, 0.3, 0.4])
        self.assertFalse(tires.needs_service())

if __name__ == '__main__':
    unittest.main()
