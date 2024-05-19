# SINGALE IN HERITANCE IN PYTHON
class Vahicale:
    def __init__(self, cost, milage):
        self.cost = cost
        self.milage = milage
    def show_vahicale_details(self):
        print("Cost Of Vahicale", self.cost)
        print("Milage Of Vahiclae", self.milage)
        print("I am a vahicale")
v1 = Vahicale(250000, 5000)
v1.show_vahicale_details()
print()
class Car(Vahicale):
    def show_car_details(self):
        print("this is a car")
v1 = Car(7860, 5555)
print(v1.show_car_details())

print()

class Car(Vahicale):
    def __init__(self, cost, milage, tyers, hp):
        super().__init__(cost, milage)
        self.tyers = tyers
        self.hp = hp
    def show_car_details(self):
        print("Numbers of tyers In car", self.tyers)
        print("Houres power of the car", self.hp)
        print("i am a car")
v1 = Car(780000, 200, 12, 450)
v1.show_vahicale_details()
v1.show_car_details()
# CONSTRUCTION IN SINGLE INHERITANCE IN PYRHON
print()
class Father:
    def __init__(self):
        self.money = 1000
        print("Father Class Construction")
    def show(self):
        print("Father Class Instance Method")
    
class Son(Father):
    def disp(self):
        print("Son Class Instance Method")
h = Son()
print(h.money)
h.show()
h.disp()
