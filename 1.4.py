class Point:
    "Класс для представления координат точек на плоскости"
    x = 1
    y = 1

pt = Point()
Point.x = 100
print( id(pt), id(Point), sep="\n" )


class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

pt1 = Point3D(0,0,0)
print(pt1.__dict__)
delattr(pt1, 'z')
print(pt1.z)