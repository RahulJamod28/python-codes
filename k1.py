# Self parameter
# Aap ek class ke andar function bhi dal skte ho
class Employee:
    language = "python"
    salary = 1000

    def getInfo(self):   # function method
        print(f"The language is {self.language}. The salary is {self.salary}")
    
    def greet(self):      # function method
        print("Good Morning")

rahul = Employee()
# rahul.language = "java"   #Instance attribute
rahul.getInfo()
rahul.greet()
# Employee.getInfo(rahul)

    