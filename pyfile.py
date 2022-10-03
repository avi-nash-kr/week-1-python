
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
        print(f"My name is {self.name}, age is {self.age}, salary is {self.salary} and role is {self.role}")
        
        
 
a=details("avi", 22)
a.printdetails()
print()
b=employe("a", 22,70000, "Engineer")
b.printdetails()
print()
print()

for i in (a,b):
    i.printdetails()
         
        
    
    
    