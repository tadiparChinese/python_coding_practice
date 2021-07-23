# If, for some reasons, you need to call a regular class method as a static method 
# (in other words, you do not have an object to pass to "self"), 
# use the @classmethod decorator to ask Python to generate correct arguments when calling the method. 
# Python will substitute the class type to "self". And for the oppisite case, 
# use @staticmethod to omit the "self" parameter, which makes able to call a method on a class instead of an object. 
# Be careful and think about the "self" value in this case if you use such approach.

a, b = 0, 1
while a < 100:
    print(a)
    a, b = b, a+b