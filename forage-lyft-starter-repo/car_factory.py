from serviceable import Serviceable
from car import Car

from engine.engine import Engine
from battery.battery import Battery
from tire.tire import Tires

from engine.engine_types.capulet_engine import CapuletEngine
from engine.engine_types.sternman_engine import SternmanEngine
from engine.engine_types.willoughby_engine import WilloughbyEngine

from battery.battery_types.nubbin_battery import NubbinBattery
from battery.battery_types.spindler_battery import SpindlerBattery

from tire.tire_types.carrigan_tires import CarriganTires
from tire.tire_types.octoprime_tires import OctoPrimeTires

class CarFactory:
    
    @staticmethod
    def create_calliope(current_date, last_service_date, current_milage, last_service_milage, wear_array):
        engine = CapuletEngine(current_milage, last_service_milage)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = CarriganTires(wear_array)
        car = Car(engine, battery, tires)
        return car
    
    @staticmethod
    def create_glissade(current_date, last_service_date, current_milage, last_service_milage, wear_array):
        engine = WilloughbyEngine(current_milage, last_service_milage)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = OctoPrimeTires(wear_array)
        car = Car(engine, battery, tires)
        return car

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_is_on, wear_array):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = CarriganTires(wear_array)
        car = Car(engine, battery, tires)
        return car
    
    @staticmethod
    def create_rorschach(current_date, last_service_date, current_milage, last_service_milage, wear_array):
        engine = WilloughbyEngine(current_milage, last_service_milage)
        battery = NubbinBattery(current_date, last_service_date)
        tires = OctoPrimeTires(wear_array)
        car = Car(engine, battery, tires)
        return car
    
    @staticmethod
    def create_thovex(current_date, last_service_date, current_milage, last_service_milage, wear_array):
        engine = CapuletEngine(current_milage, last_service_milage)
        battery = NubbinBattery(current_date, last_service_date)
        tires = CarriganTires(wear_array)
        car = Car(engine, battery, tires)
        return car