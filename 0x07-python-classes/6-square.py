#!/usr/bin/python3
class Square:

    def __init__(self, size=0, position=(0, 0)):
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    def area(self):
        return (self.size) * (self.size)

    def my_print(self):
        if self.size == 0:
            print("")
        else:
            for y in range(self.position[1]):
                print(" ")
            for i in range(self.size):
                for x in range(self.position[0]):
                    print(" ", end="")
                for j in range(self.size):
                    print("#", end="")
                print("")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is tuple and isinstance(value, int):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value > 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
