import unittest
from datetime import date
from battery.battery_types.spindler_battery import SpindlerBattery

class TestNubbinBattery(unittest.TestCase):

    def test_needs_service_true(self):
        # The battery was last serviced more than 3 years ago
        current_date = date.today()
        last_service_date = current_date.replace(year=current_date.year - 4)
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service(), "Battery should need service as it's been over 2 years since last service")

    def test_needs_service_false(self):
        # The battery was serviced less than 3 years ago
        current_date = date.today()
        last_service_date = current_date.replace(year=current_date.year - 1)
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service(), "Battery should not need service as it's been less than 2 years since last service")


if __name__ == '__main__':
    unittest.main()
