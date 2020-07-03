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
