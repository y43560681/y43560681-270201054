import math


class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def get_radius(self):
        return self.radius


    def set_radius(self, radius):
        if radius > 0:
            self.radius = radius

    def get_height(self):
        return self.height

    def set_height(self, height):
        if height > 0:
            self.height = height

    def cylinder_area(self):
        base_area = math.pi * (self.radius ** 2)
        surface_area = 2 * math.pi * self.radius * self.height
        return (2 * base_area) + surface_area

    def cylinder_volume(self):
        return math.pi * (self.radius ** 2) * self.height


n = Cylinder(3, 4)

print("Area : ", n.cylinder_area())
print("Volume : ", n.cylinder_volume())