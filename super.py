class name:
    def __init__(self,name1):
        self.n=name1
    def display(self):
        print(self.n)
class roll(name):
    def __init__(self,n1,r):
        super().__init__(n1)
        self.r=r
    def display(self):
        super().display()
        print(self.r)
x=roll("Parth Doshi",15)
x.display()
