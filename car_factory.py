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
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire


class CarFactory():

    @classmethod
    def create_calliope(self, current_mileage, last_service_mileage, current_date, last_service_date, tire_wear):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date=current_date, last_service_date=last_service_date)
        tire = CarriganTire(tire_wear)
        car = Car(engine, battery, tire)
        return car

    @classmethod
    def create_glissade(self, current_mileage, last_service_mileage, current_date, last_service_date, tire_wear):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tire = CarriganTire(tire_wear)
        car = Car(engine, battery, tire)
        return car

    @classmethod
    def create_palindrome(self, warning_light_is_on, current_date, last_service_date, tire_wear):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(current_date, last_service_date)
        tire = OctoprimeTire(tire_wear)
        car = Car(engine, battery, tire)
        return car

    @classmethod
    def create_rorschach(self, current_mileage, last_service_mileage, current_date, last_service_date, tire_wear):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tire = OctoprimeTire(tire_wear)
        car = Car(engine, battery, tire)
        return car

    @classmethod
    def create_thovex(self, current_mileage, last_service_mileage, current_date, last_service_date, tire_wear):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tire = OctoprimeTire(tire_wear)
        car = Car(engine, battery, tire)
        return car
