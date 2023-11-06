from tire.tire import Tires

class CarriganTires(Tires):
    def __init__(self, wear_array):
        self.wear_array = wear_array
    
    def needs_service(self):
        for tire_wear_level in self.wear_array:
            if tire_wear_level >= 0.9:
                return True
        return False
        