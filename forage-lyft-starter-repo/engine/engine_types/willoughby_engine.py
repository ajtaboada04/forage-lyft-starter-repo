# from abc import ABC

# from car import Car


# class WilloughbyEngine(Car, ABC):
#     def __init__(self, last_service_date, current_mileage, last_service_mileage):
#         super().__init__(last_service_date)
#         self.current_mileage = current_mileage
#         self.last_service_mileage = last_service_mileage

#     def engine_should_be_serviced(self):
#         return self.current_mileage - self.last_service_mileage > 60000

from engine.engine import Engine

class WilloughbyEngine(Engine):
    def __init__(self, current_milage, last_service_milage):
        self.current_milage = current_milage
        self.last_service_milage = last_service_milage
        self.service_interval = 60000 # the willoughby engine needs service every 60,000 miles
        
    def needs_service(self):
        return self.current_milage - self.last_service_milage > self.service_interval