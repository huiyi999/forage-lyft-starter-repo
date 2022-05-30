from datetime import datetime

from engine.capulet_engine import CapuletEngine
from battert.spindler_battery import SpindlerBattery
from car import Car


class Calliope(Car):
    def __init__(self, last_service_date, current_date, current_mileage, last_service_mileage):
        self._engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        self._battery = SpindlerBattery(last_service_date, current_date)

    def needs_services(self) -> bool:
        return self._engine.needs_service() or self._battery.needs_service()
