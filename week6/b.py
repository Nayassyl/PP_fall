class circles():
    def __init__(self, centr = Point(0,0), radius = 0):
        self.__centr = centr
        self.__radius = radius
    def get_centre(self):
        return self.__centr
    def set_centre(self):
        self.__centr = centr
    def get_radius(self):
        return self.__radius
    def set_radius(self,radius):
        self.__radius = radius
    def get_area(self):
        return (math.pi)*(self.__radius**2)
    def get_length(self):
        return 2*(math.pi)*(self.__radius)
    def intersection(self,new):
        if point.distance(self.__centr,new.__centr)>self.__radius+new.__radius:
            return "doesnt lie"
        elif point.distance(self.__centr,new.__centr)<self.__radius+new.__radius:
            return "intersect"
        else:
            return "one in one"
point  = circles(Point(1,2),3)
point2 = circles(Point(2,4),3)
a = circles()
a.intersection(point,point2)