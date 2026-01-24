# class student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum +=val
#         print("Hi",self.name, "Your avg score is:",sum/3)        

# s1 = student("Rahul",[97,95,65])   
# s1.get_avg()

# s1.name = "Sanjay"
# s1.get_avg()


# # static method
# class student:
#     @staticmethod     # As such self ki jarurat nhi hoti he
#     def college():
#         print("ABC college")

# s1 = student()
# s1.college()


# abstarction: - unnecessory chijo ko chhupa dena our neccessory chije sirf vodikhayi
# encapsulation: -  jo abhi tak jo hamne class or object code likha he yhi abstrtn our encapsulation hai

# Abstraction
# class car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False

#     def start(self):              
#         self.clutch = True        # ye jo unnecessory chije thi vo mujhe dikhayi nhi di this is called abstrctn
#         self.acc = True
#         print("car is started....")

# car1 = car()       
# car1.start() 


class account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc

    # debit method
    def debit(self,amount):
        self.balance -=amount
        print("Rs.",amount,"was debited")
        print("total balance = ",self.get_balance())

    # credit method
    def credit(self,amount):
        self.balance +=amount
        print("Rs.",amount,"was credit")
        print("total balance = ",self.get_balance())

    def get_balance(self):
        return self.balance    

acc1 = account(1000,  980718210036947)
acc1.debit(800)
acc1.credit(5000)
acc1.debit(4000)
# print(acc1.balance)
# print(acc1.account_no)
      
      







