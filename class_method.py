class employee:
    total=0
    def __init__(self,fn,ln,salary):
        self.fn=fn
        self.ln=ln
        self.sal=salary
        employee.total+=1
    def details(self):
        return'{} {} {}'.format(self.fn,self.ln,self.sal)
    def amount_promo(self):
        self.sal=int(self.sal*2.0)
        return'{} {} {}'.format(self.fn,self.ln,self.sal)
    @classmethod
    def raiseamt(cls,amount):
        cls.amount=amount
print("Before: ",employee.total)
emp1=employee('Parth','Doshi',20000)
emp2=employee('Parth','Doshi',30000)
employee.raiseamt(1.06)
print(emp1.amount)
print("After: ",employee.total)
print("After increment: ",emp1.amount_promo())
print("After increment:",emp2.amount_promo())
