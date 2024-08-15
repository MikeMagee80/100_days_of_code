
# # Classes   blueprints for creating new objects
# # Objects instances of a class

# # Use Pascal naming convention

# class Point:
#     def draw(self):
#         print("draw")


# point = Point()
# print(type(point))  # <class '__main__.Point'>
# print(isinstance(point, Point))  # True



#-----------------

# Constructors

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
        
#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")

# point = Point(1, 2)
# point.draw()  # Point (1, 2)


#-----------------



# class Point:
#     default_color = "red"

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
        
#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")

# point = Point(1, 2)
# print(point.default_color)
# print(Point.default_color)
# point.draw() 

# another = Point(3, 4)
# another.draw()


#-------------------

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     @classmethod    
#     def zero(cls):    #cls is short for class
#         return cls(0, 0)  # same as Point(0, 0)

#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")


# point = Point.zero()
# point.draw() 

#---------------------

# Magic Methods  __something__  "A guide to Python's magic methods"

# class Point:

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return f"({self.x}, {self.y})"    


#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")

# point = Point(1, 2)
# print(point)


#-----------------------

# Comparison magic methods

# class Point:

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y
    
#     def __gt__(self, other):
#         return self.x > other.x and self.y > other.y


# point = Point(10, 20)
# other = Point(1, 2)
# print(point > other)


#--------------------

# arithmetic operations


# class Point:

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)

# point = Point(10, 20)
# other = Point(1, 2)
# combined = point + other
# print(combined.x)


#--------------------


# class TagCloud:
#     def __init__(self):
#         self.tags = {}  # empty dictionary

#     def add(self, tag):
#         self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

#     def __getitem__(self, tag):
#         return self.tags.get(tag.lower(), 0)
    
#     def __setitem__(self, tag, count):
#         self.tags[tag.lower()] = count

#     def __len__(self):
#         return len(self.tags)

#     def __iter__(self):
#         return iter(self.tags)

# cloud = TagCloud()
# cloud["python"] = 10
# len(cloud)
# cloud.add("Python")
# cloud.add("python")
# cloud.add("python")
# print(cloud.tags)  # {'python': 3}


#---------------------------

#  Private Members

# class TagCloud:
#     def __init__(self):
#         self.__tags = {}  # empty dictionary

#     def add(self, tag):
#         self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

#     def __getitem__(self, tag):
#         return self.__tags.get(tag.lower(), 0)
    
#     def __setitem__(self, tag, count):
#         self.__tags[tag.lower()] = count

#     def __len__(self):
#         return len(self.__tags)

#     def __iter__(self):
#         return iter(self.__tags)

# cloud = TagCloud()
# print(cloud._TagCloud__tags)

#-------------------

# Properties

# class Product:
#     def __init__(self, price):
#         self.price = price

#     @property
#     def price(self):
#         return self.__price
    
#     @price.setter
#     def price(self, value):
#         if value < 0:
#             raise ValueError("Price can't be negative.")
#         self.__price = value


# product = Product(10)

# print(product.price)



#------------------

# Inheritance

class Animal:


class Mammal:
    def eat(self):
        print("eat")

    def walk(self):
        print("walk")

class Fish:
    def eat(self):
        print("eat")
