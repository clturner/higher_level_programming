#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):

    def __init__(self, size):
        name = "size"
        if super().integer_validator(name, size):
            width = size
            height = size
            Rectangle.__init__(self, width, height)
            self.__width = size
            self.__height = size

    def area(self):
        return(self.__width * self.__height)
