from math import hypot
class Vector2:

    __slots__ = ['__x', '__y']


    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y 
    
    def getstr(self):
        return f"X {self.__x} Y {self.__y}"
    
    def get(self, type = None):
        a = {'x': self.__x, 'y': self.__y}
        if not type:
            return self.__x, self.__y
        elif type not in ['x', 'y']:
            return None
        else:
            return a[type]
    
    def zero(self):
        self.__x, self.__y = 0, 0
    
    def update(self, x=0,y=0):
        self.__x += Vector2.__isint(x)
        self.__y += Vector2.__isint(y)


    @staticmethod
    def __isint(value):
        if isinstance(value, int):
            return value 
        else:
            raise TypeError("Must be int", value)

    def normalized(self):
        x, y = 0, 0
        if self.__x < 0:
            x = -1
        elif self.__x == 0:
           x = 0
        else:
            x = 1 

        if self.__y < 0:
            y = -1
        elif self.__y == 0:
            y = 0
        else:
            y = 1
        return x, y 
    
    def distance_to(self, vector):
        if not isinstance(vector, Vector2):
            raise ValueError("Must be Vector2")
        else:
            return hypot(self.__x - vector.__x, self.__y - vector.__y)

    

