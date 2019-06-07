class employee:
    def get(self,fn,ln):
        self.fn=fn
        self.ln=ln
    def display(self):
        print(self.fn)
        print(self.ln)
el=employee()
el.get('Parth','Doshi')
el.display()
