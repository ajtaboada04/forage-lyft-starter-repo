import unittest
from engine.engine_types.capulet_engine import CapuletEngine

class TestCapuletEngine(unittest.TestCase):

    def test_needs_service_true(self):
        # Test that the engine needs service when the current mileage is over the limit since last service
        engine = CapuletEngine(current_milage=100000, last_service_milage=69999)
        self.assertTrue(engine.needs_service(), "Engine should need service when the mileage is over the service interval")

    def test_needs_service_false(self):
        # Test that the engine does not need service when the current mileage is within the limit since last service
        engine = CapuletEngine(current_milage=50000, last_service_milage=30000)
        self.assertFalse(engine.needs_service(), "Engine should not need service when the mileage is within the service interval")

if __name__ == '__main__':
    unittest.main()
