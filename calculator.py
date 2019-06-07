class calculator:
    def add(self):
        x=int(input("Enter number 1: "))
        y=int(input("Enter number 2: "))
        self.c=x+y
        print(self.c)
    def sub(self):
        x=int(input("Enter number 1: "))
        y=int(input("Enter number 2: "))
        self.c=x-y
        print(self.c)
    def mul(self):
        x=int(input("Enter number 1: "))
        y=int(input("Enter number 2: "))
        self.c=x*y
        print(self.c)
    def div(self):
        x=int(input("Enter number 1: "))
        y=int(input("Enter number 2: "))
        self.c=x/y
        print(self.c)
d=calculator()
d.add()
d.sub()
d.mul()
d.div()

