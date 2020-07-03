#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    def __init__(self, width, height):
        name = "width"
        if super().integer_validator(name, width):
            self.__width = width
            name = "height"
        if super().integer_validator(name, height):
            self.__height = height

    def __str__(self):
        return("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        return(self.__width * self.__height)