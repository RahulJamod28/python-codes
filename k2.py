# static method
class Employee:
    language = "python"
    salary = 1000

    def getInfo(self):
        print(f"The language is {self.language} The salary is {self.salary}")
    
    @staticmethod
    def greet():
        print("GoodMorning")

harry = Employee()
harry.language = "java"   
# rahul.getInfo()
harry.getInfo()
harry.greet()
# Employee.getInfo(rahul)
print(harry.language,harry.salary)
