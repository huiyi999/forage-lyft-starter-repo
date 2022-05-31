"""
Created on 2022-05-30
@author: chy
"""
import unittest

from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire


class TestCarriganTire(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = (0.8, 0.9, 1, 0.8)
        tire = CarriganTire(tire_wear)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        tire_wear = (0.1, 0.2, 0.3, 0.4)
        tire = CarriganTire(tire_wear)
        self.assertFalse(tire.needs_service())


class TestOctoprimeTire(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = (0.8, 0.9, 1, 0.8)
        tire = OctoprimeTire(tire_wear)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        tire_wear = (0.1, 0.2, 0.3, 0.4)
        tire = OctoprimeTire(tire_wear)
        self.assertFalse(tire.needs_service())


if __name__ == "__main__":
    unittest.main()
