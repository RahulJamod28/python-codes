# # OOPS Part 01
# attribute ka mtlb hota he koi bhi varable data
# class student:
#     name = "Sharadha didi"

# s1 = student()
# print(s1.name)    

# class Car:
#     name = "BMW"
#     color = "Green"
#     brand = "Rols Royals"

# car1 = Car()
# print(car1.name)
# print(car1.color)
# print(car1.brand)

class Student:               # class
    college_name = "ABC college"
    name = "anonymous"  # class attr

    # default constructor
    def __init__(self,):
        pass

     # parameterized constructor   
    def __init__(self, name, marks):
        self.name = name      # instance attribute  obj attr > class attr
        self.marks = marks
        print("adding a new student in database.....")

    def welcome(self):                  # methods
        print("welcome student")    
        print("welcome student",self.name)

    def get_marks(self):
        return self.marks    

s1 = Student("Sanjay",95)   # object
print(s1.name)               
print(s1.marks)  
s1.welcome()   
print(s1.get_marks)

s2 = Student("Rahul",98)  
print(s2.name)    
print(s2.marks)  
print(s2.college_name)