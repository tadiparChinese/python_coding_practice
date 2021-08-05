class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{} {}'.format(self.first, self.last)

    @property
    def fullname(self):
        return'{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

emp1 = Employee('John', 'Smith')
emp1.fullname = 'Virat Kohli'

print(emp1.first)
print(emp1.email)
print(emp1.fullname)

del emp1.fullname