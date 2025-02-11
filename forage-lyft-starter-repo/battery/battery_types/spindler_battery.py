from datetime import date
from dateutil.relativedelta import relativedelta
from battery.battery import Battery

class SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.service_interval_years = 3 # changed form 2 to 3 because of upgrade

    def needs_service(self):
        service_threshold_date = self.last_service_date + relativedelta(years=self.service_interval_years)
        return self.current_date > service_threshold_date
