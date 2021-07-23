#baseclass polygon  __init()__ get_perimeter() display_info()
#triangle(features)
#qudrilateral(features)

class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def display_info():
        print('A polygon is a two dimentional shape with straight lines')
    
    def get_perimeter(self):
        perimeter = sum(self.sides)
        return perimeter

class Triangle(Polygon):
    def display_info(self):
        print('A triangle is polygon with 3 edges')
        # Polygon.display_info()
        super().display_info()

class Quadrilateral(Polygon):
    def display_info(self):
        print('A Quadrilateral is a polygon with 4 edges')

#method overloading
t1 = Triangle([5,6,7])
perimeter = t1.get_perimeter()
print(f'The perimeter of Triangle is {perimeter}')

#method overriding
t1.display_info()