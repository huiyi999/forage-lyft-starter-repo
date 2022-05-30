"""
Created on 2022-05-30
@author: chy
"""

from battery.battery import Battery
from datetime import date
from utils import calculate_threshold_date


class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        service_threshold_date = calculate_threshold_date(self.last_service_date, 2)
        return service_threshold_date < self._current_date
