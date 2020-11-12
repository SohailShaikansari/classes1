# 1. classes
# class is a blue_print for creating new objects.
# An object is an instance of a class.
# class : Human
# objects : John , Mary , Jack


# 2.Creating classes
# class MyPoint  ---> Pascal naming concvention
'''
class Point:
    def draw(self):
        print("draw")


point = Point()
print(type(point))
print(isinstance(point, Point))
print(isinstance(point, int))
'''


# 3. Constructor ---> magic method
'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
print(point.x)
point.draw()
'''

# 4. Class vs Instance attributes


'''

class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


Point.default_color = "yellow"
point = Point(1, 2)
print(point.default_color)
print(Point.default_color)
point.draw()
point.z = 10

another = Point(3, 4)
print(another.default_color)
another.draw()

print(point.x)
point.draw()

'''

# 5. class vs Instance Methods
#  @class method --> define a method at class level

'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Point {(self.x) , (self.y)}")


point = Point(0, 0)
point.draw()
point = Point.zero()
point.draw()
'''


# 6. Magic methods
# using the str function we can get the same result as a
# point object
'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point ({self.x} , {self.y})"  # we can use return

    def draw(self):
        print(f"Point ({self.x} , {self.y}")


point = Point(1, 2)
print(str(point))
'''

# 7. Comparing Objects

'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#    def __eq__(self, other):
#        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y


point = Point(10, 20)
other = Point(1, 2)
# print(point == other)
print(point > other)
'''

# 8. Performing Arithmetic Operations
'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


point = Point(1, 2)
other = Point(10, 20)
combined = point + other
print(combined.x)
'''

# 9. Making Custom containers

'''
class TagCloud:
    def __init__(self):
        self.tags = {}  # Initializing tags attribute to an empty dictionary

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        return iter(self.tags)


cloud = TagCloud()
# we can only read we cannot set any value to implement we use the below magic method after getitem
cloud["python"] = 10
len(cloud)
cloud.add("Python")
cloud.add("python")
cloud.add("python")
print(cloud.tags)
'''

# 10. Private Members


class TagCloud:
    def __init__(self):
        self.__tags = {}  # Initializing tags attribute to an empty dictionary

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


'''
cloud = TagCloud()
print(cloud.__tags)
cloud.add("Python")
cloud.add("python")
cloud.add("python")
print(cloud.__tags["PYTHON"])
'''
cloud = TagCloud()
print(cloud.__dict__)
print(cloud._TagCloud__tags)
