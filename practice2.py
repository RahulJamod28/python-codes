# OOP Part 02

# class student:
#     def __init__(self,name):
#         self.name = name

# s1 = student("Rahul")
# print(s1.name)
# del s1
# print(s1.name)        


# class account:
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass     # double underscore se private ho jata he
    
#     def reset_pass(self):
#         print(self.__acc_pass)

# acc1 = account("123456","abcde")

# print(acc1.acc_no)
# print(acc1.reset_pass())


class person:
    __name = "RahulJamod"
       
    def __hello(self):
        print("hello person ! ")

    def welcome(self):
       self.__hello()
    

p1 = person()

print(p1.welcome())