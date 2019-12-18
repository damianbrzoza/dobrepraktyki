"""
Comment for file
"""

from abc import ABC, abstractmethod


class AbstractListClass(ABC):
    def __init__(self):
        """
        Abstract List Class
        """
        self.lst = []
        print("INIT")
        
    def add_to_list(self, element: int ):
        self.lst.append(element)

    @abstractmethod
    def print_list(self):
        raise NotImplementedError


class ListClassNumbers(AbstractListClass):
    def __init__(self):
        """
        ListClassNumbers, list with numbers
        """
        super().__init__()
        print("INIT2")

    def print_list(self):
        for i in range(len(self.lst)):
            print(self.lst[i])


class ListClassString(AbstractListClass):
    def __init__(self):
        """
        ListClassString, list with strings
        """
        super().__init__()
        print("INIT2")

    def print_list(self):
        print(", ".join(self.lst))


class Point:
    def __init__(self, x: float, y: float, z: float):
        """
        Point, class for store point coordinates
        """
        self.x = x
        self.y = y
        self.z = z


class Cube:
    def __init__(self, point_a: Point, point_b: Point, point_c: Point, point_d: Point):
        """
        Cube, class for store vertices of cube
        """
        self.point_a = point_a
        self.point_b = point_b
        self.point_c = point_c
        self.point_d = point_d

    def sum_of_points(self):
        return (self.point_a.x + self.point_a.y + self.point_a.z) ** 2 \
               + (self.point_b.x + self.point_b.y + self.point_b.z) ** 2 \
               + (self.point_c.x + self.point_c.y + self.point_c.z) ** 2 \
               + (self.point_d.x + self.point_d.y + self.point_d.z) ** 2


if __name__ == '__main__':
    numbers = ListClassNumbers()
    strings = ListClassString()

    numbers.add_to_list(4)
    numbers.add_to_list(5)
    numbers.add_to_list(2)
    numbers.add_to_list(10)
    numbers.add_to_list(30)

    strings.add_to_list('a')
    strings.add_to_list(" ala ma kota")
    strings.add_to_list('kolejny Element')
    strings.add_to_list('wez')
    strings.add_to_list('to popraw')

    numbers.print_list()
    strings.print_list()

    cube = Cube(Point(1, 2, 3), Point(2, 2, 2), Point(3, 3, 3), Point(2, 3, 1))

    print(cube.sum_of_points())
