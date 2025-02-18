from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors
    
    def describe(self):
        return f"Car: {self.make} {self.model}, Doors: {self.num_doors}"
