# Object Oriented Programming
class Employee:              # class employee animal language ho skti
    language = "python"      # this is a class attribute
    age = 20
    salary = 1000

rahul = Employee()
rahul.language = "javascript"
rahul.name = "Rahul"           # this is an instance attribute                     # object rahul     salry age name ye attribute hai
print(rahul.language,rahul.name,rahul.age,rahul.salary)

sanjay = Employee()
sanjay.name = "Sanjay Roro Robins"
print(sanjay.name,sanjay.age,sanjay.salary)

# Here name is instance attribute and salary and language and age are class 
# attribute as they directly belong to the class
