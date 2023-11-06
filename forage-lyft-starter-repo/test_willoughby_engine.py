import unittest
from engine.engine_types.willoughby_engine import WilloughbyEngine

class TestWilloughbyEngine(unittest.TestCase):

    def test_needs_service_true(self):
        # Create an instance where the engine needs service (mileage difference > 60000)
        engine = WilloughbyEngine(current_milage=120000, last_service_milage=59000)
        self.assertTrue(engine.needs_service(), "Engine should need service when mileage is over the service interval")

    def test_needs_service_false(self):
        # Create an instance where the engine does not need service (mileage difference <= 60000)
        engine = WilloughbyEngine(current_milage=100000, last_service_milage=50000)
        self.assertFalse(engine.needs_service(), "Engine should not need service when mileage is within the service interval")

# This allows the test to be run from the command line
if __name__ == '__main__':
    unittest.main()
