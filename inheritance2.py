class person:
    def name(self):
        x=input("Enter first name: ")
        y=input("Enter last name: ")
        print("First Name is:",x)
        print("Last Name is:",y)
class employee(person):
    def id(self):
        eid=int(input("Enter employee id: "))
        print("Employee ID is:",eid)
f=employee()
f.name()
f.id()

