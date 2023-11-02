from battery.battery import Battery

class SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.service_interval = 2    # the spindler battery needs service once every 2 years
        
    def needs_service(self):
        # if the current date is greater than the last service date + the service interval, return True
        if self.current_date > self.last_service_date + self.service_interval:
            return True
        else:
            return False