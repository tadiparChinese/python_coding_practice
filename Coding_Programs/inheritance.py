class Employee:
    raise_amt = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first+ '.'+last+'@gmail.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
    raise_amt = 1.10
    def __init__(self, first, last, pay, prg_lng):
        super().__init__(first, last, pay)
        self.prg_lng = prg_lng

#list of employees that manager has to be supervised
class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.fullname())

dev1 = Developer('Sandip', 'Sharma', 50000, 'Python')
dev2 = Developer('Ramesh', 'Singh', 60000, 'Java')

manager1 = Manager('Sue', 'Smith', 90000, [dev1])

# print(manager1.email)
# manager1.add_emp(dev2)
# manager1.remove_emp(dev1)
# manager1.print_emp()

# print(dev1.pay)
# dev1.apply_raise()
# print(dev1.pay)


# print(dev1.email)
# print(dev2.pgm_lng)


print(isinstance(manager1, Manager)) #True
print(isinstance(manager1, Employee)) #True
print(isinstance(manager1, Developer)) #False

print(issubclass(Developer, Employee)) #True
print(issubclass(Manager, Employee)) #True
print(issubclass(Manager, Developer)) #False
