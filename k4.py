# practices
# Q 1
class programmer:
    company = "Microsoft"
    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = programmer("Rahul",12000,454331)
print(p.name,p.salary,p.pin,p.company)
N = programmer("Nilam",25000,454331)
print(N.name,N.salary,N.pin,N.company)


# Q 2
class calculator:
    def __init__(self,n):
        self.n = n

    def square(self):
        print(f"The square is {self.n*self.n}")

    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"The squareroot is {self.n**1/2}")    
        
a = calculator(4)
a.square()
a.cube()
a.squareroot()
       