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

    def get_distance(self, obj):
        if not isinstance(self, Point) or not isinstance(obj, Point):
            print('Передана не точка')
        elif not hasattr(self, ('x' and 'y')) or not hasattr(obj, ('x' and 'y')):
            print('Координаты не заданы')
            return None
        else:
            return ((self.x - obj.x)**2 + (self.y - obj.y)**2)**(1/2)

p1 = Point()
p1.set_coordinates(1, 2)
print(p1.get_distance(100))
print(p1.get_distance([1, 2, 3]))
print(p1.get_distance(Point()))