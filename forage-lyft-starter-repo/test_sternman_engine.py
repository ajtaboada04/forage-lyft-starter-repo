import unittest
from engine.engine_types.sternman_engine import SternmanEngine

class TestSternmanEngine(unittest.TestCase):

    def test_needs_service_true(self):
        # Test that the engine needs service when the warning light is on (True)
        engine = SternmanEngine(warning_light_is_on=True)
        self.assertTrue(engine.needs_service(), "Engine should need service when the warning light is on")

    def test_needs_service_false(self):
        # Test that the engine does not need service when the warning light is off (False)
        engine = SternmanEngine(warning_light_is_on=False)
        self.assertFalse(engine.needs_service(), "Engine should not need service when the warning light is off")

if __name__ == '__main__':
    unittest.main()
