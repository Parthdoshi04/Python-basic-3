class circle:
    def area(self):
        x=float(input("Enter radius for caluclating area: "))
        self.ans=3.14*x*x
        print("Area is: ",self.ans)
    def perimeter(self):
        x=float(input("Enter radius for caluclating perimeter: "))
        self.ans=2*3.14*x
        print("Area is: ",self.ans)
c=circle()
c.area()
c.perimeter()
