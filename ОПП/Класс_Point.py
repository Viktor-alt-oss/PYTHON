class Point:
    def set_coordinates(self, x, y):
        setattr(self, 'x', x)
        setattr(self, 'y', y)

    def get_distance_to_origin(self):
        if not hasattr(self, 'x') or not hasattr(self, 'y'):
            return None
        return (self.x**2 + self.y**2)**(1/2)
        
    def display(self):
        if not hasattr(self, 'x') or not hasattr(self, 'y'):
            print('Координаты не заданы')
        else:
            print(f'Point({self.x},{self.y})')
    
p1 = Point()
p1.set_coordinates(6, 8)
p1.display()
print(p1.get_distance_to_origin())

p2 = Point()
p2.display()
p2.set_coordinates(3, 4)
p2.display()
print(p2.get_distance_to_origin())

p3 = Point()
p3.display()
print(p3.get_distance_to_origin())
p3.x = 4
p3.display()
print(p3.get_distance_to_origin())
p3.y = 3
p3.display()
print(p3.get_distance_to_origin())