class parent:
    def surname(self):
        print("Rang De")
class child:
    def name(self):
        print("Brown")
class total(parent,child):
    pass
nm=total()
nm.name()
nm.surname()
