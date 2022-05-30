from datetime import datetime

from engine.sternman_engine import SternmanEngine
from battert.spindler_battery import SpindlerBattery
from car import Car


class Palindrome(Car):
    def __init__(self, last_service_date, current_date, warning_light_is_on):
        self._engine = SternmanEngine(warning_light_is_on)
        self._battery = SpindlerBattery(last_service_date, current_date)

    def needs_services(self) -> bool:
        return self._engine.needs_service() or self._battery.needs_service()
