"""
Created on 2022-05-30
@author: chy
"""

import unittest
from datetime import date, datetime
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery


class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = datetime.today().date()
        last_service_date = date.fromisoformat("2020-01-01")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = datetime.today().date()
        last_service_date = date.fromisoformat("2021-01-01")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())


class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = datetime.today().date()
        last_service_date = date.fromisoformat("2014-01-01")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = datetime.today().date()
        last_service_date = date.fromisoformat("2020-01-01")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())


if __name__ == "__main__":
    unittest.main()
