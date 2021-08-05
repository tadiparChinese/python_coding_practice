class Employee:
  num_of_emps = 0
  raise_amt = 1.04

  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.email = first + '.' + last + '@company.com'
    self.pay = pay

    Employee.num_of_emps += 1

  def fullname(self):
    return '{}{}'.format(self.first, self.last)
  
  def apply_raise(self):
    self.pay = int(self.pay + self.raise_amt)

  @classmethod
  def set_raise_amt(cls, amount):
    cls.raise_amt = amount

  @classmethod
  def from_string(cls, emp_str):
    return cls(first, last, pay)

emp1 = Employee('Corey', 'sharma', 50000)
emp2 = Employee('Test', 'User', 40000)


emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Ramesh-Jha-60000'
emp_str_3 = 'John-Doe-80000'

new_emp_1 = Employee.from_string(emp_str_1)

# print(Employee.raise_amt)
# print(emp1.raise_amt)
# print(emp2.raise_amt)
print(new_emp_1.email)
print(new_emp_1.pay)





class Student:
  def __init__(self, name, marks):
    self.name = name
    self.marks = marks
  
  def msg(self):
    print(self.name+ " got "+ self.marks, "%")

  @classmethod
  def get_per(cls, name, marks):
    return cls(name, str(int(marks)/600)*100)

  @staticmethod
  def get_age(age):
    if age < 17:
      print("belongs to school")
    else:
      print("belongs to college")

s1 = Student("sia", "93")
s2 = Student.get_per("ria", "400")
s2.msg()
s1.get_age(18)