
class Vehicle:
    vehicle_name = "Mercedes"
    mileage = 50
    capacity = 34
    price = 123000  

    def __init__(self,vehicle_name,mileage,capacity,price):
        self.vehicle_name = vehicle_name
        self.mileage = mileage
        self.capacity = capacity
        self.price = price

class SubVehicle(Vehicle):
    engine = "SI-Engine"
    chasis_no = 28.457

    def __init__(self,vehicle_name, mileage,capacity,price, engine, chasis_no):
        super().__init__(vehicle_name,mileage,capacity,price) ## must call MRO(method resolving order "left to right") mthod. 
        self.engine = engine
        self.chasis_no = chasis_no

childObj = SubVehicle("shwift",30,1000,"10lakhs","xyzenginee",658775767)
print("vehicle_name:",childObj.vehicle_name)
print("vehicle_mileage:",childObj.mileage)
print("vehicle_capacity:",childObj.capacity)
print("vehicle_price:",childObj.price)
print("vehicle_enginee:",childObj.engine)
print("vehicle_chasis_no:",childObj.chasis_no)