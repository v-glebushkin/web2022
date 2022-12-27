import math
radius = None

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
        self.__class__.all.append(self)
        super().__init__(x, y)

    def area(self): # вычисление площади круга
        return self.radius * self.radius * math.pi

    @staticmethod
    def total_area(): # сумма площадей всех кругов
        total = 0
        for c in Circle.all:
            total = total + c.area()
        return total

    #def __new__(cls):

# Реализовать: Rectangle
# Подумать: От чего лучше наследовать

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

circle1 = Circle(5, 10, 10)
circle1.radius = 5
circle2 = Circle()
circle1.move(3, 4)

print(circle1.radius, circle2.radius)
print(circle1.area(), circle2.area())
print(Circle.area(circle1))
print(Circle.pi)
print(circle1.__class__) # от какого класса создан
print(Circle.total_area())

print(circle1.x, circle1.y)
print(circle2.x, circle2.y)

square = Square(10)
rect = Rectangle(10, 20)
square.move(2, 3)
print(square.x, square.y)
print(square.area())


class P:
    z = 'Hello'
    def set_p(self):
        self.x = 'class P'
    def print_p(self):
        print(self.x)

class C(P):
    def set_c(self):
        self.x = 'class C'
    def print_c(self):
        print(self.x)

c = C()
c.set_p()
c.print_p()
c.print_c()
c.set_c()
c.print_c()
c.print_p()

print(c.z, C.z, P.z)
C.z = 'Hi'
print(c.z, C.z, P.z)
c.z = 'Ciao'
print(c.z, C.z, P.z)



class Mine:
    def __init__(self):
        self.x = 2
        self.__y = 3

    def get_y(self):
        print(self.__y)

    def set_y(self, y):
        if not isinstance(y, int):
            raise AttributeError
        self.__y = y


class Temperature:
    def __init__(self):
        self.__temp_fahr = 0

    @property
    def temp(self):
        return (self.__temp_fahr - 32) * 5 / 9

    @temp.setter
    def temp(self, new_temp):
        self.__temp_fahr = new_temp * 9 /5 + 32

m = Mine()
#print(m.x)
#m.get_y()
m.set_y(10)
#m.get_y()


t = Temperature()
#print(t.__temp_fahr)
print(t.temp)
t.temp = 34
#print(t.__temp_fahr)
print(t.temp)