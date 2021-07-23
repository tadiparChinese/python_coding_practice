# If, for some reasons, you need to call a regular class method as a static method 
# (in other words, you do not have an object to pass to "self"), 
# use the @classmethod decorator to ask Python to generate correct arguments when calling the method. 
# Python will substitute the class type to "self". 
# And for the oppisite case, use @staticmethod to omit the "self" parameter, 
# which makes able to call a method on a class instead of an object. Be careful and 
# think about the "self" value in this case if you use such approach.

class Class:

    @classmethod
    def class_meth(self, param):
        # method with self
        print('1' + param)

    @staticmethod
    def static_meth(param):
        # method without self
        print('2' + param)

obj = Class()
#case1
obj.class_meth('HI') # ok
Class.static_meth('Yo') # ok

# but what if vise versa?
# we need decorators
Class.class_meth('HI') #@classnethod
obj.static_meth('Yo') #@staticmethod
