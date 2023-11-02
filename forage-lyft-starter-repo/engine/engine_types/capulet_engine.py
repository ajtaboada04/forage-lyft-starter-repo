# from abc import ABC

# from car import Car


# class CapuletEngine(Car, ABC):
#     def __init__(self, last_service_date, current_mileage, last_service_mileage):
#         super().__init__(last_service_date)
#         self.current_mileage = current_mileage
#         self.last_service_mileage = last_service_mileage

#     def engine_should_be_serviced(self):
#         return self.current_mileage - self.last_service_mileage > 30000

from engine.engine import Engine

class CapuletEngine(Engine):
    def __init__(self, current_milage, last_service_milage):
        self.current_milage = current_milage
        self.last_service_milage = last_service_milage
        self.service_interval = 30000 # the capulet engine needs service every 30,000 miles
        
    def needs_service(self):
        return self.current_milage - self.last_service_milage > self.service_interval
        