# init constructor
# static method
class Employee:
    language = "python"
    salary = 1000

    def __init__(self,name,salary,language):     # dunder method which is automaticly called
        self.name = name
        self.salary = salary
        self.language = language                       
        print("Hey i am creating an object")   
        
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    
    @staticmethod
    def greet():
        print("GoodMorning")

rahul = Employee("Rahul",1200,"java")
# rahul.name = "Rahul"
print(rahul.name,rahul.salary,rahul.language)
rahul.greet()
rahul.getInfo()
# rohan = Employee()  # init call ho jayega jab aap ek object bnaoge tab
    