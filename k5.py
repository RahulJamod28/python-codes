# practices
# Q 3
class Demo:
    a = 4

o = Demo()
print(o.a)  # print the class attribute because instance attribute is not present
o.a = 0     # instance attribute is set
print(o.a)  # prints the instance attribute because instance aatribute is present
print(Demo.a)  # prints the class attribute


# Q 4

class calculator:
    def __init__(self,n):
        self.n = n

    def square(self):
        print(f"The square is {self.n*self.n}")

    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"The squareroot is {self.n**1/2}")    

    @staticmethod
    def hello():
        print("Hello Rahul And Nilam")    
        
a = calculator(4)
a.square()
a.cube()
a.squareroot()
a.hello()