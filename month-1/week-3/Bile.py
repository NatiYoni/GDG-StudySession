from vehicle import Vehicle

class Bike(Vehicle):
    def __init__(self, make, model, bike_type):
        super().__init__(make, model)
        self.bike_type = bike_type
    
    def describe(self):
        return f"Bike: {self.make} {self.model}, Type: {self.bike_type}"
