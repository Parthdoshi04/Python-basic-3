class employee:
    def __init__(self,fn,ln,id):
        self.fn=fn
        self.ln=ln
        self.id=id
    def details(self):
        return '{} {} {}'.format(self.fn,self.ln,self.id) #used for returning multiple values .format number of{} = number of arguments
emp1=employee('Parth','Doshi',15)
emp2=employee('Rockstar','Boy',25)
print("Using Object: ",emp1.details())
print("Using Object: ",emp2.details())
print("Using Class: ",employee.details(emp1))
print("Using Class: ",employee.details(emp2))
