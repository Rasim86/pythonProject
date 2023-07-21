class Car:
    # создаем атрибуты класса
    car_count = 0

    # создаем методы класса
    def start(self, name, make, model):
        print("Двигатель заведен")
        self.name = name
        self.make = make
        self.model = model
        Car.car_count += 1

car_a = Car()
car_a.start("Corrola", "Toyota", 2015)
print(car_a.name)
print(car_a.car_count)


car_b = Car()
car_b.start("City", "Honda", 2013)
print(car_b.name)
print(car_b.car_count)


class Car:
    def __init__(self,model,year):
        self.model = model
        self.year = year

car = Car('skoda',2008)
print(car.model, car.year)

class Car:

    @staticmethod
    def get_class_details():
        print ("Это класс Car")

Car.get_class_details()


class Point3D:
    coords: list

    def __init__(self, x, y, z):
        self.x: int = x
        self.y: int = y
        self.z: int = z
        Point3D.coords = [self.x, self.y, self.z]

    def set_coords(self, x, y, z):
        c = Point3D(x, y, z)
        return tuple(c.coords)

qwe = Point3D(1,2,3)
qw = qwe.set_coords(1,2,3)
print(qw)
print(qwe.x, qwe.z)


class Point(Point3D):
    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y, z)


def abyrvalg():
    x, y = int(input()), int(input())
    a = []
    for i in range(5):
        a.append(Point(x, y))
    return a

a = abyrvalg()
print(a)