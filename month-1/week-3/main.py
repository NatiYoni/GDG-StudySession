from car import Car
from bike import Bike

def vehicle_info(vehicle):
    print(Vehicle.describe())

car = Car("Toyota", "Corolla", 4)
bike = Bike("Yamaha", "MT-07", "Sport")

vehicle_info(car)
vehicle_info(bike)
