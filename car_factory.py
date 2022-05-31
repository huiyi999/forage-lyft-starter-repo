"""
Created on 2022-05-30
@author: chy
"""
import datetime
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class CarFactory():
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage,
                 warning_light_is_on=False):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_date = last_service_date
        self.warning_light_is_on = warning_light_is_on
        self.last_service_mileage = last_service_mileage

    def create_calliope(self):
        engine = CapuletEngine(current_mileage=self.current_mileage, last_service_mileage=self.last_service_mileage)
        battery = SpindlerBattery(current_date=self.current_date, last_service_date=self.last_service_date)
        car = Car(engine, battery)
        return car

    def create_glissade(self):
        engine = WilloughbyEngine(current_mileage=self.current_mileage, last_service_mileage=self.last_service_mileage)
        battery = SpindlerBattery(current_date=self.current_date, last_service_date=self.last_service_date)
        car = Car(engine, battery)
        return car

    def create_palindrome(self):
        engine = SternmanEngine(warning_light_is_on=self.warning_light_is_on)
        battery = SpindlerBattery(current_date=self.current_date, last_service_date=self.last_service_date)
        car = Car(engine, battery)
        return car

    def create_rorschach(self):
        engine = WilloughbyEngine(current_mileage=self.current_mileage, last_service_mileage=self.last_service_mileage)
        battery = NubbinBattery(current_date=self.current_date, last_service_date=self.last_service_date)
        car = Car(engine, battery)
        return car

    def create_thovex(self):
        engine = CapuletEngine(current_mileage=self.current_mileage, last_service_mileage=self.last_service_mileage)
        battery = NubbinBattery(current_date=self.current_date, last_service_date=self.last_service_date)
        car = Car(engine, battery)
        return car
