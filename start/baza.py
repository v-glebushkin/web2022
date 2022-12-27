import math

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y

class Circle(Shape):
    pi = math.pi
    all = []

    def circle(self):
        pass

    def __init__(self, radius = 1, x = 0, y = 0): # инициализация радиусов и сбор всех экземпляров
        self.radius = radius
        self.__class__.all.append(self) # добавляем каждый новый экземпляр в список all
        super().__init__(x, y)

    def area(self): # вычисление площади круга
        return self.radius * self.radius * math.pi

    @staticmethod
    def total_area(): # сумма площадей всех кругов
        total = 0
        for c in Circle.all:
            total = total + c.area()
        return total

class Rectangle(Shape):
    def __init__(self, a, b, x = 0, y = 0):
        self.a = a
        self.b = b
        super().__init__(x, y)

    def area(self):
        return self.a * self.b

class Square(Rectangle):
    def __init__(self, a, x = 0, y = 0):
        Rectangle.__init__(self, a, a, x, y)

c1 = Circle()
print(c1.radius, c1.x, c1.y)

c2 = Circle(2, 1, 1)
print(c2.radius, c2.x, c2.y)

c2.move(2, 2)
print(c2.radius, c2.x, c2.y)

print(Circle.all)
print(Circle.total_area(), c2.total_area())