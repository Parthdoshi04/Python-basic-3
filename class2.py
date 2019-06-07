class employee:
    def __init__(self,fn,ln,salary):
        self.fn=fn
        self.ln=ln
        self.sal=salary
    def details(self):
        return'{} {} {}'.format(self.fn,self.ln,self.sal)
    def amount_promo(self):
        self.sal=int(self.sal*2.0)
        return'{} {} {}'.format(self.fn,self.ln,self.sal)
emp1=employee('Parth','Doshi',20000)
emp2=employee('Parth','Doshi',30000)

print(emp1.amount_promo())
print(emp2.amount_promo())
