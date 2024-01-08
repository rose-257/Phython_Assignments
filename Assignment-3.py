class Person:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
    def update(self):
        name=input("Enter new name: ")
        age=input("Enter new age: ")
        address=input("Enter new Address: ")
        self.name=name
        self.age=age
        self.address=address
    def display(self):
        print("the name is ",self.name)
        print("the age is ",self.age)
        print("the address is ",self.address)
        
p=Person("Rose","22","Kannur")
p.display()
p.update()
p.display()
