# Assignment part-1 
# class Circle():
#     def __init__(self, r):
#         self.radius = r

#     def area(self):
#         return self.radius**2*3.14
    
#     def perimeter(self):
#         return 2*self.radius*3.14

# NewCircle = Circle(10)
# print(NewCircle.area())
# print(NewCircle.perimeter())

# Assignment part-2

# class IOString():
#     def __init__(self):
#         self.str1 = ""

#     def get_String(self):
#         self.str1 = input()

#     def print_String(self):
#         print(self.str1.upper())

# str1 = IOString()
# str1.get_String()
# str1.print_String()

# Assignment part-3

class py_solution:
    def reverse_words(self, s):
        return ' '.join(reversed(s.split()))


print(py_solution().reverse_words('hello .py'))






