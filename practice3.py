# inheritance
# # single inheritance
# class car:
#     color = "black"
#     @staticmethod
#     def start():
#         print("car started.....")

#     @staticmethod
#     def stop():
#         print("car stoped..")

# class toyotacar(car):
#     def __init__(self,name):
#         self.name = name

# car1 = toyotacar("fortuner")
# car2 = toyotacar("prius")

# print(car1.start())
# print(car2.stop())
                    

# multilevel inheritance
class car:
    @staticmethod
    def start():
        print("car started.....")

    @staticmethod
    def stop():
        print("car stoped..")

class toyotacar(car):
    def __init__(self,brand):
        self.brand = brand


class fortuner(toyotacar):
    def __init__(self, type):
        self.type = type

car1 = fortuner("diesel")
car1.start()
        

# multiple inheritance
class A:
    varA = "welcome to class A"
class B:
     varB = "welcome to class B"

class C(A,B):
    varC = "welcome to class C"


c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA)         
