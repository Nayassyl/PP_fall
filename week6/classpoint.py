import math


class Point:
    def __init__(self, xCoord=0, yCoord=0):
        self.__xCoord = xCoord
        self.__yCoord = yCoord

    def get_xCoord(self):
        return self.__xCoord
    # set x coordinate

    def set_xCoord(self, xCoord):
        self.__xCoord = xCoord
    # get y coordinate

    def get_yCoord(self):
        return self.__yCoord
    # set y coordinate

    def set_yCoord(self, yCoord):
        self.__yCoord = yCoord
    # get current position

    def get_position(self):
        return self.__xCoord, self.__yCoord
    # change x & y coordinates by p & q

    def move(self, p, q):
        self.__xCoord += p
        self.__yCoord += q

    # overload + operator
    def __add__(self, point_ov):
        return Point(self.__xCoord + point_ov.__xCoord, self.__yCoord + point_ov.__yCoord)
    # overload - operator

    def __sub__(self, point_ov):
        return Point(self.__xCoord - point_ov.__xCoord, self.__yCoord - point_ov.__yCoord)
    # overload * operator

    def __mul__(self, point_ov):
        return Point(self.__xCoord * point_ov.__xCoord, self.__yCoord * point_ov.__yCoord)
    # overload / operator

    def __div__(self, point_ov):
        return Point(self.__xCoord / point_ov.__xCoord, self.__yCoord / point_ov.__yCoord)
    # overload less than by x

    def __it__(self, point_ov):
        return Point(self.__xCoord < point_ov.__xCoord)

    def dist(self, point_ov):
        return math.sqrt((point_ov.__xCoord - self.__xCoord) ** 2 + (point_ov.__yCoord - self.__yCoord) ** 2)
    # printing

    def __str__(self):
        return f'The coordinates are: {self.__xCoord, self.__yCoord}'


class circle():
    def __init__(self, center = Point(0, 0), radius = 0):
        self.__center = center
        self.__radius = radius

    def get_center(self):
        return self.__center

    def set_center(self, new_center):
        self.__center.__xCoord = new_center.__xCoord
        self.__center.__yCoord = new_center.__yCoord

    def get_rad(self):
        return self.__radius

    def set_rad(self, new_rad):
        self.__radius = new_rad

    def area(self):
        return math.pi * self.__radius ** 2

    def lenn(self):
        return 2 * math.pi * self.__radius

    def intersection(self, circ2):
        if self.__center.dist(circ2.__center) <= (self.__radius - circ2.__radius):
            return 'Second circle lie in First circle'
        if self.__center.dist(circ2.__center) <= (circ2.__radius - self.__radius):
            return 'First circle lie in Second circle'
        if self.__center.dist(circ2.__center) < (self.__radius + circ2.__radius):
            return "They're intersect"
        if (self.__radius + circ2.__radius) < (self.__center.dist(circ2.__center)):
            return "They're not intersect"
        if (self.__radius + circ2.__radius) == (self.__center.dist(circ2.__center)):
            return "They're intersect tangentically"


class triangle():
    def __init__(self, f=Point(0, 0), s=Point(0, 0), t=Point(0, 0)):
        self.__f = f
        self.__s = s
        self.__t = t
        self.a = self.__f.dist(self.__s)
        self.b = self.__f.dist(self.__t)
        self.c = self.__s.dist(self.__t)
        self.angle_a_b = math.degrees(
            math.acos((self.a**2 + self.b**2 - self.c**2) / (2 * self.a * self.b)))
        self.angle_a_c = math.degrees(
            math.acos((self.a**2 + self.c**2 - self.b**2) / (2 * self.a * self.c)))
        self.angle_b_c = 180 - (self.angle_a_b + self.angle_a_c)
    
    def perimeter(self):
        return self.__f.dist(self.__s) + self.__f.dist(self.__t) + self.__s.dist(self.__t)

    def angles(self):
        return( """
first angle: %0.2f
second angle: %0.2f
third angle: %0.2f""" % (self.angle_a_b, self.angle_a_c, self.angle_b_c))

    def area(self):
        area = (self.a * self.b * math.sin(math.radians(self.angle_a_b))) / 2
        print('Area:%0.2f' % (area))
    
    def tr_type(self):
        if self.a == self.b and self.b == self.c:
            return'equilateral'
        if self.a == self.b or self.b == self.c or self.a == self.c:
            return 'isosceles'
        else: return 'scalene'
    
    def is_right(self):
        if round(self.angle_a_b) == 90 or round(self.angle_a_c) == 90 or round(self.angle_b_c) == 90:
            return True
        return False





# tr1 = triangle(Point(0, 3), Point(4, 0), Point(0, 0))
# print(tr1.tr_type())
# print(tr1.angles())
# print(tr1.is_right())


# xpos1, ypos1 = [int(i) for i in input("Enter the x and y coordinates of center of first circle in form (x y):").split()]
# rad1 = int(input("Enter the radius of first circle:"))
# xpos2, ypos2 = [int(i) for i in input("Enter the x and y coordinates of center of second circle in form (x y):").split()]
# rad2 = int(input("Enter the radius of second circle:"))

# center1 = Point(xpos1, ypos1)
# center2 = Point(xpos2, ypos2)

# circ1 = circle(center1, rad1)
# circ2 = circle(center2, rad2)

# print(circ1.intersection(circ2))
