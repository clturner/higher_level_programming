#!/usr/bin/python3
class MyList(list):
    def print_sorted(self):
        new_list = MyList()
        for i in self:
            new_list.append(i)
            new_list.sort()
        print(new_list)
