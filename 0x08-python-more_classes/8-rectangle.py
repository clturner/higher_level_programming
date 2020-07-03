#!/usr/bin/python3
class Rectangle:
    number_of_instances = 0
    print_symbol = '#'
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value


    def __str__(self):
        if self.__width is 0 or self.height is 0:
            return 0
        else:
            for i in range(self.__height):
                for j in range(self.__height -1):
                   print(self.print_symbol * self.width)
                return(self.print_symbol * self.width)

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
                return 2 * (self.__width + self.__height)

    def __repr__(self):
        return('Rectangle({}, {})'.format(self.width, self.height))

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
        return

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2
"""
        area1 = area(rect_1)
        area2 = area(rect_2)
        if area1 > area2:
            return rect_1
        elif area1 < area2:
            return rect_2
        else:
            return rect_1
"""
