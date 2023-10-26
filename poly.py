class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("road")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sea")

class Plane(Vehicle):
  def move(self):
    print("Air")

car1 = Car("audi", "A6")
boat1 = Boat("cruise", "adventure")
plane1 = Plane("air india", "747")

for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()