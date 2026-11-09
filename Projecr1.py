class Vehicle:
    def __init__(self,brand,max_speed):
        self.brand = brand
        self.max_speed = max_speed
    def show_detalis(self):
        print("Brand: ",self.brand)
        print("Max Speed: ",self.max_speed, 'km/h')
    
class Car(Vehicle):
    def __init__(self,brand,max_speed,seats,model):
        self.seats = seats
        self.model = model
        super().__init__(brand,max_speed)
    def show_detalis(self):
        print("Seats: ", self.seats)
        print("Model: ", self.model)
        super().show_detalis()
    def fuel_type(self,fuel):
        self.fuel = fuel
        print(self.model,"uses",fuel)
car = Car("BMW", 150,5,"3 Series")

car.show_detalis()
car.fuel_type("petrol")

print("Is Car child class of Vehicle? :", issubclass(Car,Vehicle))