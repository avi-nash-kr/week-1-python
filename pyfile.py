
class details:
    
    def __init__(self, name, age):
        self.name=name
        self.age=age
        
    def printdetails(self):
        print(f" My name is {self.name} and age is {self.age}")
    
    
class employe(details):
    
    def __init__(self,name,age,salary,role):
        self.salary=salary
        self.role=role
        
        details.__init__(self,name,age)
        
    def printdetails(self):
        print(f"name is {self.name}, age is {self.age}, salary is {self.salary} and role is {self.role}")
        
        
 
x=details("avi", 22)
x.printdetails()
print()
y=employe("a", 22,70000, "Engineer")
y.printdetails()
print()
print()

for i in (x,y):
    i.printdetails()
         
        
    
    
    
